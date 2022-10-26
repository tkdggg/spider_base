
# class stu():
#     name='kksk'
#     age=0
#
#     def eat(self):
#         # self,谁调用这个方法，谁就是self    对象就是self
#         print(self.name,'eating')
#
#     def sleep(self):
#         print(self.name,'sleeping')



# object() 所有类的基类
class stu(object):
    pass

    def __init__(self,name):
        print('初始方法，第一个 自己运行')
        self.name=stu.name
        self.age=stu.age
#       类似于字典新建key

stu.name='kksk'
print(stu.name)












