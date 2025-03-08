import pytest
from unittest.mock import patch
from test_find import find_word_in_dict  # 确保正确导入你的 Python 文件

# 模拟 build_file_map 返回的文件映射
MOCK_FILE_MAP = {
    "a": "DICT/A/A-a.txt",
    "b": "DICT/B/B-b,c,d,e.txt",
    "z": "DICT/Z/Z.TXT",
}

@pytest.fixture
def mock_build_file_map():
    """Mock build_file_map 返回文件映射"""
    with patch("test_find.build_file_map", return_value=MOCK_FILE_MAP):
        yield

def test_find_word_exists(mock_build_file_map):
    """测试匹配到正确的文件"""
    assert find_word_in_dict("apple", "DICT") == "DICT/A/A-a.txt"
    assert find_word_in_dict("banana", "DICT") == "DICT/B/B-b,c,d,e.txt"
    assert find_word_in_dict("zebra", "DICT") == "DICT/Z/Z.TXT"

def test_find_word_not_found(mock_build_file_map):
    """测试单词不在任何文件中"""
    assert find_word_in_dict("xylophone", "DICT") == "未找到匹配的文件"

def test_find_word_case_insensitive(mock_build_file_map):
    """测试忽略大小写匹配"""
    assert find_word_in_dict("Apple", "DICT") == "DICT/A/A-a.txt"
    assert find_word_in_dict("BaNaNa", "DICT") == "DICT/B/B-b,c,d,e.txt"
