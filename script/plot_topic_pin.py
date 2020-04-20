import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import numpy as np
import datetime
from matplotlib import collections as matcoll

def get_timestamp(date, timeFormat='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.strptime(date, timeFormat)


df_all = pd.read_csv('../data/tweets_cutoff0.01_sorted.csv',sep='\t')

start_time = get_timestamp(df_all['created_at'].values[0])

df = pd.read_csv('../hbtm_var_mu/all_cluster_cutoff0.01_all.csv', header=None)



df1 = df[[0,1,12,13]]
df1.columns = ['topic','time','count','mark']

topic_selected = [2,13,3,21,20,19,48,24,23,51,61,62,60,64,71,75,88,83,94,109,111,115,120,
                 102,123,135,142,151,84,157,159,158,166,168,171,180,184,183,191,201,
                 207,199,212,209,229,228,233,234,227,238,245,254,256,213,255,273,265,279,
                 280,252,291,296,299,295,297,302]

df1['tdiff_sec'] = df1['time'].apply(lambda x: x*24*3600)
df1['date'] = df1['tdiff_sec'].apply(lambda x: start_time + datetime.timedelta(seconds=x))

print(df1.head())



df1.sort_values(by='date',inplace=True)

thres = 10

data1 = df1.values
data2 = []
r,c = df1.shape

good_topic = []
for i in range(r):
    if data1[i,0] in topic_selected and data1[i,2] > thres:
        data2.append(data1[i])
        good_topic.append(data1[i,0])

print(good_topic)

df1 = pd.DataFrame(data2, columns=df1.columns)


r,c = df1.shape


fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(df1['date'].values, df1['count'].values, s=20, c='black')
for i in range(r):
    x = df1['date'].values[i]
    y = df1['count'].values[i]
    ax.plot([x,x],[1,y],color='black',alpha=0.5)

ax.set_ylim(10,max(df1['count'].values)*2)
ax.set_yscale('log', basey=10)

ax.set_aspect(10)

plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=True,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=True,
    labelleft=True) # labels along the bottom edge are off

plt.show()





