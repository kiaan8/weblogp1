from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user1')
        self.post1 = Post.objects.create(
            title='Post1',
            text='this is the description',
            status=Post.STATUS_CHOICES[0][0],  #Published
            author=self.user


        )
        self.post2 = Post.objects.create(
            title='post2',
            text='this is the description',
            status=Post.STATUS_CHOICES[1][1], #Draft
            author=self.user
        )

    def test_post_model_string(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200 )

    def test_post_title_on_blog(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)

    def test_post_details_on_blog_detail_page(self):
        response = self.client.get('/blog/1')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.author)


    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('post_detail',args=[1000]))
        self.assertEqual(response.status_code, 404)

    


