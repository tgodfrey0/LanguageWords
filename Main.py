import random

def selectTargetLanguage():
    print("1)Russian\n2)English\n3)German")
    choice = input("Please select your target language: ")
    if((choice.upper() == "1") or (choice.upper() == "RUSSIAN")):
        return "RUSSIAN"
    elif((choice.upper() == "2") or (choice.upper() == "ENGLISH")):
        return "ENGLISH"
    elif((choice.upper() == "3") or (choice.upper() == "GERMAN")):
        return "GERMAN"
    else:
        print("\nPlease enter a valid option")
        selectTargetLanguage()

def getWords(language):
    """
    subject = noun
    adverb = adverb
    verb = verb
    adjective = adjective
    direct_object = noun
    indirect_object = noun
    location = location
    """
    files = [open(str("./LanguagePacks/nouns/" + language), "r"),
    open(str("./LanguagePacks/adverbs/" + language), "r"),
    open(str("./LanguagePacks/verbs/" + language), "r"),
    open(str("./LanguagePacks/adjectives/" + language), "r"),
    open(str("./LanguagePacks/nouns/" + language), "r"),
    open(str("./LanguagePacks/nouns/" + language), "r"),
    open(str("./LanguagePacks/locations/" + language), "r")]
    words = []
    for i in range(7):
        lines = files[i].readlines()
        words.append(lines[random.randint(0, len(lines)-1)].strip("\n"))
    return words

def display(words):
    print("\nBelow are your randomly generated words:")
    print("Subject: " + words[0])
    print("Adverb: " + words[1])
    print("Verb: " + words[2])
    print("Adjective: " + words[3])
    print("Direct Object: " + words[4])
    print("Indirect Object: " + words[5])
    print("Location: " + words[6])

target_language = selectTargetLanguage()
display(getWords(target_language))
while(input("Press any key for more words, type \"exit\" to quit\n").lower() != "exit"):
    display(getWords(target_language))
# Include nunbers in adjectives
print("Goodbye")