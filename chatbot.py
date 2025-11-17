import random

# ------------------- FUNCTIONS -------------------

# Greet the user
def greet(name):
    print(f"Welcome {name}")

# Show game menu
def showMenu():
    playing = True
    while playing:
        print("\n!--- Activity Menu ---!")
        print("1. Study 📕")
        print("2. Play Games 🎮")
        print("3. Eat 🍴")
        print("4. Sleep 💤")
        print("5. Read 📖")
        print("6. Quit Game 🙋‍♀️")

        choice = input("Enter your choice (1–6): ")
        print("\nYour stats for choice:")

        if choice in ["1", "2", "3", "4"]:
            updateStats(choice)
            showStatus()

            if choice == "1":
                print("Chatbot: You’re studying hard! Keep it up 🎯\n")
            elif choice == "2":
                print("Chatbot: Yay! Playing games is fun 🏓\n")
            elif choice == "3":
                print("Chatbot: Eating is always a good idea 🍰\n")
            elif choice == "4":
                print("Chatbot: Sweet dreams! 😴\n")

        elif choice == "5":
            showQuote()
            showStatus()

        elif choice == "6":
            print("Chatbot: Leaving the game... back to chatting! 🗣")
            print("Your Final Stats:", stats)
            playing = False

        else:
            print("Not a valid choice! ☹")

# Get chatbot input
def GetResponse():
    userInput = input("You: ").lower()

    if userInput in responses:
        print(f"Chatbot: {responses[userInput]}")

        if userInput in ["game", "play"]:
            playChoice = input("You: ").lower()
            if playChoice == "yes":
                showMenu()
            else:
                print("Chatbot: Okay bestu 😻 we can keep chatting")

    else:
        print("Chatbot: Hmm... Idk what to say! 😖")

    return userInput

# End chat
def endChat(userInput):
    return not (userInput == "bye")

# Update stats
def updateStats(choice):
    if choice == "1":  # Study
        stats["energy"] -= 20
        stats["points"] += 10
        stats["mood"] = "🤓"

    elif choice == "2":  # Play games
        stats["energy"] -= 10
        stats["points"] += 5
        stats["mood"] = "🎮"

    elif choice == "3":  # Eat
        stats["energy"] += 15
        stats["mood"] = "🍔"

    elif choice == "4":  # Sleep
        stats["energy"] = 100
        stats["mood"] = "😴"

# Show stats
def showStatus():
    print(f"\nEnergy: {stats['energy']}")
    print(f"Points: {stats['points']}")
    print(f"Mood: {stats['mood']}\n")

# Show random quote
def showQuote():
    quote = random.choice(quotes)
    print(f"\n📚 Motivational Quote: {quote}\n")
    stats["points"] += 5
    stats["mood"] = "💡"

# End game summary
def endGame():
    print("\n🎉 Game Over! 🎉")
    print("Here's your final summary:")
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")
    print(f"Energy: {stats['energy']}")
    print(f"Points: {stats['points']}")
    print(f"Mood: {stats['mood']}")
    print("Thanks for playing the GenZ Life Simulator! 💖")

# ------------------- DATA -------------------

# User profile
user = {
    "name": "",
    "age": 0
}

# Stats
stats = {
    "energy": 100,
    "mood": "😊",
    "points": 0
}

# Chatbot responses
responses = {
    "hi": "hey bestuu 😚😚",
    "hello": "hey bestie! 👋 how's it going?",
    "how are you": "im vibing, wbu 🤗🤗",
    "how is life going": "well im just a bot here to answer your questions 😄",
    "im happy": "that's great! is there any specific reason you are happy today? 😊",
    "not really": "that's okay, sometimes we do feel that way without any reason 💗",
    "im sad": "aww is there any specific reason because of which you are feeling sad? 🥺",
    "i do not know the real reason": "that's totally normal, sometimes we feel things we can't explain 🤍",
    "how to change my mood and feel better": "try music, a walk, talking to someone you trust, or journaling 💛",
    "okay thanks": "no need for that, I am always here if you ever need me 💖",
    "play": "OOOOO😁😁....Want to play a GenZ life simulator with me? yes/no 🤗🤗",
    "game": "OOOOO😁😁....Want to play a GenZ life simulator with me? yes/no 🤗🤗",
    "bye": "aww 😚😚 see you soon, take care bye! 🤗🫂",
    "what's up": "Just chilling and chatting with my bestuu 😎",
    "tell me a joke": "Why don’t skeletons fight each other? They don’t have the guts! 😂",
    "motivation": "Remember, you are amazing and capable of anything! 💪✨",
    "thank you": "anytime bestie! 😘",
    "good morning": "Good morning! ☀️ Ready to slay today? 🫶",
    "good night": "Sweet dreams bestie! 😴🌙"
}


# List of quotes
quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "You are stronger than you think.",
    "Small steps every day lead to big results.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Dream big. Start small. Act now. – Robin Sharma",
    "Push yourself, because no one else is going to do it for you.",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Don’t limit your challenges, challenge your limits.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Stay positive, work hard, make it happen.",
    "Great things never come from comfort zones.",
    "Do something today that your future self will thank you for.",
    "Your only limit is your mind.",
    "You don’t have to be perfect to be amazing.",
    "Success doesn’t just find you; you have to go out and get it.",
    "Wake up with determination, go to bed with satisfaction.",
    "Every day is a new beginning. Take a deep breath and start again.",
    "Believe in yourself and all that you are. – Christian D. Larson",
    "Discipline is the bridge between goals and accomplishment. – Jim Rohn",
    "Keep your face always toward the sunshine—and shadows will fall behind you.",
    "Work hard in silence, let success make the noise.",
    "The secret of getting ahead is getting started. – Mark Twain",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Perfection is a myth!"
]

# ------------------- MAIN PROGRAM -------------------

user["name"] = input("Enter your name: ")
user["age"] = int(input("Enter your age: "))

print(user)
greet(user["name"])

print("Chatbot: Hey bestuu! 💖 I'm here to chat. Type 'bye' anytime to exit.")

chatting = True

while chatting:
    userInput = GetResponse()
    chatting = endChat(userInput)

endGame()
