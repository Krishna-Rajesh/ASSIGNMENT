def water (h):
  area =0
  x1,x2=0,len(h)-1
  while x1<x2:
    area=max(area,(abs(x1-x2)*min(h[x1],h[x2])))


    if h[x1]>h[x2]:
      x2-=1
    else:
       x1+=1
  return area
b=input().split(",")
h=[int(i) for i in b]
print(water(h))

