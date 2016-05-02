# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist):  return [dct[key] for key in keylist]

def list2dict(L, keylist): return {x:y for x,y in zip(keylist, L)}
