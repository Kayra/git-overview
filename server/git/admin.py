from django.contrib import admin
from .models import Contributor, PullRequest, Issue, User

admin.register(Contributor, PullRequest, Issue, User)(admin.ModelAdmin)
