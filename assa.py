import requests
from bs4 import BeautifulSoup

def fetch_cambridge_definitions(word):
    url = f"https://dictionary.cambridge.org/dictionary/english-chinese-traditional/{word}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://dictionary.cambridge.org/",
        "Accept-Encoding": "gzip, deflate, br"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    
    # 遍历每个词性区块
    for entry in soup.find_all('div', class_='pr entry-body__el'):
        # 提取词性
        part_of_speech = entry.find('span', class_='pos dpos')
        pos = part_of_speech.text.strip() if part_of_speech else ""
        
        # 提取英文释义
        en_defs = [d.get_text(" ", strip=True) for d in entry.find_all('div', class_='def ddef_d db')]
        
        # 提取中文释义
        zh_defs = [t.get_text(" ", strip=True) for t in entry.find_all('span', class_='trans') 
                  if t and not t.get_text(strip=True).isascii()]
        
        # 建立中英文对应关系
        paired = []
        for en, zh in zip(en_defs, zh_defs):
            paired.append({"en": en, "zh": zh})
        
        # 合并结果
        if en_defs or zh_defs:
            results.append({
                "part_of_speech": pos,
                "definitions": paired
            })
    
    # 去重处理
    unique_results = []
    seen = set()
    for item in results:
        key = (item["part_of_speech"], tuple(d["en"] for d in item["definitions"]))
        if key not in seen:
            seen.add(key)
            unique_results.append(item)
    
    return unique_results if unique_results else None



# 测试代码
if __name__ == "__main__":
    word = input("请输入要查询的单词: ")
    results = fetch_cambridge_definitions(word)
    
    if results:
        print(f"\n单词 '{word}' 的完整释义:")
        for entry in results:
            print(f"\n[{entry['part_of_speech']}]")
            for idx, definition in enumerate(entry["definitions"], 1):
                print(f"{idx}. 英文: {definition['en']}")
                print(f"   中文: {definition['zh']}")
    else:
        print(f"未找到单词 '{word}' 的释义。")