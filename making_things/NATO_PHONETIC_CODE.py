""" GOOGLE = nato phonetic alphabet table python
  refer to : http://www.101computing.net/nato-phonetic-alphabet/
  Did You Know?

  The NATO Phonetic Alphabet is the most widely used spelling alphabet.
  A spelling alphabet (aka radio alphabet, or telephone alphabet) is a set of
  words used to stand for the letters of an alphabet in oral communication.

  Each word in the spelling alphabet typically replaces the name of the letter
  with which it starts. It is used to spell out words when speaking to someone
  not able to see the speaker, or when the audio channel is not clear.
 """

NATO_PHONETIC_ALPH = """
    A	Alfa
    B	Bravo
    C	Charlie
    D	Delta
    E	Echo
    F	Foxtrot
    G	Golf
    H	Hotel
    I	India
    J	Juliett
    K	Kilo
    L	Lima
    M	Mike
    N	November
    O	Oscar
    P	Papa
    Q	Quebec
    R	Romeo
    S	Sierra
    T	Tango
    U	Uniform
    V	Victor
    W	Whiskey
    X	X-ray
    Y	Yankee
    Z	Zulu
    -	Dash
    """
TITLE ="""
\t __________________________________________
\t   *** NATO PHONETIC ALPHABET ENCODING ***
\t ------------------------------------------
\t    - 2017.10.8 -  made by : %s
\t __________________________________________\n\n\n"""

def show_title():
    print(TITLE % '!Kay SuparX!')

def get_code_from_NPA(str_code):    # input 'str' -> output 'dict'
    arr_line = str_code.strip().split("\n")
    dict_code = {}

    for arr_word in arr_line:      #27
        b = arr_word.strip().split()
        dict_code[b[0]] = b[1]

    return dict_code                # <class 'dict'>

def input_phrase():                 # return CHKD_word...
    print("__"*30)
    str_word = input('TYPE YOUR WORD: ')
    print(".."*30)

    arr_word = str_word.strip().split()
    chkd_word = ""

    for word in arr_word:
        if word.isalpha() == True:
            chkd_word = chkd_word + word.upper() + " "
        else:
            if word.count('-'):
                chkd_word = chkd_word + word.upper() + " "
            else:
                print("\n\n\n.. WRONG LETTERS ... TRY AGAIN~!!!! \n SYSTEM TERMINATED~!! ")
                chkd_word = ""
                break
    return chkd_word                            # <class 'str'>

def get_NPA_encode(normal_word, dict_code):     # input = srt, dict
    NPA_encode_word = ""
    # print("normal_word =", normal_word)
    for letter in normal_word:
        if letter != " ":
            NPA_encode_word = NPA_encode_word + "%s = %s" %(letter, dict_code[letter]) + "\n"
        else:
            NPA_encode_word = NPA_encode_word + "\n"
    return NPA_encode_word                              # <class 'str'>

def main():
    dict_code = get_code_from_NPA(NATO_PHONETIC_ALPH)   # <class 'dict'>
    chkd_word = input_phrase()                          # <class 'str'>

    # print(type(chkd_word))
    print('ORIGINAL WORD = ',chkd_word)   # <class 'str'>
    print()

    NPA_encode_word = get_NPA_encode(chkd_word, dict_code)
    print(NPA_encode_word)



show_title()

while True:
    main()
