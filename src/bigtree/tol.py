import json

from init_project import PROJECT

class TreeOfLife:
    def __init__(self):
        with open(PROJECT/'data'/'tree_of_life.json') as f:
            ToL = self.ToL = json.load(f)
            self.lives = ToL['lives']
            self.index = ToL['index']
            self.lookup = ToL['lookup']
            self.orphans = ToL['orphans']

    def life(self, name=None, id=None):
        if type(name) == str: return self.lives[self.lookup[name]]
        if type(id) == int: return self.lives[self.index[id]]