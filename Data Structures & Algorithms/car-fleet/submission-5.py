class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # arrange each car and its speed into an sorted dict
        cars = dict()
        for i, pos in enumerate(position):
            cars[pos] = speed[i]

        # calculate time to destination
        etas = []
        for pos, speed in sorted(cars.items(), reverse=True):
            if speed > 0:
                time_to_dest = (target-pos)/speed
            else:
                time_to_dest = 0
            
            if not etas or time_to_dest > etas[-1]:
                etas.append(time_to_dest)
        
        return len(etas)