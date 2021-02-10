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

target_language = selectTargetLanguage()
print(target_language)