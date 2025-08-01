
from django.db import models
from django.shortcuts import reverse

# Your existing Post model
class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf' ,'Draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=3)

    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=50)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    # New: Add a rating field
    RATING_CHOICES = (
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)

    def __str__(self):
        return f'Comment by {self.author_name} on {self.post.title}'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name