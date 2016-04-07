from .githubAPI import Git
from .models import Repository, Contributor, PullRequest, Issue, User

gitData = Git()


def repositoryDetails():
    """
    Updates the model with the details of the repository.
    The repository is composed of:
    name(string), url(string)
    """

    repository = gitData.repository

    try:
        repositoryObject = Repository.objects.get(id=1)
        repositoryObject.name = repository.name
        repositoryObject.url = repository.html_url
    except Repository.DoesNotExist:
        repositoryObject = Repository(name=repository.name, url=repository.html_url)

    repositoryObject.save()


def topContributors():
    """
    Updates the model with the top five contributors to the repository.
    Each contributor is composed of:
    name(string), contributions(int), url(string), avatar_url(string)
    """

    contributors = gitData.contributors()

    contributorsList = []

    for contributor in contributors:
        try:
            if "Check your git settings!" not in contributor.name:
                name = contributor.name.encode('utf-8')
                contributions = contributor.contributions
                url = contributor.html_url
                avatarUrl = contributor.avatar_url
                contributorsList.append((contributions, name, url, avatarUrl))
        except (AttributeError, TypeError):
            pass

    sorted(contributorsList)

    for index, contributor in enumerate(contributorsList[:5]):
        defaultValues = {
            'contributions': contributor[0],
            'url': contributor[2],
            'avatarUrl': contributor[3],
            'position': index
        }
        Contributor.objects.update_or_create(name=contributor[1].decode('utf-8'), defaults=defaultValues)


def recentPullRequests():
    """
    Updates the model with the five most recent pull requests.
    Each pull request is composed of:
    title(string), creationDate(datetime.datetime), url(string), body(string)
    """

    pullRequests = gitData.openPullRequests()

    pullRequestList = []

    for pullRequest in pullRequests:
        title = pullRequest.title
        creationDate = pullRequest.created_at.date()
        url = pullRequest.html_url
        body = pullRequest.body
        pullRequestList.append((title, creationDate, url, body))

    sorted(pullRequestList)

    for index, pullRequest in enumerate(pullRequestList[:5]):
        PullRequest.objects.update_or_create(title=pullRequest[0], creationDate=pullRequest[1], url=pullRequest[2], body=pullRequest[3], position=index)


def recentIssues():
    """
    Updates the model with the five most recent issues.
    Each issue is composed of:
    title(string), creationDate(datetime.datetime), url(string), body(string)
    """

    issues = gitData.issues()

    issueList = []

    for issue in issues:
        title = issue.title
        creationDate = issue.created_at.date()
        url = issue.html_url
        body = issue.body
        issueList.append((title, creationDate, url, body))

    sorted(issueList)

    for index, issue in enumerate(issueList[:5]):
        Issue.objects.update_or_create(title=issue[0], creationDate=issue[1], url=issue[2], body=issue[3], position=index)


def mostMergesUser():
    """
    Updates the model with the user who has merged the most pull requests.
    The user is composed of:
    name(string)
    """

    pullRequests = gitData.closedPullRequests()

    pullsRequestNamesList = []

    for pullRequest in pullRequests:
        try:
            pullsRequestNamesList.append((pullRequest.merged_by.name.encode('utf-8')))
        except AttributeError:
            pass

    userName = max(set(pullsRequestNamesList), key=pullsRequestNamesList.count)

    merges = pullsRequestNamesList.count(userName)

    for pullRequest in pullRequests:
        try:
            if userName in pullRequest.merged_by.name.encode('utf-8'):
                url = pullRequest.merged_by.html_url
                avatarUrl = pullRequest.merged_by.avatar_url
                break
        except AttributeError:
            pass

    try:
        userObject = User.objects.get(id=1)
        userObject.name = userName.decode('utf-8')
        userObject.merges = merges
        userObject.url = url
        userObject.avatarUrl = avatarUrl
    except User.DoesNotExist:
        userObject = User(name=userName.decode('utf-8'), merges=merges, url=url, avatarUrl=avatarUrl)

    userObject.save()


def updateAPIData():
    repositoryDetails()
    topContributors()
    recentPullRequests()
    recentIssues()
    mostMergesUser()
