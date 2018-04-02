def climbingLeaderboard(scores, alice):
    # first, convert list of scores into ranks
    # we know that 1st score is max score
#     scores[0] = max_score
#     new_score_list = [1]
#     current_score = 1
#     for b in range(1,len(scores)):
#         if scores[b] == scores[b-1]:
#             new_score_list.append(current_score)
#         elif scores[b] < scores[b-1]:
#             current_score += 1
#             new_score_list.append(current_score)

    

        
    for a in alice: # iterate through e/ of alice scores; 5 25 50 120
        scores = set(scores) # make scores become a set
        scores.add(a) # insert alice's scores into set ONE AT A TIME

        scores = list(scores) # turn set back into list to get indices
        scores.sort(reverse=True) # reveres scores so that they're in descending order

        print "scores list is " + str(scores)
    
        # for index in range(len(scores)-1, 0, -1): # [120, 100, 50, 40, 25, 20, 10, 5]
        #     if scores[index] in alice:
        #         print index + 1
        #     break
        for index in range(len(scores)-1, -1, -1):
            if scores[index] == a:
                print index + 1

climbingLeaderboard([100,100,50,40,40,20,10],[5,25,50,120])

# Problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem