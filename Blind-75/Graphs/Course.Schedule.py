class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        mp = defaultdict(list)
        for a, b in prerequisites:
            mp[a].append(b)
        
        visiting = set()
        visited = set()

        def DFS(c):
            if c in visiting: return False
            if c in visited: return True

            visiting.add(c)
            for pre in mp[c]:
                if DFS(pre) is False:
                    return False
            visiting.remove(c)
            visited.add(c)
            return True
        
        for course in range(numCourses):
            if DFS(course) is False:
                return False 
        
        return True
        
        