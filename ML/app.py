import streamlit as st #streamlit run app.py
import pickle
from tmdbv3api  import Movie,TMDb

def get_recommendations(title):
    idx = movies[movies['title']==title].index[0]
    sim_score = list(enumerate(cosine_sim[idx]))
    sim_score = sorted(sim_score,key=lambda x:x[1], reverse=True)
    sim_scorse =sim_score[1:11]
    movie_indices = [i[0] for i in sim_scorse]
    titles = []
    images = []
    for i in movie_indices:
        id = movies['id'].iloc[i]
        details = movie.details(id)
        image_path = details['poster_path']
        if image_path:
            image_path = 'https://image.tmdb.org/t/p/w500'+details['poster_path']
        else:
            image_path = 'http://via.placeholder.com/150x200'
        images.append(image_path)
        titles.append(details['title'])
    return titles,images

#프로그램시작
movie = Movie()
tmdb = TMDb()
tmdb.api_key='c668cda4cf75bf267ef2aeffa2da0341' #강사썜꺼
tmdb.language='ko-KR'

movies = pickle.load(open('data/movies.pickle','rb'))
cosine_sim = pickle.load(open('data/cosine_sim.pickle','rb'))
st.set_page_config(layout = 'wide')
st.header('영화추천')

movies_list = movies['title'].values
title = st.selectbox('영화제목을 선택하세요',movies_list)

if st.button('Recommend'):
    titles,images = get_recommendations(title)
    #print(titles)
    idx = 0
    for i in range(0,2):
        cols = st.columns(5)
        for col in cols:
            col.image(images[idx])
            col.write(titles[idx])
            idx+=1