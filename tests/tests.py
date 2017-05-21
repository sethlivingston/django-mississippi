from django.contrib.sites.models import Site
from django.http import HttpRequest, HttpResponse, Http404
from django.test import TestCase

from mississippi.models import Resource, ResourceType, SiteResource
from mississippi.views import dispatch


class DispatchTestCase(TestCase):
    """ Ensure incoming requests and slugs get dispatched to correct view functions """

    def setUp(self):
        self.dallas = Site.objects.create(domain='dallas.test.com')
        self.denver = Site.objects.create(domain='denver.test.com')

        self.article_type = ResourceType.objects.create(name='article')
        self.event_type = ResourceType.objects.create(name='event')

        self.article_for_one_site = Resource.objects.create(slug='article1', type=self.article_type)
        SiteResource.objects.create(site=self.dallas, resource=self.article_for_one_site)
        self.article_for_two_sites = Resource.objects.create(slug='article2', type=self.article_type)
        SiteResource.objects.create(site=self.dallas, resource=self.article_for_two_sites)
        SiteResource.objects.create(site=self.denver, resource=self.article_for_two_sites)
        self.article_for_all_sites = Resource.objects.create(slug='article3', type=self.article_type)

    def test_dispatches_to_resource_with_one_site(self):
        # Set up
        actual_request = None
        actual_resource = None

        def view_fn(request, resource):
            nonlocal actual_request
            actual_request = request
            nonlocal actual_resource
            actual_resource = resource
            return HttpResponse()

        view_map = {
            'article': view_fn,
        }

        request = HttpRequest()
        request.site = self.dallas

        # Run
        dispatch(request, self.article_for_one_site.slug, view_map)

        # Test
        self.assertEqual(request, actual_request)
        self.assertEqual(self.article_for_one_site, actual_resource)

    def test_dispatches_to_resource_with_multiple_sites(self):
        # Set up
        actual_request = None
        actual_resource = None

        def view_fn(request, resource):
            nonlocal actual_request
            actual_request = request
            nonlocal actual_resource
            actual_resource = resource
            return HttpResponse()

        view_map = {
            'article': view_fn,
        }

        request = HttpRequest()
        request.site = self.dallas

        # Run
        dispatch(request, self.article_for_two_sites.slug, view_map)

        # Test
        self.assertEqual(request, actual_request)
        self.assertEqual(self.article_for_two_sites, actual_resource)

    def test_dispatches_to_resource_with_no_sites(self):
        # Set up
        actual_request = None
        actual_resource = None

        def view_fn(request, resource):
            nonlocal actual_request
            actual_request = request
            nonlocal actual_resource
            actual_resource = resource
            return HttpResponse()

        view_map = {
            'article': view_fn,
        }

        request = HttpRequest()
        request.site = self.dallas

        # Run
        dispatch(request, self.article_for_all_sites.slug, view_map)

        # Test
        self.assertEqual(request, actual_request)
        self.assertEqual(self.article_for_all_sites, actual_resource)

    def test_throws_404_when_no_resource(self):
        # Set up
        request = HttpRequest()
        request.site = self.dallas
        threw_404 = False

        # Run
        try:
            dispatch(request, 'nopenopenope', {})
        except Http404:
            return

        self.fail('Should have raised Http404')
