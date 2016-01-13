from .githubAPI import Git

gitData = Git()


def topContributors():
    """
    Returns the top five contributors to the repository.
    Each dict in the list is composed of:
    name(string), contributions(int), url(string), avatar_url(string)
    """

    contributors = gitData.contributors()

    contributorsList = []

    for contributor in contributors:
        try:
            name = contributor.name.encode('utf-8')
            contributions = contributor.contributions
            url = contributor.html_url
            avatarUrl = contributor.avatar_url
            contributorsList.append((contributions, name, url, avatarUrl))

        except AttributeError:
            pass

    sorted(contributorsList)

    print(contributorsList)

    contributorsDicts = []

    for contributor in contributorsList[:5]:
        list(contributor)
        contributorsDicts.append({'contributions': contributor[0], 'name': contributor[1].decode("utf-8"), 'url': contributor[2], 'avatarUrl': contributor[3]})

    return(contributorsDicts)


def recentPullRequests():
    """
    Returns the five most recent pull requests.
    Each dict in the list is composed of:
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

    pullRequestDicts = []

    for pullRequest in pullRequestList[:5]:
        list(pullRequest)
        pullRequestDicts.append({'title': pullRequest[0], 'creationDate': str(pullRequest[1]), 'url': pullRequest[2], 'body': pullRequest[3]})

    return(pullRequestDicts)


def recentIssues():
    """
    Returns the five most recent issues.
    Each dict in the list is composed of:
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

    issueDicts = []

    for issue in issueList[:5]:
        list(issue)
        issueDicts.append({'title': issue[0], 'creationDate': str(issue[1]), 'url': issue[2], 'body': issue[3]})

    return(issueDicts)


def mostMergesUser():
    """
    Returns the user who has merged the most pull requests.
    The dictionary is composed of:
    name(string)
    """

    pulls = gitData.closedPullRequests()

    pullsList = []

    for pull in pulls:
        try:
            print(pull.merged_by.name.encode('utf-8'))
            pullsList.append((pull.merged_by.name.encode('utf-8')))
        except AttributeError:
            pass

    name = max(set(pullsList), key=pullsList.count)

    return({'name': name.decode("utf-8")})
