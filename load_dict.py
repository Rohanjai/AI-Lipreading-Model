import numpy as np

def load_dict(labels):
    words = list(set(list(labels)))
    words.sort()
    label_dict = dict()
    for i,j in enumerate(words):
        label_dict[i]=j
    return label_dict