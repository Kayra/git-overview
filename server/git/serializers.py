from rest_framework import serializers

from .models import Contributor, PullRequest, Issue


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor


class PullRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PullRequest


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
