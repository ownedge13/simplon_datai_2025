import matplotlib.pyplot as plt 
from os.path import join
def plotfig(df): 
    # Afficher un histogramme de la distribution des âges des passagers
    fig = plt.figure(figsize=(4,4))
    plt.hist(df["age"], density=True, bins=50)
    plt.grid()
    plt.title('age')
    plt.show()

    fig.savefig(join("static","img","histage.png"))