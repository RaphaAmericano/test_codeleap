
from django.test import TestCase
from base.models import Post

class PostModelTestCase(TestCase):
    def setUp(self):

        self.post = Post.objects.create(
            username="joao",
            title='Test Post',
            content='This is a test post.',
        )

    def test_post_creation(self):
        self.assertEqual(self.post.username, 'joao')
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is a test post.')
        self.assertIsNotNone(self.post.created_datetime)
        self.assertIsNotNone(self.post.id)

    