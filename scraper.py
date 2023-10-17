import pandas as pd
import requests
from dotenv import load_dotenv
import os
import tempfile


# Set up your Google Custom Search Engine (CSE) and obtain an API key
# Replace 'YOUR_API_KEY' and 'YOUR_CSE_ID' with your actual values

API_KEY = ''
CSE_ID = ''

input_file = 'input.csv'

df = pd.read_csv(input_file)

# Function to search Google Custom Search and extract LinkedIn URL
def search_and_get_linkedin_profile(Name, Major, Year):
    search_query = f"{Name} {Major} {Year} Purdue LinkedIn"
    api_url = f"https://www.googleapis.com/customsearch/v1?q={search_query}&key={API_KEY}&cx={CSE_ID}"

    try:
        response = requests.get(api_url)
        data = response.json()
        
        # Extract the first LinkedIn URL from the search results (if available)
        if 'items' in data and len(data['items']) > 0:
            linkedin_url = data['items'][0]['link']
        else:
            linkedin_url = ""
    except Exception as e:
        print(f"Error: {e}")
        linkedin_url = ""
    
    return linkedin_url

# Add a new 'LinkedIn' column with profile URLs to the input.csv file
df['LinkedIn'] = df.apply(lambda row: search_and_get_linkedin_profile(row['Name'], row['Major'], row['Year']), axis=1)

df.to_csv(input_file, index=False)
