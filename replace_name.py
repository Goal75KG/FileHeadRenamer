import os
import argparse

# 定义常用文件头和文件后缀
FILE_SIGNATURES = {
    b'\xFF\xD8\xFF': 'jpg',
    b'\x89PNG': 'png',
    b'GIF87a': 'gif',
    b'GIF89a': 'gif',
    b'\x25\x50\x44\x46': 'pdf',
    b'\x50\x4B\x03\x04': 'zip',
    b'\x52\x61\x72\x21': 'rar',
    b'\x25\x21\x50\x53': 'ps',
    b'\xD0\xCF\x11\xE0': 'doc',
    b'\x49\x44\x33': 'mp3',
    b'\x42\x4D': 'bmp',          
    b'\x49\x49\x2A\x00': 'tif',  
    b'\x4D\x4D\x00\x2A': 'tif',  
    b'\x0A\x05\x01\x08': 'pcx',  
    b'\x52\x49\x46\x46': 'webp', 
    b'\x00\x00\x01\x00': 'ico',  
    b'\x00\x00\x02\x00': 'cur',  
    b'\x38\x42\x50\x53': 'psd',  
    # 可根据需要添加其他文件类型
}

def identify_file_extension(file_path):
    """根据文件头识别文件后缀"""
    with open(file_path, 'rb') as f:
        file_header = f.read(10)
    for signature, extension in FILE_SIGNATURES.items():
        if file_header.startswith(signature):
            return extension
    return None

def preview_replacement(files):
    """预览替换后的文件名"""
    for file_path in files:
        correct_extension = identify_file_extension(file_path)
        if correct_extension:
            new_file_name = f"{os.path.splitext(file_path)[0]}.{correct_extension}"
            print(f"{file_path} -> {new_file_name}")
        else:
            print(f"{file_path}: 无法识别文件类型")

def replace_all(files):
    """替换文件后缀名"""
    for file_path in files:
        correct_extension = identify_file_extension(file_path)
        if correct_extension:
            new_file_name = f"{os.path.splitext(file_path)[0]}.{correct_extension}"
            os.rename(file_path, new_file_name)
            print(f"已重命名: {file_path} -> {new_file_name}")
        else:
            print(f"{file_path}: 无法识别文件类型，跳过")

def main():
    parser = argparse.ArgumentParser(description="识别文件头并替换文件后缀名")
    parser.add_argument("directory", help="要处理的文件夹路径")
    parser.add_argument("-p", "--preview", action="store_true", help="预览替换后的文件名")
    parser.add_argument("-a", "--all", action="store_true", help="替换所有文件后缀名")

    args = parser.parse_args()
    
    # 获取目录下的所有文件
    files = [os.path.join(args.directory, f) for f in os.listdir(args.directory) if os.path.isfile(os.path.join(args.directory, f))]

    if args.preview:
        preview_replacement(files)
    elif args.all:
        replace_all(files)
    else:
        print("请使用 -p 预览或 -a 替换全部文件后缀名")

if __name__ == "__main__":
    main()
