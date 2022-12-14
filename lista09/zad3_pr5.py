s=sorted(map(sum,[map(int,g.split()) for g in open("in.txt",'r').read().split('\n\n')]))[-3:]
print(s[-1],sum(s))