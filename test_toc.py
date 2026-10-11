import re
import markdown
from typing import List, Dict

# 复制 extract_headers 和 table_of_contents 函数
def extract_headers(markdown_text: str) -> List[Dict]:
    headers = []
    parsed_md = markdown.markdown(markdown_text)
    lines = parsed_md.split("\n")

    stack = []
    for line in lines:
        if line.startswith("<h") and len(line) > 2 and line[2].isdigit():
            level = int(line[2])
            header_text = line[line.index(">") + 1 : line.rindex("<")]

            while stack and stack[-1]["level"] >= level:
                stack.pop()

            header = {
                "level": level,
                "text": header_text,
            }
            if stack:
                stack[-1].setdefault("children", []).append(header)
            else:
                headers.append(header)

            stack.append(header)

    return headers

def table_of_contents(markdown_text: str) -> str:
    def generate_table_of_contents(headers, numbering=None):
        if numbering is None:
            numbering = []
        
        toc = "<ul>"
        for i, header in enumerate(headers, 1):
            current_numbering = numbering + [str(i)]
            number_str = ".".join(current_numbering)
            
            toc += f"<li>{number_str} {header['text']}"
            
            if "children" in header:
                toc += generate_table_of_contents(header["children"], current_numbering)
            
            toc += "</li>"
        
        toc += "</ul>"
        return toc

    try:
        headers = extract_headers(markdown_text)
        toc = "## Table of Contents\n\n" + generate_table_of_contents(headers) + "\n\n"
        return toc
    except Exception as e:
        print("table_of_contents Exception : ", e)
        return markdown_text

# 测试用的 Markdown 文本
test_markdown = """# 霍尔木兹海峡局势对A股市场的影响

## 霍尔木兹海峡简介及其全球重要性

### 霍尔木兹海峡的地理位置与自然特征
霍尔木兹海峡位于阿拉伯半岛和伊朗之间。

### 霍尔木兹海峡的战略地位
霍尔木兹海峡是全球最重要的石油运输通道之一。

### 霍尔木兹海峡的地缘政治风险
近年来，该地区的地缘政治局势变得越来越复杂。

## 霍尔木兹海峡对全球油价的影响

### 油价波动的直接原因
地缘政治局势变化直接影响国际油价。

### 供需关系的变化
海峡局势变化影响长期供需关系。

## A股市场对霍尔木兹海峡地缘政治紧张局势的反应

### 金融市场波动与A股市场的关联
全球金融市场波动传导至A股市场。

### A股市场中能源板块的具体影响
能源板块受油价波动直接影响。

### 投资者情绪与市场行为的变化
投资者采取避险策略。
"""

# 生成目录
toc = table_of_contents(test_markdown)

# 打印结果
print("=== 生成的目录 ===")
print(toc)
print("=== 目录结束 ===")
