import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns
plt.style.use('seaborn-deep')


data = pd.read_csv('wykop2.csv')

popul_ideo = ['Liberalism', 'Classical Liberalism', 'Neoliberalism', 'Libertarian Socialism',
            'Centre-Left Libertarianism', 'Libertarianism', 'Centrism', 'Centre-Left', 
            'Social Libertarianism', 'Progressivism', 'Social Democracy', 'Agorism', 
            'Moderate Conservatism', 'Neoconservatism', 'Libertarian Capitalism',
            ]

sns.heatmap(data.corr(), xticklabels=data.corr().columns, yticklabels=data.corr().columns, annot=True)

color_wheel = {'neuropa': "#ff8204", 
               'konfederacja': "#0804ff",
              }

colors = data['tag'].map(lambda x: color_wheel.get(x))
scatter_matrix(data, color = colors, diagonal='kde', grid=True)

data.boxplot(by = 'tag', column=['cap', 'nat', 'aut', 'trad'], layout=(1,4), grid=True)
data.boxplot(by = 'sex', column=['cap', 'nat', 'aut', 'trad'], layout=(1,4), grid=True)

data[data.ideology.isin(popul_ideo)].groupby('ideology').boxplot(layout=(2,7), column=['cap', 'nat', 'aut', 'trad'])
data[data.ideology.isin(popul_ideo)].boxplot(by='ideology',layout=(2,2), column=['cap', 'nat', 'aut', 'trad'], rot=75)

ax1 = data.plot.scatter(x='cap', y='aut', color = colors, edgecolor = 'black')
ax1.axes.fill_between((0,0.5),0.5,1, color = '#f4baba', zorder = -100)
ax1.axes.fill_between((0.5,1),0.5,1, color = '#96d4f7', zorder = -100)
ax1.axes.fill_between((0,0.5),0,0.5, color = '#c7e3bb', zorder = -100)
ax1.axes.fill_between((0.5,1),0,0.5, color = '#f1f8a3', zorder = -100)
ax1.axes.grid(b=None)
ax1.set_aspect('equal', 'box')
ax1.set_yticks([])
ax1.set_xticks([])
ax1.axvline(x=0.5, color='grey', zorder = -100, alpha = 0.4)
ax1.axhline(y=0.5, color='grey', zorder = -100, alpha = 0.4)

plt.show()
