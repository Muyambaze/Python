
name=input("Enter your name:")
print(f"Hi {name}")
date=input("What is the date today: ")
mood=input("What is your mood today: ")
mood_yes=input("What was your yesterday's mood: ")
motivation=input("What keeps you moving?: ")
num_mood=int(mood) # Changing strings to integers
num_mood_yes=int(mood_yes)
total_mood=num_mood+num_mood_yes
average_mood=total_mood/2
print(f"The average mood is: {average_mood:.2f}")
print(f"What motivates is: {motivation}")
print("And I expect tomorrow to be the best")
# word count foe each entry
name_words=name.split() # Seperating sentence into words
name_count=len(name_words)
print(f"The name contains {name_count} word(s)")
mood_words=mood.split()
mood_count=len(mood_words)
print(f"The mood contains {mood_count} word(s)")
motivation_words=motivation.split()
motivation_count=len(motivation_words)
print(f"The motivation contains {motivation_count} word(s)")

# To check the largest entry, we consider the onw with thw larges number of letters

entries = {"Name": name, "Mood": mood, "Yesterday's Mood": mood_yes, "Motivation": motivation}
longest_entry = max(entries, key=lambda k: len(entries[k].replace(" ", "")))
print(f"The longest entry is: {longest_entry} → {entries[longest_entry]}")



