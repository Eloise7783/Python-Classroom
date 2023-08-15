'''Count Module'''
def count(sequence, item):
    '''counts the amount of items in a sequence'''
    counter = 0
    for thing in sequence:
        if thing == item:
            counter += 1
    return counter
