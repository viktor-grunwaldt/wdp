from turtle import*
w=input();pu()
for i,c in enumerate(w):
  for j,k in zip((0,0,2,2,4,4),(0,1)*3):
    goto(i*50+k*20,-j*10);dot(20,(__import__("B").B[c][k+j]=='0',)*3)