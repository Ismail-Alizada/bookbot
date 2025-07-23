from stats import word_count,character_count,sort_on,sort_dictionary
import sys

def get_text_from_file(pathfile):
    with open(pathfile) as f:
        string_contents= f.read()
    return string_contents



def main():
    
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    word_count(get_text_from_file(sys.argv[1]))
    occurence_of_each_character=character_count(get_text_from_file(sys.argv[1]))
    sorted_dictionary_list=sort_dictionary(occurence_of_each_character)
    
    for character_data in sorted_dictionary_list:
        print(f"{character_data["char"]}: {character_data["count"]}")


main()
