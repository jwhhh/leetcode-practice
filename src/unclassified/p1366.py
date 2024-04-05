from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 0:
            return ""
    
        teams_num = len(votes[0])
        if teams_num == 0:
            return ""

        # collect statistics
        vote_count_dict = {}
        for vote in votes:
            for pos in range(len(vote)):
                val = vote[pos]
                if val not in vote_count_dict:
                    vote_count_dict[val] = [0] * teams_num
                vote_count_dict[val][pos] += 1
                
        # rank from statistics
        vote_count_dict = sorted(vote_count_dict.items())
        sorted_vote_count = sorted(vote_count_dict, key=lambda e: e[1], reverse=True)
        res_list = [e[0] for e in sorted_vote_count]
        
        return "".join(res_list)
        
        
# votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]

# row i: team (i+'A')
# col j: #votes in position j

# 26 * 26
# vote_count = [
#     [2, 2, 2],
#     [2, 2, 2],
#     [2, 2, 2]
# ]

# vote_count = [
#     [5, 0, 0],
#     [0, 2, 3],
#     [0, 3, 2]
# ]
