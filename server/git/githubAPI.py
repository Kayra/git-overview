from github import Github


class Git(object):

    def __init__(self):
        git = Github()
        repoId = 1431547
        self.repository = git.get_repo(repoId)

    def contributors(self):
        return self.repository.get_contributors()

    def openPullRequests(self):
        return self.repository.get_pulls()

    def closedPullRequests(self):
        return self.repository.get_pulls(state='closed')

    def issues(self):
        return self.repository.get_issues()
