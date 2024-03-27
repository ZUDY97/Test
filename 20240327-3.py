total = 0

for i in range (3333, 10000, 1) :
    if i % 1234 == 0 :
        continue
    if total + i > 100000 :
        print ("i", i)
        break ;
        print (total)
            
