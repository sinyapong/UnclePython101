import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8', newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)   # datalist = ['pen','pencil','eraser']
        
def readcsv():
    with open('data.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data
        
        
# data = ['ขนมเยลลี่', 20, '07.00 น.']
# writecsv(data)
data = readcsv()
print(data)   # [['ขนมเยลลี่', '20', '07.00 น.']]
        