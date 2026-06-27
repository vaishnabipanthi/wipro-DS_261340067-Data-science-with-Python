def dictionary_facts():
    people_facts = {
        "Jeff": "Is afraid of Dogs.",
        "David": "Plays the piano.",
        "Jason": "Can fly an airplane."
    }
    
    for person, fact in people_facts.items():
        print(f"{person}: {fact}")
        
    print() # blank line
    
    # change a fact
    people_facts["Jeff"] = "Is afraid of heights."
    # add an additional person
    people_facts["Jill"] = "Can hula dance."
    
    for person, fact in people_facts.items():
        print(f"{person}: {fact}")

if __name__ == "__main__":
    dictionary_facts()