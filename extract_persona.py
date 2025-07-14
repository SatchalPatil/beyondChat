import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def configure_gemini():
    """Configure the Gemini API client."""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY in environment variables.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash')

def build_persona(input_json_file, output_persona_file):
    """
    Build a user persona from Reddit data using the Gemini API and save it to a text file.
    
    Args:
        input_json_file (str): Path to the JSON file containing Reddit data
        output_persona_file (str): Path to save the persona text file
    """
    try:
        # Read JSON data
        with open(input_json_file, 'r', encoding='utf-8') as f:
            reddit_data = json.load(f)
        
        username = reddit_data.get('username', 'Unknown')
        posts = reddit_data.get('posts', [])
        comments = reddit_data.get('comments', [])
        
        print(f"Parsing JSON: {len(posts)} posts and {len(comments)} comments found for user {username}")
        
        # Prepare text for LLM
        content = "User Reddit Data:\n"
        content += f"Username: {username}\n\nPosts:\n"
        for post in posts:
            content += f"Post ID: {post['id']}\n"
            content += f"Title: {post['title']}\n"
            content += f"Body: {post.get('body', 'N/A')}\n"
            content += f"URL: {post['url']}\n"
            content += f"Subreddit: {post['subreddit']}\n\n"
        
        content += "Comments:\n"
        for comment in comments:
            content += f"Comment ID: {comment['id']}\n"
            content += f"Body: {comment['body']}\n"
            content += f"URL: {comment['url']}\n"
            content += f"Subreddit: {comment['subreddit']}\n\n"
        
        model = configure_gemini()
        
        #prompt for LLM
        prompt = """
        You are an expert in user persona creation. Analyze the provided Reddit user data (posts and comments) and create a detailed user persona. The persona must follow this exact structure, with the specified categories. For each characteristic, provide a description and cite the specific post or comment by its ID and URL. If insufficient data is available for a category, provide a brief explanation and note that more data is needed.

        Format the persona as follows:
        User Persona: [Username]

        Characteristics

        - Location: [Description of inferred location, e.g., city, state, country, or past locations]
            - Citation: [Post/Comment ID], [URL]
            - [Additional citations as needed]

        - **Age:** [Estimated age range with reasoning, noting if more data is needed]
            - Citation: [Post/Comment ID], [URL]
            - [Additional citations as needed]

        - **Occupation:** [Inferred occupation or professional status with reasoning]
            - Citation: [Post/Comment ID], [URL]
            - [Additional citations as needed]

        - **Interests:** [List of interests inferred from posts/comments]
            - Citation: [Post/Comment ID], [URL]
            - [Additional citations as needed]

        - **Personality Traits:** [Description of personality traits, e.g., observant, cynical]
            - Citation: [Post/Comment ID], [URL]
            - [Additional citations as needed]

        - **Behaviors:** [Observable behaviors, e.g., seeking information online]
            - Citation: [Post/Comment ID], [URL]
            - [Additional citations as needed]

        - **Frustrations:** [Issues or complaints expressed by the user]
            - Citation: [Post/Comment ID], [URL]
            - [Additional citations as needed]

        - **Motivation:** [What keeps the user motivated]
            - Citation: [Post/Comment ID], [URL]
            - [Additional citations as needed]

        Reddit Data:
        {content}
        """
        prompt = prompt.format(content=content)
        
        response = model.generate_content(prompt)
        persona_text = response.text
        
        # Save persona to text file
        with open(output_persona_file, 'w', encoding='utf-8') as f:
            f.write(persona_text)
        
        print(f"Persona generated and saved to {output_persona_file}")
        return True
    
    except Exception as e:
        print(f"Error building persona: {str(e)}")
        return False