##############################################################################
#
# Copyright (c) 2008 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

__version__ = '0.1'

import os, sys

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

def alltests():
    # use the zope.testing testrunner machinery to find all the
    # test suites we've put under ourselves
    try:
        from zope.testing.testrunner import get_options
    except ImportError:
        from zope.testing.testrunner.options import get_options
    try:
        from zope.testing.testrunner import find_suites
    except ImportError:
        from zope.testing.testrunner.find import find_suites
    try:
        from zope.testing.testrunner import configure_logging
        configure_logging()
    except ImportError:
        pass
    from unittest import TestSuite
    here = os.path.abspath(os.path.dirname(sys.argv[0]))
    args = sys.argv[:]
    defaults = ['--test-path', here]
    options = get_options(args, defaults)
    suites = list(find_suites(options))
    return TestSuite(suites)

setup(name='repoze.whooze',
      version=__version__,
      description='A repoze.who IAuthentication plugin for Zope 3',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        ],
      keywords='wsgi zope authentication',
      author="Agendaless Consulting",
      author_email="repoze-dev@lists.repoze.org",
      url="http://www.repoze.org",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['repoze'],
      zip_safe=False,
      tests_require = [
          'zope.interface',
          'zope.security',
          'zope.testing',
          'zope.publisher',
          'zope.traversing',
          'zope.securitypolicy',
          'zope.app.security',
          'zope.app.zcmlfiles',
          ],
      install_requires=[
          'zope.interface',
          'zope.security',
          'zope.app.security',
          ],
      test_suite="__main__.alltests",
      entry_points = """\
      """
      )
