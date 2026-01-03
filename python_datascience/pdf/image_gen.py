import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

if __name__ == '__main__':
    # ===============================
    # Data for RQ4
    # ===============================
    countries = ['Bangladesh', 'Pakistan', 'Maldives', 'Bhutan', 'Sri Lanka']

    # Total docs per country
    total_docs = [30, 19, 4, 3, 6]

    # Average normalized SARAIF readiness (SRI)
    sri = [0.38, 0.57, 0.34, 0.45, 0.24]

    # Cumulative support (sum of SARAIF dimension scores)
    cumulative_support = [74, 55, 11, 18, 12]

    # Radar chart data (normalized G,T,C,L,M,O)
    radar_data = {
        'Bangladesh': [0.5, 1, 0.8, 0, 1, 0.67],
        'Pakistan': [0.45, 0.77, 0.27, 0, 0.56, 1],
        'Maldives': [0, 0, 0.4, 0, 0.25, 0],
        'Bhutan': [0.35, 0.16, 0.2, 0.5, 0.25, 0.83],
        'Sri Lanka': [0, 0.28, 0, 0, 0, 0]
    }
    dimensions = ['G', 'T', 'C', 'L', 'M', 'O']

    # ===============================
    # Bubble Chart
    # ===============================
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(total_docs, sri, s=[cs * 10 for cs in cumulative_support], alpha=0.6, c='skyblue',
                          edgecolors='black')
    for i, txt in enumerate(countries):
        plt.annotate(txt, (total_docs[i] + 0.3, sri[i] + 0.01), fontsize=10)
    plt.xlabel('Number of Contributing Documents')
    plt.ylabel('Average Framework Support Score (SRI)')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ===============================
    # Radar Chart
    # ===============================
    from math import pi

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, polar=True)

    angles = [n / float(len(dimensions)) * 2 * pi for n in range(len(dimensions))]
    angles += angles[:1]  # close the loop

    for country in countries:
        values = radar_data[country]
        values += values[:1]  # close the loop
        ax.plot(angles, values, linewidth=2, label=country)
        ax.fill(angles, values, alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dimensions)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'])
    ax.set_ylim(0, 1)
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    plt.tight_layout()
    plt.show()