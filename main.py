#----------------------------------------------------
# letter_count(string)
#---------------------------------------------------
def letter_count(string):
    dict = {}
    words = string.split()

    for word in words:
        for letter in word:
            if letter.lower() in dict:
                dict[letter.lower()] += 1
            else:
                dict[letter.lower()] = 1
    
    return dict

#----------------------------------------------------
# count_words(string)
#---------------------------------------------------
def count_words(string):
    words = string.split()
    count = len(words)
    return f"{count} words found in the document"
 
#----------------------------------------------------
# open_file_for_process(file_path)
#---------------------------------------------------
def open_file_for_process(file_path):
    file_contents = ""
    try:
        with open(file_path) as f:
            file_contents = f.read()
            #print(count_words(file_contents))
            #print(letter_count(file_contents))
    except FileNotFoundError:
        print("Sorry, the file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return file_contents

#----------------------------------------------------
# report_header(file_string)
#---------------------------------------------------
def report_header(file_string):
    print(f"--- Begin report of {file_string} ---")

#----------------------------------------------------
# main()
#---------------------------------------------------
def main():
    file_string = "books/frankenstein.txt"
    report_header(file_string)
    file_contents = open_file_for_process(file_string)
    #print(file_contents)
    print(count_words(file_contents))
    print()
    letter_dict = letter_count(file_contents)
    sorted_dict = {k: letter_dict[k] for k in sorted(letter_dict)}

    for key, value in sorted_dict.items():
        if key.isalpha():
            print(f"The {key} character was found {value} times")

    print("--- End report ---")

#----------------------------------------------------
# The main()
#---------------------------------------------------
main()