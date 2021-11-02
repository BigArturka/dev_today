from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    link = models.CharField(max_length=500, verbose_name='Link')
    author = models.CharField(max_length=2000, verbose_name='Author')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    vote_count = models.IntegerField(verbose_name="Amount of upvotes", default=0)

    def __str__(self):
        return f'{self.pk}-{self.title}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    author = models.CharField(max_length=2000, verbose_name='Author')
    link = models.TextField(max_length=2000, verbose_name='Comment content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    article = models.ForeignKey('api.Post', related_name='comments',
                                on_delete=models.CASCADE, verbose_name='Article')

    def __str__(self):
        return f'{self.pk}-{self.author}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Vote(models.Model):
    article = models.ForeignKey('api.Post', related_name='voutes', verbose_name='article', on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                                related_name='articles', verbose_name='Author')

    def __str__(self):
        return f'{self.article}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Rating'