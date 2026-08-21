from heapq import heappush, heappop
start = tuple(map(int, input("Enter 9 values (0 for blank): ").split()))
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
queue, seen = [(0, start)], {start}
while queue:
    moves, state = heappop(queue)
    if state == goal:
        print("Minimum moves:", moves)
        break
    blank = state.index(0)
    for nxt in (blank-3, blank+3, blank-1, blank+1):
        if 0 <= nxt < 9 and abs(blank % 3 - nxt % 3) <= 1:
            item = list(state); item[blank], item[nxt] = item[nxt], item[blank]
            item = tuple(item)
            if item not in seen:
                seen.add(item); heappush(queue, (moves + 1, item))

