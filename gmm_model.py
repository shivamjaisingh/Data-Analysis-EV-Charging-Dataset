import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from datetime import datetime
import pandas as pd
import numpy as np
from reading_data import data_open_trans

df_open_transactions = data_open_trans()
print(df_open_transactions.columns.values)

start_time = pd.to_datetime(df_open_transactions['UTCTransactionStart'])


def creating_hour_values(transaction_start_time):
    return float(transaction_start_time.strftime("%H")) + float(transaction_start_time.strftime("%M")) / 60


df_open_transactions['Start Integer Hour_P'] = start_time.apply(lambda row: creating_hour_values(row))

print(df_open_transactions.columns.values)

# print(df_open_transactions['Start Integer Hour_P'])

data = df_open_transactions[['Start Integer Hour_P', 'ConnectedTime']]

plt.scatter(data['Start Integer Hour_P'], data['ConnectedTime'], s=2)
plt.title('Start Time and Total Connected Time')
plt.xlabel('Start Connection Hour ')
plt.ylabel('Total Hours Connected')
plt.show()

gmm = GaussianMixture(n_components=9, covariance_type='full').fit(data)
# print(gmm.means_)
# print('\n')
# print(gmm.covariances_)

# predictions from kmeans
labels = gmm.predict(data)
print(labels)
frame = pd.DataFrame(data)
frame['cluster'] = labels
frame.columns = ['Start Integer Hour_P', 'ConnectedTime', 'cluster']

# plotting results
color = ['green', 'red', 'blue', 'cyan', 'magenta', 'yellow', 'black', 'orange', 'pink']
for k in range(0, 9):
    data = frame[frame["cluster"] == k]
    plt.scatter(data['Start Integer Hour_P'], data['ConnectedTime'], c=color[k], s=2)

plt.title('GMM Visualization with 9 clusters of charging sessions')
plt.xlabel('Start Connection Hour ')
plt.ylabel('Total Hours Connected')
plt.show()
