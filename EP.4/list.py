box = ['ปากกา', 'ดินสอ', 'ยางลบ']
brand = {'pen':['Lamy','Pentel','Fiber-castel'], 'pencil':['hourse','staedtler'], 'eraser':'ยางลบ 2 สี'}

print(brand.keys())
# dict_keys(['pen', 'pencil', 'eraser'])

print(brand.values())
# dict_values([['Lamy', 'Pentel', 'Fiber-castel'], ['hourse', 'staedtler'], 'ยางลบ 2 สี'])

for b in box:
    print(b)  
# ปากกา
# ดินสอ
# ยางลบ

for br in brand.keys():
    print(br)
    
for br in brand.items():
    print(br)
    
print(len(brand))
