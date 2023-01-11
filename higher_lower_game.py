import art
from game_data import data
import random
from replit import clear

score = 0
game_over = False

# random_picker function - take the celebrety list as a attribute and randomely picked a item in the list and return it
def random_picker(list):
    """Take the celebrety list as a attribute and randomely picked a item in the list and return it"""
    return random.choice(list)

pick_a = random_picker(data)

while not game_over:

    # Generate Logo
    print(art.logo)

    # First time pick the item randomely and stored in 2 different variables - (Call random_picker function)
    
    pick_b = random_picker(data)

    # Random pick A
    # vs art
    # Random pick B
    print(f"Compare A: {pick_a['name']}, a {pick_a['description']}, from {pick_a['country']} - {pick_a['follower_count']}.")
    print(art.vs)
    print(f"Against B: {pick_b['name']}, a {pick_b['description']}, from {pick_b['country']} - {pick_b['follower_count']}.")

    # Get the answer from user
    user_answer = input("Who has more followers? 'A' or 'B': ").lower()

    # compare follower function - take 2 dictionaries as attributes and return the dictionary with most follower count
    def compare_follower(a, b):
        """Take 2 dictionaries as attributes and return the dictionary with most follower count"""
        if a['follower_count'] >= b['follower_count']:
            return a
        else:
            return b

    # call compare_follower function to compare the follower count
    most_follower_account = compare_follower(pick_a, pick_b)

    # clear()
    clear()

    # if user answer right answer dictionary_b saved to dictionary_a variable and call the random_picker function and save the dictionary in dictionary_b variable
    # And score increase by 1
    if (most_follower_account == pick_a and user_answer == "a") or (most_follower_account == pick_b and user_answer == "b"):
        score += 1
        pick_a = pick_b
        print(f"You're right! Current Score: {score}")
    else:
        # if user wrong - clear(), message, score
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True

    # repeat the process

    