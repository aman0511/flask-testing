import unittest

from base import BaseTestCase


class TestMainBlueprint(BaseTestCase):
    ''' Test the blueprint registration'''
    render_templates = False

    def test_index(self):
        response = self.client.get('http://localhost:5000/?email=%22askdj%22',
                                   follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertContext('app', "ad@min.com")
        self.assertTemplateUsed('index.html')
        assert "" == response.data
        self.assert_template_used('index.html')

    def test_other(self):
        response = self.client.get('/test', follow_redirects=True)
        self.assertTemplateUsed('test.html')

if __name__ == '__main__':
    unittest.main()
