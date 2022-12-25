    # 1. N/2 찾기
    # 2. Counter로 종류 세기
    # len(list(nums.keys())) > N/2 면 N/2 return
    # else: return len(list(nums.keys()))

import collections

def solution(nums):
    return min(len(nums)/2, len(set(nums)))
