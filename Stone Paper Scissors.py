import random

def BotChoice():
    return random.randint(1, 3)

def Check(pick):
    if pick == 1:
        return "Stone"
    elif pick == 2:
        return "Paper"
    else:
        return "Scissors"

def Calc_Points(user_pick, bot_pick):
    points_Bot = 0
    points_user = 0

    if user_pick == bot_pick.lower():
        print("Same pick as bot\nNo points for both")
    elif (user_pick == "stone" and bot_pick == "Paper") or \
         (user_pick == "paper" and bot_pick == "Scissors") or \
         (user_pick == "scissors" and bot_pick == "Stone"):
        print(f"Bot picked {bot_pick}\n+1 point for bot")
        points_Bot += 1
    else:
        print(f"Bot picked {bot_pick}\n+1 point for you")
        points_user += 1

    return points_Bot, points_user

repeat = True
while repeat:
    op = int(input("1. Start game\n2. Exit\nEnter Choice: "))
    if op == 1:
        games = int(input("Enter the number of games: "))
        print("Game is starting...")
        
        total_points_bot = 0
        total_points_user = 0

        for _ in range(games):
            user_pick = input("1. Stone\n2. Paper\n3. Scissors\nEnter your pick: ")
            if user_pick == "1":
                user_pick = "stone"
            elif user_pick == "2":
                user_pick = "paper"
            elif user_pick == "3":
                user_pick = "scissors"
            else:
                print("Invalid choice, try again.")
                continue

            pick = BotChoice()
            bot_pick = Check(pick)
            points_bot, points_user = Calc_Points(user_pick, bot_pick)

            total_points_bot += points_bot
            total_points_user += points_user

        print(f"Final Score - Bot: {total_points_bot}, You: {total_points_user}")
        if total_points_bot > total_points_user:
            print("Bot Won the game")
        elif total_points_user > total_points_bot:
            print("You Won the game")
        else:
            print("The game ended in a Draw")
    elif op == 2:
        repeat = False
    else:
        print("Invalid choice, please try again.")
