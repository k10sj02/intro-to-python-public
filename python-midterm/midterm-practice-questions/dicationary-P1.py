import json
from difflib import get_close_matches

word = input("Enter word: ")
data = json.load(open("data.json"))
w = word.lower()

if w in data:
   if type(data[w]) == list:
    for item in data[w]:
        print ("")
        print(item)
        print("****")
elif w.title() in data: 
   if type(data[w.title()]) == list:
    for item in data[w.title()]:
        print ("")
        print(item)
        print("****")    
    
elif len(get_close_matches(w, data.keys())) > 0:
     yn = input(f"Did you mean {get_close_matches(w, data.keys())[0]} instead? Enter Y if yes, or N if no: " )
     if yn == "Y":
         w=(data[get_close_matches(w, data.keys())[0]])
         if type(w) == list:
           for item in w:
            print ("")
            print(item)
            print("****")
     elif yn == "N":
            print ("The word doesn't exist. Please double check it.")
     else:
            print("We didn't understand your entry.")
else:
    print( "The word doesn't exist. Please double check it.")


