# --------------------------------------
# CSCI 127, Lab 8                      |
# Today's Date                         |
# Your Name                            |
# --------------------------------------

#The comma Character has to be treated different as it seperates the words in a .csv file"

def create_dictionary(file_name): 
    filehandle = open(file_name, 'r')
    dictionary = {}
    
    for i in filehandle:
        files = i.split(',')
        binary = i[:8]
        if i[9:14] == "space":
            character = " "
        elif i[9:14] == "quote":
            character = '"'
        elif i[9:14] == "comma":
            character = ","
        else:
            character = i[9]
        dictionary[character] = binary

    filehandle.close()
    return dictionary

def translate(s, d, f): # rename the parameters as you wish
    new_file = open(f, 'w')
    for i in s:
        if i not in d:
            new_file.write("\nUNDEFINED\n")
        else:
            new_file.write(d[i])
        
        

def decode(s, d): # rename the parameters as you wish
    for i in s:
        if s.index(i) % 8 == 0:
            print(s.substring(i,i+8))

# --------------------------------------
def main():
    dictionary = create_dictionary("ascii-codes.csv")
    sentence = "A long time ago in a galaxy far, far away..."
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Montana State University (406) 994-0211"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "“True friends stab you in the front.” —Wilde"
    translate(sentence, dictionary, "output-3.txt")
    
    # Honors Section challange:
    decode('010001110110111101101111011001000010000001101010011011110110001000100001', dictionary)

# --------------------------------------

main()
