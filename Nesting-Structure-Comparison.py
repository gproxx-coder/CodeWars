# https://www.codewars.com/kata/520446778469526ec0000001/train/python

def same_structure_as(original,other):
    
    if type(original) in [int, str, float] and type(other) in [int, str, float]:
        return True
    
    elif (type(original) in [int, str, float, set, tuple, dict] and type(other) == list) or (type(other) in [int, str, float, set, tuple, dict] and type(original) == list):
        return False
    
    if type(original) == list and type(other) == list:
        if len(original) != len(other):
            return False
        
        for idx in range(len(original)):
            print(original[idx] , "----", other[idx])
            if type(original[idx]) == list and type(other[idx]) == list and other[idx] and len(original[idx]) != len(other[idx]):
                return False
            elif type(original[idx]) == list and type(other[idx]) in [int, str, float]:
                return False
            elif type(other[idx]) == list and type(original[idx]) in [int, str, float]:
                return False
            elif type(original[idx]) == list and type(other[idx]) == list:
                if len(original[idx]) != len(other[idx]):
                    return False
                for inner in range(len(original[idx])):
                    if type(original[idx][inner]) == list and type(other[idx][inner]) in [int, str, float]:
                        return False
    
        return True
