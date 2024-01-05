from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your tests here.

class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='Test title',
            text="this is a test text",
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user
        )
        cls.post2 = Post.objects.create(title='post2', text='post 2 test', status=Post.STATUS_CHOICES[1][0],
                                         author=cls.user)


    def test_Post_model_str(self):
        self.assertEqual(str(self.post1),self.post1.title)

    def test_post_list_url(self):
       response = self.client.get('/blog/')
       self.assertEqual(response.status_code, 200)
    def test_post_list_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
    def test_post_title_on_blog(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response,self.post1.title)

    def test_detail_view_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)
    def test_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail',args=[self.post1.id]))

    def test_post_details_on_blog_detail_page(self):
        response = self.client.get(reverse('post_detail',args=[self.post1.id]))
        self.assertContains(response,self.post1.title)
        self.assertContains(response,self.post1.text)
    def test_status_404_if_post_does_not_exist(self):
        response = self.client.get(reverse('post_detail',args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_draft_not_show_in_page_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response,self.post1.title)
        self.assertNotContains(response,self.post2.title)

    def test_post_add_view(self):
        response = self.client.post(reverse('post_create'),{
            'title': 'Title 1',
            'text': 'Title 1 text',
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last().title,'Title 1')


    def test_update_view(self):
        response = self.client.post(reverse('post_update',args=[self.post1.id]),{
            'title': 'Updated Title',
            'text': 'Updated Text',
            'status': 'pub',
            'author': self.user.id
        })
        self.assertEqual(response.status_code,302)


    def test_delete_view(self):
        response = self.client.post(reverse('post_delete',args=[self.post1.id]))
        self.assertEqual(response.status_code,302)
