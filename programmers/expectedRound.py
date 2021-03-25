"""
- 참가자 번호 주어지고, 언젠가는 만난다..
- 이거는 한 번 수학적인 규칙을 찾아봐야할 것 같다.

전체 진행 라운드 : n에 해당하는 2의 지수 값

# 숫자의 지수승(2) 구하기 
- import math
- math.log2(number) ~ 다른 숫자는 안되더라 log10은 가능

# 파이썬에서 몫 구하기 # 
- // 슬래쉬 두개임!! !!! 두개짜리로 구함!!
- / 슬래쉬 하나는 나머지까지 같이(분수형태)
------------- 첫번째 생각 ---------------
- 2로 나눈 값의 전후로 어쩌구 저쩌구
- 각 값을 빼서 어쩌구 저쩌구
=> 위의 모든 방법을 시도했으나, 실패... 뭔가 수학적으로 뭐가 있는거같은데에

------------- 검색 -------------
- 2를 나눠서 같은 같이 되는 위치를 확인 => 검색하길 잘했다.. 이런 방식이 .... ㅎㅎ^^;;
    = 참가 번호를 같게 만드는 것!
    
    ex ) 1, 2 ->(몫) 0, 1 이 되는데, 1을 더해서 나누면 2,3 -> 1, 1로 동일
"""
import math

def solution(n,a,b):
    answer = 0
    while(a!=b):
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
        
    return answer