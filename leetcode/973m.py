class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[float('inf'), point] for point in points]
        for idx, (distance, point) in enumerate(distances):
            distances[idx][0] = (point[0] ** 2 + point[1] ** 2) ** 0.5
        distances.sort(key=lambda x: x[0])
        return [x[1] for x in distances][:k]
