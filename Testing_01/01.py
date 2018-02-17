# import numpy
# print(numpy.__version__)
import types


# a = 7.
# b = a/3
#
#
# a = range(10)
# print(a.__len__())
# b = a[:len(a)-1]
# # print(len(a))
# # print(a[-1])
# # print(b)
# c = list(range(10))
# # print(type(c))
# # print(a)
# d = a[len(a)-1]
# print(type(c))
# b = list(a)
# # print(type(b))
# # example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]
# # print(type(example_list))
#
# print(type(a))

# for i in b:
#     print(i)
#
# for i in a:
#     print(i)

# s = set({'sadf', 'sdfsadf'})
# print(s)
#
# t = ('sadfsf', 'sdfsadf')
# print(type(t))

# def fib(max):
#     a, b = 0, 1
#     # while 1:
#     yield b
#     print(a)
#
# # c = fib(1).__next__()
# # d = fib(3).__next__()
# # print(c)
# # d = fib(3)
#
# for a in fib(2):
#     print('')       #每执行到yield，返回生成一个迭代器
#     # print(a)


# class Fib(object):
#     def __init__(self):
#         self.n, self.a, self.b = 0, 0, 1
#
# class Fib2(Fib):
#     pass
#
# a = Fib().name
# a.name = 'orange'
# print(a.name)

# class Person(object):
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#     def showAge(self):
#         # print("%s: %s" % (self.age, self.name))
#         # print("%s" % self.name)
#         print("%.2f, %s" % (self.age, self.name))
#
#
# p1 = Person('orange', 27)
# p1.weight = 80          #动态绑定属性
# print(p1.weight)

#
# class Person(object):
#
#     def __init__(self, name):
#         self.__name = name      #定义私有属性
#
# p1 = Person('orange')

# class Person(object):
#     __name = ''
#     __age = 0
#
#     __kill__ = 'bingo'
#
#     # def __init__(self, name, age):
#     #     self.__age = age
#     #     self.__name = name
#
#     # def get_name(self):
#     #     return self.__name
#
#     def get_attr(self):
#         return self.__age, self.__name
#
#     def set_attr(self, name, age):
#         if age > 10:
#             self.__age = age
#         self.__name = name
#
#
# p1 = Person()
# print(p1.__kill__)
# p1.set_attr('orange', 5)
# attr = p1.get_attr()
# print(p1.get_attr())

# class Animal(object):
#     def run(self):
#         print('running...')
#
#
# class Dog(Animal):
#     def run(self):
#         print("Dog running...")
#
#
# class Cat(Animal):
#     def run(self):
#         print("Cat running...")
#
#
# a = list()
# b = Animal()
# c = Dog()
#
# print(isinstance(a, list))
#
# print(isinstance(a, dict))
#
# print(isinstance(c, Animal))
#
# print(isinstance(c, Dog))


# class Animal(object):
#     def run(self):
#         print('animal run....')
#
#
# def run_twice(obj):
#     obj.run()
#     obj.run()
#
#
# cat = Animal()
# run_twice(cat)      #需要保证传入对象有run的方法即可   file-like-object


# type((x for x in range(10))) == types.GeneratorType

# str = 'ABC'
# print(dir(str))
# str.__len__()

# def __nameP__():
#     return 'orange'
#
# class Person(object):
#     pass
#
#
# p1 = Person()
# __nameP__()


# class MyDog(object):
#     def __len__(self):
#         return 100
#
#
# dog = MyDog()
#
# class Tree(object):
#     def __init__(self):
#         self.tall = 10
#         self.leaves = 1000
#
#     @staticmethod
#     def die():
#         print('Gone Forever')
#
#     def Grow(self):
#         print('Grow')
#
# tree1 = Tree()
# # print(hasattr(tree1, 'tall'))
# # setattr(tree1, 'age', 100)
# # print(tree1.age)
# # getattr(tree1, 'tall', 404)
#
# Tree.die()
# tree1.Grow()
# # print(getattr(tree1, 'tall'))


# class Person(object):
#     __slots__ = ('name', 'age')     #能够指定该类可以绑定的属性，但是子类无效
#
#
# class Student(Person):
#     __slots__ = ('iq')              #若子类继承父类，且也同时指定绑定属性，则其可绑定属性为自身加父类可绑定属性
#
#
# # p1 = Person()
# # p1.name = 'orange'
# # p1.age = 20
# stu1 = Student()
# stu1.iq = 150
# stu1.name = 'orange'
# stu1.age = 10


# class Person(object):
#     def __init__(self):
#         self._age = None
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int):
#             raise ValueError('type error')
#
#         if value<0 or value >100:
#             raise ValueError('value error')
#         self._age = value
#
#
# p1 = Person()
# p1.age = 'sdf'
# print(p1.age)

# class Screen(object):
#
#     def __init__(self):
#         self._width = None
#         self._height = None
#         self._resolution = None
#
#     @property
#     def width(self):
#         return self.width
#
#     @width.setter
#     def width(self, value):
#         self._width = value
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         self._height = value
#
#     @property
#     def resolution(self):
#         self._resolution = self._width * self._height
#         return self._resolution
#
#
# s1 = Screen()
# s1.width = 375
# s1.height = 667
# print(s1.resolution)

# class Person(object):
#
#     def talk(self):
#         print('Person talk')
#
#
# class runalble(object):
#
#     def canRun(self):
#         print('can run')
#
#
# class Student(Person, runalble):        #支持多继承, MixIn设计
#     pass
#
#
# stu1 = Student()
# stu1.canRun()
# stu1.talk()

# class Person(object):
#     def __init__(self, name):
#         self._name = name
#
#     def __str__(self):
#         return 'jadsfojsdjf'
#
#
# p1 = Person('orange')
# print(p1)

#
# class Fib(object):
#
#     def __init__(self):
#         self.a, self.b = 0, 0
#
#     def __iter__(self):
#         return self         #实例本身即是迭代对象，返回自己
#
#     def __next__(self):         #由for调用，每次for都会调用迭代对象的next方法
#         self.a, self.b = self.a+1, self.b+1
#         # print("%s" % self.a)
#         if self.a>10:
#             raise StopIteration
#         return self.a
#
#
# for a in Fib():
#     print(a)

# class Fib(object):
#
#     def __getitem__(self, n):       #实现该方法，可以使用下标式取值
#         self._a, self._b = 1, 1
#         for x in range(n):
#             self._a, self._b = self._b, self._a+self._b
#         return self._a
#
#
# f = Fib()
# print(f[10])

# class Person(object):
#
#     age = 19
#     __name = 'orange'
#     def __getattr__(self, item):        #当访问一个不存在的属性时，会调用该方法
#         return "%s" % self.__name
#
#
# p1 = Person()
# print(p1.age)
# print(p1.name)

# class Person(object):
#
#     def __init__(self, name):
#         self.__name = name
#
#     def __call__(self):
#         print("my name is %s" % self.__name)
#
#
# p1 = Person('orange')
# if callable(p1()):      #判断是否可以直接调用
#     p1()             #默认调用__call__方法


# from enum import Enum, unique
#
# @unique         #保证值没有重复
# class Month(Enum):
#     Jan = 1
#     Feb = 2
#
# print(Month.Jan.value)


# Month = Enum('Month', (
#     'Jan', 'Feb', 'Mar', 'Apr',
#     'May', 'Jun', 'Jul', 'Aug',
#     'Sep', 'Oct', 'Nov', 'Dec'
# ))

# class Person(object):
#     pass
#
#
# Month = Enum.__call__('Month', ['Jan', 'Feb'])
#
# for name, member in Month.__members__.items():
#     print(name, '-->', member, ',', member.value)


# def fn(name='world'): # 先定义函数
#     print('Hello, %s.' % name)
#
#
# # Hello = type('Hello', (object,), {'hello': fn('orange')})
# Hello = type('Hi', (object,), dict(hello=fn()))     # 动态创建一个class, 第一个参数是Cls名字，第二个是继承类，第三个是动态绑定方法
#
# h = Hello()
# print(type(h))
# h.hello


# class listM(object):
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls)
#
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
#
#
# class List(listM):
#     pass


# l1 = List()

# sum = lambda arg1, arg2: arg1 + arg2    #lambda声明匿名函数，函数不能访问除传入参数外其它所有变量，其主体是一个表达式，而不能放代码块
# print(sum(1, 2))


# def testingArgs(firstArg, *args, **kwargs):
#     # print(firstArg)
#     # for v in args:
#     #     print(v)
#     #args（*修饰可变参数）的类型是tuple，kwargs（**修饰关键字参数）的类型是Dict，作用类似于封包与解包的过程
#     for v, k in  kwargs.items():
#         print(v, k)
#
# a = {'sjdfo':12, 'sdfad':'dasfsdf'}
# type(a)
# testingArgs(1, 12, 13, 14, k1=10, ke=11)

# var = 'yes' if 1>0 else 'no'    #if else 行内表达式
# print(var)
#
# def returnName(name = 'name'):
#     print(name)
#
#
# returnName()       #如果没有默认值，且缺少传入参数，则崩溃

#
# a = None
# def testing():
#     global a    #声明该a是来自外部的变量a，而不是函数内部的局部变量
#     a = 100
#     # print(a)
#
#
# testing()
# print(a)

