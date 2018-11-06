from github import Github
import os
import numpy as np
import matplotlib.pyplot as plt

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

#function to display data as pie chart
def displayPie(data, labels):
    plt.figure(figsize=(20,20))
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=0)
    plt.axis('equal')
    plt.show()
#function to display data as bar chart
def displayBar(data, labels, title):
    y_pos = np.arange(len(data))
    plt.bar(y_pos, data, align='center', alpha=0.5)
    plt.xticks(y_pos, labels)
    plt.title(title)
    plt.show()
