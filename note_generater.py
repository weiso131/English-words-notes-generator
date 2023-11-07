"""
@author: weiso131
"""

import time

from dict_function import find_word
from pathlib import Path

replace_ = {"{a}" : "\n## ",
            "{/a}" : "\n",
            "{b}" : "\n### ",
            "{/b}" : "\n",
            "{c}" : "-  ",
            "{/c}" : "\n",
            "{w}" : "[網址](",
            "{/w}": ")\n"}


word_path = ""
note_path = ""
reset_counter = ""
words = ""
check = ""
while (True):
    while (True):
        word_path = input("單字路徑(xxx.txt):")
        if (".txt" in word_path):
            try:
                with open("text_doc/" + word_path, "r") as file:
                    words = file.read()
                    file.close()
                    break
            except:
                print("路徑不存在，請重新輸入")
    while ((".txt" in note_path) != True):
        note_path = input("筆記記錄路徑(xxx.txt):")
        
                
    while (reset_counter != "y" and reset_counter != "n"):
        reset_counter = input("重製counter(y/n):")
    
    
    print("單字路徑: ", "text_doc/" + word_path)
    print("筆記路徑: ", "text_doc/" + note_path)
    if(reset_counter == "y"): print("重製counter")
    else: print("不重製counter")
    
    while (check != "y" and check != "n"):
        check = input("確認無誤?(y/n)")
    if(check == "y"):break
    


words = words.split('\n')


notes = ""

note_file = Path("text_doc/" + note_path)
note_file.touch(exist_ok = True)


with open("text_doc/" + note_path, "r", encoding = "utf-8") as file:
    notes = file.read()
    file.close()

    

counter = 0
if (reset_counter == "n"):
    with open("text_doc/counter.txt", "r", encoding = "utf-8") as file:
        counter = int(file.read())
        file.close()
print("counter:" ,counter)
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
    with open("text_doc/" + note_path, "w", encoding = "utf-8") as file:
        
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





