from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_control
from django.views.decorators.http import last_modified

from mississippi.models import Resource


def dispatch(request: HttpRequest, slug: str, view_map: dict):
    """ Locate resource type, resource, and dispatch to view function in provided map """
    queryset = Resource.objects.select_related()
    resource = get_object_or_404(queryset, Q(sites=request.site) | Q(sites=None), slug__iexact=slug)

    view_fn = view_map[resource.type.name]
    if resource.type.cache:
        @cache_control(public=True, max_age=resource.type.cache_max_age_in_seconds)
        @last_modified(lambda _, inner_resource: inner_resource.last_modified)
        def cached_view_fn(inner_request, inner_resource):
            return view_fn(inner_request, inner_resource)

        return cached_view_fn(request, resource)
    else:
        return view_fn
