import os

MAX_LINE = 3800
IMGNUM = 20000  # 最大图片数量

def get_files(path):
    img_files = []
    # 获取指定路径下所有的文件名
    for root, dirs, files in os.walk(path):
        for file in files:
            img_files.append(file)
    return img_files

def search_words(aim_code):
    root = "DICT/"
    xxx = ""

    # 根据aim_code的第一个字符修改xxx的值
    if aim_code[0].islower():
        xxx = chr(ord(aim_code[0]) - 32)
    
    root += xxx + "/"
    
    # 获取文件列表
    img_files = get_files(root)
    num = len(img_files)
    
    # 如果只有一个文件，直接使用
    if num == 1:
        root += img_files[0]
    else:
        # 多个文件，查找符合aim_code第二个字符的文件
        found = False
        for filename in img_files:
            # 检查文件名是否与aim_code的第二个字符匹配
            if filename[2] == aim_code[1]:
                root += filename
                print(f"Found file: {root}")
                found = True
                break
        
        if not found:
            # 如果没有找到合适的文件
            return "no this words!"

    # 读取文件并查找目标单词
    try:
        with open(root, 'r', encoding='gbk') as file:
            rownum = 0
            for line in file:
                rownum += 1
                line = line.strip()
                if line == aim_code:
                    next_line = file.readline().strip()
                    print(f"Found word: {aim_code} at line {rownum}")
                    print(f"Next line: {next_line}")
                    return next_line
    except FileNotFoundError:
        print(f"Cannot read {root}")
        return "cannot translate this words!"

    return "no this words!"


