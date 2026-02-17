import random

def check_answer(question, options, correct_answer):
    """Function to ask a question, display the options and to check user's answers"""

    print("\n"+question)

    #Shuffle the options
    random.shuffle(options)

    letters = ['A', 'B', 'C', 'D']

    # Create a list of options with the corresponding letters
    anwser_map = {}

    for i, option in enumerate(options):
        print(f"{letters[i]}. {option}")
        anwser_map[letters[i]] = option

    # Get the user input
    user_input = input("\nEnter yout option(A/B/C/D): ").strip().upper()

    #Check the user's answer againts the correct anwser
    if anwser_map.get(user_input) == correct_answer:
        print("\nBoom! Joey would say: How you doin’? 😎")
        return 1
    else:
        print(f"\nNot quite… but hey, even Ross makes mistakes. \nThe correct option is {correct_answer}.")
        return 0

# Display the 25 questions
questions = [
    ("What is the name of Ross’s second wife?",
    ['Carol Willick', 'Emily Waltham', 'Susan Bunch', 'Mona'],
    'Emily Waltham'),

    (" What instrument does Phoebe often play?",
    ['Piano', 'Violin', 'Guitar', 'Drums'],
    'Guitar'),

    ("What is Chandler’s job for most of the series?",
    ['Accountant', 'Lawyer', 'Copywriter', 'Data analyst in statistical processing'],
    'Data analyst in statistical processing'),

    ("What is the name of Joey’s agent?",
    ['Estelle Leonard', 'Janice Litman', 'Erica Ford', 'Kathy'],
    'Estelle Leonard'),

    ("Which character says “We were on a break!”?",
    ['Chandler Bing', 'Joey Tribbiani', 'Ross Geller', 'Mike Hannigan'],
    'Ross Geller'),

    ("What is the name of Monica’s restaurant where she becomes head chef?",
    ['Javu', 'The Moondance Diner', 'Café des Artistes', 'Alessandro’s'],
    'Alessandro’s'),

    ("What is Rachel’s first job in New York?",
    ['Assistant buyer', 'Waitress at Central Perk', 'Fashion designer', 'Receptionist'],
    'Waitress at Central Perk'),

    ("What is the name of Joey’s stuffed penguin?",
    ['Waddles', 'Pingu', 'Hugsy', 'Snowy'],
    'Hugsy'),

    ("Who was Monica’s first serious boyfriend on the show?",
    ['Richard Burke', 'Pete Becker', 'Paul the Wine Guy', 'Alan'],
    'Richard Burke'),

    ("What is the name of Phoebe’s twin sister?",
    ['Regina Buffay', 'Ursula Buffay', 'Lily Buffay', 'Nina Buffay'],
    'Ursula Buffay'),

    ("What is Ross’s profession?",
    ['Paleontologist', 'Archaeologist', 'Biologist', 'Historian'],
    'Paleontologist'),

    ("Which character accidentally reveals Chandler and Monica’s relationship first?",
    ['Phoebe', 'Joey', 'Ross', 'Rachel'],
    'Joey'),

    ("What is the name of Ross’s son?",
    ['Jack', 'Daniel', 'Ben', 'Eric'],
    'Ben'),

    ("Which Las Vegas event happens to Ross and Rachel?",
    ['They lose all their money', 'They win a casino jackpot', 'They get engaged', 'They get married while drunk'],
    'They get married while drunk'),

    ("What is the name of Chandler’s annoying ex-girlfriend?",
    ['Janice', 'Kathy', 'Nina', 'Joanna'],
    'Janice'),

    ("What is Phoebe’s husband’s name?",
    ['David', 'Mike Hannigan', 'Gary', 'Frank Jr.'],
    'Mike Hannigan'),

    ("What is Monica obsessed with keeping clean?",
    ['Her office', 'Her car', 'Her apartment', 'Her shoes'],
    'Her apartment'),

    ("What is Rachel’s daughter’s name?",
    ['Ella', 'Emma', 'Emily', 'Ava'],
    'Emma'),           

    (" Which character is the first to get a turkey stuck on their head?",
    ['Monica', 'Rachel', 'Phoebe', 'Joey'],
    'Joey'),

    ("What is Joey’s famous acting role on TV?",
    ['Dr. Mark Sloan', 'Dr. Joey Tribbiani', 'Dr. Drake Ramoray', 'Dr. House'],
    'Dr. Drake Ramoray'),

    ("Who walks Carol down the aisle at her wedding?",
    ['Joey', 'Chandler', 'Ross', 'Susan'],
    'Ross'),

    ("What is Chandler afraid of?",
    ['Commitment and dogs', 'Heights', 'Water', 'Dogs'],
    'Dogs'),

    ("What is the name of Monica and Rachel’s apartment number after it changes?",
    ['21', '20', '19', '18'],
    '20'),

    ("What does Ross yell when someone touches his sandwich?",
    ['“My sandwich!”', '“Don’t eat that!”', '“That’s mine!”', '“Put it back!”'],
    'My sandwich!'),

    ("How many babies does Phoebe carry for her brother?",
    ['One', 'Two', 'Four', 'Three'],
    'Three')  
]

questions_table = [
    # first row
    {
        "question": "What is the name of Ross’s second wife?",
        "options": ['Carol Willick', 'Emily Waltham', 'Susan Bunch', 'Mona'],
        "correct_answer": '',
    }
]

def run_quiz():
    """Main function to run the quiz"""

    print("\nWelcome to the Friends's TV Show Quiz! Could this be any more exciting?")

    answer_player = input("Are you ready to play? (yes/no): ").strip().lower()

    if answer_player != "yes":
        print("\nOkay, maybe next time!")
        return

    print("\nGrab a coffee and let’s play!")

    # Initialize score to 0
    score = 0

    # Generate a random list of 25 questions
    random_questions = random.sample(questions, 5)
    for question, options, correct_answer in random_questions:
        score += check_answer(question, options, correct_answer)
   

    #Display teh final score
    print(f"Your final score is: {score}/5")

    #Display a message
    if score >= 5:
        print("Legendary performance! Even Monica Geller would celebrate with you.")
    elif score >= 3:
        print("Solid run! Not perfect, but definitely sitcom-worthy.")
    else:
        print("Hey, it happens! Even Joey Tribbiani wouldn’t get them all right.")

# Call the run_quiz function
run_quiz()