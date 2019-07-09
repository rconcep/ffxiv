import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate_graphs(combat_dataframe):
    fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=True)

    combat_dataframe['DPS'].plot(drawstyle='steps-post', linewidth=2, ax=axes[0])
    combat_dataframe['damage'].plot(drawstyle='steps-post', linewidth=2, ax=axes[1])
    combat_dataframe['heat_gauge'].plot(drawstyle='steps-post', linewidth=2, ax=axes[-1], color='red', label='Heat')
    combat_dataframe['battery_gauge'].plot(drawstyle='steps-post', linewidth=2, ax=axes[-1], color='cyan', label='Battery')

    axes[0].set_xlabel('time [s]')
    axes[0].set_title('DPS')
    axes[0].grid(True)

    axes[1].set_xlabel('time [s]')
    axes[1].set_title('Damage')
    axes[1].grid(True)

    axes[-1].set_ylim([0, 100])
    axes[-1].set_xlabel('time [s]')
    axes[-1].set_title('resources')
    axes[-1].grid(True)
    axes[-1].legend()

    fig.suptitle('Simulation Results')

    plt.show()