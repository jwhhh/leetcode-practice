from typing import List


# logs[i] = [ID_i, time_i] meaning user ID_i performed an action at minute time_i
# UAM: #unique minutes in which the user performed an action
# -> an indexed array `answer` of size `k`, answer[j] is #users whose UAM=j
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        logs = [tuple(log) for log in logs]
        logs_unique = set(logs)     # e.g. {(0, 2), (1, 2), (1, 3), (0, 5)}
        
        uam = dict()
        for log in logs_unique:
            uid = log[0]
            if uid not in uam:
                uam[uid] = 0
            uam[uid] += 1

        answer = [0] * k
        for count in uam.values():
            answer[count-1] += 1

        return answer