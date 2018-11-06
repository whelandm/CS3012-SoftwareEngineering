from github import Github

# return count of stargazers for all repos
def stargazers(g, u):
    labels = []
    count = []
    for repo in g.get_user(u).get_repos():
        label = repo.name
        current = repo.stargazers_count
        if current != 0:
            labels.append(label)
            count.append(current)
    return labels, count
