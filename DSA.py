from random import *
def tub_son(begin,end):
  tub = []
  for i in range(begin,end):
    for j in range(2,i):
      if i%j==0:
        break
    else:
      tub.append(i)
  return tub

def sipher(a,b):
  if a == 0:
    return b,0,1
  else:
    q,x1,y1 = sipher(b%a,a)
    x = y1 - (b//a)*x1
    y=x1
  return q,x,y

def mod_teskari(a,b):
  q1,x,y=sipher(a,b)
  if q1 == 1:
    return x % b
  else:
    raise Exception("Qiymat noto'g'ri")

def hash(file_path):
    with open(file_path,'rb') as f:
        size=16
        hash_value=0
        index=0
        while True:
            segment=f.read(size)
            if not segment:
                break
            if len(segment)<size:
                segment=segment.ljust(size,b'\0')
            index+=1
            segment_value=int.from_bytes(segment,byteorder='big')
            hash_value^=segment_value
    return hash_value

tub1=tub_son(512,1024)
tub2=tub_son(2,1024)

p=tub1[randint(0,len(tub1)-1)]
for i in tub2:
  if(p-1)%i==0:
    q=i

h= randint(1,int(q-1))

g= h**int((p-1)/q) % p

x=randint(1,int(q-1))

y=(h**int((p-1)/q)) % p

hashed = hash("Hello.txt")

print(f"p={p}\nq={q}\ng={g}\nh={h}\ny={y}\nx={x}")