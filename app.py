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
    fig = px.histogram(dfs, y="Pay2014", title="Payout")
    fig1 = px.histogram(dfs, y="Salary_Winnings", title="Salary_winnings")
    fig2 = px.histogram(dfs, y="Endorsements",title="Endosrements")
    fig3 = px.bar(df,x=df.index,y='Pay2014',color ='Pay2014',log_y=True,title="Payout median")
    fig4 = px.bar(df,x=df.index,y='Salary_Winnings',color ='Pay2014',log_y=True,title="Salary Winning median")
    fig5 = px.bar(df,x=df.index,y='Endorsements',color ='Pay2014',log_y=True,title="Endorsement median")
    fig6 = px.scatter(dfs, x="Sport", y="Pay2014",title="Payout",labels={"Pay2014" : "Payout"})
    fig7 = px.scatter(dfs, x="Sport", y="Endorsements",title="Endorsements")
    fig8 = px.scatter(dfs, x="Sport", y="Salary_Winnings",title="salary winning")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON5 = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON6 = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON7 = json.dumps(fig7, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON8 = json.dumps(fig8, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template(
        'index.html',
        payhist=graphJSON, 
        salhist=graphJSON1, 
        endhist=graphJSON2, 
        paybar=graphJSON3, 
        salbar=graphJSON4, 
        endbar=graphJSON5, 
        payscatter=graphJSON6, 
        endscatter=graphJSON7, 
        salscatter=graphJSON8)

@app.route('/bivar')
def bivar():
  
    return render_template('bivar.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 