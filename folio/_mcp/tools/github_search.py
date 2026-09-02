from github import Github
from folio.config import github_token

def search_github(query: str):
    """search github for repositories, open source code, projects, and developers"""
    try:
        g = Github(github_token) if github_token else Github()

        repos = g.search_repositories(query = query, sort = "stars")

        output = []

        for repo in repos[:5]:
            output.append({
                "name"        : repo.full_name,
                "description" : repo.description,
                "stars"       : repo.stargazers_count,
                "url"         : repo.html_url
            })
        return output
    except Exception as e:
        return f"> GitHub search failed: {str(e)}"
