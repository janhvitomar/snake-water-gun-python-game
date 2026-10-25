# snak, water, and gun Game.
import random

def game_win(user, computer):

    if user == computer:
        return None

    # Snake vs Water
    if user == "s" and computer == "w":
        return True
    if user == "w" and computer == "s":
        return False

    # Water vs Gun
    if user == "w" and computer == "g":
        return True
    if user == "g" and computer == "w":
        return False

    # Gun vs Snake
    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False


user_score = 0
computer_score = 0
draws = 0

round_no = 1

while round_no <= 3:

    print("\n========================")
    print("       ROUND", round_no)
    print("========================")

    # User's choice
    user = input("Choose Snake(s), Water(w), Gun(g): ").lower()

    # Check invalid input
    if user not in ["s", "w", "g"]:
        print("❌ Invalid choice!")
        print("Please choose only s, w, or g.")
        print("🔄 Starting this round again...")
        continue

    # Computer's choice
    rand_no = random.randint(1, 3)

    if rand_no == 1:
        computer = "s"
    elif rand_no == 2:
        computer = "w"
    else:
        computer = "g"

    # Find result
    result = game_win(user, computer)

    print("\nYou chose:", user)
    print("Computer chose:", computer)

    if result is None:
        print("🤝 It's a draw!")
        draws += 1

    elif result:
        print("🎉 You win this round!")
        user_score += 1

    else:
        print("😔 Computer wins this round!")
        computer_score += 1

    # Increase round only after VALID input
    round_no += 1

    print("\nCurrent Score:")
    print("You:", user_score)
    print("Computer:", computer_score)
    print("Draws:", draws)


# Final result
print("\n========================")
print("       FINAL RESULT")
print("========================")

print("Your score:", user_score)
print("Computer score:", computer_score)
print("Draws:", draws)

if user_score > computer_score:
    print("\n🎉 YOU WON THE GAME!")

elif computer_score > user_score:
    print("\n😔 COMPUTER WON THE GAME!")

else:
    print("\n🤝 THE GAME IS A DRAW!")