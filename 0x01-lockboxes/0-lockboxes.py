#!/usr/bin/python3
'''method that determines if all the boxes can be opened
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    boxe = set([0])
    un_boxe = set(boxes[0]).difference(set([0]))
    while len(un_boxe) > 0:
        id_boxe = un_boxe.pop()
        if not id_boxe or id_boxe >= n or id_boxe < 0:
            continue
        if id_boxe not in boxe:
            un_boxe = un_boxe.union(boxes[id_boxe])
            boxe.add(id_boxe)
    return n == len(boxe)
