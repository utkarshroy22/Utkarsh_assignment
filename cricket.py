# Cricket Score Calculator

runs = 0
balls = 0

while True:
    ball = input("Enter runs scored (0-6) or 'w' for wicket or 'q' to quit: ")

    if ball == 'q':
        break
    elif ball == 'w':
        print("Wicket!")
        balls += 1
    elif ball.isdigit() and int(ball) in range(7):
        runs += int(ball)
        balls += 1
    else:
        print("Invalid input!")

# Final Score
overs = balls // 6
remaining_balls = balls % 6

print("\nFinal Score:")
print("Runs:", runs)
print("Overs:", f"{overs}.{remaining_balls}")