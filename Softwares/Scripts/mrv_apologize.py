#!/usr/bin/env python3
# coding=utf-8

## @file mrv_apologize.py
## @brief Let Mr. V apologize for someone's birthday.
##
## Copyright (c) 2023-24 Leisquid Li.
##
## This Shell script is licensed under the GNU Affero General Public License
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
## '24. 3. 8  new

import sys

APOLOGY_TEXT: str = """针对今晚%s%s周年生日会直播中出现的“延迟播出”“信源中断”等问题，Vsinger团队在此向大家致以诚挚歉意，非常抱歉在今天这个日子影响了各位的庆生心情，给大家带来了不好的体验，辜负了你们对%s的关爱，十分抱歉。

Vsinger团队已经开启问题原因调查，直播是硬件设备、网络环境、运维管理等综合能力的体现，这次问题的发生暴露了我们的不足，Vsinger团队将引以为鉴，深刻反思，也将在近日给各位朋友一个结果交代。

老V将把此次直播期间所有收到的打赏和礼物全部给到同人项目组，给到所有创作者，感谢你们对%s%s周年的辛勤付出。对一直陪伴%s的朋友们，老V真诚希望给予庆生补偿，也希望各位给Vsinger团队一些时间。再次抱歉，万分感谢！

Vsinger全体制作及运营团队
20%02d年%d月%d日
"""

def usage():
    print("用法：%s 歌手名 周年 年(yy) 月(M) 日(d)" % sys.argv[0])
    exit(114)


def main():
    if (len(sys.argv) == 6):
        print(APOLOGY_TEXT % (sys.argv[1], sys.argv[2], sys.argv[1], sys.argv[1], sys.argv[2], sys.argv[1], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))
    else:
        usage()

if (__name__ == "__main__"):
    main()
    exit(0)
