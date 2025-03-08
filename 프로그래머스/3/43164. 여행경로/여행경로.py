def DFS(airport_order, n, tickets_dict):
    if len(airport_order) == (n+1):
        return airport_order
    
    now_airport = airport_order[-1]
    if now_airport not in tickets_dict:
        return
    
    neighbor_airport_list = tickets_dict[now_airport]
    
    for idx, neighbor_airport in enumerate(neighbor_airport_list):
        if neighbor_airport == 'X':
            continue
        tickets_dict[now_airport][idx] = 'X'
        result = DFS(airport_order + [neighbor_airport], n, tickets_dict)
        tickets_dict[now_airport][idx] = neighbor_airport
        
        if result:
            return result
        

def solution(tickets):
    n = len(tickets)  # 항공권 수
    tickets_dict = {}
    
    for ticket in tickets:
        start = ticket[0]
        end = ticket[1]
        if start not in tickets_dict:
            tickets_dict[start] = [end]
        else:
            new_list = tickets_dict[start] + [end]
            new_list.sort()
            tickets_dict[start] = new_list
            
    
    answer = DFS(['ICN'], n, tickets_dict)

    return answer