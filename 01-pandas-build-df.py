import pandas as pd
import pandas.util.testing as tm
import numpy as np

"""
Préparation des dataframes pour UNION
"""
np.random.seed(2222)

# Construction de df1 : 5 lignes/3 cols 
# L'index est de type char
tm.N, tm.K = 5, 3
df1 = tm.makeDataFrame()

tm.N, tm.K = 4, 2
df2 = tm.makeDataFrame()

df1
df2

# On va modifier l'index pour le remplacer par une colonne "index"
# le nouvel index est un number qui s'incrémente
df1.reset_index(inplace=True)
df2.reset_index(inplace=True)
df1
df2

# On supprime ensuite la colonne "index"
df1.drop("index", axis=1, inplace=True)
df2.drop("index", axis=1, inplace=True)
df1
df2

"""
Création de df via dictionnaires

  ,d88b.d88b,
  88888888888
  `Y8888888Y'
    `Y888Y'  
      `Y'

"""
nuul = np.nan
nuul

df5 = pd.DataFrame({'colA': [0, 1, 1, nuul, 4]
                  , 'colB': [ 'b', 'bb', 'bbb', 'XXXX', 'bbbbb']
                  })

df5
