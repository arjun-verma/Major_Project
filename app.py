import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from flask import Flask, render_template
import json
import plotly

app = Flask(__name__)



@app.route('/')
def index():
    dfs = pd.read_csv('datasets/Salary.csv')
    dfs.drop(['Unnamed: 0'], axis = 1, inplace = True)
    df = dfs.groupby(['Sport']).median()
    fig = px.bar(df,x=df.index,y='Pay2014',color ='Pay2014',log_y=True,title="Pay 2014 median")
    fig2 = px.bar(df,x=df.index,y='Salary_Winnings',color ='Pay2014',log_y=True,title="Salary Winning median")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', pay2014graph=graphJSON, salwingraph=graphJSON2)

@app.route('/bivar')
def bivar():
  
    return render_template('bivar.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 