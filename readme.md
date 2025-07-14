Reddit Persona Generator
Overview
This Python script scrapes a Reddit user's posts and comments, analyzes them using the Gemini API, and generates a user persona in a structured Markdown format. The persona includes the following characteristics, each with a description and citations to specific posts or comments:

Location: Inferred location (e.g., city, country).
Age: Estimated age range with reasoning.
Occupation: Inferred occupation or professional status.
Interests: List of interests derived from posts/comments.
Personality Traits: Observed traits (e.g., curious, outspoken).
Behaviors: Notable behaviors (e.g., active Reddit user).
Frustrations: Issues or complaints expressed by the user.

The script includes content filtering to avoid sensitive topics that may trigger the Gemini API's content moderation (e.g., PROHIBITED_CONTENT errors).
Requirements

Python: Version 3.8 or higher.
Dependencies:
praw: For Reddit API access.
python-dotenv: For environment variable management.
google-generativeai: For Gemini API access.


API Keys:
Reddit API credentials (REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET).
Gemini API key (GEMINI_API_KEY).



Setup

Install Dependencies:Install the required Python packages:
pip install praw python-dotenv google-generativeai


Configure Environment Variables:Create a .env file in the project directory with the following:
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
GEMINI_API_KEY=your_gemini_api_key


Obtain Reddit API credentials from Reddit Apps.
Obtain a Gemini API key from Google Cloud.


Project Structure:Ensure the following files are in your project directory:

main.py: Main script to run the program.
reddit_extract.py: Handles Reddit data fetching.
extract_persona.py: Generates the persona using the Gemini API.



Usage

Run the script:python main.py


Enter a Reddit user profile URL when prompted, e.g.:https://www.reddit.com/user/Dense_Educator8783/


The script will:
Fetch up to 100 posts and 100 comments from the user's Reddit profile.
Save the raw data to username_reddit_data.json.
Filter out sensitive content (e.g., posts/comments containing words like "harassing," "violence").
Generate a persona using the Gemini API.
Save the persona to username_persona.txt.



Output
The script produces two files:

username_reddit_data.json: Raw Reddit data (posts and comments) in JSON format.
username_persona.txt: User persona in Markdown format, e.g.:# User Persona: Dense_Educator8783

## Characteristics

- **Location:** New York, inferred from subreddit activity in r/nyc.
    - Citation: Post ID: abc123, https://www.reddit.com/r/nyc/comments/abc123/
- **Age:** Likely 20-30, based on references to college life.
    - Citation: Comment ID: xyz789, https://www.reddit.com/r/nyc/comments/[post_id]/xyz789/
- **Occupation:** Student, inferred from mentions of coursework.
    - Citation: Post ID: def456, https://www.reddit.com/r/college/comments/def456/
- **Interests:** Gaming and social events, based on subreddit participation.
    - Citation: Comment ID: ghi012, https://www.reddit.com/r/gaming/comments/[post_id]/ghi012/
- **Personality Traits:** Curious and outspoken, based on comment tone.
    - Citation: Comment ID: mno678, https://www.reddit.com/r/nyc/comments/[post_id]/mno678/
- **Behaviors:** Active Reddit user, frequently engages in discussions.
    - Citation: Comment ID: mno678, https://www.reddit.com/r/nyc/comments/[post_id]/mno678/
- **Frustrations:** Dissatisfaction with local transportation services.
    - Citation: Post


