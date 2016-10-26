import pandas as pd
import matplotlib.pyplot as plt

weather=pd.read_csv('C:/programming/Analyses/Weather Data/Datasets/yearly_rdu_weather.csv')
weather=weather.drop(['Unnamed: 0'], axis=1)

weather['PRCP_inch']=weather['PRCP'].map(lambda x: round(x*.0393701,2))
weather['TAVG_faren']=weather['TAVG'].map(lambda x: round(x*(9/5) + 32,2))


def print_graph(x,y):  #x=numsim
   

    fig, ax = plt.subplots(1, 1, figsize=(12, 9))
    ax.plot(x,y,lw=3, label='PRCP', color='green')
    ax.set_xlabel("Year",size=14)
    ax.set_ylabel("PRCP",size=14)
    ax.legend(loc='best')
    plt.title("Total Yearly RDU Rainfall in Inches", size=16)
    plt.grid(True)
    plt.show()

print_graph(weather['Year'], weather['PRCP_inch'])


def print_graph(x,y):  #x=numsim
   

    fig, ax = plt.subplots(1, 1, figsize=(12, 9))
    ax.plot(x,y,lw=3, label='PRCP', color='green')
    ax.set_xlabel("Year",size=14)
    ax.set_ylabel("Avg Temp in F",size=14)
    ax.legend(loc='best')
    plt.title("Avg RDU Yearly Temp in degrees F", size=16)
    plt.grid(True)
    plt.show()

print_graph(weather['Year'], weather['TAVG_faren'])


