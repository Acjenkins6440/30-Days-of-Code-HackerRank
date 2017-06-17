phoneBook = {}
q = 1
for x in range(int(input())):
    y = input().split()
    phoneBook[y[0]]= y[1]
q = input()
while q != 'None':
    
    if phoneBook.get(q, 'b') != 'b': 
        print(q+ "=" + phoneBook[q])
        q = input()
    else:     
        print('Not found')
        q = input()
