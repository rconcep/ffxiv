import matplotlib.pyplot as plt
import numpy as np

SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


def plot_potency(df, truncate_actions=False):
    """
    Plot depicting cumulative potency of a rotation over time.
    
    :param df: A Pandas DataFrame, output from Samurai.parse_rotation()
    :param truncate_actions: If True, x-axis labeled as time instead of actions
    """

    fig, ax = plt.subplots(figsize=(12, 4))

    xlocs = np.arange(len(df))
    bar_width = 0.2
    ax.bar(xlocs, df['Total Potency'], bar_width, label='rotation')
    
    if not truncate_actions:
        ax.set_xticks(xlocs)
        plt.xticks(rotation=70)
        ax.set_xticklabels(df['Weaponskill']+'\n'+
                           [',\n'.join(abilities) if len(abilities) > 0 else '' for abilities in df['Abilities']])
        ax.set_xlabel('Actions')
    else:
        ax.set_xlabel('Time')
    
    ax.set_ylabel('Cumulative Potency')
    ax.yaxis.grid(True)
    ax.legend(loc='best')

    fig.tight_layout(pad=2)


def compare_potencies(dfs, labels):
    """
    Compares the potencies of two rotations over time.

    :param dfs: A list of DataFrames, output from Samurai.parse_rotation()

    :param labels: A list of labels corresponding to each DataFrame
    """

    fig, ax = plt.subplots(figsize=(12, 4))

    xlocs = dfs[0]['Time']
    ax.plot(xlocs, dfs[0]['Total Potency'], '-s', label=labels[0])

    xlocs = dfs[-1]['Time']
    ax.plot(xlocs, dfs[-1]['Total Potency'], ':o', label=labels[-1])

    plt.xticks(rotation=70)
    ax.set_xticks(xlocs)
    ax.set_xlabel('Time')
    ax.set_ylabel('Cumulative Potency')
    ax.yaxis.grid(True)
    ax.legend(loc='best')

    fig.tight_layout(pad=2)


def compare_n_potencies(dfs, labels):
    """
    Compares the potencies of n rotations over time.

    :param dfs: A list of DataFrames, , output from Samurai.parse_rotation()

    :param labels: A list of labels corresponding to each DataFrame
    """

    fig, ax = plt.subplots(figsize=(12, 4))

    for k, df in enumerate(dfs):
        xlocs = dfs[k]['Time']
        ax.plot(xlocs, dfs[k]['Total Potency'], '-o', label=labels[k])

    plt.xticks(rotation=70)
    ax.set_xticks(xlocs)
    ax.set_xlabel('Time')
    ax.set_ylabel('Cumulative Potency')
    ax.yaxis.grid(True)
    ax.legend(loc='best')

    fig.tight_layout(pad=2)