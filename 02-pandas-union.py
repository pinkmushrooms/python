# Concaténation UNION ALL
pd.concat([df1, df2], sort=False)

# Dans l'autre sens
pd.concat([df2, df1], sort=False)

# Si on veut faire un UNION << simple >>
df3 = pd.concat([df2, df1, df2], sort=False).drop_duplicates()
df3
