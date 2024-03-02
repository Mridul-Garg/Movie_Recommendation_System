import streamlit as st
import pickle
import pandas as pd
import requests
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c76d7b7837224129d1b9d00078481406&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dist = similarity[movie_index]
    movies_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]
    posters=[]
    recommended_movies=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id

        recommended_movies.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return recommended_movies,posters

st.title('Movie Recommender System')
selected_movie = st.selectbox(
'Enter a movie you like or recently watched: ',
movies['title'].values)
if st.button('Recommend'):
    name,post=recommend(selected_movie)

    col1,col2,col3,col4,col5= st.columns([1,1,1,1,1],gap='medium')
    with col1:
        st.text(name[0])
        st.image(post[0])

    with col2:
        st.text(name[1])
        st.image(post[1])

    with col3:
        st.text(name[2])
        st.image(post[2])

    with col4:
        st.text(name[3])
        st.image(post[3])

    with col5:
        st.text(name[4])
        st.image(post[4])