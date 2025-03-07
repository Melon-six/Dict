import pytest
import os
import shutil
from extract_file import extract_letters, build_file_map, find_word_in_dict

@pytest.mark.parametrize("filename, expected", [
    ("A.txt", ["A"]),
    ("A~C.txt", ["A", "B", "C"]),  # 处理 A~C
    ("D,E,F.txt", ["D", "E", "F"]),  # 处理逗号分隔
    ("G~I,K.txt", ["G", "H", "I", "K"]),  # 处理 A~C + 额外字母
])
def test_extract_letters(filename, expected):
    """ 测试 extract_letters 是否能正确解析文件名 """
    assert extract_letters(filename) == expected

@pytest.fixture
def setup_fake_dict(tmp_path):
    """ 在临时目录创建模拟字典文件夹 """
    dict_dir = tmp_path / "Dict"
    dict_dir.mkdir()

    # 创建模拟的 txt 文件
    (dict_dir / "A~C.txt").touch()
    (dict_dir / "D,E,F.txt").touch()
    (dict_dir / "G~I,K.txt").touch()

    return dict_dir

def test_build_file_map(setup_fake_dict):
    """ 测试 build_file_map 是否能正确建立字母到文件路径的映射 """
    dict_dir = setup_fake_dict
    file_map = build_file_map(dict_dir)

    # 预期的文件映射
    expected_mapping = {
        "a": str(dict_dir / "A~C.txt"),
        "b": str(dict_dir / "A~C.txt"),
        "c": str(dict_dir / "A~C.txt"),
        "d": str(dict_dir / "D,E,F.txt"),
        "e": str(dict_dir / "D,E,F.txt"),
        "f": str(dict_dir / "D,E,F.txt"),
        "g": str(dict_dir / "G~I,K.txt"),
        "h": str(dict_dir / "G~I,K.txt"),
        "i": str(dict_dir / "G~I,K.txt"),
        "k": str(dict_dir / "G~I,K.txt"),
    }

    assert file_map == expected_mapping

@pytest.mark.parametrize("word, expected_file", [
    ("apple", "A~C.txt"),  # A 开头的单词应匹配 A~C.txt
    ("banana", "A~C.txt"),  # B 开头的单词应匹配 A~C.txt
    ("dog", "D,E,F.txt"),  # D 开头的单词应匹配 D,E,F.txt
    ("grape", "G~I,K.txt"),  # G 开头的单词应匹配 G~I,K.txt
    ("zebra", "未找到匹配的文件"),  # Z 开头的单词未找到
])
def test_find_word_in_dict(setup_fake_dict, word, expected_file):
    """ 测试 find_word_in_dict 是否能正确匹配单词 """
    dict_dir = setup_fake_dict
    result = find_word_in_dict(word, dict_dir)

    # 如果找到了匹配文件，则检查文件名是否匹配
    if expected_file != "未找到匹配的文件":
        assert os.path.basename(result) == expected_file
    else:
        assert result == expected_file
