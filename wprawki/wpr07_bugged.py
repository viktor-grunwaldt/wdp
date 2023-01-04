# 3.1958;15937;Rozejście szlaków;15943;Kotuszów;jacobs_trail_None
# 0.0768;5804;Slavný, rozc.;5799;Slavný;hiking_trail_yellow;hiking_trail_blue
# dł;nr;begin;nr;end;(colors)
from more_itertools import flatten

with open("data/w7_plg.csv", "r") as f:
    data = f.read()


colors = [line.split(';')[5:] for line in data.splitlines()]
colors = set(flatten(colors))
print(colors)
for color in colors:
    vertices_names = dict()
    pointers = dict()
    pools = []
    for line in data.splitlines():
        _, nr1, name1, nr2, name2, *edge_colors = line.split(";")
        nr1, nr2 = map(int, (nr1, nr2))
        vertices_names[nr1] = name1
        vertices_names[nr2] = name2
        if color not in edge_colors:
            continue

        match (nr1 in pointers, nr2 in pointers):
            case True, True:
                pool1, pool2 = pointers[nr1], pointers[nr2]
                # no action needed if edge in same pool
                if pool1 == pool2:
                    continue
                    # pass

                # skip merging if pool is empty
                if not pools[pool2]:
                    print("skipping pool")
                    continue

                # remap pointers to merged pool
                for vertice in pools[pool2]:
                    pointers[vertice] = pool1

                # merge pools
                pools[pool1] |= pools[pool2]
                pools[pool2] = None
            # one vertice is new
            case True, False:
                pool_nr = pointers[nr1]
                pools[pool_nr].add(nr2)
                pointers[nr2] = pool_nr
            case False, True:
                pool_nr = pointers[nr2]
                pools[pool_nr].add(nr1)
                pointers[nr1] = pool_nr
            # both vertices are new
            case False, False:
                pointers[nr1] = len(pools)
                pointers[nr2] = len(pools)
                pools.append({nr1, nr2})

    print(color, sum(1 for i in pools if i))
