from pylonsapp.tests import *

class TestStudyController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='study', action='index'))
        # Test response...
