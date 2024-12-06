from django.test import TestCase, Client
from django.urls import reverse
from base.models import Post
import json
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.main_url = reverse('careers')
        self.post = Post.objects.create(
            title='Teste Post',
            content='Teste Post Content',
            username='joao'
        )
        self.detail_url = reverse('careers_param_request', kwargs={'id': self.post.id})    

    def test_get_function(self):
        
        response = self.client.get(self.main_url)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_patch_function(self):
        payload = { 'title': 'Teste Post 2 nova versão'}
        
        response = self.client.patch(self.detail_url, data=payload, content_type='application/json' )
        
        self.assertEquals(response.status_code, 200)

        self.post.refresh_from_db()
        self.assertEquals(self.post.title, payload['title'])
        
    def test_delete_function(self):
        response = self.client.delete(self.detail_url)

        self.assertEquals(response.status_code, 204)
        self.assertEquals(Post.objects.count(), 0)