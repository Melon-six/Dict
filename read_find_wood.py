import re
from find_word_dir import get_dir

def extract_word_definition(search_word):
    with open(get_dir(search_word), "r", encoding="utf-8") as file:
        text = file.read()

    # 使用正则表达式匹配单词及其定义
    pattern = rf"\b{search_word}\b.*?(?=\n[A-Z]|\n[a-z]|\n\d+|\Z)"
    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group().strip()  # 返回找到的内容，去除多余空格
    else:
        return f"未找到单词 '{search_word}' 的定义。"

# 示例使用
search_word = "about"   # 你要查找的单词

result = extract_word_definition(search_word)
print(result)
