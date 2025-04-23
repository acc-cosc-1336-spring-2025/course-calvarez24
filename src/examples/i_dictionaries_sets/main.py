#main program
import dictionaries

def main():
    baseball = {'Jodi', 'Carmen', 'Aida', 'Alicia'}
    basketball = {'Eva', 'Carmen', 'Alicia', 'Sarah'} 

    print('The following play baseball but not basketball: ')
    baseball_only = baseball.difference(basketball)
    for player in baseball_only:
        print(player)  
    
    print('The following only play one sport:')
    only_one_sport_set = baseball.symmetric_difference(basketball)
    for player in only_one_sport_set:
        print(player)

    print('The following play basketball but not baseball:')
    basketball_only = basketball.difference(baseball)
    for player in basketball_only:
        print(player)
main()
