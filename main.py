import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import datetime as dt
from datetime import datetime
from reading_data import data_open_trans
from sklearn import mixture

# from reading_data import data_meter_values
df_open_transactions = data_open_trans()
# df_meter_values = data_meter_values()

print(df_open_transactions.columns.values)

# print(df_meter_values.columns.values)

# print(df_open_transactions.describe(datetime_is_numeric=True, include="all").to_string())
# print(df_open_transactions['TransactionStartTime'].head())
# print(df_open_transactions['TransactionStopTime'].head())
#
# print('Total Unique Start Cards out of ', (df_open_transactions['StartCard'].count()), ' : ',
#       (df_open_transactions['StartCard'].nunique()))
# print((df_open_transactions.groupby(['Day/Night'])['TotalEnergy'].sum()))
# print((df_open_transactions.groupby(['Day/Night'])['MaxPower'].sum()))
# # first graph
# print(df_open_transactions.groupby(['Start Integer Hour'])['TransactionId'].count())
start_time = pd.to_datetime(df_open_transactions['UTCTransactionStart'])


def creating_hour_values(transaction_start_time):
    return int(float(transaction_start_time.strftime("%H")) + float(transaction_start_time.strftime("%M")) / 60)


df_open_transactions['Start Integer Hour_P'] = start_time.apply(lambda row: creating_hour_values(row))
df = pd.DataFrame(df_open_transactions.groupby(['Start Integer Hour_P'])['TransactionId'].count())
print(df.shape)
y = pd.DataFrame(df['TransactionId'], columns=['hours'])
x = range(24)
# dd = df.plot()
# dd.set_xticks(range(len(df)))
# plt.figure(figsize=(40,20))
fig=plt.figure()
fig.patch.set_facecolor('xkcd:lightblue')
plt.grid()
plt.plot(x, df, linestyle='solid', color='black')
plt.scatter(pd.DataFrame(range(24)), df, s=85, edgecolors='deeppink', c='black')
plt.xlabel('Time of the day')
plt.ylabel('Total Transactions')
plt.title('Charging transactions per hour of the day')
plt.xlim(-2, 25)
plt.show()
# # first graph
#
# chargeTime = df_open_transactions['ChargeTime'] > 0
# day = df_open_transactions['Day/Night'] == "Day"
# night = df_open_transactions['Day/Night'] == "Night"
#
# day_charge = df_open_transactions[chargeTime & day]
# night_charge = df_open_transactions[chargeTime & night]
# print(type(day_charge), day_charge.shape)
# print(type(night_charge), night_charge.shape)
#
# day_charge['ChargeTime'].hist(bins=50, alpha=0.5)
# night_charge['ChargeTime'].hist(bins=50, alpha=0.4)
# plt.show()
#
# df1 = df_open_transactions['ChargeTime'].hist(bins=50)
# dd1 = df1.plot()
# plt.show()
#
# sns.countplot(df_open_transactions['Day/Night'])
# plt.show()
#
# sns.countplot(df_open_transactions['Day of the Week'])
# plt.show()
#
# x1 = df_open_transactions['TransactionId']
# y1 = df_open_transactions['ConnectedTime']
# plt.scatter(x1, y1, s=2,  label="Connected Time")
#
# x2 = df_open_transactions['TransactionId']
# y2 = df_open_transactions['ChargeTime']
#
# plt.scatter(x2, y2, s=2, label="Charge Time")
#
# plt.xlabel("Transaction IDs")
# plt.title("Connected Time vs Charge Time")
# plt.legend()
# plt.xticks(x2, "")
# plt.tick_params(
#     axis='x',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=True)
# plt.show()
#
#
# plt.clf()
# df2 = df_meter_values['Collectedvalue'].hist(bins=100, )
# df2.plot()
# plt.ylabel("Collected Value")
# plt.show()


# on = df_open_transactions['String_P'].str.count("ON PEAK")
#
# mid = df_open_transactions['String_P'].str.count("MID PEAK")
#
# off = df_open_transactions['String_P'].str.count("OFF PEAK")


# print(on, mid, off)
# peaks = [on, mid, off]
# plt.pie(peaks)
# plt.show()


# date_year = pd.to_datetime(df_open_transactions['UTCTransactionStart'])
#
#
# def determine_peak(dto):
#     if dto.strftime("%B") in ["November", "December", "January", "February", "March", "April"]:
#         if (dto.strftime("%A") == "Saturday") or (dto.strftime("%A") == "Sunday") or (
#                 23 >= int(dto.strftime("%H")) >= 19) or (
#                 7 >= int(dto.strftime("%H")) >= 0):
#             return "OFF PEAK"
#         if 11 <= int(dto.strftime("%H")) <= 17:
#             return "MID PEAK"
#         else:
#             return "ON PEAK"
#     else:
#         if (dto.strftime("%A") == "Saturday") or (dto.strftime("%A") == "Sunday") or (
#                 23 >= int(dto.strftime("%H")) >= 19) or (
#                 7 >= int(dto.strftime("%H")) >= 0):
#             return "OFF PEAK"
#         if 11 <= int(dto.strftime("%H")) <= 17:
#             return "ON PEAK"
#         else:
#             return "MID PEAK"
#
#
# date_year['Peaks_Python'] = date_year.apply(lambda row: determine_peak(row))
#
# print(type(df_open_transactions))
# print(type(date_year))
# print(df_open_transactions)
# df_open_transactions['Peaks_Python'] = date_year.apply(lambda row: determine_peak(row))
# print(date_year['Peaks_Python'].head(10))

# df_open_transactions['Peaks_Python'] = date_year['Peaks_Python']
#
# print(df_open_transactions['Peaks_Python'])
#
# df_open_transactions.to_csv("dataset_new", sep=',', encoding='utf-8')
