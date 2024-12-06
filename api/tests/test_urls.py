from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import careers_param_request, careers
class TestUrls(SimpleTestCase):

    def test_careers_list_url_is_resolved(self):
        url = reverse('careers')
        self.assertEquals(resolve(url).func, careers)

    def test_careers_url_with_params_is_resolved(self):
        url = reverse('careers_param_request', kwargs={ 'id': 1 })
        self.assertEquals(resolve(url).func, careers_param_request)