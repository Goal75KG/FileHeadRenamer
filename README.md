# File Renamer Script

该脚本通过识别文件头来确定文件的实际格式，并根据检测结果自动替换文件的后缀名。适用于文件格式混淆、文件类型错误标记等情况。

## 功能
- 根据文件头检测文件格式并识别后缀
- 预览替换后的文件名
- 批量替换文件后缀名

## 文件签名支持
当前支持以下常见文件格式：
- 图片：`jpg`, `png`, `gif`, `bmp`, `tif`, `pcx`, `webp`, `ico`, `cur`, `psd`
- 文档和压缩文件：`pdf`, `zip`, `rar`, `ps`, `doc`, `mp3`

您可以在代码中的 `FILE_SIGNATURES` 字典中自行添加其他文件格式的签名。

## 使用方法
### 1. 下载或克隆项目
将脚本文件 `file_renamer.py` 下载到本地。

### 2. 使用Python运行脚本
在命令行中，运行以下命令：

#### 预览替换后的文件名
此模式下不会进行实际重命名操作，只显示文件名的变化：

```bash
python file_renamer.py "<目录路径>" -p
```

示例：

```bash
python file_renamer.py "C:\Users\Username\Pictures" -p
```

#### 替换所有文件后缀名

此模式会对所有可识别的文件进行实际的后缀名重命名：

```bash
python file_renamer.py "<目录路径>" -a
```

示例：

```bash
python file_renamer.py "/home/username/Pictures" -a
```

### 参数说明


- `directory`

  ：必填，指定要处理的文件夹路径。路径可以为绝对路径或相对路径。

  - **绝对路径** 示例（Windows）： `"C:\Users\Username\Pictures"`
  - **绝对路径** 示例（Linux或Mac）： `"/home/username/Pictures"`
  - **相对路径** 示例： `./images`（假设当前目录下的 `images` 文件夹）
  - **当前目录**： `.` 表示当前脚本所在的目录

- `-p, --preview`：预览模式，仅显示替换后的文件名，不执行实际重命名。

- `-a, --all`：替换模式，将识别的文件后缀进行重命名操作。

### 注意事项

- 请务必在运行替换命令前备份文件，以避免意外丢失或覆盖数据。
- 路径需要用引号括起来，以防包含空格或特殊字符。

## 文件头签名参考

- `jpg`：`b'\xFF\xD8\xFF'`
- `png`：`b'\x89PNG'`
- `gif`：`b'GIF87a'`, `b'GIF89a'`
- `bmp`：`b'\x42\x4D'`
- `tif`：`b'\x49\x49\x2A\x00'`, `b'\x4D\x4D\x00\x2A'`
- `pcx`：`b'\x0A\x05\x01\x08'`
- `webp`：`b'\x52\x49\x46\x46'`
- `ico`：`b'\x00\x00\x01\x00'`
- `cur`：`b'\x00\x00\x02\x00'`
- `psd`：`b'\x38\x42\x50\x53'`

## 系统要求

- Python 3.6或更高版本

## 常见问题

1. **文件类型无法识别怎么办？**
   请确保文件格式在 `FILE_SIGNATURES` 字典中有正确的文件头签名。您可以根据需要添加更多签名。
2. **脚本可以处理非图片文件吗？**
   是的，当前支持多种文件格式（如PDF、ZIP、RAR、MP3等），可以在 `FILE_SIGNATURES` 中添加所需格式。

## 许可证

本项目使用 MIT 许可证。