import random
import os

numbers = [1,2,3,4,5,6,7,8,9]
ISUSER1 = True
INPUT_COUNT = 0
HAS_WON = ''
random.shuffle(numbers)
matrix = []
count = 0
user_input = [['','',''],['','',''],['','','']]
display_matrix = [['|',' ','|',' ','|',' ','|'],['|',' ','|',' ','|',' ','|'],['|',' ','|',' ','|',' ','|']]
entered_inputs = []

for i in range(0,len(numbers),3):
    matrix.append(numbers[i:i+3])
#print(matrix)
def get_matrix_index(usr_inp):
    entered_inputs.append(usr_inp)
    for i in range(3):
        if usr_inp in matrix[i]:
           inx =  matrix[i].index(usr_inp)
           if inx >= 0:
               return (i,inx)
           
def update_tt_matrix(data):
    user_input[data[0]][data[1]] ='X' if isUser1 else 'O'

def check_for_sequence():
    global hasWon
    for i in range(3):
        if user_input[i].count('X') == 3 or user_input[i].count('0'):
            #print('Has won 1')
            hasWon = user_input[i][0]
            return True
    for i in range(3):
        if (user_input[0][i] == user_input[1][i] == user_input[2][i]) and user_input[0][i] != '':
            #print('Has won 2')
            hasWon = user_input[0][i]
            return True
    if (user_input[0][0] == user_input[1][1] == user_input[2][2]) and user_input[0][i] != '':
        #print('Has won 3')
        hasWon = user_input[0][0]
        return True
    return False

def update_display_matrix(data):
    pos = 1
    if data[1] != 0:
        pos = data[1]*2 + 1
    display_matrix[data[0]][pos] = 'X' if  isUser1 else 'O'


while input_count < 9 :
    #s = ','.join(entered_inputs)
    usr_inp = input(f'Enter a number except {entered_inputs} ')
    if usr_inp.isdigit() and int(usr_inp) not in entered_inputs:
        input_count = input_count + 1
        d = get_matrix_index(int(usr_inp))
        update_tt_matrix(d)
        update_display_matrix(d)
        isUser1 = not isUser1
        os.system('cls')
        for i in range(3):
            print(*['              '],*display_matrix[i])
        if input_count > 4:
            if check_for_sequence():
                message = 'Nithya' if hasWon == 'X' else 'Abhishek' 
                print(f'Congragulations!!! {message}')
                break
if(hasWon == ''):            
    print ('Game over.Better luck next time')

 # def add_car_to_cart(self,car_id:int):
    #     data.cartData.append({'id':car_id, 'cust_id': sd.logged_in_cust_id})
    #     print('Successfully Added To Cart!!!')
    #     selection = input("Enter 'V' to add to cart or 'B' to go back to list: ")
    #     while selection.upper() != 'B' and selection.upper() != 'V':
    #         print('Invalid Input')
    #         selection = input("Enter 'V' to add to cart or 'B' to go back to list: ")
    #     if selection.upper() == 'V':
    #         self.__view_cart()
    #     else:
    #         self.list_all_availabe_cars()
