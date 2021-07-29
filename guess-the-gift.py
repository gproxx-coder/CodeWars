# https://www.codewars.com/kata/52ae6b6623b443d9090002c8/train/python

def guess_gifts(wishlist, presents):
    final, all_presents = set(), set()
    for dt in presents:
        all_presents.add(dt['size']+dt['clatters']+dt['weight'])
        
    for dt in wishlist:
        if dt['size'] + dt['clatters'] + dt['weight'] in all_presents:
            final.add(dt['name'])
    return final

wishlist = [{'name': "mini puzzle", 'size': "small", 'clatters': "yes", 'weight': "light"},
            {'name': "toy car", 'size': "medium", 'clatters': "a bit", 'weight': "medium"},
            {'name': "card game", 'size': "small", 'clatters': "no", 'weight': "light"}]
            
presents = [{'size': "medium", 'clatters': "a bit", 'weight': "medium"},
            {'size': "small", 'clatters': "yes", 'weight': "light"}]

print(guess_gifts(wishlist, presents))
