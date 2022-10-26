"""
csv
逗号分隔值（Comma-Separated Values，CSV，有时也称为字符分隔值，因为分隔字符也可以不是逗号），
其文件以纯文本形式存储表格数据（数字和文本）
"""
import csv

#创建文件编辑对象
# newline 新行内容治为空
# encoding='utf-8-sig'  # 可解决office打开中文乱码的问题
file = open('z-风车动漫视频爬取.csv', 'w', encoding='utf-8', newline='')
# 通过csv的write方法，创建csv的编辑对象
file_csv = csv.writer( file )

#通过csv的编辑对象写入表格内容
# writerow 传入列表，列表中每个元素，站表格的一个单元格

file_csv.writerow(    [1,2,3,4,5,6]    )
file_csv.writerow(    [1,2,3,4,5,6]    )
file_csv.writerow(    [1,2,3,4,5,6]    )
file_csv.writerow(    [1,2,3,4,5,6]    )
file_csv.writerow(    [1,2,3,4,5,6]    )
file_csv.writerow(    [1,2,3,4,5,6]    )