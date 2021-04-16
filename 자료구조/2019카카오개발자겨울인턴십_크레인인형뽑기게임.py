def solution(board, moves):
    
    cnt = 0     # 집은 인형 총 개수
    result = 0  # 바구니에 남은 인형 개수
    basket = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                cnt += 1    # 집은 횟수 증가
                new = board[j][i-1]     # 바구니에 들어갈 인형
                board[j][i-1] = 0       # 비어있음으로 변경
                
                if basket:       # 바구니가 비어있지 않을 때
                    if basket[-1] == new:       # 바구니의 가장 위에 있는 인형 == 새로 들어갈 인형
                        basket.pop()    # 터트림
                        result -= 1     # 바구니 안 인형 개수 1 감소
                        break
                        
                basket.append(new)      # 바구니에 인형 추가
                result += 1     # 바구니 안 인형 개수 1 증가
                break

    return cnt - result
