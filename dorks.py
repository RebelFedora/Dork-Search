import requests

def search_github_dorks(query, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    params = {
        'q': query
    }
    try:
        response = requests.get('https://api.github.com/search/code', headers=headers, params=params)
        response.raise_for_status()
        results = response.json()
        return results.get('items', [])
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def main():
    # Enter your GitHub token
    github_token = input("Enter your GitHub token: ")

    # Enter the dork query you want to search for
    dork_query = input("Enter the dork query you want to search for: ")

    results = search_github_dorks(dork_query, github_token)
    for result in results:
        print(f"Repository: {result['repository']['full_name']}")
        print(f"File: {result['path']}")
        print(f"URL: {result['html_url']}")
        print()

if __name__ == "__main__":
    main()