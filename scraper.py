from bs4 import BeautifulSoup
import re

def extract_user_info(html_file):
    """
    Extract user information from the mock forum HTML file.
    Returns a list of dictionaries containing user data.
    """
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    users_data = []
    
    for post in soup.find_all('div', class_='post'):
        user_info = post.find('div', class_='user-info').text.strip()
        post_content = post.find('div', class_='post-content').text.strip()
        
        # Extract username and email using regex
        username_match = re.search(r'User: (\w+)', user_info)
        email_match = re.search(r'Email: ([\w.@]+)', user_info)
        
        if username_match and email_match:
            users_data.append({
                'username': username_match.group(1),
                'email': email_match.group(1),
                'post_content': post_content
            })
    
    return users_data

if __name__ == "__main__":
    # Test the scraper
    users = extract_user_info('forum.html')
    print("\nExtracted User Information:")
    print("-" * 50)
    for user in users:
        print(f"Username: {user['username']}")
        print(f"Email: {user['email']}")
        print(f"Post: {user['post_content']}")
        print("-" * 50) 