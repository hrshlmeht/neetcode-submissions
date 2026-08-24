class TimeMap:

    def __init__(self):
        self.obj = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.obj[key].append((value,timestamp))
        return None
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.obj:
            return ""
                
        if timestamp<self.obj[key][0][1]:
            return ""

        left,right = 0, len(self.obj[key])-1
        cur = self.obj[key]
        while left<=right:
            mid = (left+right)//2
            
            if cur[mid][1]==timestamp:
                return cur[mid][0]

            if cur[mid][1]>timestamp:
                right=mid-1
            else:
                left = mid+1
        
        return cur[right][0]