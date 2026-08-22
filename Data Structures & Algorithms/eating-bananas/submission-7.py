class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        start = 1
        end = max(piles)
        result = max(piles)
        while start <= end:
            k = (start + end )//2
            hours = 0 
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                result = min(result, k)
                end = k - 1   
            else:
                start = k + 1 
            
        
        return result


        

        #brute force approach #exceeds timelimit though
        # start = 1
        # end = max(piles)

        # while start <= end:

        #     total_hours = 0

        #     for pile in piles:
        #         hours = pile // start

        #         if pile % start != 0:
        #             hours += 1

        #         total_hours += hours

        #     if total_hours <= h:
        #         return start

        #     start += 1

        # return end


        