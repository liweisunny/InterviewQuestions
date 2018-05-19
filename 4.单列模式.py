#__author:liwei
#date:2017/2/23

# 单例模式的几种实现方案

# ①使用 __new__()方法实现
# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             cls._instance =  super(Singleton, cls).__new__(cls, *args, **kw)
#         return cls._instance
#
# class MyClass(Singleton):
#     a = 1
# cls=MyClass()
# cls2=MyClass()
# print(id(cls),id(cls2))


# ②使用装饰器实现
# from functools import wraps
# def singleton(cls):
#     instance={}
#     @wraps(cls)
#     def getInstance(*args,**kwargs):
#         if cls not in instance:
#            instance[cls]=cls(*args,**kwargs)
#         return instance[cls]
#     return getInstance
# @singleton
# class MyClass(object):
#     a=1
# cls=MyClass()
# cls2=MyClass()
# print(id(cls),id(cls2))


# ③ 使用元类实现
# class Singleton(type):
#     def __init__(self,name,bases,class_dict):
#         super(Singleton,self).__init__(name,bases,class_dict)
#         self._instance=None
#     def __call__(self,*args,**kwargs):
#         if self._instance is None:
#             self._instance=super(Singleton,self).__call__(*args,**kwargs)
#         return self._instance
#
# class MyClass(object):
#     __metaclass__=Singleton
# cls=MyClass()
# cls2=MyClass()
# print(id(cls),id(cls2))



# ④共享属性 （并非真正的单列，只是控制了内存空间）
# class Borg(object):
#     _state={}
#     def __new__(cls, *args, **kwargs):
#         ob=super(Borg,cls).__new__(cls,*args,**kwargs)
#         ob.__dict__=cls._state
#         return ob

# class MyClass(Borg):
#     a = 1
# cls=MyClass()
# cls2=MyClass()
# print(id(cls),id(cls2))

