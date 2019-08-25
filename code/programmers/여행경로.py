
def solution(tickets):
    def DFS(airplains, visited):
        nonlocal answer, tickets_number

        if answer:
            return 
        if len(visited) == tickets_number+1:
            answer = visited
            return visited


        if visited[-1] in airplains:
            for dep in range(len(airplains[visited[-1]])):
                new = {k:value if k != visited[-1] else [value[v] for v in range(len(value)) if v != dep] for k, value in airplains.items()}
                DFS(new, visited+[airplains[visited[-1]][dep]])
    answer = []
    
    airplains = {}
    for t in tickets:
        if t[0] in airplains.keys():
            airplains[t[0]].append(t[1])
        else:
            airplains[t[0]] = [t[1]]

    for ap in airplains.values():
        ap.sort()
    
    tickets_number = len(tickets)

    DFS(airplains, ['ICN'])
    return answer

if __name__ == "__main__":
    tickets = [["ICN", "A"], ["ICN", "A"], ["A", "ICN"]]
    print(solution(tickets))