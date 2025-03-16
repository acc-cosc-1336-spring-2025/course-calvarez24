def test_config():
    return True

def print_hello():
    num = 5 #we're displaying hello 5 times w a loop
    indx = 0

    while (indx < num): #while loop statement + boolean expression
        print(indx, (indx < num), 'hello')
        indx = indx + 1 #statement that makes indx < num FALSE

#3 = 1*1 +2*2+3*3 = 14 ===== num = 3  total = total + num * num 
def sum_of_squares(num):
    total = 0
    
    while num > 0: #the loop
        total = total + num * num
        print(num, num > 0, total)
        num = num - 1 #statement that makes the boolean expression false and stops the loop
   
    return total
    
def sum_of_squares_indx(num): #this means it will start at 0 instead of the numbers we gave it
    indx = 0
    total = 0 

    while indx <= num:
        total = total + indx * indx
        indx = indx + 1
        
    return total
