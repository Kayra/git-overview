from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Contributor, PullRequest
from .serializers import ContributorSerializer, PullRequestSerializer

from . import dataInterface


@api_view(['GET'])
def getContributors(request):
    """
    Returns the five users with the most contributions to the project.
    """

    dataInterface.topContributors()

    try:
        contributors = Contributor.objects.all()
    except Contributor.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = ContributorSerializer(contributors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPullRequests(request):
    """
    Returns the five most recently opened pull requests.
    """

    dataInterface.recentPullRequests()

    try:
        pullRequests = PullRequest.objects.all()
    except PullRequest.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = PullRequestSerializer(pullRequests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getIssues(request):
    """
    Returns the five most recently opened issues.
    """

    issueDicts = dataInterface.recentIssues()

    return Response(issueDicts)


@api_view(['GET'])
def getMostMergesUser(request):
    """
    Returns the user who has merged the most pull requests.
    """

    mostMergesUser = dataInterface.mostMergesUser()

    return Response(mostMergesUser)
