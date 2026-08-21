from collections import deque
start, goal = (3, 3, 1), (0, 0, 0)
queue, seen = deque([(start, [])]), {start}
while queue:
    state, path = queue.popleft()
    if state == goal:
        print("Solution:", path + [state]); break
    m, c, side = state
    for dm, dc in ((1,0),(2,0),(0,1),(0,2),(1,1)):
        nm, nc = (m-dm, c-dc) if side else (m+dm, c+dc)
        new = (nm, nc, 1-side)
        if 0 <= nm <= 3 and 0 <= nc <= 3 and (nm == 0 or nm >= nc) and (3-nm == 0 or 3-nm >= 3-nc) and new not in seen:
            seen.add(new); queue.append((new, path + [state]))

