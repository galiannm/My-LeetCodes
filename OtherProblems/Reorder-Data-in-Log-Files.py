class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digi = []
        letter = []
        for log in logs:
            identifier, content = log.split(" ", 1) 
            if content[0].isdigit(): 
                digi.append(log)
            else:
                letter.append((identifier, content, log))
        letter.sort(key=lambda t:(t[1], t[0]))
        return [log for _,_,log in letter] + digi