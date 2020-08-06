import random
import sys
from visualization import SongVisual
#from empty import SongVisual
#keeping a copy there before i fuck itup
import random
import string

LETTERSANDPUNCTUATIONS=(string.ascii_uppercase) + (string.ascii_uppercase).lower() + str("\'")
NUMLINES=random.randint(4,20)

def process_line(line):
    '''
    Process a line of text to extract (state, new_word) pairs.

    We add the BEGIN and END keywords so that we can initialize the
    sentence and know when the line ends.
    '''

    line_list=(line.lower().strip().split())
    line_list.insert(0,'BEGIN')
    line_list.append('END')


    line=[]

    if (line == '') or line == False:
        #cound also use x.isspace()
        return 'empty line'

    for i in range(len(line_list)-2):
        if line_list[i]=='END':
            break
        #list_after=line_list[i+1:]  list of all the words after this word
        key=str(line_list[i])
        one_after=line_list[i+1]
        two_after=line_list[i+1] +' ' +line_list[i+2]
        if line_list[i+2]=='END':
            two_after=one_after
            #easier to give the tuple a value but it's a repeat so it will be parsed out anyway
        tuple1=(key,one_after,two_after)
        line.append(tuple(tuple1)) #tuples

    return line #list of tuples of the word, the words after it

def process_textfile(filename):
    '''
    Creates a dictionary with transition pairs
    based on a file provided

    For the first part of the assignment, we use a
    placeholder text that you will have to replace
    at some point.

    Based on the placeholder text, the dictionary
    should contain the following key-value pairs:

    'blue,': ['END']
    'by': ['yellow', 'day.', 'day?']
    'still': ['hopping', 'going']
    '''
    d = {}

    for lines in open(filename, 'r'):
        if ',' in lines:
        # IS THERE A WAY TO HAVE AFTER A COMMA COUNT AS A NEW SENTENCE?
            split_line=lines.split(',')
            for line in split_line:
                line_clean=no_punct(line)
                line=process_line(line_clean)
                put_into_dictionary(d,line)
        else:
            line_clean=no_punct(lines)
            line=process_line(line_clean)
            put_into_dictionary(d,line)

    #realized that anything after 'and' would usually make a good new sentence starter
    beginners=d.get('BEGIN')
    beginners.extend(d.get('and'))
    d['BEGIN']=beginners

    return d

def no_punct(line):
    clean_str=''
    for i in range(len(line)):
        if line[i] not in LETTERSANDPUNCTUATIONS:
            clean_str += ' '
            continue
        else:
            clean_str += line[i]
    return clean_str

def put_into_dictionary(d, line):
    if line == 'empty line':
        return d
    for elem in line:
        if elem[0] in d.keys():
            oldlist=d.get(elem[0])
            if elem[1] not in oldlist:
                oldlist.append(elem[1])
                #cann take out last line if you dont want the word after, just 2 words
                oldlist.append(elem[2])
            d[elem[0]]=oldlist
        else:
            new_list=[]
            new_list.append(elem[1])
            #cann take out last line if you dont want the word after, just 2 words
            new_list.append(elem[2])
            d[elem[0]]=new_list
            #need to account for repeat words
    return d

def generate_line(d):
    """
    Generates a random sentence based on the dictionary
    with transition pairs
    """
    sentence=''
        #random.choice to pick a random element from a list
    next=random.choice(d.get('BEGIN'))
        #first is BEGIN but we don't want to use it

    while next != 'stop':
        sentence += (str(next)+' ')
        if ' ' in next:
            last_word=(next.split())[1]
        else:
            last_word=next
        next=next_word(last_word)
    return sentence

def next_word(last_word):
    if not d.get(last_word):
        return 'stop'
    word = random.choice(d.get(last_word))
    if word == 'END':
        return 'stop'
    else:
        return word

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ('ERROR: Run as python markov.py <filename>')
        exit()

    d = process_textfile(sys.argv[1])
    #it creates a dictionary from the texts that I put in the file I call as first argument

    print(d)

    #news_song=
    # #import new song class stufff - making a visual of these song lines
    newsong= []
    for i in range(NUMLINES):
        line = str(generate_line(d))
        newsong.append(no_punct(line))

    visualize_song=SongVisual(newsong)

        #put line onto canvas for the class