def test_config():
    return True

def string_access_a_character():
    lang = "C++"

    print(lang)

    print(lang[0]) 
    print(lang[1])
    print(lang[2])

    lang[0] = 'c' #cannot modify individual characters in string

def loop_a_string_w_while():
    lang = "Python" #Python is 6 characters long, that's the size of lang
    INDX = 0 #where you want it to start within "Python"

    while(INDX < len(lang)): #len gives us the size of lang, size starts with 1
        print(lang[INDX])
        INDX += 1 #index + 1, this will eventually make indx < len(lang) false

    #print(lang[5]) will print out an extra n

def loop_a_string_w_for_range():
    lang = "Python"

    for i in range(0, len(lang)):
        print(lang[i])

def loop_a_string_with_for():
    lang = "Python"

    for ch in lang: #ch = character
        print(ch)

def validate_password(password):
    is_valid = False
    correct_length = False
    has_upper_case = False
    has_lower_case = False
    has_digit = False

    if(len(password)) >= 7:
        correct_length = True
    
        for ch in password:
            if ch.isupper():
                has_upper_case = True
            if ch.islower():
                has_lower_case = True
            if ch.isdigit():
                has_digit = True
            
        if correct_length and has_upper_case and \
            has_lower_case and has_digit:
            is_valid = True 
        else:
            is_valid = False

    return is_valid
    
