"""
- 숫자를 2진수로 바꾸는 함수가 있을겨 ( 없다면 스스로 하기.. )
----------- 처음 생각 -----------
- n 보다 큰 자연수를 순차적으로 탐색하면서 1의 개수가 같은게 나오면 리턴 (최후의 방법)
        or
        
[ 규칙 생각하기 ]        
- n 2진수 변환 -> 1의 개수 세기 (X)
    -> 여기서 생각은, 1이 위치한 가장 작은 자리를 0으로 바꾸고 그 다음거를 1로 바꾸기?..
    
    -> ex) 10 = 1010 // 1100 요런식으로 ??
    
            11 = 1011
            12 = 1100 이렇게?
            
        ex2) 78 = 1001110 // 예상은  1011100
            답은 1010011 .. 완전 틀려버렸꼬..
            
- 음. 마지막에 있는 1 무리 앞에 1로 바꾸고 바로 뒷자리는 0 나머지 1들이 존재하면 다 뒤로 밀기
    ex) 78 = 1001110 => 1010011 (O)
        15 = 1111 => 10111 (O)
        10 = 1010 => 1100 (O)
        14 = 1110 => 10011 (O)
 => 답은 이거로 하면 나올듯 한데, 구현을 하기가.. 
    필요 ) 1의 개수 , 마지막에 있는 1의 무리의 인덱스(이넘을 유지하기가.. 하우투?)
    
    마지막에 있는 1의 무리의 인덱스
    flag = false로 두고
    1 만나면 true로 변환하고 index 업데이트 (flag==false일때만)
    
    0 만나면 flag = false로 변환

0. 주어진 n을 2진수로 변환해야함 ( 내장함수 bin(), oct(), hex() 사용! 리턴은 문자열)
1. 필요한 정보 : 1의 개수(count) , 앞에서 1이 얼마나 쓰였는가(before), 1의 마지막 무리의 위치(idx)
    + 앞에서 1이 얼마나 쓰였는가를 세는게 좀?! 101101 이런식이면   101110 
    
    ~~~ 1을 10으로 바꿀경우,, 101101 -> 1011(0)10 그냥 자리를 바꾼다는 느낌이 나을거같은데?
    
2. 1의 마지막 무리의 앞을 1로 그 뒤는 0으로 놓되, 나머지 1을 맨 끝으로
3. 나머지 1들을 맨 뒤로 옮김
    => 여기서 좀 복잡해짐.. 사실 이젠 이 방법이 아닌 것 같음.. 그래도 간다..
    => restOne(남은 1의 개수 = 뒤로 가야할 1의 개수), restSize(남은 사이즈)
    
    =>=> size를 기준으로 해버리면, 1111 -> 10111 이렇게 사이즈가 달라지는걸 처리를 못해
    => 차라리 1 -> 10으로 바꾸는게..
    
    
    "110"(6)->"1001"(9)

--------------- 결론 ---------------
0. 주어진 n을 2진수로 변환해야함 ( 내장함수 bin(), oct(), hex() 사용! 리턴은 문자열)
1. 필요한 정보 : 1의 개수(count) , 앞에서 1이 얼마나 쓰였는가(before), 1의 마지막 무리의 위치(idx), 남은 1의 개수(restOne)

2. 마지막 1의 무리의 첫번째 1 -> 10으로 바꾸기
    + 이때 더 채워야할 사이즈도 구하기(restSize)

3-1. index == 0 일땐 앞에 "10" 붙이기
3-2. index != 0 일땐 죽 나열하다가 해당 Index부위에 "10" 붙이기

4. 나머지는 "0"*(restSize-restOne) + "1"*(restOne) 으로 붙여주면된다.

( 이전에 했던 방식은 좀 더 복잡 했다.)
    

--------------- 에러 케이스 ----------------
- 모두 1 일 때 = 위와 같은 방식으로 헤결 가능
- 1111 -> 10111 : index = 0 인 경우를 따로 처리함. (10만 더해주는 식으로)
- 1100 -> 1001 : 위와 같이 따로 처리할 경우 여기서 에러가 남( 테케1 나머진 다오케 )

--------- 새롭게 알게된것 ---------
- python len으로 배열 범위 넘어가는거는 그냥 0으로 취급함. 오호! 그래서 에러가 안난거야

"""
def getIdx(n):
    flag = False
    idx = -1 # -1은 그냥 초기값때문에!
    count = 0 
    before = -1
    for index, num in enumerate(n):
        
        if(num=="1"):
            if(flag==False):
                idx = index
                before = count
                flag = True
                
            count += 1
        elif(num=="0"):
            flag = False
    
    return idx, count, before
                                
def solution(n):
    answer = 0
    
    n = format(n, "b")
    
    index, count, before = getIdx(n)
    
    restOne = count-before-1
    
    restSize = len(n[index+1:])
    if(index == 0):        
        n = "10" + "0"*(restSize-restOne) +"1"*(restOne)
    else:
        n = n[:index-1]+"10"+"0"*(restSize-restOne) +"1"*(restOne)
        
    answer = int(n, 2)
    return answer