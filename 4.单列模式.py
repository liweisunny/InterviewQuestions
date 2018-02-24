#__author:liwei
#date:2017/2/23

# 使用 __new__()方法实现
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a=1

cls=MyClass()
cls2=MyClass()
print(id(cls))
print(id(cls2))
