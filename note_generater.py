"""
@author: weiso131
"""

import time

from dict_function import find_word


replace_ = {"{a}" : "\n## ",
            "{/a}" : "\n",
            "{b}" : "\n### ",
            "{/b}" : "\n",
            "{c}" : "-  ",
            "{/c}" : "\n",
            "{w}" : "[網址](",
            "{/w}": ")\n"}



words = ""

with open("text_doc/words.txt", "r") as file:
    words = file.read()
    file.close()
    


words = words.split('\n')


notes = ""

with open("text_doc/note.txt", "r", encoding = "utf-8") as file:
    notes = file.read()
    file.close()


counter = 0
with open("text_doc/counter.txt", "r", encoding = "utf-8") as file:
    counter = int(file.read())
    file.close()

n = len(words)



for i in range(counter, n):
    w = words[i]
    
    try:
        text = find_word(w)
    except:
        print("目標電腦拒絕連線")
        time.sleep(15)
        i -= 1
        print()
    counter += 1
    
    
    if (text == None):
        continue
    for k in replace_.keys():
        text = text.replace(k, replace_[k])
    
    #print(text)
    
    notes += text
    #print(w, ' is complete')
    with open("text_doc/note.txt", "w", encoding = "utf-8") as file:
        
        file.write(notes)
        file.close()
    with open("text_doc/counter.txt", "w", encoding = "utf-8") as file:
        
        file.write(str(counter))
        file.close()
    time.sleep(10)
    
    


"""
TODO:
1.判斷這個單字能不能找到(看網頁標題)(ok)
2.將每個句子對應到它所表示的單字意思裡面(ok)
3.尋找每個意思的詞性(ok)
"""

"""
1. debug

"""





