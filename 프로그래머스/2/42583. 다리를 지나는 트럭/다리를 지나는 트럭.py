# bridge_length: 다리에 올라갈 수 있는 트럭 수
# weight: 다리가 견딜 수 있는 무게

def solution(bridge_length, weight, truck_weights):
    
    end_trucks = []
    ing_trucks = []  # [트럭무게, 시간]
    
    truck_cnt = len(truck_weights)
    time = 0
    
    while len(end_trucks) != truck_cnt:
        if len(ing_trucks) > 0:
            # ing 트럭 중에 첫번째 차가 다리를 다 건너면 빼내기
            if ing_trucks[0][1] == bridge_length:
                front_ing_truck = ing_trucks.pop(0)
                end_trucks.append(front_ing_truck)

            # ing 트럭들의 건너는 시간 업데이트
            for truck in ing_trucks:
                truck[1] += 1
                
        # ing 트럭들의 무게 합
        sum_ing_trucks = 0
        for k in ing_trucks:
            sum_ing_trucks += k[0]
            
        # 대기트럭에서 뽑기
        if len(truck_weights) > 0:
            if sum_ing_trucks + truck_weights[0] <= weight:
                front_wait_truck = truck_weights.pop(0)
                ing_trucks.append([front_wait_truck, 1])
            
        # 전체 시간 더해주기
        time += 1
    
    
    answer = time
    return answer
