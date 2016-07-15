#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    stemmer = SnowballStemmer("english")
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)
        #words = stemmer(text_string)
        #print text_string
        ### project part 2: comment out the line below
        #words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        

    #print text_string 
    word_list = text_string.strip().split()
    word_cleaned_list = []
    for word in word_list:
        word_stem = stemmer.stem(word)
        #print (word_stem,end="")
        word_cleaned_list.append(word_stem)
    """
    words = word_cleaned_list[0]
    for word in word_cleaned_list:
        if word == words:
            continue
        words= words+" "+word
    """
    words = ""
    words = ' '.join(word_cleaned_list)
    #print words
    return words

    

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    #print text



if __name__ == '__main__':
    main()

