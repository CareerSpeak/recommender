import json
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Function to clean and preprocess text data
def extract_keywords(text):
    # Remove non-alphanumeric characters and convert to lowercase
    text = re.sub(r'[^a-zA-Z0-9\-\'\@\+\.\/\s]', '', str(text))
    text = text.lower()
    return text


# Function to recommend job roles based on keywords
def recommend_job_role(keywords):
    with open('data.json') as json_data:
        job_role_dataset = json.load(json_data)
    vectorizer = TfidfVectorizer()
    keyword_matrix = vectorizer.fit_transform([' '.join(job_role_dataset[job])
                                               for job in job_role_dataset])

    user_keywords = ' '.join(keywords)
    user_vector = vectorizer.transform([user_keywords])

    similarities = cosine_similarity(user_vector, keyword_matrix).flatten()
    recommended_job_index = similarities.argmax()
    recommended_job_role = list(job_role_dataset.keys())[recommended_job_index]

    return recommended_job_role
