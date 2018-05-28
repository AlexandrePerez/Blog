# -*- coding: utf-8 -*-
# article: https://alexandre-perez.fr/2018/05/variable-static-en-python/


# ----- APPROACH 1 -----
counter_global = 0


def add_1_global():
    global counter_global
    counter_global += 1
    print("add_1_global:      {}".format(counter_global))
    return counter_global


# ----- APPROACH 2 -----
def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


@static_vars(count=0)  # counter becomes an attribute of the function add_1_decorator, only once, at function
# definition time
def add_1_decorator():
    add_1_decorator.count += 1
    print("add_1_decorator:   {}".format(add_1_decorator.count))


# ----- APPROACH 3 -----
# todo is it the same as below? Or mutable arg is different -- almost the same, we exploit the call at definition time
# Default argument values are evaluated only once at function definition time, which means that modifying the default
# value of the argument will affect subsequent calls of the function.
def add_1_mutable(static={"count": 0}):
    static["count"] += 1
    print("add_1_mutable:     {}".format(static["count"]))


# ----- APPROACH 4 -----
def add_1_generator():
    k = 0
    while True:
        k += 1
        print("add_1_generator:   {}".format(k))
        yield k


# ----- APPROACH 5 -----
# 3 method but 1 & 2 are amost the same
class Counter:
    count_1 = 0
    count_2 = 0
    count_3 = 0

    @staticmethod
    def add_1_staticmethod():
        Counter.count_2 += 1
        print("add_1_staticmethod:{}".format(Counter.count_2))

    @classmethod
    def add_1_classmethod(cls):
        Counter.count_3 += 1
        print("add_1_classmethod: {}".format(Counter.count_3))


def add_1_object():
    Counter.count_1 += 1
    print("add_1_object:      {}".format(Counter.count_1))


# ----- TEST -----
if __name__ == "__main__":
    generator = add_1_generator()
    generator2 = add_1_generator()

    for i in range(3):
        print("--- iteration {} ---".format(i))
        add_1_global()
        add_1_decorator()
        add_1_mutable()
        next(generator)
        add_1_object()
        Counter.add_1_staticmethod()
        Counter.add_1_classmethod()
