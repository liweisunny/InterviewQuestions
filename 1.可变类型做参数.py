#__author:liwei
#date:2017/2/23

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print (l)

f(2)
f(3,[3,2,1])
f(3)

# 执行结果：
    # [0, 1]
    # [3, 2, 1, 0, 1, 4]
    # [0, 1, 0, 1, 4]

# 解释：

    # python函数在定义的时候，默认参数l的值就被计算出来了，即[]，[]所占用的内存地址也不会变了，除非重新赋值，因为[]是一个可变对象，每次给他li.append()添加值，只是改变了其值，其所指向的对象地址没有变。
    # 所以第三次函数调用沿用的是第一次函数调用后的l的值；第二次函数调用给l参数重新赋值了，所以出现上面的结果。

# 我们修改一下上面的代码，将 print (l) 替换成 print (l,id(l)),执行结果如下：
    # [0, 1] 3070103915592
    # [3, 2, 1, 0, 1, 4] 3070103916360
    # [0, 1, 0, 1, 4] 3070103915592

# 能发现第一次函数调用的l和第三次函数调用的l占用同一块内存地址，是同一个l。

# 不明白的话就试着运行下面的代码吧：

l_mem = []

l = l_mem           # the first call
for i in range(2):
    l.append(i*i)

print (l)             # [0, 1]

l = [3,2,1]         # the second call
for i in range(3):
    l.append(i*i)

print (l)             # [3, 2, 1, 0, 1, 4]

l = l_mem           # the third call
for i in range(3):
    l.append(i*i)

print (l)             # [0, 1, 0, 1, 4]