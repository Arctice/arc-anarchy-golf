a,b=0,0
while 1:
 s=int(input());b+=s-1;a+=s%2
 if a-b:print("Player"+str((b>a)+1)+(" wins the set"if a>6or b>6 else" leads"),max(a,b),'-',min(a,b))
 else:print("Set is tied at",a)