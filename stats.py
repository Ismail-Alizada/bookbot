def word_count(text):
    all_words_list= text.split()
    number_of_words = len(all_words_list)
    print(f"{number_of_words} words found in the document")

def character_count(text):
    lower_case_text=text.lower()
    character_dictionary={}
    for char in lower_case_text:
        if char in character_dictionary:
            character_dictionary[char]+=1
        else:
            character_dictionary[char]=1
    return character_dictionary


def sort_on(items):
    return items["count"]

def sort_dictionary(dictionary):
    list_of_dictionaries=[]
    for characaters in dictionary:
        small_dict={}
        if characaters.isalpha():
            small_dict["char"]=characaters
            small_dict["count"]=dictionary[characaters]
            list_of_dictionaries.append(small_dict)
    list_of_dictionaries.sort(reverse=True,key=sort_on)
    return(list_of_dictionaries)




