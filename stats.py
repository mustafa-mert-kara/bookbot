def count_words(text):
    word_list=text.split()
    return len(word_list)

def count_letters(text):
    text=text.lower()
    letter_count={}
    for char in text:
        try:
            letter_count[char]+=1
        except:
            letter_count[char]=1
    return sort_dict(letter_count)

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    list_of_letters=[]
    for val in dict:
        list_of_letters.append({"letter":val,"count":dict[val]})
    list_of_letters.sort(reverse=True,key=sort_on)
    result_dict={}
    for val in list_of_letters:
        result_dict[val["letter"]]=val["count"]
    return result_dict


