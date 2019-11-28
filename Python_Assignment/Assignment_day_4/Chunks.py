li = []
fo = open("Photo.png", 'rb')

for l in fo:
  li.append(l)
fo.close()

with  open("Photo3.png","wb") as fo:
 for i in range (0,11):
     fo.write(li[i])


