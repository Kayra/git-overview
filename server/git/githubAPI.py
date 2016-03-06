from github import Github


class Git:

    git = Github()

    repoId = 1431547

    repository = git.get_repo(repoId)

    def contributors(self):
        return Git.repository.get_contributors()

    def openPullRequests(self):
        return Git.repository.get_pulls()

    def closedPullRequests(self):
        return Git.repository.get_pulls(state='closed')

    def issues(self):
        return Git.repository.get_issues()
