# Generated by Django 4.1.3 on 2022-12-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DominikRadziszewski', '0007_post_sampleprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='nameOfCategory',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='descriptionOfContact',
        ),
        migrations.RemoveField(
            model_name='picturesofpost',
            name='descriptionOfPicture',
        ),
        migrations.RemoveField(
            model_name='post',
            name='descriptionOfPost',
        ),
        migrations.AddField(
            model_name='category',
            name='nameOfCategoryEnglish',
            field=models.CharField(default='Website', max_length=32),
        ),
        migrations.AddField(
            model_name='category',
            name='nameOfCategoryPolish',
            field=models.CharField(default='Strona Internetowa', max_length=32),
        ),
        migrations.AddField(
            model_name='contact',
            name='descriptionOfContactEnglish',
            field=models.TextField(default=None, max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='descriptionOfContactPolish',
            field=models.TextField(default=None, max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='pictureOfContact',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='picturesofpost',
            name='descriptionOfPictureEnglish',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='picturesofpost',
            name='descriptionOfPicturePolish',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='descriptionOfPostEnglish',
            field=models.TextField(default=None, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='descriptionOfPostPolish',
            field=models.TextField(default=None, max_length=1024),
            preserve_default=False,
        ),
    ]
