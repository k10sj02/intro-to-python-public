**Code Along:**
The first part of the code processes a text file named `password.txt`, which represents a sample Linux password file. It parses the file's contents, filtering out lines that don't contain both a username and a shell program. It then creates a CSV file named `report.csv` with two columns: `username` and `shell`, containing the extracted information.

The second part of the code generates a sub-folder named `PRO675S1M` and creates a random number of text files (between 10 and 15). Each file contains 20 randomly selected words from a dictionary file. The code then searches through each file, identifies the longest word in each, and prints a report showing the filename and its longest word.

**Main.py:** 
This Python script processes a text string, performing operations like converting it to lowercase, removing punctuation, and counting word occurrences. It then identifies and displays the most common and least common words within the text, before generating and printing a report based on the processed text. Each operation is facilitated by separate modules imported at the beginning of the script.

**least-common:**
The script defines a function named `least_common` that utilizes the `word_count` module to count word occurrences in a given string, sorts the words based on their frequencies, and prints them along with their counts.

**most-common:**
This Python script defines a function named `most_common` that takes a string as input, calculates the frequency of each word in the string using the `word_count` module, sorts the words based on their frequency in descending order, and finally prints out the most common words along with their frequencies.

**lower-case**
This Python script defines a function called `lower_case` that takes a string as input, converts all characters to lowercase using the `lower()` method, and then returns the modified string.

**punc_remover**
This Python script defines a function called `punc_remover` that takes a string as input. It removes punctuation marks from the string and replaces them with spaces. Then, it splits the string into words and prints both the list of words and the modified string without punctuation. Finally, it returns the list of words.
