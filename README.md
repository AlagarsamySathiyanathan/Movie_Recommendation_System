# Bollywood Movie Recommendation System

== Overview

This project is a Content-Based Movie Recommendation System that suggests similar Bollywood movies based on genre similarity.

The system was built using a custom dataset of approximately 4000 movies, where IMDb IDs were collected and detailed movie metadata was extracted, cleaned, and processed before model development.

The application is deployed using Streamlit for an interactive web interface.

== 📸 Application Demo

### 📊 Full Application View
![Full App View](https://github.com/user-attachments/assets/a3ee2e69-7b0f-46da-a294-8172a6b4d416)

### 🔎 Movie Search Interface
![Search UI](https://github.com/user-attachments/assets/ffa97613-5271-40f1-9ecd-ab89735d19c4)

### 🎯 Recommendation Results
![Recommendation Results](https://github.com/user-attachments/assets/c2070dbd-2cf6-48a5-92d6-a0852a644c03)



## Dataset Creation Pipeline

The dataset was created in multiple stages:

Extracted IMDb IDs for movie titles

Retrieved detailed metadata for each movie

## Collected attributes including:

Movie Name

Rating

Genre

Year

Duration

Cast

## Performed data cleaning and null value handling

Standardized genre formatting

## Model Development

The recommendation engine uses a Content-Based Filtering approach.

Technique Used:

TF-IDF Vectorization on movie genres

Cosine similarity computation

Fuzzy title matching using difflib

How It Works:

User enters a movie name

System finds closest matching title

Computes similarity between selected movie and all others

Returns top N most similar movies

Optional actor-based filtering is available

## Features

Genre-based movie recommendations

Fuzzy search for better title matching

Actor-based filtering

Top-N recommendation selection

Interactive Streamlit UI

## Tech Stack

Python

Pandas

NumPy

Scikit-learn

Streamlit

OpenPyXL

📂 Project Structure

├── getting_single_movie_detail
├── getting_imdb_id
├── getting_all_movies_details
├── R_S_deploye.py
├── Bollywood_movies_original_df.xlsx
├── requirements.txt
└── README.md

## Installation & Setup

Clone the repository:

git clone https://github.com/yourusername/bollywood-movie-recommendation.git
cd bollywood-movie-recommendation


Create virtual environment (recommended):

python3 -m venv movie_env
source movie_env/bin/activate   # Mac/Linux


Install dependencies:

pip install -r requirements.txt


Run the application:

streamlit run R_S_deploye.py

## Future Improvements

Add movie overview-based NLP recommendations

Hybrid recommendation (Genre + Rating)

Add movie posters using external API

Deploy on cloud (Streamlit Cloud / Render / AWS)

## Key Learning Outcomes

Built complete data collection pipeline

Implemented content-based filtering system

Applied TF-IDF and cosine similarity

Developed interactive ML web application

Managed dependency issues and environment setup
