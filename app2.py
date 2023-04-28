import streamlit as st 
import pickle
import pandas as pd
import requests
import joblib



def fetch_poster(movie_id):
    url= "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    # print("Full path     : ",full_path)
    return full_path



def recomend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:13]
    recomeneded_movies_poster=[]
    recomeneded_movies=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recomeneded_movies.append(movies.iloc[i[0]].title)
        recomeneded_movies_poster.append(fetch_poster(movie_id))
        # print(fetch_poster(movie_id))
    return recomeneded_movies,recomeneded_movies_poster



# moviesDic=pickle.load(open('movieDic.pkl','rb'))
moviesDic=joblib.load('movieDic.joblib')
# similarity=pickle.load(open('similarity.pkl','rb'))
similarity=joblib.load('similarity.joblib')




movies=pd.DataFrame(moviesDic)

st.title("Movies Recommender System")

selected_movie=st.selectbox("Select a Mvoies",movies['title'].values)

if st.button('Recommend'):
    names,poster=recomend(selected_movie)
    col1,col2,col3,col4=st.columns(4)
    col5,col6,col7,col8=st.columns(4)
    col9,col10,col11,col12=st.columns(4)

    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image([poster[1]])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
    with col6:
        st.text(names[5])
        st.image(poster[5])
    with col7:
        st.text(names[6])
        st.image([poster[6]])
    with col8:
        st.text(names[7])
        st.image(poster[7])

    with col9:
        st.text(names[8])
        st.image(poster[8])
    with col10:
        st.text(names[9])
        st.image(poster[9])
    with col11:
        st.text(names[10])
        st.image(poster[10])
    with col12:
        st.text(names[11])
        st.image(poster[11])
   