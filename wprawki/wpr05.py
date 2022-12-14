from itertools import combinations, combinations_with_replacement, product
from operator import itemgetter
from more_itertools import flatten
# universe scores are valued this way:
# 0 = team[0] wins
# 1 = draw
# 2 = team[1] wins

# def megaproduct(n, k):
#         if k == 0:
#             return []
#         if k == 1:
#             return range(n)
#         return product(range(n), flatten(megaproduct(n, k-1)))

# print(list(megaproduct(3, 6)))
# print(list(product(range(3), repeat=6)))

def group_perms(n):
    group_size = 2*n
    matches = list(combinations(range(group_size), 2))
    possible_scores = set()
    print(matches)

    # https://stackoverflow.com/questions/62418012/n-fold-cartesian-product-on-a-single-list-in-python
    for universe in product(range(3), repeat=len(matches)):
        # if not all(x<=y for x,y in zip(universe, universe[1:])):
        #     continue
        ignored_result = False
        scores = [0]*group_size
        for match_ind, result in zip(matches, universe):
            t1, t2 = match_ind
            match result:
                case 0: scores[t1]+=3
                case 1: scores[t1]+=1; scores[t2]+=1
                case 2: scores[t2]+=3
                case _:
                    raise Exception("fucky wucky, out of bounds!", result)
        if not ignored_result:
            possible_scores.add(tuple(sorted(scores)))
    
    print(f"lowest score to pass in {group_size=}: ", min(map(itemgetter(n), possible_scores)))
    print(f"high score to pass in {group_size=}: ", max(map(itemgetter(n-1), possible_scores)))
    return possible_scores


# def group_perms_smart(n):
#     group_size = 2*n
#     matches = list(combinations(range(group_size), 2))
#     possible_scores = set()
#     print(matches)

#     # https://stackoverflow.com/questions/62418012/n-fold-cartesian-product-on-a-single-list-in-python
#     for universe in product(range(2), repeat=len(matches)):
#         # if not all(x<=y for x,y in zip(universe, universe[1:])):
#         #     continue
#         ignored_result = False
#         scores = [0]*group_size
#         for match_ind, result in zip(matches, universe):
#             t1, t2 = match_ind
#             match result:
#                 case 0: scores[t1]+=3
#                 case 1: scores[t1]+=1; scores[t2]+=1
#                 case _:
#                     raise Exception("Match ended horribly, nukes were droped!", result)
#         if not ignored_result:
#             possible_scores.add(tuple(scores))
    
    return possible_scores

all_scores = group_perms(2)
# print(all_scores)
print(len(all_scores))

# test = group_perms_smart(2)
# print(len(test))
# print(test ^ all_scores)