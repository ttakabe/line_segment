import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  datetime import datetime
import matplotlib.dates as mdates
import matplotlib.lines as mlines
from matplotlib.collections import LineCollection

baseline_dic = {'20170401': '0.0', '20170615': '10.0', '20170824': '20.0', '20171116': '17.5'}

# pair
pairs = ['20170401-20170615','20170824-20171116']

primaries = []
secondaries = []
for d in pairs:
    primary = d[:8]
    secondary = d[-8:]

    primaries.append([datetime.strptime(primary, '%Y%m%d'), baseline_dic[primary]])
    secondaries.append([datetime.strptime(secondary, '%Y%m%d'), baseline_dic[secondary]])

df_primary = pd.DataFrame(primaries, columns=['date', 'data'])
df_primary['date'] = mdates.date2num(df_primary['date'])
df_primary = df_primary.set_index('date')

df_secondary = pd.DataFrame(secondaries, columns=['date', 'data'])
df_secondary['date'] = mdates.date2num(df_secondary['date'])
df_secondary = df_secondary.set_index('date')

points_primary = np.array([np.array(df_primary.index), df_primary['data']]).T.reshape(-1, 1, 2)
points_secondary = np.array([np.array(df_secondary.index), df_secondary['data']]).T.reshape(-1, 1, 2)

segments = np.concatenate([points_primary, points_secondary], axis=1)

lc = LineCollection(segments, color="black", linewidth=1)
ax =  plt.subplot()
plt.xticks(rotation = 20)
ax.add_collection(lc)
plt.plot([datetime.strptime('20170401', '%Y%m%d')], [0.0], markersize=12, marker='.', c='b')
plt.plot([datetime.strptime('20170615', '%Y%m%d')], [10.0], markersize=12, marker='.', c='b')
plt.plot([datetime.strptime('20170824', '%Y%m%d')], [20.0], markersize=12, marker='.', c='b')
plt.plot([datetime.strptime('20171116', '%Y%m%d')], [17.5], markersize=12, marker='.', c='b')
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d"))
ax.set_ylabel('data')
plt.savefig('line_segment.png')
