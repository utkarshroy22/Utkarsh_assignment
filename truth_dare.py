import random

# Predefined questions and dares
truth_list = [
    "What is your biggest fear?",
    "Have you ever lied to your best friend?",
    "What is your most embarrassing moment?"
]

dare_list = [
    "Do 5 push-ups",
    "Sing a song loudly",
    "Dance for 30 seconds"
]

# Randomly choose between truth and dare
option = random.choice(["Truth", "Dare"])

print("Selected Option:", option)

# Display Result
if option == "Truth":
    print("Truth Question:", random.choice(truth_list))
else:
    print("Dare Task:", random.choice(dare_list))