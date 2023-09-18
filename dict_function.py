"""
@author: weiso131
"""

import requests
from bs4 import BeautifulSoup
import re
    
def find_word(word):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    url = "https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/"
    real_url = url + word
    header = {"User-Agent" : user_agent}
    
    rest = requests.get(real_url, headers = header)
    print("status code:", rest.status_code)
    #檢查連線狀態，應該要是200
    
    soup = BeautifulSoup(rest.text, 'html.parser')
    #html5lib速度慢但容錯率高，另外pip
    #我這邊用html.parser
    
    html_row_split = rest.text.split('\n')
    #給分行查詢使用
    
    pure_meaning, pure_tran_sentence = get_meaning(soup) #中文意思、例句中文翻譯
    sentence = get_sample_sentence(soup) #例句
    pos = get_pos(soup)#詞性
    
    if (check_title(soup, word) != word):
        return "## can't find the word " + word
    
    word_note = "\n## " + word + '\n'
    counter = 0

    
    for i in range(len(pure_meaning)):
        text  = '### ' + pos[i] + ' ' + pure_meaning[i] + '\n'
        
        if (i < len(pure_meaning) - 1):
            next_index = find_part_in_html(pure_meaning[i + 1], html_row_split)
            
            #print(next_index, pure_meaning[i])
            
            while (find_part_in_html(pure_tran_sentence[counter], html_row_split) < next_index):
                #print(find_part_in_html(pure_tran_sentence[counter], html_row_split),pure_tran_sentence[counter])
                text += "例句:" + sentence[counter] + "\n中文:" + pure_tran_sentence[counter] + '\n'
                
                counter += 1
        else:
            while(counter < len(sentence)):
                text += "例句:" + sentence[counter] + "\n中文:" + pure_tran_sentence[counter] + '\n'
                counter += 1
        
        word_note += text + '\n'
    
    return word_note
        
    

def get_meaning(soup):
    """
    找到單字中文意思
    還有例句中文
    
    cm_finded會有字中文意思和例句中文
    mat_finded會有例句中文和其他來亂的
    
    所以就判斷
    如果cm_finded[i]在mat_finded裡面
    就是例句中文
    反之就是單字中文意思
    """
    chinese_mean = ['trans', 'dtrans', 'dtrans-se', 'break-cj']
    mean_and_trash = 'hdb'
    cm_finded = soup.find_all('span', class_ = chinese_mean)
    mat_finded = soup.find_all('span', class_ = mean_and_trash)
    
    pure_meaning = []
    pure_sentence = []
    
    for data in cm_finded:
        if (data in mat_finded):
            pure_sentence.append(data.text)
        else:
            pure_meaning.append(data.text)
    
    
    return pure_meaning, pure_sentence
    
def get_sample_sentence(soup):
    
    """
    找出所有單字例句
    """
    
    class_ = ['eg', 'deg']#例子在這個class裡面
    
    finded = soup.find_all('span', class_ = class_)
    sentence = []
    for s in finded:
        text = s.text
        if (ord(text[0]) == 10):
            """
            確認第一個字是不是字母
            如果是空白就代表他不是我要找的句子
            """
            break
        sentence.append(text)
    return sentence

def get_pos(soup):
    """
    取得單字詞性
    """
    class_ = ['pos', 'dpos']
    
    finded = soup.find_all('span', class_ = class_)
    
    pos = list(data.text for data in finded)
    
    return pos

def check_title(soup, word):
    class_ = ['di-title']


    finded = soup.find_all('div', class_ = class_)
    if (len(finded) < 2):
        return "xxxxx"
    return finded[1].text
    
def find_part_in_html(text, html_row_split):
    """
    找出每個句子的先後順序
    方便之後對每個意思提供例句
    """
    text_split = text[:(len(text) - 1)].split(" ")
    
    for i in range(len(html_row_split)):
        if (text_split[0] in html_row_split[i]):
            
            exam = True
            
            for t in text_split:
                
                #字串裡面有標點符號可能會爛掉
                punct = r'[^\w\s]'
                if (re.search(punct, t) != None): continue
            
                if ((t in html_row_split[i]) == False):
                    exam = False
                    break
            if (exam):
                return i
            
    return -1
    


    

#find_word("analysis")
    
    
    

    
    
    
    
    