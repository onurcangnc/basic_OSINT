import requests

def search_social_media(username):
    social_media_sites = [
        "https://www.facebook.com/{}",
        "https://www.twitter.com/{}",
        "https://www.instagram.com/{}",
        "https://www.linkedin.com/in/{}",
    ]
    
    print("Social Media Profiles:")
    for site in social_media_sites:
        url = site.format(username)
        response = requests.get(url)
        if response.status_code == 200:
            print(f"- {site.format(username)}")
        else:
            print(f"- {site.format(username)} - Not found")

def search_github(username):
    github_url = f"https://api.github.com/users/{username}"
    headers = {"User-Agent": "Your-App-Name"}  # Replace with your app's name

    response = requests.get(github_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("GitHub Profile:")
        print(f"- Name: {data['name']}")
        print(f"- Bio: {data['bio']}")
        print(f"- Repositories: {data['public_repos']}")
    else:
        print("GitHub profile not found.")

# ... add other API functions here ...

if __name__ == "__main__":
    target_username = input("Enter target username: ")

    search_social_media(target_username)
    search_github(target_username)
    # Add calls to other API functions here
