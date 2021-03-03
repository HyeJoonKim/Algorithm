def solution(tickets):
    
    tickets.sort(reverse=True)
    dict = {}
    
    for ticket in tickets:
        if ticket[0] in dict:
            dict[ticket[0]].append(ticket[1])
        else:
            dict[ticket[0]] = [ticket[1]]
    
    st = ['ICN']
    ans = []
    while st:
        top = st[-1]
        if top not in dict or len(dict[top])==0:
            ans.append(st.pop())    # 이 한줄로 개고생함
        else:
            st.append(dict[top].pop())
    ans.reverse()
    return ans
