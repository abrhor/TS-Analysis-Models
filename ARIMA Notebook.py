>>> import numpy as np
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> from statsmodels.graphics.tsaplots import plot_acf
>>> import statsmodels.api as sm
>>> import quandl
>>> ibm = quandl.get("WIKI/IBM").loc[:, "Close"].tolist()
>>> ibm = np.array(ibm)
>>> print(len(ibm))
13887
>>> ibm = ibm[:-560]
>>> print(len(ibm))
13327
>>> ibm = quandl.get("WIKI/IBM").loc[:, "Close"].tolist()
>>> close = np.array(ibm[-560:])
>>> returns = np.diff(np.log(close))
>>> df = quandl.get("WIKI/IBM")
>>> plt.plot(df.loc[:,"Close"])
[<matplotlib.lines.Line2D object at 0x116d3bac8>]
>>> plt.show()
>>> time = df.index.values
>>> time = time[-560:]
>>> time = time[1:]
>>> plt.plot(time, returns)
[<matplotlib.lines.Line2D object at 0x119918c88>]
>>> plt.show()
>>> plot_acf(returns)
<matplotlib.figure.Figure object at 0x116aa85f8>
>>> plt.show()
>>> plt.hist(returns)
(array([   5.,    1.,    5.,   29.,  118.,  226.,  129.,   37.,    7.,    2.]), array([-0.06038291, -0.04943162, -0.03848033, -0.02752904, -0.01657775,
       -0.00562647,  0.00532482,  0.01627611,  0.0272274 ,  0.03817868,
        0.04912997]), <a list of 10 Patch objects>)
>>> plt.show()
>>> adfuller = sm.adfuller(returns)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'statsmodels.api' has no attribute 'adfuller'
>>> from statsmodels.tsa.stattools import adfuller
>>> adfuller = adfuller(returns)
>>> print('P-value from AD-Fuller Test: ', adfuller[1])
P-value from AD-Fuller Test:  2.27232688437e-30
>>> # Stationary, so proceed
... 
>>> from statsmodels.tsa import arima_model
>>> import seaborn as sns
>>> plot_acf(returns[-100:]
