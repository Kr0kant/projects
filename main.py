#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #добавили модуль math
import numpy #добавили модуль numpy
import matplotlib.pyplot as mpp #импортируем модуль pyplot из matplotlib и называем его mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': #проверка на запуск как программы (не библиотеки)
    arguments = numpy.arange(0, 200, 0.1) #создаём массив дробных элементов
    mpp.plot( #функция, которой задаётся график
        arguments, #передаем функции plot список - значения по x
        [math.sin(a) * math.sin(a/20.0) for a in arguments] #передаем функции plot список - значения по y
    )
    mpp.show() #открываем график на экране