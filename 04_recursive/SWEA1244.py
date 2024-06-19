'''
Created by: minseo
Date: 3/27/24
Desc :
Excute time : ms(time.perf_counter())
'''
import time

# 측정 시작
start_time = time.perf_counter()

import sys

sys.stdin = open('SWEA1244.txt', 'r')

from typing import List


def int2list(num: int) -> list[int]:
    int_list = []
    str_num = str(num)
    for index in range(len(str_num)):
        int_list.append(int(str_num[index]))
    return int_list


def shuffle_card(will_try: int, fn_card_list: List[int], now_index: int = 0) -> List[int]:
    will_try -= 1
    highest_index = fn_card_list.index(max(fn_card_list[now_index:]))
    print(f"{now_index}-{highest_index}")
    fn_card_list[highest_index], fn_card_list[now_index] = fn_card_list[now_index], fn_card_list[highest_index]
    if highest_index == now_index:
        will_try += 1
    if not will_try or now_index > len(fn_card_list) - 1:
        return fn_card_list
    else:
        return shuffle_card(will_try, fn_card_list, now_index+1)


def list2str_ptr(num: int, r_list: list):
    print(f"#{num}", end=' ')
    for element in r_list:
        print(element, end='')
    print()


iters = int(input())
for now_iter in range(iters):
    card, change = map(int, input().split())
    card_list = int2list(card)
    print(f"변경 횟수 : {change}, 변경전 :", end="")
    list2str_ptr(now_iter, card_list)
    card_list = shuffle_card(change, card_list)
    list2str_ptr(now_iter, card_list)

# 측정 종료 시간
end_time = time.perf_counter()
# 실행 시간 출력
print(f"실행 싯간: {(end_time - start_time) * 1000:.7f} milliseconds")
