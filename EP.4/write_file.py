
def writedata():
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write('สวัสดี')

def adddata(text):
    with open('add-data.txt', 'a', encoding='utf-8') as file:
        file.writelines(text + '\n' )
        
def readdata():
    with open('add-data.txt', encoding='utf-8') as file:
        data = file.readlines()
        print(data)
        
 
# adddata('ดินสอ  10  บาท')
# adddata('ปากกา  20  บาท')
# adddata('ยางลบ  30  บาท')
readdata()