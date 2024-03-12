from collections import deque

grid = open('./input.txt', 'r').read().splitlines()

start_points = set()

for i in range(len(grid[0])):
    start_points.add((0, -1, 0, 1))
    start_points.add((0, i, 1, 0))
    start_points.add((len(grid) - 1, i, -1, 0))
    start_points.add((len(grid) - 1, len(grid[0]) - 1, 0, -1))

def count(start):
    seen = set()
    q = deque([start])

    while q:
        r, c, dr, dc = q.popleft()

        r += dr
        c += dc

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue
        
        ch = grid[r][c]

        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "/":
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
                    
    coords = {(r, c) for (r, c, _, _) in seen}

    return len(coords)

highest = 0

for start_point in start_points:
    current_count = count(start_point)
    highest = current_count if current_count > highest else highest

print(highest)