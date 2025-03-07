import pytest
import os
from test_find23 import extract_word_definition  # 确保导入你的函数

# 定义测试文件路径
TEST_FILE_PATH = "./Dict/A/A-b.txt"

# 测试数据（请根据实际数据修改）
TEST_CASES = [
    ("about", "about"),  # 检查是否能找到 "about"
    ("apple", "apple"),  # 假设 "apple" 存在于 A-b.txt
    ("abandon", "abandon"),  # 检查 "abandon" 是否存在
    ("abnormal", "abnormal"),  # 检查 "abnormal"
    ("nonexistentword", "未找到单词 'nonexistentword' 的定义。")  # 测试不存在的单词
]

@pytest.mark.parametrize("search_word, expected_substring", TEST_CASES)
def test_extract_word_definition(search_word, expected_substring):
    """
    测试 extract_word_definition 是否正确返回单词定义。
    """
    if not os.path.exists(TEST_FILE_PATH):
        pytest.skip(f"测试文件 {TEST_FILE_PATH} 不存在，跳过测试。")

    result = extract_word_definition(TEST_FILE_PATH, search_word)

    # 如果是未找到的情况，直接比较字符串
    if "未找到单词" in result:
        assert result == expected_substring
    else:
        # 否则检查返回的内容是否包含搜索词
        assert search_word in result

if __name__ == "__main__":
    pytest.main()
