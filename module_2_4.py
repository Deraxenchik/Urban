lobi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
busteri = []
prishepochniki =[]
for zxc_ in lobi:
    if zxc_ == 1:
        continue
    guli = True
    for zxc in range(2, int(zxc_**0.5) + 1):
        if zxc_ % zxc == 0:
            guli = False
            break
    if guli:
        busteri.append(zxc_)
    else:
        prishepochniki.append(zxc_)
print(busteri)
print(prishepochniki)