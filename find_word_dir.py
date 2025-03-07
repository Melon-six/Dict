import os
import re
import os

DICT_ROOT = "DICT/"

def get_target_file(aim_code):
    """ 根据首字母和第二个字母匹配合适的文件 """
    if not aim_code or not aim_code[0].isalpha():
        return None  # 无效输入

    first_letter = aim_code[0].upper()
    second_letter = aim_code[1] if len(aim_code) > 1 else ""

    directory = os.path.join(DICT_ROOT, first_letter)
    if not os.path.exists(directory):
        return None  # 没有该首字母的目录

    # 查找正确的文件
    for filename in os.listdir(directory):
        if len(filename) > 2 and second_letter in filename:
            return os.path.join(directory, filename)

    return None  # 找不到匹配的文件

def search_words(aim_code):
    """ 在字典中查找目标单词的翻译 """
    if not aim_code or not aim_code[0].isalpha():
        return "invalid input"

    target_file = get_target_file(aim_code)
    if not target_file:
        return "no this words!"  # 没有找到合适的文件

    # 读取文件并查找目标单词
    try:
        with open(target_file, 'r', encoding='gbk', errors='ignore') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                line = line.strip()
                if line == aim_code and i + 1 < len(lines):
                    return lines[i + 1].strip()  # 返回下一个单词的解释
    except FileNotFoundError:
        return "cannot translate this words!"

    return "cannot translate this words!"  # 单词未找到
# 测试
# print(search_words("about"))
# print(search_words("hallo"))

# test_words = ["about", "apple", "banana", "zebra", "orange", "hello", "victory", "xylophone"]
# for word in test_words:
#     result = search_words(word)
#     print(result)

# # **运行测试**
# if __name__ == "__main__":
#     # **提前构建全局文件映射**
#     dir_map = build_directory_map("DICT")
#     file_map = build_file_map(dir_map)


# def get_dir(word: str):
#     """ 使用已构建的映射，而不是每次重新构建 """
#     return find_word_file(word, dir_map, file_map)

# # 直接测试特定单词
# print(get_dir("banana"))  # 应该找到 A-b.txt
# print(get_dir("axolotl"))  # 应该找到 A-u,v,w,x,y,z.txt
