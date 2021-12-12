

match_table=[' * ',' * ',' * ',' * ',' * ',' * ',' * ',' * ',' * ' ]
player_one=list()
player_two=list()
is_player_one_turn=True
counter=0

#Displaying Match Table in 3x3 format
def display_table(table):
    display=''
    counter=1
    for i in range(0,len(table)):
        if counter%3==0:
            display+=str(table[i])+"\n"
        else:
            display+=str(table[i])
        counter+=1
    print(display)
     
#Takes input from player
def AppendIndex():
    chosen_index=''
    global is_player_one_turn 
    while chosen_index.isdigit()== False or chosen_index != ' * ':
        if is_player_one_turn:
            chosen_index= input('Player 1 please enter Number: ')
        else:
            chosen_index= input('Player 2 please enter Number: ')


        if chosen_index.isdigit() == False:
            print('please enter valid number in range(1,9): ')
        else:
            ichosen_index=int(chosen_index)
            if ichosen_index in range(1,10):
                if match_table[ichosen_index-1]==' * ':   
                    if is_player_one_turn:
                        player_one.append(ichosen_index)
                        is_player_one_turn=False
                    else:
                        player_two.append(ichosen_index) 
                        is_player_one_turn=True
                    return(ichosen_index)
                else:
                    print('selected index is not available!!')
            else:
                print('Please select the correct number!!')

#Replacing with x or o                  
def ReplaceMatchTable(index):
    if is_player_one_turn==False:
         match_table[index-1]=' x '
    else:
        match_table[index-1]=' o '
 
    return match_table

#Check the given array is in winner array list
def check_winner(player_arr):
     win_arr= ([1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7])
     
     for i in win_arr:
        if set(i).issubset(set(player_arr)):
            
            return True
#To restart the game
def restart():
    restart=input('do you want to restart(yes/no): ')
    global match_table,player_one,player_two,is_player_one_turn,counter
    if restart== 'yes':
        match_table=[' * ',' * ',' * ',' * ',' * ',' * ',' * ',' * ',' * ' ]
        player_one=list()
        player_two=list()
        is_player_one_turn=True
        counter=0
    else:
        return False


while (True):
    temp_arr = ReplaceMatchTable(AppendIndex())
    display_table(temp_arr)
    counter+=1
         
    if is_player_one_turn== False:
        if check_winner(player_one):
            print("Player One!!! WINNER WINNER!!! CHICKEN DINNER!!!") 
            if(restart()==False):
                break
    else:
        if check_winner(player_two):
            print("Player Two!!! WINNER WINNER!!! CHICKEN DINNER!!!")
            if(restart()==False):
             break
   
    if counter==9:
        print('Match Draw')
        if(restart()==False):
            break






    







