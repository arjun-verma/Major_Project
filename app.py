import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from flask import Flask, render_template
import json
import plotly

app = Flask(__name__)

@app.route('/home')
def home():
    
    return render_template('home.html')

@app.route('/')
def index():
    dfs = pd.read_csv('datasets/Salary.csv')
    dfs.drop(['Unnamed: 0'], axis = 1, inplace = True)
    dfs.rename(columns={'Pay2014' : 'Payout'}, inplace = True)
    df = dfs.groupby(['Sport']).median()
    dft = pd.read_csv('datasets/Teams.csv')
    dft.drop(['Unnamed: 0'], axis = 1, inplace = True)
    dft.fillna(0)
    dft.columns = ['Rank','Last_Year_Rank','Avg_Annual_pay_per_player','Percent_Change_From Last_Year','Total_Payroll'
    ,'Total_Payroll_Rank','Avg_player_5_year_earnings','Percent_change_over_last_5_years','Team', 'League']
    dft1 = dft[['League', 'Avg_Annual_pay_per_player', 'Percent_Change_From Last_Year'
    ,'Total_Payroll', 'Avg_player_5_year_earnings', 'Percent_change_over_last_5_years']]
    dft2 = dft1.groupby(['League']).median()
    plt.rcParams["axes.formatter.limits"] = (-5, 12)
    fig = px.histogram(dfs, y="Payout", title="Payout")
    fig1 = px.histogram(dfs, y="Salary_Winnings", title="Salary_winnings")
    fig2 = px.histogram(dfs, y="Endorsements",title="Endosrements")
    fig3 = px.bar(df,x=df.index,y='Payout',color ='Payout',log_y=True,title="Payout median")
    fig4 = px.bar(df,x=df.index,y='Salary_Winnings',color ='Payout',log_y=True,title="Salary Winning median")
    fig5 = px.bar(df,x=df.index,y='Endorsements',color ='Payout',log_y=True,title="Endorsement median")
    fig6 = px.scatter(dfs, x="Sport", y="Payout",title="Payout",labels={"Payout" : "Payout"})
    fig7 = px.scatter(dfs, x="Sport", y="Endorsements",title="Endorsements")
    fig8 = px.scatter(dfs, x="Sport", y="Salary_Winnings",title="salary winning")
    fig9 = px.bar(dft2, x=dft2.index, y='Avg_Annual_pay_per_player',
             color='Avg_Annual_pay_per_player', log_y=True, title="Average Annual pay per player")
    fig10 = px.bar(dft2, x=dft2.index, y='Percent_Change_From Last_Year',
             color='Percent_Change_From Last_Year', log_y=True, title="Percent change from last year's survey")
    fig11 = px.bar(dft2, x=dft2.index, y='Total_Payroll',
             color='Total_Payroll', log_y=True, title="Total Payroll")
    fig12 = px.bar(dft2, x=dft2.index, y='Avg_player_5_year_earnings',
             color='Avg_player_5_year_earnings', log_y=True, title="Average player last 5 year Earning")
    fig13 = px.bar(dft2, x=dft2.index, y='Percent_change_over_last_5_years',
             color='Percent_change_over_last_5_years', log_y=True, title="Percent change in last 5 years")
    fig14 = px.box(dft,'Avg_Annual_pay_per_player')
    fig15 = px.box(dft,'Percent_Change_From Last_Year')
    fig16 = px.box(dft,'Total_Payroll')
    fig17 = px.box(dft,'Avg_player_5_year_earnings')
    fig18 = px.box(dft,'Percent_change_over_last_5_years')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON5 = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON6 = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON7 = json.dumps(fig7, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON8 = json.dumps(fig8, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON9 = json.dumps(fig9, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON10 = json.dumps(fig10, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON11 = json.dumps(fig11, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON12 = json.dumps(fig12, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON13 = json.dumps(fig13, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON14 = json.dumps(fig14, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON15 = json.dumps(fig15, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON16 = json.dumps(fig16, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON17 = json.dumps(fig17, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON18 = json.dumps(fig18, cls=plotly.utils.PlotlyJSONEncoder)

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
        salscatter=graphJSON8,
        aappp=graphJSON9,
        pcflys=graphJSON10,
        tp=graphJSON11,
        apl5ye=graphJSON12,
        pcfl5y=graphJSON13,
        box1=graphJSON14,
        box2=graphJSON15,
        box3=graphJSON16,
        box4=graphJSON17,
        box5=graphJSON18,)

@app.route('/bivar')
def bivar():
    dfs = pd.read_csv('datasets/Salary.csv')
    dfs.drop(['Unnamed: 0'], axis = 1, inplace = True)
    dfs.rename(columns={'Pay2014' : 'Payout'}, inplace = True)
    df = dfs.groupby(['Sport']).median()
    dft = pd.read_csv('datasets/Teams.csv')
    dft.drop(['Unnamed: 0'], axis = 1, inplace = True)
    dft.fillna(0)
    dft.columns = ['Rank','Last_Year_Rank','Avg_Annual_pay_per_player','Percent_Change_From Last_Year','Total_Payroll'
    ,'Total_Payroll_Rank','Avg_player_5_year_earnings','Percent_change_over_last_5_years','Team', 'League']
    dft1 = dft[['League', 'Avg_Annual_pay_per_player', 'Percent_Change_From Last_Year'
    ,'Total_Payroll', 'Avg_player_5_year_earnings', 'Percent_change_over_last_5_years']]
    dft2 = dft1.groupby(['League']).median()
    plt.rcParams["axes.formatter.limits"] = (-5, 12)
    fig = px.scatter(dfs, x='Payout', y='Salary_Winnings',title="Payout Vs Salary winning",labels={"Payout" : "Payout"})
    fig1 = px.scatter(dfs, x='Payout', y='Endorsements',title="Payout Vs Endorsements",labels={"Payout" : "Payout"})
    fig2 = px.scatter(dfs, x='Salary_Winnings', y='Endorsements',title="Salary winnings Vs Endorsements")
    fig3 = px.scatter(dft,x='Avg_Annual_pay_per_player',y='Avg_player_5_year_earnings',color='Avg_player_5_year_earnings',title = 'Average annual pay per player vs Average player 5 year earning')
    fig4 = px.scatter(dft,x='Avg_player_5_year_earnings',y='Total_Payroll',color='Total_Payroll',title = 'Average player 5 year earning vs Total Payroll')
    fig5 = px.scatter(dft,x='Percent_Change_From Last_Year',y='Percent_change_over_last_5_years',color='Percent_change_over_last_5_years',title = 'Percent change in last year vs Percent change in last 5 year')
    fig6 = px.scatter_3d(dft,x='Avg_Annual_pay_per_player',y='Avg_player_5_year_earnings',z='Total_Payroll',color='Avg_Annual_pay_per_player',title = 'Average Annual vs Average 5 Year Annual vs Total Pay')
    fig7 = px.scatter_3d(dfs,x='Payout',y='Salary_Winnings',z='Endorsements',color='Payout',title='Payout vs Sallary Winnings vs Endorsement')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON5 = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON6 = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON7 = json.dumps(fig7, cls=plotly.utils.PlotlyJSONEncoder)
  
    return render_template(
        'bivar.html',
        sp1=graphJSON,
        sp2=graphJSON1,
        sp3=graphJSON2,
        box1=graphJSON3,
        box2=graphJSON4,
        box3=graphJSON5,
        td1=graphJSON6,
        td2=graphJSON7,)

@app.route('/about')
def about():

    return render_template('about.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 