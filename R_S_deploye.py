#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 10:35:25 2025

@author: roshinisenthil
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import difflib
import ast


movies_df=pd.read_excel("Bollywood_movies_original_df.xlsx")
tfidf=TfidfVectorizer()
vectors=tfidf.fit_transform(movies_df["Genres"])
indexed=pd.Series(index=movies_df["Movie Name"].str.strip(),data=movies_df.index)

def movie_recommendation(name,num,filter_actor=None):
    # clean and find closest match using difflib
    movie_title=movies_df["Movie Name"].tolist()
    name=name.strip()
    match=difflib.get_close_matches(name,movie_title,n=1,cutoff=0.6)
    
    if not match:
        print("Movie not found")
        return []
    
    matched_name=match[0]
    dis=linear_kernel(vectors[indexed[matched_name]],vectors)
    scores=list(enumerate(dis[0]))
    scores=sorted(scores,key=lambda x : x[1],reverse=True)
    scores=scores[1:]
    
    recommendation=[]
    for idx,score in scores:
        row=movies_df.iloc[idx]
        if filter_actor:
            cast_list=row["Cast"]
            if isinstance(cast_list,str):
                cast_list=ast.literal_eval(cast_list)
            if not any(filter_actor.lower() in actor.lower() for actor in cast_list):
                continue
            
        recommendation.append({     
            "Movie Name": row["Movie Name"],
            "Rating": row["Rating"],
            "Year": row["Year"],
            "Genres": row["Genres"],
            "Cast": row["Cast"]
        })     
        if len(recommendation)==num:
            break
    return recommendation



            
    # --------- Streamlit UI Starts Here ---------
    
st.title("Bollywood Movie Recommendation Engine")
st.image("movies.jpg")


movie_name=st.text_input("Enter the Movie Name:","")
num_recommendation=st.slider("How many recommendations?", 1, 10, 5)
filter_actor=st.text_input("Filter by actor (optional):")                             

if st.button("Get Recommendation"):
    if not movie_name.strip():
        st.warning("Please enter a movie name.")
    else:
        result=movie_recommendation(movie_name,num_recommendation,filter_actor if filter_actor else None)
        
        if result:
            df_result=pd.DataFrame(data=result)
            df_result=df_result.sort_values("Rating",ascending=False)
            st.success(f"Showing Top {len(df_result)} recommendations:")
            st.dataframe(df_result)
        else:
            st.error("No recommendations found. Try a different movie or actor.")


    
    
    
    
    