# 3.1958;15937;Rozejście szlaków;15943;Kotuszów;jacobs_trail_None
# 0.0768;5804;Slavný, rozc.;5799;Slavný;hiking_trail_yellow;hiking_trail_blue
# dł;nr;begin;nr;end;(colors)
with open("data/w7_plg.csv", "r") as f:
    data = f.read()


class Subgraph:
    def __init__(self):
        self.vertices_names = dict()
        self.pointers = dict()
        self.pools = []

    def add_edge(self, nr1: int, name1: str, nr2: int, name2: str):
        self.vertices_names[nr1] = name1
        self.vertices_names[nr2] = name2

        match (nr1 in self.pointers, nr2 in self.pointers):
            case True, True:
                pool1, pool2 = self.pointers[nr1], self.pointers[nr2]
                # no action needed if edge in same pool
                if pool1 == pool2:
                    return
                    # pass

                # skip merging if pool is empty
                if not self.pools[pool2]:
                    print("skipping pool")
                    return

                # remap self.pointers to merged pool
                for vertice in self.pools[pool2]:
                    self.pointers[vertice] = pool1

                # merge self.pools
                self.pools[pool1] |= self.pools[pool2]
                self.pools[pool2] = None
            # one vertice is new
            case True, False:
                pool_nr = self.pointers[nr1]
                self.pools[pool_nr].add(nr2)
                self.pointers[nr2] = pool_nr
            case False, True:
                pool_nr = self.pointers[nr2]
                self.pools[pool_nr].add(nr1)
                self.pointers[nr1] = pool_nr
            # both vertices are new
            case False, False:
                self.pointers[nr1] = len(self.pools)
                self.pointers[nr2] = len(self.pools)
                self.pools.append({nr1, nr2})

    def count_pools(self):
        return sum(1 for i in self.pools if i)


graph_dict = dict()

for line in data.splitlines():
    _, nr1, name1, nr2, name2, *edge_colors = line.split(";")

    for color in edge_colors:
        if color not in graph_dict:
            graph_dict[color] = Subgraph()

        graph_dict[color].add_edge(int(nr1), name1, int(nr2), name2)


for color, subgraph in graph_dict.items():
    print(color, "has\t", subgraph.count_pools(), "components")
