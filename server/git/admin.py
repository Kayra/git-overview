from django.contrib import admin
from .models import Repository, Contributor, PullRequest, Issue, User

admin.register(Repository, Contributor, PullRequest, Issue, User)(admin.ModelAdmin)
