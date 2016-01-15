from django.db import models


class Contributor(models.Model):
    name = models.CharField(max_length=255)
    contributions = models.IntegerField()
    url = models.CharField(max_length=255)
    avatarUrl = models.CharField(max_length=255)
    position = models.IntegerField()


class PullRequest(models.Model):
    title = models.CharField(max_length=255)
    creationDate = models.DateField()
    url = models.CharField(max_length=255)
    body = models.TextField()
    position = models.IntegerField()


class Issue(models.Model):
    title = models.CharField(max_length=255)
    creationDate = models.DateField()
    url = models.CharField(max_length=255)
    body = models.TextField()
    position = models.IntegerField()


class User(models.Model):
    name = models.CharField(max_length=255)
    merges = models.IntegerField()
    url = models.CharField(max_length=255)
    avatarUrl = models.CharField(max_length=255)
