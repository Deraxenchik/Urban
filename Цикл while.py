ciforka = 0
spisochek = [42, 69, 322, 13, 0, 99, - 5, 9, 8, 7, - 6, 5]
while ciforka < len(spisochek):
    if spisochek[ciforka] > 0:
        print(spisochek[ciforka])      
    if spisochek[ciforka] < 0:
        break
    ciforka+=1