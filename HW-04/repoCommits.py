import requests
import json

def getRepoCommits(userID):
    repos_url = f"https://api.github.com/users/{userID}/repos"
    response = requests.get(repos_url)

    repos_data = json.loads(response.text)
    repos_with_commits = []
    
    for repo in repos_data:
        repo_name = repo['name']
        commits_url = f"https://api.github.com/repos/{userID}/{repo_name}/commits"
        commits_response = requests.get(commits_url)

        commits_data = json.loads(commits_response.text)
        num_commits = len(commits_data)
        repos_with_commits.append(f"Repo: {repo_name} Number of commits: {num_commits}")
    
    for repo in repos_with_commits:
        print(repo)

if __name__ == "__main__":
    #userID = input("Enter GitHub username: ")
    userID = 'richkempinski'
    getRepoCommits(userID)