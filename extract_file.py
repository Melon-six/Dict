import os
import re

def extract_letters(filename):
    """ 从文件名提取包含的字母 """
    base_name = os.path.basename(filename).split('.')[0].strip()  # 去除扩展名，并去掉首尾空格
    parts = re.split(r'[,~]', base_name)  # 处理逗号分隔、波浪号表示范围

    letters = []
    i = 0
    while i < len(parts):
        parts[i] = parts[i].strip()  # 确保没有空格
        if i + 1 < len(parts) and "~" in base_name:
            start, end = parts[i], parts[i+1].strip()  # 确保 start 和 end 没有空格
            if len(start) == 1 and len(end) == 1:  # 确保是单个字符
                letters.extend(chr(c) for c in range(ord(start), ord(end) + 1))
                i += 2  # 跳过已处理的
                continue
        letters.append(parts[i])  # 处理单独的字母
        i += 1

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


