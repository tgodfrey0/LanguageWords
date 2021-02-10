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
    adjective = adjective
    direct_object = noun
    indirect_object = noun
    location = location
    """
    files = [open(str("./LanguagePacks/nouns/" + language), "r"),
    open(str("./LanguagePacks/adverbs/" + language), "r"),
    open(str("./LanguagePacks/adjectives/" + language), "r"),
    open(str("./LanguagePacks/nouns/" + language), "r"),
    open(str("./LanguagePacks/nouns/" + language), "r"),
    open(str("./LanguagePacks/locations/" + language), "r")]
    words = []
    for i in range(7):
        lines = files[i].readlines()
        words.append(lines[random.randInt(0, lines.len()-1)])
    # subject, adverb, adjective, direct_object, indirect_object, location
    return words

words = getWords(selectTargetLanguage())
print(words)
# subject, adverb, verb, adjective, direct object, indirect object, location