boxes = [12, 5, 8, 8, 23, 15, 7, 8, 9, 12, 34, 6,
         # 6,
         9, 16, 8, 23, 12, 7, 5, 3]
boxes.sort()
truck = []

for i in boxes:
    truck.append(i)
    if sum(truck) > 100:
        break
if sum(truck) - boxes[0] <= 100:
    truck.remove(truck[0])
else:
    truck.pop()

print(boxes)
print(truck)
print(sum(truck))