class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        #sort the people list 
        people.sort()
        ans = 0 
        left = 0
        right = len(people)-1 

        while left <= right:  
            if people[left] + people[right] <= limit:    
                left += 1
                right -=1
            else:
                right -=1

            ans = ans +1     

        print(ans)   
        return (ans) 

         
        
         









        