n = int(input())
w = float(input())
l = float(input())
m = int(input())
o = int(input())


area = n * n
bench = m * o
tiles_area = w * l
area_with_tiles = area - bench
tiles_area = area_with_tiles/tiles_area
time = tiles_area * 0.2

print(round(time,2))
print(round(tiles_area,2))