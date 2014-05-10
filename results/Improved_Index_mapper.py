#!/usr/bin/python
import sys
import csv
import re

from collections import defaultdict

# Purpose: End Project Building a better Inverse Index
#
# This is an attempt to improve upon the inverse indexing program.
# Since this is a simple look up for words I decided that Stop Words
# would constitute the primary improvement.
# I ran the mapper with and without stopwords and the file was 
# twice as large without them. 
# Since the query depends on a key lookup, this was an immediate improvement.
# I used reg exp to do the appropriate parsing of words from the 
# body of the text line[4] as we did for a previous exercise.
#
# The SPACE complexity of an indexer depends on the size of words and their location.
# The key is manageable even if the amount of disitinct words were 100M.
# Thus the key and the counter are small but the location or position 
# where the words occur  would constitute a larger amount of memory.
# The TIME complexity is the time to search, or parse the body for words.
# We use re.complie on a  regex for words [A-Za-z]+ . This is a little
# bit more optimised than other methods. 
# There is also the time to build the dictionary and this is the order of the number
# of keys plus the insertion. The latter being O(k). Other improvements 
# would be a lookup for repeats. 
#
# Input : Forum_node.tsv
# Output: Key = word ; Value = post id
#
# The reducer will combine the information into a dictionary of word count and document
# post ids.


def mapper():
    
    reader = csv.reader(sys.stdin, delimiter='\t')
   
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    stop_words_s= "a,b,c,d,e,f,g,h,j,k,l,m,n,o,p,q,r,s,t,u,v,w,u,x,y,z,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,em,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,s,said,say,says,she,should,since,so,some,t,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your,\\p"
    
    word = None
    stop_words_l = stop_words_s.split(",")
    cnt=0
    pat = '[^ |.|\?|\n|\t|!|:|;|\"|(|)|<|>|[|]|#|$|=|-|/|,]'
    
    # only words no digits or punct.
    get_Word_regx = r'[A-Za-z]+'
    pat_word =re.compile(get_Word_regx,re.IGNORECASE) 
    # Pattern for node (post ) id all digits
    digit_pat = re.compile(r'[\d]+')
    
    
    for line in reader:
        
        if line[0] == "id":  # ignore the first line
            continue
        
        if line[4] == "" : 
            continue
        # get all of the words in body spearated by blanks into list
        body_l = re.findall(pat_word,line[4]) 
        # normalise to lower
        body_l= [s.lower() for s in body_l]

        nodenumber_l = line[0].strip().split()
        
        node_id_l = re.findall(digit_pat, nodenumber_l[0]) # remove garbage from node id line[0].
        # make sure post id exists and is a digit
        if node_id_l[0].isdigit() :
            for word in body_l :  
                if word in stop_words_l: 
                    continue
                print "{0}\t{1}".format(word , node_id_l[0])
   
        
           
               
def main():
    import StringIO
   
    try :
        mapper()
    except:
        pass
    
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()