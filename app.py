import streamlit as st
import pickle
import math

# -------------------------------
# Recommendation Function
# -------------------------------
def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_idx]
    movies_list_idx = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list_idx:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[movie_id].title)
    
    return recommended_movies

# -------------------------------
# Load Data
# -------------------------------
movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))
# -------------------------------
# Streamlit Dashboard
# -------------------------------
st.set_page_config(page_title="Movie Recommender")
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox('Select a movie:', movies_list)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.subheader(f'Top 5 Movies Similar to "{selected_movie_name}":')

    # Determine number of columns per row (2 in your case)
    num_cols = 2
    rows = math.ceil(len(recommendations)/num_cols)

    for i in range(rows):
        cols = st.columns(num_cols)
        for j, col in enumerate(cols):
            idx = i*num_cols + j
            if idx < len(recommendations):
                movie = recommendations[idx]
                col.markdown(
    f"""
    <a href="{movie_links.get(movie, '#')}" target="_blank" style="text-decoration:none">
        <div style="
            border:2px solid #28a745; 
            padding:20px; 
            border-radius:10px; 
            background-color:#1e1e1e; 
            color:white; 
            text-align:center; 
                min-height:100px; 
            display:flex; 
            justify-content:center; 
            align-items:center; 
            font-size:18px; 
            font-weight:bold; 
            margin-bottom:10px;
        ">
            {movie}
        </div>
    </a>
    """,
    unsafe_allow_html=True
)