#imports
from github import Github
import os
import json

# gathers all data from given repo, sorting individual pieces of data into nodes
# and creating appropriate links between them, as follows:
#                              Repo Name
#      /            /              |           \               \
#  File Count     Size        Language     Stargazers      Contributor Count
#   int         int             str             int             int
#  | | | | |                                               | | | | | | | |
# file names                                              contributor names
# [][][][][]                                              [][][][][][][][]
#                                                        / \
#                                               followers   commits
#                                                 int         int
def getRepo(g, repo_name):
    data = {}
    nodes = []
    links = []
    repo = g.get_repo(repo_name)

    name = {"id":"repo","group":1,"label":repo.name,"level":1}
    nodes.append(name)
    language = {"id":"language","group":1,"label":repo.language,"level":2}
    nodes.append(language)
    size = {"id":"size","group":1,"label":"size: "+ str(repo.size),"level":2}
    nodes.append(size)
    stargazers = {"id":"stargazers","group":1,"label":"stargazers: " + str(repo.stargazers_count),"level":2}
    nodes.append(stargazers)
    link = {"source":"language","target":"repo","strength":2}
    links.append(link)
    link = {"source":"size","target":"repo","strength":2}
    links.append(link)
    link = {"source":"stargazers","target":"repo","strength":2}
    links.append(link)

    nodes, links = countFiles(repo, nodes, links)

    nodes, links = countContributors(repo, nodes, links)

    data["nodes"] = nodes
    data["links"] = links
    return data

#gets and stores all contributors names, commits and follower count
def countContributors(repo, nodes, links):
    count = 0
    for contributor in repo.get_stats_contributors():
        author = contributor.author
        name = {"id":str(count)+"name","group":1,"label":author.name,"level":3}
        nodes.append(name)
        link = {"source":str(count)+"name","target":"contributorscount","strength":1}
        links.append(link)
        follower_count = countFollowers(author)
        follower = {"id":str(count)+"followers","group":1,"label":"followers:" + str(follower_count),"level":4}
        nodes.append(follower)
        link = {"source":str(count)+"followers","target":str(count)+"name","strength":1}
        links.append(link)
        commit = {"id":str(count)+"contributors","group":1,"label":"commits: " + str(contributor.total),"level":4}
        nodes.append(commit)
        link = {"source":str(count)+"contributors","target":str(count)+"name","strength":1}
        links.append(link)
        count = count + 1
    count = {"id":"contributorscount","group":1,"label":"contributors: " + str(count),"level":2}
    nodes.append(count)
    link = {"source":"contributorscount","target":"repo","strength":2}
    links.append(link)
    return nodes, links

#counts followers of given contributor
def countFollowers(contributor):
    count = 0
    for follower in contributor.get_followers():
        count = count+1
    return count

#counts files in given repo and gathers names, adds this info to nodes
def countFiles(repo, nodes, links):
    count = 0
    for file in repo.get_contents(""):
        count = count + 1
        name = {"id":file.name,"group":1,"label":file.name,"level":3}
        nodes.append(name)
        link = {"source":file.name,"target":"filecount","strength":1}
        links.append(link)
    count = {"id":"filecount","group":1,"label":"files: " + str(count),"level":2}
    nodes.append(count)
    link = {"source":"filecount","target":"repo","strength":2}
    links.append(link)
    return nodes, links

#gather data - using authentication token and name of repo
g = Github("authentication token here")
r = 'PyGithub/PyGithub'
data = getRepoData(g, r)
#move data into JSON file for use in index.html
with open('graphFile.json', 'w') as outfile:
    json.dump(data, outfile)
