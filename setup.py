import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-mississippi',
    version='0.2.2',
    packages=find_packages(),
    include_package_data=True,
    license='ISC License',
    description='Promote resources to first class citizens for prefix-less URLs and easy sitemaps.',
    long_description=README,
    url='https://github.com/sethlivingston/django-mississippi',
    author='Seth Livingston',
    author_email='webdevbyseth@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
