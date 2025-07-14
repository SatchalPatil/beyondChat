import json
from reddit_extract import fetch_user_data
from extract_persona import build_persona

def main():

    user_url = input("Enter Reddit user profile URL (e.g., https://www.reddit.com/user/kojied/): ")
    
    username = user_url.split('/user/')[-1].strip('/')
    
    user_data = fetch_user_data(username)
    
    if user_data:
        # Save Reddit data to JSON file
        reddit_data_file = f"{username}_reddit_data.json"
        try:
            with open(reddit_data_file, 'w', encoding='utf-8') as f:
                json.dump(user_data, f, indent=4, ensure_ascii=False)
            print(f"Reddit data saved to {reddit_data_file}")
        except Exception as e:
            print(f"Error saving JSON to {reddit_data_file}: {str(e)}")
            return
        
        # Build and save user persona
        persona_file = f"{username}_persona.txt"
        build_persona(reddit_data_file, persona_file)
        print(f"Persona saved to {persona_file}")
    else:
        print("Failed to fetch user data.")

if __name__ == "__main__":
    main()