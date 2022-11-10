import pandas as pd

df = pd.read_csv('amazon_music/train.tsv', names=['user', 'item', 'score', 'alt'], sep='\t')
df = df[['user','item','score']]
a = df[['user', 'item']].groupby(['user']).agg(['count']).reset_index()
a.columns = a.columns.droplevel(1)
a['group'] = pd.qcut(a['item'], 4, labels=[0, 1, 2, 3])
a[['user', 'group']].to_csv('amazon_music/u_clusters.tsv', sep='\t', header=False, index=False)

a = df[['user', 'item']].groupby(['item']).agg(['count']).reset_index()
a.columns = a.columns.droplevel(1)
a['group'] = pd.qcut(a['user'], 4, labels=[0, 1, 2, 3])
a[['item', 'group']].to_csv('amazon_music/i_clusters.tsv', sep='\t', header=False, index=False)



