# 実行方法: src の上の bigtree ディレクトリで
#   env PYTHONPATH=./src python3 src/test/test_tol.py
# あるいは、環境変数の PYTHONPATH を export PYTHONPATH=`pwd`/src と設定しておいてから
#    python3 src/test/test_tol.py
# 後者の方法だと、cd src/test したあとで、単に python3 test_tol.py としても実行できる。

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