import pytest
import os
from word_lookup import find_word_definition

# 定义测试字典目录（与你的真实目录一致）
TEST_DICT_DIR = "./Dict"

@pytest.mark.parametrize("word, expected_substring", [
    ("about", "about"),  # 预期应当找到 "about" 的定义
    ("abandon", "abandon"),  # 预期应当找到 "abandon" 的定义
    ("apple", "apple"),  # 预期应当找到 "apple" 的定义
    ("nonexistentword", "未找到单词 'nonexistentword' 的定义。")  # 预期应当找不到
])
def test_find_word_definition(word, expected_substring):
    """ 测试 find_word_definition 是否能正确查找单词定义 """
    result = find_word_definition(word, TEST_DICT_DIR)
    assert expected_substring in result, f"查找 {word} 失败，返回结果: {result}"
