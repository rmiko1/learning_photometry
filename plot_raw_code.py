
# 2/21/25 Photometry Analysis Code (read raw file and graph)

import pandas as pd
import matplotlib.pyplot as plt

#filepath_415 = "C:\\Users\\rache\\Desktop\\test_415_2025-02-18T11_35_22.csv"

#filepath_470 = "C:\\Users\\rache\\Desktop\\test_470_2025-02-18T11_35_22.csv"

filepath_470 = "D:\\Ashna_test\\test_470_2025-02-18T12_15_48.csv"
filepath_415 = "D:\\Ashna_test\\test_415_2025-02-18T12_15_48.csv"

def read_file(filepath_415, filepath_470):
    pd_415 = pd.read_csv(filepath_415)
    pd_470 = pd.read_csv(filepath_470)

    print(pd_415.head())

    print(pd_470.head())

    pd_415_clean = pd_415[['Timestamp', 'Region0G']]
    pd_470_clean = pd_470[['Timestamp', 'Region0G']]


    print(pd_415_clean.head())
    print(pd_470_clean.head())



    return pd_415_clean, pd_470_clean


pd_415_clean, pd_470_clean = read_file(filepath_415, filepath_470)



def plot_415_470(pd_415_clean, pd_470_clean, time_start, time_stop):



    fig, ax = plt.subplots()

    ax.plot(pd_415_clean['Region0G'].iloc[time_start:time_stop], label = '415')
    ax.plot(pd_470_clean['Region0G'].iloc[time_start:time_stop], label = '470')

    ax.set_xlabel('frames')  # Add an x-label to the Axes.
    ax.set_ylabel('raw fluorescence')  # Add a y-label to the Axes.
    ax.set_title("415 vs 470")  # Add a title to the Axes.
    ax.legend()  # Add a legend.


    plt.show()


def plot_two_traces(trace1, trace2, time_start, time_stop, trace1_label = '415', trace2_label = '470', title = '415 vs 470'):

    fig, ax = plt.subplots()

    ax.plot(trace1.iloc[time_start:time_stop], label = trace1_label)
    ax.plot(trace2.iloc[time_start:time_stop], label = trace2_label)

    ax.set_xlabel('frames')  # Add an x-label to the Axes.
    ax.set_ylabel('raw fluorescence')  # Add a y-label to the Axes.
    ax.set_title(title)  # Add a title to the Axes.
    ax.legend()  # Add a legend.


    plt.show()