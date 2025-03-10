import aiohttp
from bs4 import BeautifulSoup
import asyncio

async def fetch_cambridge_definitions(word):
    url = f"https://dictionary.cambridge.org/dictionary/english-chinese-traditional/{word}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://dictionary.cambridge.org/",
        "Accept-Encoding": "gzip, deflate, br"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                print(f"请求失败，状态码: {response.status}")
                return None
            
            response_text = await response.text()
            soup = BeautifulSoup(response_text, 'html.parser')
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

async def get_english_definitions(word):
    """ 获取英文释义 """
    results = await fetch_cambridge_definitions(word)
    formatted_string = ""
    for entry in results:
        formatted_string += f"Part of Speech: {entry['part_of_speech']}\n"
        for definition in entry['definitions']:
            formatted_string += f"  English: {definition['en']}\n  Chinese: {definition['zh']}\n"
        formatted_string += "\n"

    return formatted_string

# 示例运行代码
if __name__ == "__main__":
    word = "example"
    definitions = asyncio.run(get_english_definitions(word))
    print(definitions)
