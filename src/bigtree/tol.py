import copy
import json

import pandas as pd

import bigtree
PROJECT = bigtree.PROJECT


COLUMNS = 'col:ID col:parentID col:status col:scientificName col:rank'.split()
CoL = pd.read_csv(PROJECT / 'data' / 'NameUsage.tsv', sep='\t', header=0, on_bad_lines='warn', usecols=COLUMNS).rename(columns=lambda x: x.split(':')[1]).query('status == "accepted"').drop(columns=['status'])
CoL.reset_index()


def build():
    ROOT = 'ROOT of LIVES'

    # CoL ID -> index の対応表
    index = {id: i for i, id in enumerate(CoL.ID)}
    index[ROOT] = -1

    # Life の木構造（MacBook Air M1 で約48秒）
    # 各頂点の先頭の要素はその頂点の親の ID、それ以降はその頂点の子

    lives = [{'n': n, 'name': name, 'parent': -1, 'children': []}
           for n, name in enumerate(CoL.scientificName)]
    lives.append({'n': -1, 'name': ROOT, 'parent': -1, 'children': []})  # ToL[-1]

    # 学名 -> index の対応表
    lookup = { life['name']: life['n'] for life in lives }

    orphans = []

    for _, life in CoL.iterrows():
        _life = lives[index[life.ID]]
        try:
            if pd.isna(life.parentID): print(f'Root of life: {life.scientificName}')
            parent = lives[index[life.parentID]]
            _life['parent'] = parent['n']
            parent['children'].append(_life['n'])
        except: orphans.append({ 'id': life.ID, 'name': life.scientificName }) # parentID が登録されていない Life は無視する


    ToL = dict(lives=lives, index=index, lookup=lookup, orphans=orphans)
    with (PROJECT / 'data' / 'tree_of_lives.json').open('w') as w: json.dump(ToL, w)


class TreeOfLife:
    if not (PROJECT / 'data' / 'tree_of_lives.json').exists():
        print('Building database...', flush=True)
        build()
        print('Database built.', flush=True)
    with open(PROJECT/'data'/'tree_of_lives.json') as f:
        print('Loading database...', flush=True)
        ToL = json.load(f)
        print('Database loaded.', flush=True)

    def __init__(self):
        ToL = self.ToL
        self.lives = ToL['lives']
        self.index = ToL['index']
        self.lookup = ToL['lookup']
        self.orphans = ToL['orphans']

    def life(self, name=None, n=None):
        if type(name) == str: n = self.lookup[name]
        if type(n) == int:
            return self.lives[n]

    def subtree(self, name=None, n=None, depth=2^32):
        if type(name) == str: life = self.life(name=name)
        elif type(n) == int: life = self.life(n=n)
        else: return
        
        if depth <= 0: return copy.deepcopy(life)
        life = dict(n=life['n'], parent=life['parent'], name=life['name'],
                    children=[self.subtree(n=c, depth=depth-1) for c in life['children']])
        return life
    
    def subtrees(self, ns=[], depth=1):
        return dict(zip(ns, [self.subtree(n=n, depth=depth) for n in ns]))