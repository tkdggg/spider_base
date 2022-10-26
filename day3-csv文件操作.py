import csv
# 创建文件编辑对象
# newline 新行为空
# encodeing=’utf-8-sig‘ office可打开
# f=open('z-风车动漫视频爬取.csv','a+',encoding='utf-8')
# file_csv=csv.writer(f)
# 通过csv的编辑对象写入表格内容
import ast
# file_csv.writerow([1,2,3,4])
str="{'1':2},{'3':12}"
str=ast.literal_eval(str)
print(str[1],type(str))
