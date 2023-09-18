"""
@author: weiso131
"""


from dict_function import find_word



words = ""

with open("words.txt", "r") as file:
    words = file.read()
    file.close()
    


words = words.split('\n')


notes = ""

for w in words:
    notes += find_word(w)
    print(w, ' is complete')
    
with open("note.txt", "w") as file:
    
    file.write(notes)
    file.close()


"""
TODO:
1.判斷這個單字能不能找到(看網頁標題)(ok)
2.將每個句子對應到它所表示的單字意思裡面(ok)
3.尋找每個意思的詞性(ok)
"""

"""
1. debug

"""





