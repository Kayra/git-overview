from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=512)


class Contributor(models.Model):
    name = models.CharField(max_length=255)
    contributions = models.IntegerField()
    url = models.CharField(max_length=512)
    avatarUrl = models.CharField(max_length=255)

    class Meta:
        ordering = ['-contributions']


class PullRequest(models.Model):
    title = models.CharField(max_length=255)
    creationDate = models.DateField()
    url = models.CharField(max_length=512)
    body = models.TextField()

    class Meta:
        ordering = ['-creationDate']


class Issue(models.Model):
    title = models.CharField(max_length=255)
    creationDate = models.DateField()
    url = models.CharField(max_length=512)
    body = models.TextField()

    class Meta:
        ordering = ['-creationDate']


class User(models.Model):
    name = models.CharField(max_length=255)
    merges = models.IntegerField()
    url = models.CharField(max_length=512)
    avatarUrl = models.CharField(max_length=255)
