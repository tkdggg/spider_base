
# name=["kks","kksk","hso","henshin"]
# print(name)
# print(name[:2])
# name[:2]=["qin","qin","qin"]
# print(name)
# name.remove("qin")
# print(name)

# li=[1,11,21,323,44,54,65]
# li.sort()
# print(li)
# # 元组，无法更改
# y=(1,2,3,4)
# print(list(y))

# 字典
# li=[1,11,21,323,44,54,65]
# d={"name":"jk girl","age":12}
# d["sex"]="mid"
# print(d["name"])
# print(d)

# # 函数
# 位置传递
# 关键字传递
# def add(first,second):
#     th=first+second
#     return th,th,th
# return 返回一个值的时候，返回默认类型
# 返回多个值的时候，默认返回元组

#元组只有一个内容时，后加逗号
# print(add(10,19),type(add(10,19)))
# t=add(10,1)
# t=t+("ls",)
# print(t)

#类的创建和调用
class stu():
    name=''
    age=0

    def eat(self):
        # self,谁调用这个方法，谁就是self    对象就是self
        print(self.name,'eating')

    def sleep(self):
        print(self.name,'sleeping')

l=stu()
l.age=12
l.name='kksk'
# print(l.name)
l.sleep()
















