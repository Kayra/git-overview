from rest_framework import generics

from .models import Contributor, PullRequest, Issue, User
from .serializers import ContributorSerializer, PullRequestSerializer, IssueSerializer, UserSerializer


class ContributorList(generics.ListAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class PullRequestList(generics.ListAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer


class IssueList(generics.ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class MostMergesUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
