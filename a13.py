s.add(x)#如果数据项x不在集合s中，讲x添加到s中
s.updata(t)#合并集合t中的元素当前集合s中，并自动去除重复元素
s.pop()#随机删除并返回集合中一个元素，如果集合为空则抛出异常
s.remove(x)#如果x在集合s中，移除该元素；如果不存在则抛出异常
s.discard(x)#如果x在集合s中，移除该元素；如果不存在则报错
s.clear()#清空集合
stu_class = {1:'a',2:'b',3:'c'}
for name in stu_class.keys():#.keys之便利字典中的键
    print(name)
for name in stu_class.values(): #.values遍历字典中的值
    print(name)
for name in stu_class.items():#.items遍历字典中的键-值对
    print(name)
#replace(被替换，替换，次数)
