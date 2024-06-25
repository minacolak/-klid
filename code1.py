import math

# Öklid Mesafesi için bir fonksiyon yazma
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Kullanıcıdan noktaları alma
points = []
num_points = int(input("Kaç tane nokta girmek istiyorsunuz? "))

for _ in range(num_points):
    x = float(input("x koordinatını girin: "))
    y = float(input("y koordinatını girin: "))
    points.append((x, y))

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
if distances:
    min_distance = min(distances)
    print("Noktalar arasındaki minimum Öklid mesafesi:", min_distance)
else:
    print("Yeterli nokta yok.")


