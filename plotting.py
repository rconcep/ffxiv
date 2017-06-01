import matplotlib.pyplot as plt
import numpy as np

def plot_potency(df):
    """
    
    :param df: 
    :return: 
    """

    fig, ax = plt.subplots(figsize=(16, 4))

    SMALL_SIZE = 12
    MEDIUM_SIZE = 18
    BIGGER_SIZE = 20

    plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    xlocs = np.arange(len(df))
    bar_width = 0.4
    ax.bar(xlocs, df['total potency'], bar_width, label='rotation')

    plt.xticks(rotation=20)
    ax.set_xticks(xlocs)
    ax.set_xticklabels(df['action'])
    ax.set_xlabel('Actions')
    ax.set_ylabel('Cumulative Potency')
    ax.yaxis.grid(True)
    ax.legend(loc='best')

    fig.tight_layout(pad=2)


def compare_potencies(dfs, labels):
    """
    Compares the potencies of two rotations over time
    :param dfs: A list of dataframes
    :param labels: A list of labels
    :return: 
    """

    fig, ax = plt.subplots(figsize=(16, 4))

    SMALL_SIZE = 12
    MEDIUM_SIZE = 18
    BIGGER_SIZE = 20

    plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    xlocs = np.arange(len(dfs[0]))
    bar_width = 0.4
    ax.bar(xlocs - bar_width, dfs[0]['total potency'], bar_width, label=labels[0])
    ax.bar(xlocs, dfs[-1]['total potency'], bar_width, label=labels[-1])

    plt.xticks(rotation=20)
    ax.set_xticks(xlocs - bar_width/2)
    ax.set_xticklabels(dfs[-1]['action'])
    ax.yaxis.grid(True)
    ax.legend(loc='best')

    fig.tight_layout(pad=2)

def compare_n_potencies(dfs, labels):
    """
    Compares the potencies of n rotations over time
    :param dfs: A list of dataframes
    :param labels: A list of labels
    :return: 
    """

    fig, ax = plt.subplots(figsize=(16, 4))

    SMALL_SIZE = 12
    MEDIUM_SIZE = 18
    BIGGER_SIZE = 20

    plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    xlocs = np.arange(len(dfs[0]))
    bar_width = 0.1

    for k, df in enumerate(dfs):
        ax.bar(xlocs - bar_width/2 + k*bar_width, dfs[k]['total potency'], bar_width, label=labels[k])

    plt.xticks(rotation=20)
    ax.set_xticks(xlocs + len(labels)*bar_width/4)
    ax.set_xticklabels(dfs[0]['action'])
    ax.yaxis.grid(True)
    ax.legend(loc='best')

    fig.tight_layout(pad=2)