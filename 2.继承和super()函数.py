#__author:liwei
#date:2017/2/23

class A(object):
    def go(self):
        print ("go A go!")
    def stop(self):
        print ("stop A stop!")
    def pause(self):
        print ("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print ("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print ("go C go!")
    def stop(self):
        super(C, self).stop()
        print ("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print ("go D go!")
    def stop(self):
        super(D, self).stop()
        print ("stop D stop!")
    def pause(self):
        print ("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# 说明下列代码的输出结果

a.go()
b.go()
c.go()
d.go()
e.go()

a.stop()
b.stop()
c.stop()
d.stop()
e.stop()

a.pause()
b.pause()
c.pause()
d.pause()
e.pause()

# 分析这道题，考察的是新式类继承顺序(mro）以及super()函数额用法
# mro 不清楚的请参考：http://waisunny.com/2018/01/25/%E4%BD%A0%E7%9C%9F%E7%9A%84%E7%90%86%E8%A7%A3python%E4%B8%AD%E7%9A%84MRO%E7%AE%97%E6%B3%95%E5%90%97%EF%BC%9F/
# super()相当于返回继承顺序的下一个类，而不是父类
# 所以运行结果是：

# go:
# go A go!

# go A go!
# go B go!

# go A go!
# go C go!

# go A go!
# go C go!
# go B go!
# go D go!

# go A go!
# go C go!
# go B go!


# stop:
# stop A stop!

# stop A stop!

# stop A stop!
# stop C stop!

# stop A stop!
# stop C stop!
# stop D stop!

# stop A stop!
# stop C stop!


#pause：
# Not Implemented

# Not Implemented

# Not Implemented

# wait D wait!

# Not Implemented

