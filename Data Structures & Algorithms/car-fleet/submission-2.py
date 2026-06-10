class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # arrange each car and its speed into an sorted dict
        cars = dict()
        for i, pos in enumerate(position):
            cars[pos] = speed[i]

        etas = []

        # calculate time to destination
        time_to_dest = []
        for pos, speed in sorted(cars.items(), reverse=True):
            time_to_dest = (target-pos)/speed
            while etas and time_to_dest <= etas[-1]:
                etas.pop()
            if not etas or time_to_dest > etas[-1]:
                etas.append(time_to_dest)
        
        return len(etas)