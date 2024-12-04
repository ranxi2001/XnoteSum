# 推特标注脚本合并工具

用于将多个推特标注备注数据文件进行合并，支持自动处理重复条目。

## 功能特点

- 支持合并多个推特标注数据文件
- 自动处理重复条目（使用 | 分隔符合并）
- 保留最新的配置信息
- 自动更新时间戳
- 支持 UTF-8 编码

## 数据格式说明

输入文件格式为 JSON，包含以下主要字段：
- `$myTwitterNoteConfig`: 配置信息
- `$myTwitterNoteGroup`: 分组信息
- `$myTwitterNoteItems`: 用户标注数据
- `$myTwitterNoteTime`: 时间戳
- `$myTwitterNoteWebDAV`: WebDAV 同步时间戳

## 使用方法

1. 将需要合并的文件放在脚本同一目录下
2. 确保文件名正确：【**更改为自己要合并的文件名**】
   - 第一个文件：`myTwitterNote_data_1733332136747.txt`
   - 第二个文件：`zero.txt`
3. 运行脚本：
```bash
python main.py
```
4. 合并结果将保存在 `newsum.txt` 文件中

## 合并规则

1. 配置信息：使用最新的配置
2. 分组信息：
   - 重复分组使用 | 分隔符合并
   - 保留最新的颜色和权重设置
3. 用户标注：
   - 重复标注使用 | 分隔符合并
   - 保留最新的显示状态和高亮设置
4. 时间戳：使用最新的时间戳

## 相关背景资料

- [X推特账号备注篡改猴插件](https://onefly.top/posts/241024.html)
- [篡改猴插件](https://chromewebstore.google.com/detail/%E7%AF%A1%E6%94%B9%E7%8C%B4/dhdgffkkebhmkfjojejmpbldmpobfkfo)
- [翻译机插件](https://greasyfork.org/zh-CN/scripts/378277-%E7%BF%BB%E8%AF%91%E6%9C%BA)
- [推特备注插件](https://greasyfork.org/zh-CN/scripts/404587-twitter-add-notes-to-the-user)

## 注意事项

1. 确保输入文件为有效的 JSON 格式
2. 文件必须使用 UTF-8 编码
3. 运行脚本前请备份原始数据
4. 确保脚本具有读写权限

## 错误处理

脚本会处理以下错误情况：
- 文件不存在
- JSON 格式解析失败
- 编码错误
- 权限问题

如遇到错误，请查看控制台输出的错误信息。


这个 README 文档包含了：
1. 项目简介和功能特点
2. 详细的使用说明
3. 数据格式和合并规则说明
4. 相关资源链接
5. 错误处理说明


以及原始的背景资料链接：



