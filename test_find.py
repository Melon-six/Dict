import os
import re

def extract_letters(filename):
    """ 从文件名提取包含的字母 """
    base_name = os.path.basename(filename).split('.')[0]  # 去除扩展名
    letters = re.split(r'[,~]', base_name)  # 处理逗号分隔、波浪号表示范围
    if len(letters) == 2 and '~' in base_name:
        return list(map(chr, range(ord(letters[0]), ord(letters[1]) + 1)))  # 处理 a~m 这种范围
    return letters

def build_file_map(directory):
    """ 构建一个映射，每个字母对应的文件路径 """
    file_map = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                full_path = os.path.join(root, file)
                letters = extract_letters(file)
                for letter in letters:
                    file_map[letter.lower()] = full_path  # 统一转换为小写
    return file_map

def find_word_in_dict(word, dict_dir):
    """ 根据单词首字母匹配字典文件路径 """
    file_mapping = build_file_map(dict_dir)
    first_letter = word[0].lower()
    return file_mapping.get(first_letter, "未找到匹配的文件")


