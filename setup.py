#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup, find_packages
import metadata

app_name = metadata.name
version = metadata.version

setup(
    name = "django-%s" % app_name,
    version = version,

    # packages = [app_name, '%s.templatetags' % app_name],
    packages = find_packages(),
    include_package_data = True,

    author = metadata.authors,
    author_email = "spencer.herzberg@gmail.com",
    description = "A Django application that manages flash based slideshows.",
    long_description = \
"""
A Django application that manages mass emails sent to lists.

Features:

* Create flash slideshows with django objects.
""",
    license = "GPL",
    keywords = "django slideshow",
    classifiers = [
        'Development Status :: 1',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms = ['any'],
    url = "https://github.com/whelmingbytes/django-slideshow",
    download_url = "https://github.com/whelmingbytes/django-slideshow",
)
