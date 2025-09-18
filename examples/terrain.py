import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from fracbm.daviesharte import motion

def generate(n, H):
    x = np.arange(n)
    y = motion(n, H)  

    ymin, ymax = y.min() - 10, y.max() + 20
    xmin, xmax = x.min(), x.max()

    fig, ax = plt.subplots(figsize=(8, 6))

    cmap = LinearSegmentedColormap.from_list(
        "sunrise",
        ["#FFD580",  
        "#FFB347",  
        "#FF6F61",  
        "#6A5ACD",  
        "#0B3D91"]  
    )
    #sky gradient magic
    gradient = np.linspace(0, 1, n).reshape(-1, 1)
    ax.imshow(gradient, aspect="auto", extent=[xmin, xmax, ymin, ymax],
            origin="lower", cmap=cmap)

    #general structures
    ax.fill_between(x, y, ymin, color="saddlebrown")
    ax.fill_between(x, ymin, y, color="white")
    ax.fill_between(x, y, ymin, color="saddlebrown")

    ax.plot(x, y, color="black", linewidth=1.5)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.axis("off")
    plt.show()

if __name__ == '__main__':
    generate(500, 0.7)
    