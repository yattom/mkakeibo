import unittest
import datetime

import web_main

class mock_today(object):
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def __enter__(self):
        self.org_date = datetime.date
        d = self.date
        class MockDate(object):
            def today(self):
                return d
        datetime.date = MockDate()

    def __exit__(self, type, value, traceback):
        datetime.date = self.org_date

class IndexTest(unittest.TestCase):
    def setUp(self):
        class RenderSpy(object):
            def __init__(self, org):
                self.org = org

            def index(self, form, *args):
                self.received_form = form
                return self.org.index(form, *args)
        web_main.render = RenderSpy(web_main.render)

    def tearDown(self):
        web_main.render = web_main.render.org


    def test_get(self):
        target = web_main.Index()
        content = target.GET()
        self.assertIsNotNone(content)

    def test_form_default_is_today(self):
        with mock_today(2001, 2, 3):
            target = web_main.Index()
            content = target.GET()
            form = web_main.render.received_form
            self.assertEqual(2, form['month'].value)
            self.assertEqual(3, form['day'].value)
