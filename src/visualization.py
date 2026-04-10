import matplotlib.pyplot as plt
import seaborn as sns

def plot_kpis(kpis):

    fig, ax = plt.subplots(figsize=(10,6))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    ax.axis('off')

    y = 0.8
    for k, v in kpis.items():
        ax.text(0.5, y, f"{k}: {v:.2f}", color='white',
                ha='center', fontsize=14)
        y -= 0.15

    plt.show()


def bar_chart(data, title, xlabel, ylabel):

    fig, ax = plt.subplots(figsize=(8,5))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    sns.barplot(x=data.index, y=data.values, color="blue")

    plt.title(title, color='white')
    plt.xlabel(xlabel, color='white')
    plt.ylabel(ylabel, color='white')

    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')

    ax.grid(color='white', alpha=0.2)

    plt.tight_layout()
    plt.show()


def line_chart(data, title):

    fig, ax = plt.subplots(figsize=(8,5))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    sns.lineplot(x=data.index, y=data.values, marker="o", color="blue")

    plt.title(title, color='white')
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')

    ax.grid(color='white', alpha=0.2)

    plt.tight_layout()
    plt.show()