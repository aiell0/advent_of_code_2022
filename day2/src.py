# PART ONE
play = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
total_score: int = 0
draw: int = 3
lose: int = 0
win: int = 6
with open("example.txt", "r") as file:
    for line in file:
        rps_round = line.strip().split(" ")
        opponents_move = rps_round[0]
        my_move = rps_round[1]

        if opponents_move == "A":
            if my_move == "X":
                total_score += (play.get(my_move) + draw)
            elif my_move == "Y":
                total_score += (play.get(my_move) + win)
            elif my_move == "Z":
                total_score += (play.get(my_move) + lose)
        elif opponents_move == "B":
            if my_move == "X":
                total_score += (play.get(my_move) + lose)
            elif my_move == "Y":
                total_score += (play.get(my_move) + draw)
            elif my_move == "Z":
                total_score += (play.get(my_move) + win)
        else:
            if my_move == "X":
                total_score += (play.get(my_move) + win)
            elif my_move == "Y":
                total_score += (play.get(my_move) + lose)
            elif my_move == "Z":
                total_score += (play.get(my_move) + draw)

print("Total Score: ", total_score)

# PART TWO
play = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
total_score: int = 0
rock: int = 1
paper: int = 2
scissor: int = 3
with open("input.txt", "r") as file:
    for line in file:
        rps_round = line.strip().split(" ")
        opponents_move = rps_round[0]
        result = rps_round[1]

        if opponents_move == "A":
            if result == "X":
                total_score += (play.get(result) + scissor)
            elif result == "Y":
                total_score += (play.get(result) + rock)
            elif result == "Z":
                total_score += (play.get(result) + paper)
        elif opponents_move == "B":
            if result == "X":
                total_score += (play.get(result) + rock)
            elif result == "Y":
                total_score += (play.get(result) + paper)
            elif result == "Z":
                total_score += (play.get(result) + scissor)
        else:
            if result == "X":
                total_score += (play.get(result) + paper)
            elif result == "Y":
                total_score += (play.get(result) + scissor)
            elif result == "Z":
                total_score += (play.get(result) + rock)

print("Total Score: ", total_score)
