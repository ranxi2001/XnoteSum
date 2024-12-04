import json
import os

def merge_twitter_notes(file1_content, file2_content):
    data1 = json.loads(file1_content)
    data2 = json.loads(file2_content)
    
    merged_data = {}
    
    # 使用最新的配置
    merged_data['$myTwitterNoteConfig'] = data2['$myTwitterNoteConfig']
    
    # 合并分组
    merged_groups = {}
    for group_key in set(data1['$myTwitterNoteGroup'].keys()) | set(data2['$myTwitterNoteGroup'].keys()):
        if group_key in data1['$myTwitterNoteGroup'] and group_key in data2['$myTwitterNoteGroup']:
            group1 = data1['$myTwitterNoteGroup'][group_key]
            group2 = data2['$myTwitterNoteGroup'][group_key]
            merged_groups[group_key] = {
                'value': f"{group1['value']}|{group2['value']}" if group1['value'] != group2['value'] else group1['value'],
                'primaryColor': group2['primaryColor'],
                'secondaryColor': group2['secondaryColor'],
                'weight': group2['weight']
            }
        else:
            merged_groups[group_key] = data1['$myTwitterNoteGroup'].get(group_key) or data2['$myTwitterNoteGroup'][group_key]
    
    merged_data['$myTwitterNoteGroup'] = merged_groups
    
    # 合并用户标注
    merged_items = {}
    for item_key in set(data1['$myTwitterNoteItems'].keys()) | set(data2['$myTwitterNoteItems'].keys()):
        if item_key in data1['$myTwitterNoteItems'] and item_key in data2['$myTwitterNoteItems']:
            item1 = data1['$myTwitterNoteItems'][item_key]
            item2 = data2['$myTwitterNoteItems'][item_key]
            merged_items[item_key] = {
                'tag': f"{item1['tag']}|{item2['tag']}" if item1['tag'] != item2['tag'] else item1['tag'],
                'name': f"{item1['name']}|{item2['name']}" if item1['name'] != item2['name'] else item1['name'],
                'group': item2['group'],
                'isShow': item2.get('isShow', False),
                'index': item2.get('index', -1),
                'highlight': item2.get('highlight', False)
            }
        else:
            merged_items[item_key] = data1['$myTwitterNoteItems'].get(item_key) or data2['$myTwitterNoteItems'][item_key]
    
    merged_data['$myTwitterNoteItems'] = merged_items
    
    # 更新时间戳
    merged_data['$myTwitterNoteTime'] = max(data1.get('$myTwitterNoteTime', 0), data2.get('$myTwitterNoteTime', 0))
    merged_data['$myTwitterNoteWebDAV'] = max(data1.get('$myTwitterNoteWebDAV', 0), data2.get('$myTwitterNoteWebDAV', 0))
    
    return json.dumps(merged_data, ensure_ascii=False)

def main():
    # 获取脚本所在的目录路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # 使用 os.path.join 构建完整的文件路径
        file1_path = os.path.join(script_dir, 'myTwitterNote_data_1733332136747.txt')
        file2_path = os.path.join(script_dir, 'zero.txt')
        output_path = os.path.join(script_dir, 'newsum.txt')
        
        # 检查文件是否存在
        if not os.path.exists(file1_path):
            print(f"错误：找不到文件 - {file1_path}")
            return
            
        if not os.path.exists(file2_path):
            print(f"错误：找不到文件 - {file2_path}")
            return

        # 读取第一个文件
        with open(file1_path, 'r', encoding='utf-8') as f1:
            content1 = f1.read()
            
        # 读取第二个文件
        with open(file2_path, 'r', encoding='utf-8') as f2:
            content2 = f2.read()
            
        # 合并文件内容
        merged_content = merge_twitter_notes(content1, content2)
        
        # 写入新文件
        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.write(merged_content)
            
        print(f"合并完成！结果已保存到 {output_path}")
        
    except FileNotFoundError as e:
        print(f"错误：找不到文件 - {e}")
    except json.JSONDecodeError as e:
        print(f"错误：JSON 格式解析失败 - {e}")
    except Exception as e:
        print(f"错误：发生未知错误 - {e}")

if __name__ == "__main__":
    main()
