#!/bin/bash

## @file mrv_apologize.sh
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

APOLOGY_TEXT="针对今晚%s%s周年生日会直播中出现的“延迟播出”“信源中断”等问题，Vsinger团队在此向大家致以诚挚歉意，非常抱歉在今天这个日子影响了各位的庆生心情，给大家带来了不好的体验，辜负了你们对%s的关爱，十分抱歉。

Vsinger团队已经开启问题原因调查，直播是硬件设备、网络环境、运维管理等综合能力的体现，这次问题的发生暴露了我们的不足，Vsinger团队将引以为鉴，深刻反思，也将在近日给各位朋友一个结果交代。

老V将把此次直播期间所有收到的打赏和礼物全部给到同人项目组，给到所有创作者，感谢你们对%s%s周年的辛勤付出。对一直陪伴%s的朋友们，老V真诚希望给予庆生补偿，也希望各位给Vsinger团队一些时间。再次抱歉，万分感谢！

Vsinger全体制作及运营团队
20%02d年%d月%d日
"

usage() {
    ## 打印用法。
    ## $0 表示被执行的脚本名。
    echo "用法：$0 歌手名 周年 年(yy) 月(M) 日(d)"
    exit 114
}

main() {
    ## 格式化并打印文本。
    ## 从 $1 开始表示向脚本传入的参数内容。
    printf "${APOLOGY_TEXT}" $1 $2 $1 $1 $2 $1 $3 $4 $5
}

## 如果命令行传入参数数量等于 5
if [ $# -eq 5 ]; then
    ## 执行自定义的 main 函数
    main $*
## 否则
else
    ## 提醒用法
    usage
## 没了
fi

exit 0
