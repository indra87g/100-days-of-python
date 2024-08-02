"""
Day 19 - Github Repo Info
"""

import requests as req


def main(owner, repo):
    api = f"https://api.github.com/repos/{owner}/{repo}"

    response = req.get(api)

    if response.status_code == 200:
        repo_info = response.json()
        print(
            f"""
              Repo Name: {repo_info['name']}
              Description: {repo_info.get('description', 'No description')}
              Owner: {repo_info['owner']['login']}
              Stargazers: {repo_info['stargazers_count']}
              Forks: {repo_info['forks_count']}
              Issues: {repo_info['open_issues_count']}
              URL: {repo_info['html_url']}
              """
        )
    else:
        print("Failed to fetch.")


if __name__ == "__main__":
    owner = input("Enter github username: ")
    repo = input("Enter repo name: ")

    main(owner, repo)
