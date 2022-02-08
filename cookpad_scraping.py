import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from more_itertools import chunked


os.chdir('C:\スクレイピング')

df=pd.read_csv("クックパッド.csv")

word_list=[]
result_list=[]
mylist=[]


for i in range(len(df["キーワード"])):
    word_list.append(df.loc[i]["キーワード"])

for keyword in word_list:
    url="https://cookpad.com/search/{key_word}".format(key_word=keyword)
    html=requests.get(url)
    soup=BeautifulSoup(html.content, "html.parser")
    
    for result in soup.find_all(class_='recipe-title')[0:10]:
        result_list.append(result.text)
        time.sleep(0.2)
    
    
        
        
    
    time.sleep(0.5)
mylist=list(chunked(result_list,10))

for j in range(len(df["キーワード"])):
    new_list=mylist[j]
    new_list.insert(0,word_list[j])
    df.loc[j]=new_list
    
    
df.to_csv("クックパッド_出力後.csv",index=False , header=False ,encoding='utf-8_sig')
