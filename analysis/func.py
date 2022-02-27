import plotly.express as px
import pandas as px
import numpy as np


def get_movie_rating(df):
    rating_df = df.rating.value_counts().reset_index()
    fig = px.bar(rating_df,x='index',y='rating')
    return fig

def get_netflix_type(df):
    category_df = df.type.value_counts().reset_index()
    fig = px.pie(category_df,names='index',values='type')
    return fig

