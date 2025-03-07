import os
import re
from extract_file import find_word_in_dict  # 从 extract_file.py 导入
from extract_definition import extract_word_definition  # 从 extract_definition.py 导入

def find_word_definition(word, dict_dir: str = "./DICT" ):
    """
    在字典文件夹中查找单词的定义。
    
    参数:
    - word: 要查找的单词    
    - dict_dir: 字典文件夹路径

    返回:
    - 该单词的定义，如果找到的话
    - 如果找不到单词，返回 "未找到单词..."
    """
    # 获取对应的字典文件路径
    file_path = find_word_in_dict(word, dict_dir)

    if file_path == "未找到匹配的文件":
        return f"未找到单词 '{word}' 的定义。"

    # 在文件中查找单词定义
    return extract_word_definition(file_path, word)

# 示例使用
if __name__ == "__main__":
    dictionary_dir = "./DICT"  # 确保这是你的字典文件夹
    search_word = "about"  # 你要查找的单词
    definition = find_word_definition(search_word, dictionary_dir)
    print(definition)
