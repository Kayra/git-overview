from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getContributors(request):
    """
    Returns the five users with the most contributions to the project.
    """
    pass


@api_view(['GET'])
def getPullRequests(request):
    """
    Returns the five most recently opened pull requests.
    """
    pass


@api_view(['GET'])
def getIssues(request):
    """
    Returns the five most recently opened issues.
    """
    pass


@api_view(['GET'])
def getMostMerges(request):
    """
    Returns the user who has merged the most pull requests.
    """
    pass
