from PyDictionary import PyDictionary
dictionary=PyDictionary()



def output():
    print (dictionary.meaning(input("input word: ")))
    repeat()

def repeat():
    output()
    
repeat()


