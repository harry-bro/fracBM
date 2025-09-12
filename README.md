# fracbm

  

Fractional Brownian Motion (FBM) generators in Python.

  

## Installation

```bash

pip  install  fracbm

```

## Usage

  
```bash

import  matplotlib.pyplot  as  plt

import  fracbm

# Generate with Davies–Harte method. 1000 steps with a Hurst parameter of 0.8

B  =  fracbm.daviesharte(n=1000, H=0.8)

plt.plot(B)

plt.show()

```


## Features

Generate exact fractional Brownian motion using:

-   **Cholesky decomposition**, order $\mathcal{O}(n^3)$
-   **Davies-Harte method**, order $\mathcal{O}(n \log n)$ 	(recommended)  

Vary the Hurst parameter $H \in [0,1]$:

-   $H = 0.5$ is regular Brownian motion.
-   $H > 0.5$ causes slowly decaying positive autocorrelations (positive increments tend to follow positive increments - increments follow a trend).
-   $H < 0.5$ causes fast-decaying negative autocorrelations (negative increments tend to follow positive increments - increments revert to the mean).