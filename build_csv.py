import glob
from tqdm import tqdm
dictdata={}
list_txt=glob.glob("./wrd_ph/*.txt")
def readfile(path):
    global data
    with open(path,"r",encoding="utf-8-sig") as f:
        data=[item.strip() for item in f.readlines()]
    temp1=data[1].split("|")
    temp2=data[2].split("*")
    i=0
    try:
        while i<len(temp1):
            dictdata.update({temp1[i]:temp2[i]})
            i+=1
    except:
        print(data[0])
for j in tqdm(list_txt):
    readfile(j)
strdata=""
for j in tqdm(list(dictdata.keys())):
    strdata+=j+"\t"+dictdata[j]+"\n"
with open("g2p.csv","w",encoding="utf-8") as f:
    f.write(strdata)