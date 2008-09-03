#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8
# =============================================================================
# $Id: setup.py 123 2008-09-02 01:56:28Z s0undt3ch $
# =============================================================================
#             $URL: http://devnull.ufsoft.org/svn/TracGoogleAnalytics/trunk/setup.py $
# $LastChangedDate: 2008-09-02 02:56:28 +0100 (Tue, 02 Sep 2008) $
#             $Rev: 123 $
#   $LastChangedBy: s0undt3ch $
# =============================================================================
# Copyright (C) 2008 UfSoft.org - Pedro Algarvio <ufs@ufsoft.org>
#
# Please view LICENSE for additional licensing information.
# =============================================================================

import re
from setuptools import setup

setup(name="TracGoogleAnalytics",
      version='0.1.2',
      author="Pedro Algarvio",
      author_email='ufs@ufsoft.org',
      description='Trac plugin to enable your trac environment to be logged '
                  'by Google Analytics',
      long_description=re.sub(r'(\.\.[\s]*[\w]*::[\s]*[\w+]*\n)+', r'::\n',
                              open('README.txt').read()),
      packages=['tracext', 'tracext.google', 'tracext.google.analytics'],
      namespace_packages=['tracext', 'tracext.google'],
      package_data = {'tracext.google.analytics': ['templates/*.html',
                                                   'htdocs/*.css']},
      include_package_data = True,
      keywords = "trac plugin google analytics",
      entry_points = """
      [trac.plugins]
        tracext.google.analytics = tracext.google.analytics
        tracext.google.analytics.admin = tracext.google.analytics.admin
        tracext.google.analytics.web_ui = tracext.google.analytics.web_ui
      """,
      classifiers = [
          'Framework :: Trac',
      ]
)
