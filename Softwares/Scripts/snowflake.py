#!/usr/bin/env python3
# coding=utf-8

## If you don't know, this is a Python script.
## 如果你不知道的话，这是一个 Python 脚本。

## @file snowflake.py
## @brief Draw a snowflake on turtle with detailed comments.
##        从某中术运营复制过来，并加入了详细注释的电子雪花。
##
## Copyright (c) 2023-24 Leisquid Li.
##
## This Python script is licensed under the GNU Affero General Public License
## version 3 published by the Free Software Foundation and without any warranty
## for liability or particular purpose.
##
## You can modify and/or redistribute it under the GNU Affero General Public
## License version 3 or any later version you want.
##
## License file can be found in this repository; if not, please see
## <https://www.gnu.org/licenses/agpl-3.0.txt>.

## Change history (most recent first):
## ===================================
## '24.2.16   new

## 导入 turtle 模块。这是一个借助 “小海龟” 来画图的模块。
import turtle
## 导入 time 模块，用于计时等需要时间计算的情况。
import time

## 定义一个叫做 `snowflake` 的函数，这里用于递归画出雪花。其中它还接受两个参数，
## 一个是 `length`: int，表示要画出的一条雪花的 “枝条” 的长度；另一个是
## `depth`: int，表示递归深度，这个值越大，画出的雪花的小花瓣就越精密，当然也
## 可能会增加运行时的内存空间负担（调用的栈也会越深）。
def snowflake(length: int, depth: int):
    ## 新建一个屏幕（或者有的地方叫画布、画框）的对象实例。这样就会初始化一个
    ## “小海龟” 的画图窗口。
    screen: turtle._Screen = turtle.Screen()
    ## 指定画布的背景色。
    screen.bgcolor("#0080ff")
    ## 下面这个与屏幕的更新和动画效果有关。我可能理解得不太准确，tracer() 接受
    ## 两个参数，第一个表示 turtle 每运动多少次会更新一次屏幕，第二个表示延迟
    ## 值，约等于每两次屏幕更新的时间间隔，单位为毫秒。这里传入的参数为 (0, 0)，
    ## 表示每次 turtle 运动后屏幕都会更新，而且将延迟值控制到最低以尽可能加速
    ## 画图。
    turtle.tracer(0, 0)
    ## if 判断： 判断递归深度 (depth > 0) 成立时，执行下面被缩进的代码块中的
    ## 代码。
    if (depth > 0):
        ## for 循环：要画出的是六边形的枝条，所以指定循环次数为 6。
        for (i) in range(6):
            ## 设置 turtle 画图速度为最快。
            turtle.speed("fastest")
            ## 设置 turtle 画图颜色为白色。
            turtle.color("white")
            ## 设置 turtle 画线宽度为 5 像素。
            turtle.width(5)
            ## 让 turtle 前进 `length` 个像素，即画出长度为 `length` 的枝条。
            turtle.forward(length)
            ## 递归调用函数 snowflake()，在雪花的一个小枝桠上再画出一圈枝条，
            ## 但是每个小枝条的长度是这个枝桠的 1/3。两个斜杠组成的 `//` 运算符
            ## 表示整除，即做除法运算后舍弃小数部分向下取整。画的小枝条（花瓣）
            ## 的层次数取决于 depth 的值。
            snowflake(length // 3, depth - 1)
            ## 让 turtle 后退 `length` 个像素，回到雪花的原点。
            turtle.backward(length)
            ## 向左旋转 60 度，准备画下一个枝条。
            turtle.left(60)

## if 判断：判断在 Python 中，当前执行的脚本是否作为主程序运行（因为可能会存在
## 这个脚本是被其他程序调用的情况），是的话则执行下面被缩进的代码块中的代码。
## 这么写也算是 Python 特色了。
if (__name__ == "__main__"):
    ## 调用 snowflake() 来画雪花了。指定雪花的 “半径” 为 180，小花瓣的层次数
    ## 为 5。
    snowflake(180, 5)
    ## 主程序昏睡 100 秒，期间保持画布开启，给用户欣赏或截图。
    time.sleep(100)

## 讲解结束。请安装好 Python 3 后执行 `python snowflake.py` 查看效果。
## 有什么问题尽管告诉我罢，我什么都会做的。

## 此致。

## leisquid
## '24.2.16
