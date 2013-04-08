import unittest

import web_main

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

    def test_form_default_values(self):
        target = web_main.Index()
        content = target.GET()
        form = web_main.render.received_form
        self.assertEqual(4, form['month'].value)
        self.assertEqual(8, form['day'].value)
