# Generated by Django 3.0 on 2021-11-02 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('link', models.CharField(max_length=500, verbose_name='Link')),
                ('author', models.CharField(max_length=2000, verbose_name='Author')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('vote_count', models.IntegerField(default=0, verbose_name='Amount of upvotes')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=40, verbose_name='Session key')),
                ('rating', models.IntegerField(choices=[(1, 'up'), (-1, 'down')], verbose_name='Rating')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voutes', to='api.Post', verbose_name='article')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Rating',
                'ordering': ('article', 'rating'),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=2000, verbose_name='Author')),
                ('link', models.TextField(max_length=2000, verbose_name='Comment content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.Post', verbose_name='Article')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
