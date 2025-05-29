# Build a Mad Libs Generator with Conditional Statements!
def mad_libs():
    print("Welcome to the Mad Libs Generator!")

    # Collecting a user information
    name = input("Enter a name: ")
    animal = input("Enter your favorite animal: ")
    color = input("Enter a color: ")
    food = input("Enter your favorite food: ")
    verb = input("Enter a verb ending in -ing: ")
    place = input("Enter a place: ")
    mood = input("How are you feeling today (happy, sad, excited)? ").lower()

    # Conditional statement to change the story based on mood
    if mood == "happy":
        story = (
            f"One sunny day, {name} was {verb} through the park with a {color} {animal}. "
            f"They were on their way to {place} to eat some delicious {food}. "
            f"Everyone could see how happy {name} looked, and the world seemed perfect!"
        )
    elif mood == "sad":
        story = (
            f"On a rainy afternoon, {name} wandered alone with a {color} {animal}. "
            f"They had planned to go to {place}, but all they could think of was {food}, "
            f"which reminded them of better days. {name} kept {verb} slowly, feeling very down."
        )
    elif mood == "excited":
        story = (
            f"{name} was bursting with energy! With their {color} {animal} by their side, "
            f"they raced to {place} to enjoy a wild feast of {food}. "
            f"The day was perfect for {verb}, and everyone could feel the excitement in the air!"
        )
    else:
        story = (
            f"{name} had a strange day. With a {color} {animal}, they went to {place} to eat {food}. "
            f"No one could tell exactly how {name} felt, but the way they kept {verb} said it all..."
        )

    print("\n🎉 Your Mad Lib Story:")
    print(story)
mad_libs()
