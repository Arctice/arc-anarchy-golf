z,i=int(input()),0
while z:
 i+=1;n=i
 for d in 2,3,5:
  while not n%d:n//=d
 if n<2:print(i);z-=1