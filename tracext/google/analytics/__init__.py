# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8
# =============================================================================
# $Id: __init__.py 123 2008-09-02 01:56:28Z s0undt3ch $
# =============================================================================
#             $URL: http://devnull.ufsoft.org/svn/TracGoogleAnalytics/trunk/tracext/google/analytics/__init__.py $
# $LastChangedDate: 2008-09-02 02:56:28 +0100 (Tue, 02 Sep 2008) $
#             $Rev: 123 $
#   $LastChangedBy: s0undt3ch $
# =============================================================================
# Copyright (C) 2008 UfSoft.org - Pedro Algarvio <ufs@ufsoft.org>
#
# Please view LICENSE for additional licensing information.
# =============================================================================

from trac import __version__
if [int(x.split('dev')[0]) for x in __version__.split('.')][1] < 11:
    raise ImportError("Trac < 0.11 not supported")

## ==============================================================================
## Trac Upgrade Code
## ==============================================================================
#from trac.core import Component, implements
#from trac.env import IEnvironmentSetupParticipant
#
#class GoogleComponentSetup(Component):
#    env = config = log = None # make pylink happy
#    implements(IEnvironmentSetupParticipant)
#
#    def environment_created(self):
#        "Nothing to do when an environment is created"""
#
#    def environment_needs_upgrade(self, db):
#        cursor = db.cursor()
#        cursor.execute('SELECT value FROM system WHERE name=%s',
#                       ('adspanel.code',))
#        if cursor.fetchone():
#            self.log.debug('Found old AdsPanel code in database')
#            return True
#        self.log.debug('Did not find old AdsPanel code in database')
#        return False
#
#    def upgrade_environment(self, db):
#        cursor = db.cursor()
#        cursor.execute('SELECT value FROM system WHERE name=%s',
#                       ('adspanel.code',))
#        code = cursor.fetchone()
#        self.log.debug('Upgrading Ads HTML Code from AdsPanel to Adsense4Trac')
#        cursor.execute('INSERT INTO system (name,value) VALUES (%s,%s)',
#                       ('adsense.ads_html', code[0]))
#        cursor.execute('DELETE from system where name=%s', ('adspanel.code',))
#        db.commit()
#        self.log.debug("Upgrading configuration from AdsPanel to Adsense4Trac "
#                       "if needed")
#        for option, value in self.config.options('adspanel'):
#            if self.config.has_option('adsense', option):
#                self.config.set('adsense', option, value)
#            self.config.remove('adspanel', option)
#        self.config.save()
