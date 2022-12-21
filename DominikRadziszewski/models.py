from django.db import models


class Category(models.Model):
    nameOfCategoryPolish = models.CharField(null=False, blank=False, max_length=32, default="Strona Internetowa")
    nameOfCategoryEnglish = models.CharField(null=False, blank=False, max_length=32, default="Website")

    def __str__(self):
        return self.nameOfCategoryPolish


class Contact(models.Model):
    emailOfContact = models.CharField(null=False, blank=False, max_length=64)
    phoneOfContact = models.IntegerField(null=False, blank=False)
    descriptionOfContactPolish = models.TextField(null=False, blank=False, max_length=512)
    descriptionOfContactEnglish = models.TextField(null=False, blank=False, max_length=512)
    pictureOfContact = models.ImageField(null=False, blank=False)

    def __str__(self):
        return "Dominik Radziszewski"


class Post(models.Model):
    nameOfPost = models.CharField(null=False, blank=False, max_length=64)
    categoryOfPost = models.ForeignKey(Category, on_delete=models.CASCADE)
    descriptionOfPostPolish = models.TextField(null=False, blank=False, max_length=1024)
    descriptionOfPostEnglish = models.TextField(null=False, blank=False, max_length=1024)
    linkToSite = models.CharField(null=True, blank=True, max_length=256)
    samplePrice = models.PositiveSmallIntegerField(null=True, blank=True, default=300)

    def __str__(self):
        return self.nameOfPost


class PicturesOfPost(models.Model):
    whichPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    pictureOfPost = models.ImageField(upload_to="pictures_of_post", null=True, blank=True)
    descriptionOfPicturePolish = models.TextField(null=True, blank=True, max_length=1024)
    descriptionOfPictureEnglish = models.TextField(null=True, blank=True, max_length=1024)

    def __str__(self):
        return self.picture_of_post()

    def picture_of_post(self):
        return "{}".format(self.whichPost)
