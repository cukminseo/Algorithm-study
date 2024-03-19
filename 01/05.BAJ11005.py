'''
백준 11005번
'''
import sys

sys.stdin = open('BAJ11005.txt', 'r')
origin_num, form = map(int, input().split())
word_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ""
cnt_iter = 0
while origin_num > 0:
    # 나눠진 자릿수 구하기
    each_point = origin_num % form
    # 다시 나눌 자릿수 구하기
    origin_num = origin_num // form
    # 결과에 합치기
    result += word_set[each_point]

print(result[::-1])
