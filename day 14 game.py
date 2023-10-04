data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality Tv personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality Tv personality',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    }
]

import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def game():
    score = 0
    correct = True

    def random_numbers():
        return random.sample(data, 2)

    def compare_followers(A, B):
        return A if A["follower_count"] > B["follower_count"] else B
    
    A, B = random_numbers()
    correct_answer = compare_followers(A, B)

    while correct:

        print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")
        print(f"Compare B: {B['name']}, {B['description']}, {B['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ")

        

        if choice == 'A' or choice == 'B':

            chosen_user = A if choice == 'A' else B

            if chosen_user == correct_answer:
                score += 1
                clear_console()
                print(f"You're right! Current score: {score}")
            
            else:
                clear_console()
                print(f"Sorry, that was wrong. Final score: {score}")
                correct = False

            A = correct_answer
            B = random.choice([B for B in data if B != A])
            correct_answer = compare_followers(A, B)
                
        else:
            clear_console()
            print(f"Sorry, that was wrong. Final score: {score}")
            correct = False

game()





















