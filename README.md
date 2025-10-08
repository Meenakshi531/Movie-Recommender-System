# Movie Recommender System
## Overview
This project implements a content-based movie recommender system using the TMDB 5000 Movie Dataset. By extracting and combining key movie features such as genres, keywords, cast, and crew, the system recommends movies similar to a given title using natural language processing and feature engineering.

## Features
- Reads and merges TMDB movies and credits datasets

- Cleans and preprocesses columns including genres, keywords, cast, and crew (director)

- Extracts relevant features, combines them into a single tag string, and applies stemming for normalization

- Vectorizes movie features using CountVectorizer with the top 5000 features and English stopword filtering

- Computes content similarity using cosine similarity between movies

- Provides movie recommendations based on highest content similarity score

## Dataset
movies_metadata.csv and credits.csv from the TMDB 5000 Movie Dataset

Merged and processed to create a feature-enriched DataFrame with 4806 movies and derived tags column

## Install dependencies using pip:

### text
pip install numpy pandas scikit-learn nltk
Download the TMDB 5000 dataset and place tmdb_5000_movies.csv and tmdb_5000_credits.csv in your working directory.

## Usage
Run the Jupyter notebook Movie-Recommender-System.ipynb.

## Execute all cells sequentially to:

Load and preprocess the data

Train the recommendation model

Use the provided recommend function to get similar movies, e.g.:

python
recommend('Avatar')
This returns a list of the most similar movies.

## Model Details
- Feature columns: overview, genres, keywords, cast, director

- Stemming: Used PorterStemmer from NLTK to reduce words to root form

- Vectorization: Used CountVectorizer with 5000 features

- Similarity: Cosine similarity on vectorized tags

## Evaluation
Recommendations are based on content similarity—evaluated informally by checking the relevance of suggested movies to popular titles.

## Saving the Model
The processed data and similarity matrix are pickled as movies.pkl and similarity.pkl for fast loading and querying.

## Dependencies
Python 3.6+

pandas

numpy

scikit-learn

nltk

## Author
Meenakshi Shukla.

