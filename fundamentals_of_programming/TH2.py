# Q1. The one who couldn't finish
# There were a lot of participants in a marathon.
# Among the participants, only one person couldn't finish the race.
# You are given 2 lists, one for the participants' names and one for the names who finished the race.
# Write a program that returns the person's name who couldn't finish.

# Restrictions,
# There are people who have same names.

def solution1(participants, completion):
    answer = ""
    ##############################
    for i in range(len(completion)):
        if completion[i] in participants:
            participants.remove(completion[i])

    answer = participants[0]
    ##############################

    return answer


assert solution1(["leo", "kiki", "eden"], ["eden", "kiki"])
assert solution1(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
assert solution1(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])


# Q2. Printer
# We want to make a printer scheduling program that has priorities
# The scheduling rules are as follows

# 1. Take the first document in the queue
# 2. If there are documents that has higher priority than the current document, send it to the bottom of the queue
# 3. Or else, print the current document

# For example if there were ABCD in queue, and the priorities were 2132,
# The printer should print the documents in order of CDAB
# You are given 2 lists, priorities and the document location
# Write a program that takes 2 lists, priorities and the initial document location, as the input
# and returns which place the document will be printed


def solution2(priorities, location):
    answer = 0
    ##############################
    target = priorities[location]
    m = max(priorities)
    ind = priorities.index(m)

    ##############################

    return answer


assert solution2([2, 1, 3, 2], 2) == 1
assert solution2([1, 1, 9, 1, 1, 1], 0) == 5


