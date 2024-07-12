import json

import bigtree.tol

ToL = bigtree.tol.TreeOfLife()

HomoSapiens = ToL.life(name='Homo sapiens')
print(HomoSapiens)
print(ToL.life(n=HomoSapiens['n']))
print(ToL.subtree(name='Homo sapiens'))
print(ToL.subtree(name='Homo'))
print(ToL.life(n=HomoSapiens['parent']))
print(json.dumps(ToL.subtree(name='Mammalia', depth=3), indent=4))
print(ToL.subtrees(ns=ToL.life(name='Biota')['children'], depth=0))