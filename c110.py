import plotly.figure_factory as ff 
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["average"].tolist()
fig = ff.create_distplot([data],["average"],show_hist=False)
#fig.show()

def random_set_of_data(counter):
    dataset = []
    for i in range (0,100):
        index = random.randint(0,len(data))
        value = data[index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    sd = statistics.stdev(dataset)
    print(mean)
    print(sd)

    
def showfig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["average"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setup():
    meanlist = []
    for i in range(0,1000):
        setofmeans = random_set_of_data(100)
        meanlist.append(setofmeans)
    showfig(meanlist)

setup()

def st():
    meanlist = []
    for i in range(0,1000):
        setofmeans = random_set_of_data(100)
        meanlist.append(setofmeans)
    sd = statistics.stdev(meanlist)
    print(sd)

st()
    
    

