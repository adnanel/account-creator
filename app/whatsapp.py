#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2022  Diego Torres Milano
Created on 2022-05-23 by Culebra v21.4.1
                      __    __    __    __
                     /  \  /  \  /  \  /  \ 
____________________/  __\/  __\/  __\/  __\_____________________________
___________________/  /__/  /__/  /__/  /________________________________
                   | / \   / \   / \   / \   \___
                   |/   \_/   \_/   \_/   \    o \ 
                                           \_____/--<
@author: Diego Torres Milano
@author: Jennifer E. Swofford (ascii art snake)
"""

import re
import sys
import os
import requests
import time
import json

import unittest

sys.path.append('/opt/work/app/avc/src')

from com.dtmilano.android.viewclient import ViewClient, KEY_EVENT, CulebraTestCase

TAG = 'CULEBRA'


def get_job():
    while True:
        response = requests.get("http://localhost:3000/job")
        if response.status_code == 200:
            return json.loads(response.text)
        print("Job not available, retrying...")
        time.sleep(5)


def canonical_phone_number(formatted):
    return formatted.replace(" ", "").replace("+", "00")


job = get_job()

# example value: "387"
COUNTRY_CODE = job["countryCode"]
# example value: "63 123 456"
PHONE_NUMBER = job["phoneNumber"]
PHONE_NUMBER_NBSP = PHONE_NUMBER.replace(" ", " ")

CANONICAL_PHONE_NUMBER = canonical_phone_number(COUNTRY_CODE + PHONE_NUMBER)
print("Registering whatsapp for " + PHONE_NUMBER + " (" + CANONICAL_PHONE_NUMBER + ")")


class CulebraTests(CulebraTestCase):

    @classmethod
    def setUpClass(cls):
        cls.kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
        cls.kwargs2 = {'forceviewserveruse': False, 'startviewserver': True, 'autodump': False,
                       'ignoreuiautomatorkilled': True, 'compresseddump': True, 'useuiautomatorhelper': False,
                       'debug': {}}
        cls.options = {'find-views-by-id': True, 'find-views-with-text': True,
                       'find-views-with-content-description': True, 'use-regexps': False, 'verbose-comments': False,
                       'unit-test-class': True, 'unit-test-method': None, 'use-jar': False, 'use-dictionary': False,
                       'dictionary-keys-from': 'id', 'auto-regexps': None, 'start-activity': None,
                       'output': 'myTestCase.py', 'interactive': False, 'window': -1, 'prepend-to-sys-path': False,
                       'save-screenshot': None, 'save-view-screenshots': None, 'gui': True,
                       'do-not-verify-screen-dump': False, 'scale': 0.5, 'orientation-locked': None,
                       'multi-device': False, 'log-actions': True, 'device-art': None, 'drop-shadow': False,
                       'glare': False, 'null-back-end': False, 'concertina': False, 'concertina-config': None,
                       'install-apk': None}
        cls.sleep = 5

    @staticmethod
    def getCode(phone_number):
        while True:
            response = requests.get("http://localhost:3000/whatsapp?number=" + phone_number)
            if response.status_code == 200:
                return response.text
            print("Code for " + phone_number + " not found, retrying...")

    def setUp(self):
        super(CulebraTests, self).setUp()

    def tearDown(self):
        super(CulebraTests, self).tearDown()

    def preconditions(self):
        if not super(CulebraTests, self).preconditions():
            return False

        return True

    def testSomething(self):
        if not self.preconditions():
            self.fail('Preconditions failed')

        _s = CulebraTests.sleep
        _v = CulebraTests.verbose
        attempt = 0

        while True:
            try:
                self.device.Log.d(TAG, "dumping content of window=-1", _v)
                self.vc.dump(window=-1)
                self.device.Log.d(TAG, "touching view with text=u'OK'", _v)
                self.vc.findViewWithTextOrRaise(u'OK').touch()
                break
            except:
                attempt = attempt + 1
                if attempt > 100:
                    self.device.Log.d(TAG, "Failed, giving up...", _v)
                    break
                self.device.Log.d(TAG, "Failed, trying again...", _v)

        self.vc.sleep(_s)
        self.device.Log.d(TAG, "dumping content of window=-1", _v)
        self.vc.dump(window=-1)
        self.device.Log.d(TAG, "finding view with id=id/no_id/1", _v)
        no_id1 = self.vc.findViewByIdOrRaise("id/no_id/1")
        self.device.Log.d(TAG, "finding view with id=id/no_id/2", _v)
        no_id2 = self.vc.findViewByIdOrRaise("id/no_id/2")
        self.device.Log.d(TAG, "finding view with text=u'Welcome to WhatsApp'", _v)
        no_id2 = self.vc.findViewWithTextOrRaise(u'Welcome to WhatsApp')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/eula_view", _v)
        com_whatsapp___id_eula_view = self.vc.findViewByIdOrRaise("com.whatsapp:id/eula_view")
        self.device.Log.d(TAG,
                          "finding view with text=u'Read our Privacy Policy. Tap \"Agree and continue\" to accept the Terms of Service.'",
                          _v)
        com_whatsapp___id_eula_view = self.vc.findViewWithTextOrRaise(
            u'Read our Privacy Policy. Tap "Agree and continue" to accept the Terms of Service.')
        self.device.Log.d(TAG, "finding view with id=id/no_id/4", _v)
        no_id4 = self.vc.findViewByIdOrRaise("id/no_id/4")
        self.device.Log.d(TAG, "finding view with content-description=u'''Privacy Policy'''", _v)
        no_id4 = self.vc.findViewWithContentDescriptionOrRaise(u'''Privacy Policy''')
        self.device.Log.d(TAG, "finding view with id=id/no_id/5", _v)
        no_id5 = self.vc.findViewByIdOrRaise("id/no_id/5")
        self.device.Log.d(TAG, "finding view with content-description=u'''Terms of Service'''", _v)
        no_id5 = self.vc.findViewWithContentDescriptionOrRaise(u'''Terms of Service''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/eula_accept", _v)
        com_whatsapp___id_eula_accept = self.vc.findViewByIdOrRaise("com.whatsapp:id/eula_accept")
        self.device.Log.d(TAG, "finding view with text=u'AGREE AND CONTINUE'", _v)
        com_whatsapp___id_eula_accept = self.vc.findViewWithTextOrRaise(u'AGREE AND CONTINUE')

        self.device.Log.d(TAG, "touching view with text=u'AGREE AND CONTINUE'", _v)
        self.vc.findViewWithTextOrRaise(u'AGREE AND CONTINUE').touch()
        self.vc.sleep(_s)
        self.device.Log.d(TAG, "dumping content of window=-1", _v)
        self.vc.dump(window=-1)

        self.device.Log.d(TAG, "finding view with id=id/no_id/1", _v)
        no_id1 = self.vc.findViewByIdOrRaise("id/no_id/1")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/register_phone_toolbar_title", _v)
        com_whatsapp___id_register_phone_toolbar_title = self.vc.findViewByIdOrRaise(
            "com.whatsapp:id/register_phone_toolbar_title")
        self.device.Log.d(TAG, "finding view with text=u'Enter your phone number'", _v)
        com_whatsapp___id_register_phone_toolbar_title = self.vc.findViewWithTextOrRaise(u'Enter your phone number')
        self.device.Log.d(TAG, "finding view with id=id/no_id/3", _v)
        no_id3 = self.vc.findViewByIdOrRaise("id/no_id/3")
        self.device.Log.d(TAG, "finding view with content-description=u'''More options'''", _v)
        no_id3 = self.vc.findViewWithContentDescriptionOrRaise(u'''More options''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/scroll_view", _v)
        com_whatsapp___id_scroll_view = self.vc.findViewByIdOrRaise("com.whatsapp:id/scroll_view")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/description", _v)
        com_whatsapp___id_description = self.vc.findViewByIdOrRaise("com.whatsapp:id/description")
        self.device.Log.d(TAG,
                          "finding view with text=u'''WhatsApp will need to verify your phone number. What's my number?'''",
                          _v)
        com_whatsapp___id_description = self.vc.findViewWithTextOrRaise(
            u'''WhatsApp will need to verify your phone number. What's my number?''')
        self.device.Log.d(TAG, "finding view with id=id/no_id/6", _v)
        no_id6 = self.vc.findViewByIdOrRaise("id/no_id/6")
        self.device.Log.d(TAG, "finding view with content-description=u'''What's my number?'''", _v)
        no_id6 = self.vc.findViewWithContentDescriptionOrRaise(u'''What's my number?''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_country", _v)
        com_whatsapp___id_registration_country = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_country")
        self.device.Log.d(TAG, "finding view with text=u'United States'", _v)
        com_whatsapp___id_registration_country = self.vc.findViewWithTextOrRaise(u'United States')
        self.device.Log.d(TAG, "finding view with content-description=u'''Selected country, United States'''", _v)
        com_whatsapp___id_registration_country = self.vc.findViewWithContentDescriptionOrRaise(
            u'''Selected country, United States''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_cc", _v)
        com_whatsapp___id_registration_cc = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_cc")
        self.device.Log.d(TAG, "finding view with text=u'1'", _v)
        com_whatsapp___id_registration_cc = self.vc.findViewWithTextOrRaise(u'1')
        self.device.Log.d(TAG, "finding view with id=id/no_id/9", _v)
        no_id9 = self.vc.findViewByIdOrRaise("id/no_id/9")
        self.device.Log.d(TAG, "finding view with text=u'+'", _v)
        no_id9 = self.vc.findViewWithTextOrRaise(u'+')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_phone", _v)
        com_whatsapp___id_registration_phone = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_phone")
        self.device.Log.d(TAG, "finding view with text=u'phone number'", _v)
        com_whatsapp___id_registration_phone = self.vc.findViewWithTextOrRaise(u'phone number')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/carrier_charge_warning", _v)
        com_whatsapp___id_carrier_charge_warning = self.vc.findViewByIdOrRaise("com.whatsapp:id/carrier_charge_warning")
        self.device.Log.d(TAG, "finding view with text=u'Carrier charges may apply'", _v)
        com_whatsapp___id_carrier_charge_warning = self.vc.findViewWithTextOrRaise(u'Carrier charges may apply')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_submit", _v)
        com_whatsapp___id_registration_submit = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_submit")
        self.device.Log.d(TAG, "finding view with text=u'NEXT'", _v)
        com_whatsapp___id_registration_submit = self.vc.findViewWithTextOrRaise(u'NEXT')

        self.vc.findViewWithTextOrRaise(u'1').setText(COUNTRY_CODE)
        self.vc.sleep(_s)
        self.device.Log.d(TAG, "dumping content of window=-1", _v)
        self.vc.dump(window=-1)

        self.device.Log.d(TAG, "finding view with id=id/no_id/1", _v)
        no_id1 = self.vc.findViewByIdOrRaise("id/no_id/1")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/register_phone_toolbar_title", _v)
        com_whatsapp___id_register_phone_toolbar_title = self.vc.findViewByIdOrRaise(
            "com.whatsapp:id/register_phone_toolbar_title")
        self.device.Log.d(TAG, "finding view with text=u'Enter your phone number'", _v)
        com_whatsapp___id_register_phone_toolbar_title = self.vc.findViewWithTextOrRaise(u'Enter your phone number')
        self.device.Log.d(TAG, "finding view with id=id/no_id/3", _v)
        no_id3 = self.vc.findViewByIdOrRaise("id/no_id/3")
        self.device.Log.d(TAG, "finding view with content-description=u'''More options'''", _v)
        no_id3 = self.vc.findViewWithContentDescriptionOrRaise(u'''More options''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/scroll_view", _v)
        com_whatsapp___id_scroll_view = self.vc.findViewByIdOrRaise("com.whatsapp:id/scroll_view")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/description", _v)
        com_whatsapp___id_description = self.vc.findViewByIdOrRaise("com.whatsapp:id/description")
        self.device.Log.d(TAG,
                          "finding view with text=u'''WhatsApp will need to verify your phone number. What's my number?'''",
                          _v)
        com_whatsapp___id_description = self.vc.findViewWithTextOrRaise(
            u'''WhatsApp will need to verify your phone number. What's my number?''')
        self.device.Log.d(TAG, "finding view with id=id/no_id/6", _v)
        no_id6 = self.vc.findViewByIdOrRaise("id/no_id/6")
        self.device.Log.d(TAG, "finding view with content-description=u'''What's my number?'''", _v)
        no_id6 = self.vc.findViewWithContentDescriptionOrRaise(u'''What's my number?''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_country", _v)
        com_whatsapp___id_registration_country = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_country")
        self.device.Log.d(TAG, "finding view with text=u'Bosnia & Herzegovina'", _v)
        com_whatsapp___id_registration_country = self.vc.findViewWithTextOrRaise(u'Bosnia & Herzegovina')
        self.device.Log.d(TAG, "finding view with content-description=u'''Selected country, Bosnia & Herzegovina'''",
                          _v)
        com_whatsapp___id_registration_country = self.vc.findViewWithContentDescriptionOrRaise(
            u'''Selected country, Bosnia & Herzegovina''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_cc", _v)
        com_whatsapp___id_registration_cc = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_cc")
        self.device.Log.d(TAG, "finding view with text=" + COUNTRY_CODE, _v)
        com_whatsapp___id_registration_cc = self.vc.findViewWithTextOrRaise(COUNTRY_CODE)
        self.device.Log.d(TAG, "finding view with id=id/no_id/9", _v)
        no_id9 = self.vc.findViewByIdOrRaise("id/no_id/9")
        self.device.Log.d(TAG, "finding view with text=u'+'", _v)
        no_id9 = self.vc.findViewWithTextOrRaise(u'+')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_phone", _v)
        com_whatsapp___id_registration_phone = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_phone")
        self.device.Log.d(TAG, "finding view with text=u'phone number'", _v)
        com_whatsapp___id_registration_phone = self.vc.findViewWithTextOrRaise(u'phone number')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/carrier_charge_warning", _v)
        com_whatsapp___id_carrier_charge_warning = self.vc.findViewByIdOrRaise("com.whatsapp:id/carrier_charge_warning")
        self.device.Log.d(TAG, "finding view with text=u'Carrier charges may apply'", _v)
        com_whatsapp___id_carrier_charge_warning = self.vc.findViewWithTextOrRaise(u'Carrier charges may apply')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_submit", _v)
        com_whatsapp___id_registration_submit = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_submit")
        self.device.Log.d(TAG, "finding view with text=u'NEXT'", _v)
        com_whatsapp___id_registration_submit = self.vc.findViewWithTextOrRaise(u'NEXT')

        self.vc.findViewWithTextOrRaise(u'phone number').setText(PHONE_NUMBER.replace(" ", ""))
        self.vc.sleep(_s)
        self.device.Log.d(TAG, "dumping content of window=-1", _v)
        self.vc.dump(window=-1)

        self.device.Log.d(TAG, "finding view with id=id/no_id/1", _v)
        no_id1 = self.vc.findViewByIdOrRaise("id/no_id/1")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/register_phone_toolbar_title", _v)
        com_whatsapp___id_register_phone_toolbar_title = self.vc.findViewByIdOrRaise(
            "com.whatsapp:id/register_phone_toolbar_title")
        self.device.Log.d(TAG, "finding view with text=u'Enter your phone number'", _v)
        com_whatsapp___id_register_phone_toolbar_title = self.vc.findViewWithTextOrRaise(u'Enter your phone number')
        self.device.Log.d(TAG, "finding view with id=id/no_id/3", _v)
        no_id3 = self.vc.findViewByIdOrRaise("id/no_id/3")
        self.device.Log.d(TAG, "finding view with content-description=u'''More options'''", _v)
        no_id3 = self.vc.findViewWithContentDescriptionOrRaise(u'''More options''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/scroll_view", _v)
        com_whatsapp___id_scroll_view = self.vc.findViewByIdOrRaise("com.whatsapp:id/scroll_view")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/description", _v)
        com_whatsapp___id_description = self.vc.findViewByIdOrRaise("com.whatsapp:id/description")
        self.device.Log.d(TAG,
                          "finding view with text=u'''WhatsApp will need to verify your phone number. What's my number?'''",
                          _v)
        com_whatsapp___id_description = self.vc.findViewWithTextOrRaise(
            u'''WhatsApp will need to verify your phone number. What's my number?''')
        self.device.Log.d(TAG, "finding view with id=id/no_id/6", _v)
        no_id6 = self.vc.findViewByIdOrRaise("id/no_id/6")
        self.device.Log.d(TAG, "finding view with content-description=u'''What's my number?'''", _v)
        no_id6 = self.vc.findViewWithContentDescriptionOrRaise(u'''What's my number?''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_country", _v)
        com_whatsapp___id_registration_country = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_country")
        self.device.Log.d(TAG, "finding view with text=u'Bosnia & Herzegovina'", _v)
        com_whatsapp___id_registration_country = self.vc.findViewWithTextOrRaise(u'Bosnia & Herzegovina')
        self.device.Log.d(TAG, "finding view with content-description=u'''Selected country, Bosnia & Herzegovina'''",
                          _v)
        com_whatsapp___id_registration_country = self.vc.findViewWithContentDescriptionOrRaise(
            u'''Selected country, Bosnia & Herzegovina''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_cc", _v)
        com_whatsapp___id_registration_cc = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_cc")
        self.device.Log.d(TAG, "finding view with text=" + COUNTRY_CODE, _v)
        com_whatsapp___id_registration_cc = self.vc.findViewWithTextOrRaise(COUNTRY_CODE)
        self.device.Log.d(TAG, "finding view with id=id/no_id/9", _v)
        no_id9 = self.vc.findViewByIdOrRaise("id/no_id/9")
        self.device.Log.d(TAG, "finding view with text=u'+'", _v)
        no_id9 = self.vc.findViewWithTextOrRaise(u'+')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_phone", _v)
        com_whatsapp___id_registration_phone = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_phone")
        self.device.Log.d(TAG, "finding view with text=u'phone number'", _v)
        com_whatsapp___id_registration_phone = self.vc.findViewWithTextOrRaise(PHONE_NUMBER)
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/carrier_charge_warning", _v)
        com_whatsapp___id_carrier_charge_warning = self.vc.findViewByIdOrRaise("com.whatsapp:id/carrier_charge_warning")
        self.device.Log.d(TAG, "finding view with text=u'Carrier charges may apply'", _v)
        com_whatsapp___id_carrier_charge_warning = self.vc.findViewWithTextOrRaise(u'Carrier charges may apply')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_submit", _v)
        com_whatsapp___id_registration_submit = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_submit")
        self.device.Log.d(TAG, "finding view with text=u'NEXT'", _v)
        com_whatsapp___id_registration_submit = self.vc.findViewWithTextOrRaise(u'NEXT')

        self.device.Log.d(TAG, "touching view with text=u'NEXT'", _v)
        self.vc.findViewWithTextOrRaise(u'NEXT').touch()
        self.vc.sleep(_s)
        self.device.Log.d(TAG, "dumping content of window=-1", _v)
        self.vc.dump(window=-1)

        self.device.Log.d(TAG, "finding view with id=id/no_id/1", _v)
        no_id1 = self.vc.findViewByIdOrRaise("id/no_id/1")
        self.device.Log.d(TAG, "finding view with id=android:id/message", _v)
        android___id_message = self.vc.findViewByIdOrRaise("android:id/message")
        self.device.Log.d(TAG,
                          "finding view with text=u'''You entered the phone number...'''",
                          _v)

        android___id_message = self.vc.findViewWithTextOrRaise(
            u'''You entered the phone number:\n\n+''' + COUNTRY_CODE + " " + PHONE_NUMBER + '''\n\nIs this OK, or would you like to edit the number?''')

        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/buttonPanel", _v)
        com_whatsapp___id_buttonPanel = self.vc.findViewByIdOrRaise("com.whatsapp:id/buttonPanel")
        self.device.Log.d(TAG, "finding view with id=android:id/button3", _v)
        android___id_button3 = self.vc.findViewByIdOrRaise("android:id/button3")
        self.device.Log.d(TAG, "finding view with text=u'EDIT'", _v)
        android___id_button3 = self.vc.findViewWithTextOrRaise(u'EDIT')
        self.device.Log.d(TAG, "finding view with id=android:id/button1", _v)
        android___id_button1 = self.vc.findViewByIdOrRaise("android:id/button1")
        self.device.Log.d(TAG, "finding view with text=u'OK'", _v)
        android___id_button1 = self.vc.findViewWithTextOrRaise(u'OK')

        self.device.Log.d(TAG, "touching view with text=u'OK'", _v)
        self.vc.findViewWithTextOrRaise(u'OK').touch()
        self.vc.sleep(_s)
        self.device.Log.d(TAG, "dumping content of window=-1", _v)
        self.vc.dump(window=-1)

        self.device.Log.d(TAG, "finding view with id=id/no_id/1", _v)
        no_id1 = self.vc.findViewByIdOrRaise("id/no_id/1")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/title_toolbar_text", _v)
        com_whatsapp___id_title_toolbar_text = self.vc.findViewByIdOrRaise("com.whatsapp:id/title_toolbar_text")
        self.device.Log.d(TAG, "finding view with text=u'Verifying your number'", _v)
        com_whatsapp___id_title_toolbar_text = self.vc.findViewWithTextOrRaise(u'Verifying your number')
        self.device.Log.d(TAG, "finding view with id=id/no_id/3", _v)
        no_id3 = self.vc.findViewByIdOrRaise("id/no_id/3")
        self.device.Log.d(TAG, "finding view with content-description=u'''More options'''", _v)
        no_id3 = self.vc.findViewWithContentDescriptionOrRaise(u'''More options''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/scroll_view", _v)
        com_whatsapp___id_scroll_view = self.vc.findViewByIdOrRaise("com.whatsapp:id/scroll_view")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/description_2_top", _v)
        com_whatsapp___id_description_2_top = self.vc.findViewByIdOrRaise("com.whatsapp:id/description_2_top")
        self.device.Log.d(TAG, "finding view with text=u'Waiting to automatically detect an SMS sent to ...", _v)
        com_whatsapp___id_description_2_top = self.vc.findViewWithTextOrRaise(
            u'Waiting to automatically detect an SMS sent to +' + COUNTRY_CODE + ' ' + PHONE_NUMBER_NBSP + '. Wrong number?')
        self.device.Log.d(TAG, "finding view with id=id/no_id/6", _v)
        no_id6 = self.vc.findViewByIdOrRaise("id/no_id/6")
        self.device.Log.d(TAG, "finding view with content-description=u'''Wrong number?'''", _v)
        no_id6 = self.vc.findViewWithContentDescriptionOrRaise(u'''Wrong number?''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/verify_sms_code_input", _v)
        com_whatsapp___id_verify_sms_code_input = self.vc.findViewByIdOrRaise("com.whatsapp:id/verify_sms_code_input")
        self.device.Log.d(TAG, "finding view with text=u'––– –––'", _v)
        com_whatsapp___id_verify_sms_code_input = self.vc.findViewWithTextOrRaise(u'––– –––')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/progress_bar_code_input_blocked", _v)
        com_whatsapp___id_progress_bar_code_input_blocked = self.vc.findViewByIdOrRaise(
            "com.whatsapp:id/progress_bar_code_input_blocked")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/description_2_bottom", _v)
        com_whatsapp___id_description_2_bottom = self.vc.findViewByIdOrRaise("com.whatsapp:id/description_2_bottom")
        self.device.Log.d(TAG, "finding view with text=u'Enter 6-digit code'", _v)
        com_whatsapp___id_description_2_bottom = self.vc.findViewWithTextOrRaise(u'Enter 6-digit code')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/resend_sms_btn", _v)
        com_whatsapp___id_resend_sms_btn = self.vc.findViewByIdOrRaise("com.whatsapp:id/resend_sms_btn")
        self.device.Log.d(TAG, "finding view with text=u'Resend SMS'", _v)
        com_whatsapp___id_resend_sms_btn = self.vc.findViewWithTextOrRaise(u'Resend SMS')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/call_btn", _v)
        com_whatsapp___id_call_btn = self.vc.findViewByIdOrRaise("com.whatsapp:id/call_btn")
        self.device.Log.d(TAG, "finding view with text=u'Call me'", _v)
        com_whatsapp___id_call_btn = self.vc.findViewWithTextOrRaise(u'Call me')

        code = CulebraTests.getCode(CANONICAL_PHONE_NUMBER)

        self.vc.findViewWithTextOrRaise(u'––– –––').setText(code)
        self.vc.sleep(_s)
        self.device.Log.d(TAG, "dumping content of window=-1", _v)
        self.vc.dump(window=-1)

        self.device.Log.d(TAG, "finding view with id=id/no_id/1", _v)
        no_id1 = self.vc.findViewByIdOrRaise("id/no_id/1")
        self.device.Log.d(TAG, "finding view with id=id/no_id/2", _v)
        no_id2 = self.vc.findViewByIdOrRaise("id/no_id/2")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/permission_title", _v)
        com_whatsapp___id_permission_title = self.vc.findViewByIdOrRaise("com.whatsapp:id/permission_title")
        self.device.Log.d(TAG, "finding view with text=u'Contacts and media'", _v)
        com_whatsapp___id_permission_title = self.vc.findViewWithTextOrRaise(u'Contacts and media')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/permission_message", _v)
        com_whatsapp___id_permission_message = self.vc.findViewByIdOrRaise("com.whatsapp:id/permission_message")
        self.device.Log.d(TAG,
                          "finding view with text=u'To easily send messages and photos to friends and family, allow WhatsApp to access your contacts, photos and other media.'",
                          _v)
        com_whatsapp___id_permission_message = self.vc.findViewWithTextOrRaise(
            u'To easily send messages and photos to friends and family, allow WhatsApp to access your contacts, photos and other media.')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/cancel", _v)
        com_whatsapp___id_cancel = self.vc.findViewByIdOrRaise("com.whatsapp:id/cancel")
        self.device.Log.d(TAG, "finding view with text=u'NOT NOW'", _v)
        com_whatsapp___id_cancel = self.vc.findViewWithTextOrRaise(u'NOT NOW')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/submit", _v)
        com_whatsapp___id_submit = self.vc.findViewByIdOrRaise("com.whatsapp:id/submit")
        self.device.Log.d(TAG, "finding view with text=u'CONTINUE'", _v)
        com_whatsapp___id_submit = self.vc.findViewWithTextOrRaise(u'CONTINUE')

        self.device.Log.d(TAG, "touching view with text=u'NOT NOW'", _v)
        self.vc.findViewWithTextOrRaise(u'NOT NOW').touch()
        self.vc.sleep(_s)
        self.device.Log.d(TAG, "dumping content of window=-1", _v)
        self.vc.dump(window=-1)

        self.device.Log.d(TAG, "finding view with id=id/no_id/1", _v)
        no_id1 = self.vc.findViewByIdOrRaise("id/no_id/1")
        self.device.Log.d(TAG, "finding view with id=id/no_id/2", _v)
        no_id2 = self.vc.findViewByIdOrRaise("id/no_id/2")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/permission_title", _v)
        com_whatsapp___id_permission_title = self.vc.findViewByIdOrRaise("com.whatsapp:id/permission_title")
        self.device.Log.d(TAG, "finding view with text=u'Restore a backup'", _v)
        com_whatsapp___id_permission_title = self.vc.findViewWithTextOrRaise(u'Restore a backup')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/permission_message", _v)
        com_whatsapp___id_permission_message = self.vc.findViewByIdOrRaise("com.whatsapp:id/permission_message")
        self.device.Log.d(TAG,
                          "finding view with text=u'To find and restore your backup from Google Drive, allow WhatsApp to access your contacts, photos and other media.'",
                          _v)
        com_whatsapp___id_permission_message = self.vc.findViewWithTextOrRaise(
            u'To find and restore your backup from Google Drive, allow WhatsApp to access your contacts, photos and other media.')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/cancel", _v)
        com_whatsapp___id_cancel = self.vc.findViewByIdOrRaise("com.whatsapp:id/cancel")
        self.device.Log.d(TAG, "finding view with text=u'CANCEL'", _v)
        com_whatsapp___id_cancel = self.vc.findViewWithTextOrRaise(u'CANCEL')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/submit", _v)
        com_whatsapp___id_submit = self.vc.findViewByIdOrRaise("com.whatsapp:id/submit")
        self.device.Log.d(TAG, "finding view with text=u'CONTINUE'", _v)
        com_whatsapp___id_submit = self.vc.findViewWithTextOrRaise(u'CONTINUE')

        self.device.Log.d(TAG, "touching view with text=u'CANCEL'", _v)
        self.vc.findViewWithTextOrRaise(u'CANCEL').touch()
        self.vc.sleep(_s)
        self.device.Log.d(TAG, "dumping content of window=-1", _v)
        self.vc.dump(window=-1)

        self.device.Log.d(TAG, "finding view with id=id/no_id/1", _v)
        no_id1 = self.vc.findViewByIdOrRaise("id/no_id/1")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/title", _v)
        com_whatsapp___id_title = self.vc.findViewByIdOrRaise("com.whatsapp:id/title")
        self.device.Log.d(TAG, "finding view with text=u'Profile info'", _v)
        com_whatsapp___id_title = self.vc.findViewWithTextOrRaise(u'Profile info')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/reg_scroll_view", _v)
        com_whatsapp___id_reg_scroll_view = self.vc.findViewByIdOrRaise("com.whatsapp:id/reg_scroll_view")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/biz_info_description", _v)
        com_whatsapp___id_biz_info_description = self.vc.findViewByIdOrRaise("com.whatsapp:id/biz_info_description")
        self.device.Log.d(TAG, "finding view with text=u'Please provide your name and an optional profile photo'", _v)
        com_whatsapp___id_biz_info_description = self.vc.findViewWithTextOrRaise(
            u'Please provide your name and an optional profile photo')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/change_photo_btn", _v)
        com_whatsapp___id_change_photo_btn = self.vc.findViewByIdOrRaise("com.whatsapp:id/change_photo_btn")
        self.device.Log.d(TAG, "finding view with content-description=u'''Profile photo'''", _v)
        com_whatsapp___id_change_photo_btn = self.vc.findViewWithContentDescriptionOrRaise(u'''Profile photo''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_name", _v)
        com_whatsapp___id_registration_name = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_name")
        self.device.Log.d(TAG, "finding view with text=u'Type your name here'", _v)
        com_whatsapp___id_registration_name = self.vc.findViewWithTextOrRaise(u'Type your name here')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/emoji_btn", _v)
        com_whatsapp___id_emoji_btn = self.vc.findViewByIdOrRaise("com.whatsapp:id/emoji_btn")
        self.device.Log.d(TAG, "finding view with content-description=u'''Emoji'''", _v)
        com_whatsapp___id_emoji_btn = self.vc.findViewWithContentDescriptionOrRaise(u'''Emoji''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/register_name_accept", _v)
        com_whatsapp___id_register_name_accept = self.vc.findViewByIdOrRaise("com.whatsapp:id/register_name_accept")
        self.device.Log.d(TAG, "finding view with text=u'NEXT'", _v)
        com_whatsapp___id_register_name_accept = self.vc.findViewWithTextOrRaise(u'NEXT')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/shortcut_layout", _v)
        com_whatsapp___id_shortcut_layout = self.vc.findViewByIdOrRaise("com.whatsapp:id/shortcut_layout")
        self.device.Log.d(TAG, "finding view with id=id/no_id/10", _v)
        no_id10 = self.vc.findViewByIdOrRaise("id/no_id/10")
        self.device.Log.d(TAG, "finding view with text=u'Include WhatsApp shortcut on home screen'", _v)
        no_id10 = self.vc.findViewWithTextOrRaise(u'Include WhatsApp shortcut on home screen')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/cbx_app_shortcut", _v)
        com_whatsapp___id_cbx_app_shortcut = self.vc.findViewByIdOrRaise("com.whatsapp:id/cbx_app_shortcut")

        self.vc.findViewWithTextOrRaise(u'Type your name here').setText(u"Adnan")
        self.vc.sleep(_s)
        self.device.Log.d(TAG, "dumping content of window=-1", _v)
        self.vc.dump(window=-1)

        self.device.Log.d(TAG, "finding view with id=id/no_id/1", _v)
        no_id1 = self.vc.findViewByIdOrRaise("id/no_id/1")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/title", _v)
        com_whatsapp___id_title = self.vc.findViewByIdOrRaise("com.whatsapp:id/title")
        self.device.Log.d(TAG, "finding view with text=u'Profile info'", _v)
        com_whatsapp___id_title = self.vc.findViewWithTextOrRaise(u'Profile info')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/reg_scroll_view", _v)
        com_whatsapp___id_reg_scroll_view = self.vc.findViewByIdOrRaise("com.whatsapp:id/reg_scroll_view")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/biz_info_description", _v)
        com_whatsapp___id_biz_info_description = self.vc.findViewByIdOrRaise("com.whatsapp:id/biz_info_description")
        self.device.Log.d(TAG, "finding view with text=u'Please provide your name and an optional profile photo'", _v)
        com_whatsapp___id_biz_info_description = self.vc.findViewWithTextOrRaise(
            u'Please provide your name and an optional profile photo')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/change_photo_btn", _v)
        com_whatsapp___id_change_photo_btn = self.vc.findViewByIdOrRaise("com.whatsapp:id/change_photo_btn")
        self.device.Log.d(TAG, "finding view with content-description=u'''Profile photo'''", _v)
        com_whatsapp___id_change_photo_btn = self.vc.findViewWithContentDescriptionOrRaise(u'''Profile photo''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/registration_name", _v)
        com_whatsapp___id_registration_name = self.vc.findViewByIdOrRaise("com.whatsapp:id/registration_name")
        self.device.Log.d(TAG, "finding view with text=u'Adnan'", _v)
        com_whatsapp___id_registration_name = self.vc.findViewWithTextOrRaise(u'Adnan')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/name_counter_tv", _v)
        com_whatsapp___id_name_counter_tv = self.vc.findViewByIdOrRaise("com.whatsapp:id/name_counter_tv")
        self.device.Log.d(TAG, "finding view with text=u'20'", _v)
        com_whatsapp___id_name_counter_tv = self.vc.findViewWithTextOrRaise(u'20')
        self.device.Log.d(TAG, "finding view with content-description=u'''20 characters remaining'''", _v)
        com_whatsapp___id_name_counter_tv = self.vc.findViewWithContentDescriptionOrRaise(
            u'''20 characters remaining''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/emoji_btn", _v)
        com_whatsapp___id_emoji_btn = self.vc.findViewByIdOrRaise("com.whatsapp:id/emoji_btn")
        self.device.Log.d(TAG, "finding view with content-description=u'''Emoji'''", _v)
        com_whatsapp___id_emoji_btn = self.vc.findViewWithContentDescriptionOrRaise(u'''Emoji''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/register_name_accept", _v)
        com_whatsapp___id_register_name_accept = self.vc.findViewByIdOrRaise("com.whatsapp:id/register_name_accept")
        self.device.Log.d(TAG, "finding view with text=u'NEXT'", _v)
        com_whatsapp___id_register_name_accept = self.vc.findViewWithTextOrRaise(u'NEXT')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/shortcut_layout", _v)
        com_whatsapp___id_shortcut_layout = self.vc.findViewByIdOrRaise("com.whatsapp:id/shortcut_layout")
        self.device.Log.d(TAG, "finding view with id=id/no_id/11", _v)
        no_id11 = self.vc.findViewByIdOrRaise("id/no_id/11")
        self.device.Log.d(TAG, "finding view with text=u'Include WhatsApp shortcut on home screen'", _v)
        no_id11 = self.vc.findViewWithTextOrRaise(u'Include WhatsApp shortcut on home screen')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/cbx_app_shortcut", _v)
        com_whatsapp___id_cbx_app_shortcut = self.vc.findViewByIdOrRaise("com.whatsapp:id/cbx_app_shortcut")

        self.device.Log.d(TAG, "touching view with text=u'NEXT'", _v)
        self.vc.findViewWithTextOrRaise(u'NEXT').touch()
        self.vc.sleep(_s)
        self.device.Log.d(TAG, "dumping content of window=-1", _v)
        self.vc.dump(window=-1)

        self.device.Log.d(TAG, "finding view with id=id/no_id/1", _v)
        no_id1 = self.vc.findViewByIdOrRaise("id/no_id/1")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/pager", _v)
        com_whatsapp___id_pager = self.vc.findViewByIdOrRaise("com.whatsapp:id/pager")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/conversations_empty_permission_denied", _v)
        com_whatsapp___id_conversations_empty_permission_denied = self.vc.findViewByIdOrRaise(
            "com.whatsapp:id/conversations_empty_permission_denied")
        self.device.Log.d(TAG, "finding view with id=id/no_id/4", _v)
        no_id4 = self.vc.findViewByIdOrRaise("id/no_id/4")
        self.device.Log.d(TAG, "finding view with id=id/no_id/5", _v)
        no_id5 = self.vc.findViewByIdOrRaise("id/no_id/5")
        self.device.Log.d(TAG,
                          "finding view with text=u'To help you message friends and family on WhatsApp, allow WhatsApp access to your contacts. Tap Settings > Permissions, and turn Contacts on.'",
                          _v)
        no_id5 = self.vc.findViewWithTextOrRaise(
            u'To help you message friends and family on WhatsApp, allow WhatsApp access to your contacts. Tap Settings > Permissions, and turn Contacts on.')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/button_open_permission_settings", _v)
        com_whatsapp___id_button_open_permission_settings = self.vc.findViewByIdOrRaise(
            "com.whatsapp:id/button_open_permission_settings")
        self.device.Log.d(TAG, "finding view with text=u'SETTINGS'", _v)
        com_whatsapp___id_button_open_permission_settings = self.vc.findViewWithTextOrRaise(u'SETTINGS')
        self.device.Log.d(TAG, "finding view with id=id/no_id/7", _v)
        no_id7 = self.vc.findViewByIdOrRaise("id/no_id/7")
        self.device.Log.d(TAG, "finding view with text=u'WhatsApp'", _v)
        no_id7 = self.vc.findViewWithTextOrRaise(u'WhatsApp')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/menuitem_search", _v)
        com_whatsapp___id_menuitem_search = self.vc.findViewByIdOrRaise("com.whatsapp:id/menuitem_search")
        self.device.Log.d(TAG, "finding view with content-description=u'''Search'''", _v)
        com_whatsapp___id_menuitem_search = self.vc.findViewWithContentDescriptionOrRaise(u'''Search''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/menuitem_overflow", _v)
        com_whatsapp___id_menuitem_overflow = self.vc.findViewByIdOrRaise("com.whatsapp:id/menuitem_overflow")
        self.device.Log.d(TAG, "finding view with content-description=u'''More options'''", _v)
        com_whatsapp___id_menuitem_overflow = self.vc.findViewWithContentDescriptionOrRaise(u'''More options''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/home_tab_layout", _v)
        com_whatsapp___id_home_tab_layout = self.vc.findViewByIdOrRaise("com.whatsapp:id/home_tab_layout")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/icon", _v)
        com_whatsapp___id_icon = self.vc.findViewByIdOrRaise("com.whatsapp:id/icon")
        self.device.Log.d(TAG, "finding view with content-description=u'''Camera'''", _v)
        com_whatsapp___id_icon = self.vc.findViewWithContentDescriptionOrRaise(u'''Camera''')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/home_tab_layout", _v)
        com_whatsapp___id_home_tab_layout = self.vc.findViewByIdOrRaise("com.whatsapp:id/home_tab_layout")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/tab", _v)
        com_whatsapp___id_tab = self.vc.findViewByIdOrRaise("com.whatsapp:id/tab")
        self.device.Log.d(TAG, "finding view with text=u'CHATS'", _v)
        com_whatsapp___id_tab = self.vc.findViewWithTextOrRaise(u'CHATS')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/home_tab_layout", _v)
        com_whatsapp___id_home_tab_layout = self.vc.findViewByIdOrRaise("com.whatsapp:id/home_tab_layout")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/tab", _v)
        com_whatsapp___id_tab = self.vc.findViewByIdOrRaise("com.whatsapp:id/tab")
        self.device.Log.d(TAG, "finding view with text=u'STATUS'", _v)
        com_whatsapp___id_tab = self.vc.findViewWithTextOrRaise(u'STATUS')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/home_tab_layout", _v)
        com_whatsapp___id_home_tab_layout = self.vc.findViewByIdOrRaise("com.whatsapp:id/home_tab_layout")
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/tab", _v)
        com_whatsapp___id_tab = self.vc.findViewByIdOrRaise("com.whatsapp:id/tab")
        self.device.Log.d(TAG, "finding view with text=u'CALLS'", _v)
        com_whatsapp___id_tab = self.vc.findViewWithTextOrRaise(u'CALLS')
        self.device.Log.d(TAG, "finding view with id=com.whatsapp:id/fabText", _v)
        com_whatsapp___id_fabText = self.vc.findViewByIdOrRaise("com.whatsapp:id/fabText")
        self.device.Log.d(TAG, "finding view with text=u'SEND MESSAGE'", _v)
        com_whatsapp___id_fabText = self.vc.findViewWithTextOrRaise(u'SEND MESSAGE')
        self.device.Log.d(TAG, "finding view with content-description=u'''Send message'''", _v)
        com_whatsapp___id_fabText = self.vc.findViewWithContentDescriptionOrRaise(u'''Send message''')


if __name__ == '__main__':
    CulebraTests.main()
