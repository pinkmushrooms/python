import pandas as pd
import pandas.util.testing as tm
import numpy as np

tm.N, tm.K = 5, 3

np.random.seed(2222)

df1 = tm.makeDataFrame()

tm.N, tm.K = 4, 2
df2 = tm.makeDataFrame()
