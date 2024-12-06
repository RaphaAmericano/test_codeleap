from django.test import TestCase

from base.models import Post


class TestModels(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='test', content='test')

    def test_post(self):
        self.assertEquals(self.post.title, 'test')