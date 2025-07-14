# Reddit Persona Generator

A Python-based tool that scrapes a Reddit user's posts and comments, analyzes them using the Gemini API, and generates a structured Markdown persona profile.

---

## 🔍 Features

- Scrapes up to 100 Reddit posts and 100 comments
- Filters sensitive content to avoid Gemini API moderation blocks
- Generates detailed user persona with:
  - **Location**
  - **Age**
  - **Occupation**
  - **Interests**
  - **Personality Traits**
  - **Behaviors**
  - **Frustrations**
- Includes citations to original Reddit posts/comments
- Exports:
  - Raw data in `.json`
  - Persona in `.txt` (Markdown format)

---

## 🧠 Example Persona Output

# User Persona: Dense_Educator8783

## Characteristics

- **Location**: New York, inferred from r/nyc activity.  
  - Citation: Post ID: abc123, https://www.reddit.com/r/nyc/comments/abc123/

- **Age**: Likely 20–30, based on college references.  
  - Citation: Comment ID: xyz789, https://www.reddit.com/r/nyc/comments/[post_id]/xyz789/

- **Occupation**: Student, inferred from coursework mentions.  
  - Citation: Post ID: def456, https://www.reddit.com/r/college/comments/def456/

- **Interests**: Gaming, social events.  
  - Citation: Comment ID: ghi012, https://www.reddit.com/r/gaming/comments/[post_id]/ghi012/

- **Personality Traits**: Curious, outspoken.  
  - Citation: Comment ID: mno678, https://www.reddit.com/r/nyc/comments/[post_id]/mno678/

- **Behaviors**: Active Reddit user, frequent commenter.  
  - Citation: Comment ID: mno678, https://www.reddit.com/r/nyc/comments/[post_id]/mno678/

- **Frustrations**: Issues with local transportation.  
  - Citation: Post ID: pqr901, https://www.reddit.com/r/nyc/comments/pqr901/
⚙️ Requirements
Python: 3.8 or higher

Python Dependencies
bash
Copy
Edit
pip install praw python-dotenv google-generativeai
API Keys Required
Reddit API

REDDIT_CLIENT_ID

REDDIT_CLIENT_SECRET

Gemini API

GEMINI_API_KEY

🛠️ Setup
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/reddit-persona-generator.git
cd reddit-persona-generator
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Add environment variables

Create a .env file in the project root:

env
Copy
Edit
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
GEMINI_API_KEY=your_gemini_api_key
📁 Project Structure
bash
Copy
Edit
reddit-persona-generator/
│
├── main.py                # Main entry point
├── reddit_extract.py      # Scraper for Reddit data
├── extract_persona.py     # Gemini-based persona generator
├── .env                   # Your API keys (not tracked in git)
├── requirements.txt       # Dependency list
🚀 Usage
Run the script:

bash
Copy
Edit
python main.py
Enter a Reddit profile URL when prompted:

ruby
Copy
Edit
https://www.reddit.com/user/Dense_Educator8783/
The script will:

Fetch Reddit data

Filter sensitive terms

Generate persona via Gemini

Output:

username_reddit_data.json

