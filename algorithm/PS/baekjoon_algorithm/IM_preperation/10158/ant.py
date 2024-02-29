w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

dx = p + t % (2*w)
dy = q + t % (2*h)

if dx > w:
    dx = abs(2 * w - dx)

if dy > h:
    dy = abs(2 * h - dy)

print(dx, dy)