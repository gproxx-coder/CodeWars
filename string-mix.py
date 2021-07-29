# https://www.codewars.com/kata/5629db57620258aa9d000014/solutions/python

def get_counts_greater_than_one(s1, s2):
    from collections import Counter           
    s1_dict = {key:val for key, val in Counter(s1).items() if val > 1 and 97 <= ord(key) <= 122}
    s2_dict = {key:val for key, val in Counter(s2).items() if val > 1 and 97 <= ord(key) <= 122}
    return s1_dict, s2_dict

def mix(s1, s2):
    s1_counter, s2_counter = get_counts_greater_than_one(s1, s2)
    answer = []
    for key in set(list(s1_counter.keys()) + list(s2_counter.keys())):
        if s1_counter.get(key) and s2_counter.get(key):
            if s1_counter[key] == s2_counter[key]:
                answer.append("=:" + key * s1_counter[key])
            elif s1_counter[key] > s2_counter[key]:
                answer.append("1:" + key * s1_counter[key])
            else:
                answer.append("2:" + key * s2_counter[key])
        elif s1_counter.get(key):
            answer.append("1:" + key * s1_counter[key])
        else:
            answer.append("2:" + key * s2_counter[key])

    return "/".join(sorted(sorted(answer), key=len, reverse=True))
    
print(mix("Lords of the Fallen", "gamekult"))
