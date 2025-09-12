class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
            
        visit = set()
        def dfs(currCourse):
            if currCourse in visit: #loop detected
                return False
            if preMap[currCourse] == []: #the course can definitly be completed
                return True
            visit.add(currCourse)
            for preCrs in preMap[currCourse]:
                if not dfs(preCrs): return False
            visit.remove(currCourse)
            preMap[currCourse] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

        
        