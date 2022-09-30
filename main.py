if __name__ =="__main__":
    f =open("day1.txt","r")
    data = f.read().splitlines() #讀檔且把每筆資料分開

    data_length = len(data)
    for i in range(data_length):
        data[i]=int(data[i]) #將檔案內容另為整數型式

counter = 0
for i in range(data_length-1): #data_length(-1) 是因為執行到最後一項時會溢位
    if data[i+1]-data[i] >0:
        counter+=1
print(counter)