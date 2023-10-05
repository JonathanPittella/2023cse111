import random

while True:
    tense_option = input("Please enter 'tense' to start or 'exit' to quit: ")
    if tense_option.lower() == "tense":
        def get_noun(quantity):
            if quantity == "single":
                nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
            else:
                nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
            noun = random.choice(nouns)
            return noun

        def get_verb(quantity, tense):
            if tense == "past":
                verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
            elif tense == "present" and quantity == "single":
                verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
            elif tense == "present" and quantity != "single":
                verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
            elif tense == "future":
                verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
            else:
                raise ValueError("Invalid tense or quantity")
            verb = random.choice(verbs)
            return verb

        def get_determiner(quantity):
            if quantity == "single":
                words = ["a", "one", "the"]
            else:
                words = ["some", "many", "the"]

            # Randomly choose and return a determiner.
            word = random.choice(words)
            return word.capitalize()
        
        def make_preposition(quantity):
            if quantity == "single": 
                words = ["on", "under", "in", "beside", "between", "above", "below", "behind", "among", "with"]
            else:
                words = ["besides", "among", "across", "around", "along", "throughout", "between", "underneath", "among", "amidst",]

            word = random.choice(words)
            return word.lower()
        
        def make_subjects(quantity):
            if quantity == "single":
                words = ["bus", "lady", "shower", "floor"]
            else:
                words = ["dogs", "books", "students", "contries"]

            word = random.choice(words)
            return word.lower()
        
        def get_adjectives(quantity):
            if quantity == "single" or "plura":
                words = ["beautifull", "intelligent", "friendly", "cold", "colorful"]

            word = random.choice(words)
            return word.lower()
        
        def make_sentence(quantity, tense):
            adjectives = get_adjectives(quantity)
            subjects = make_subjects(quantity)
            preposition = make_preposition(quantity)
            determiner = get_determiner(quantity)
            noun = get_noun(quantity)
            verb = get_verb(quantity, tense)
            sentence = f"{determiner} {adjectives} {noun} {verb} {preposition} the {subjects}."
            return sentence

        def generate_sentences(num_questions):
            questions = []
            answers = []
            
            for _ in range(num_questions):
                quantity = input("Enter quantity ('single' or 'plural'): ")
                tense = input("Enter tense (past, present, or future): ")

                if quantity not in ["single", "plural"] or tense not in ["past", "present", "future"]:
                    print("Invalid input. Please enter valid quantity and tense.")
                    continue

                questions.append((quantity, tense))
                sentence = make_sentence(quantity, tense)
                answers.append(sentence)

            # Print the six answers
            print("\nGenerated Answers:")
            for i in range(6):
                if i < len(answers):
                    print(f"Answer {i + 1}: {answers[i]}.")
                else:
                    print(f"Question {i + 1}: No input provided")
                    print(f"Answer {i + 1}: N/A\n")

        if __name__ == "__main__":
            num_questions = 6  # Define the number of questions to ask
            generate_sentences(num_questions)
    elif tense_option.lower() == "exit":
        break
    else:
        print("Invalid option. Please enter 'tense' to start or 'exit' to quit.")