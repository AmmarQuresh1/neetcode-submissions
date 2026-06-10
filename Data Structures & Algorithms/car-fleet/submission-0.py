class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # arrange each car and its speed into an sorted dict
        cars = dict()
        for i, pos in enumerate(position):
            cars[pos] = speed[i]
        dict(sorted(cars.items()))

        fleets = 0
        fleet = []