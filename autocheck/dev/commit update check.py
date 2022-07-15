from github import Github

g = Github("smslsmls", "qaz!@#0808")

for repo in g.get_user().get_repos():
    print(repo.name)