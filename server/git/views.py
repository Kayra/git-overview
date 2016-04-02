from rest_framework import generics

from .models import Repository, Contributor, PullRequest, Issue, User
from .serializers import RepositorySerializer, ContributorSerializer, PullRequestSerializer, IssueSerializer, UserSerializer


class RepositoryList(generics.ListAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer


class ContributorList(generics.ListAPIView):
    queryset = Contributor.objects.all().order_by('position')[:5]
    serializer_class = ContributorSerializer


class PullRequestList(generics.ListAPIView):
    queryset = PullRequest.objects.all().order_by('position')[:5]
    serializer_class = PullRequestSerializer


class IssueList(generics.ListAPIView):
    queryset = Issue.objects.all().order_by('position')[:5]
    serializer_class = IssueSerializer


class MostMergesUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
