import array;
import random;
import sys

def check_winner(current_table):
    i = 0;
    x_winner = [];
    o_winner = [];
    while(i < len(current_table)):
        if(current_table[i] == 'x'):
            x_winner.append((i + 1));
        if(current_table[i] == 'o'):
            o_winner.append((i + 1));
        i+=1;
    if(len(x_winner) >= 3):
        if((4 in x_winner and 5 in x_winner and 6 in x_winner) or (7 in x_winner and 8 in x_winner and 9 in x_winner) or (1 in x_winner and ((2 in x_winner and 3 in x_winner) or (4 in x_winner and 7 in x_winner) or (5 in check and 9 in x_winner))) or (3 in x_winner and ((5 in x_winner and 7 in x_winner) or (6 in x_winner and 9 in x_winner)))):
            return 'x';
    if(len(o_winner) >= 3):
        if((4 in o_winner and 5 in o_winner and 6 in o_winner) or (7 in o_winner and 8 in o_winner and 9 in o_winner) or (1 in o_winner and ((2 in o_winner and 3 in o_winner) or (4 in o_winner and 7 in o_winner) or (5 in o_winner and 9 in o_winner))) or (3 in o_winner and ((5 in o_winner and 7 in o_winner) or (6 in o_winner and 9 in o_winner)))):
            return 'y';
    if((len(x_winner) + len(o_winner)) == 9):
        print('Draw! you both suck!');
        quit();
    return 'none';
def main():
    positions= [' ',' ',' ',' ',' ',' ',' ',' ',' '];

    print(positions[0],"|",positions[1],"|",positions[2]);
    print(positions[3],"|",positions[4],"|",positions[5]);
    print(positions[6],"|",positions[7],"|",positions[8]);

    while True:
        x_or_o = input("Would you like to be x or o? ");
        print(x_or_o);
        if(x_or_o != "x" and x_or_o != "o"):
            print("Please input x or o?");
            continue
        else:
            break
    if(x_or_o == 'o'):
        first = True;
        print('You go First!');
    if(x_or_o == 'x'):
        first = False;
        print('The Computer is First :(');
    while True:
        try:
            if(first == True):
                while True:
                    get_input = int(input("Pick a position between 1-9? (0 to quit) "));
                    if(get_input == 0):
                        quit();
                    if(get_input >= 1 and get_input <= 9):
                        if(positions[(get_input - 1)] != 'x' and positions[(get_input - 1)] != 'o'):
                            positions[(get_input - 1)] = x_or_o;
                            break
                    print('Position Taken')
            first = True;
            while True:
                ai = random.randint(1,9);
                if(positions[(ai - 1)] != 'x' and positions[(ai - 1)] != 'o'):
                    if(x_or_o == 'x'):
                        positions[(ai - 1)] = 'o';
                        break
                    else:
                        positions[(ai - 1)] = 'x';
                        break
            print(positions[0],"|",positions[1],"|",positions[2]);
            print(positions[3],"|",positions[4],"|",positions[5]);
            print(positions[6],"|",positions[7],"|",positions[8]);
            if(check_winner(positions) == 'x' or check_winner(positions) == 'y'):
                
                if(check_winner(positions) == x_or_o):
                    print('winner winner chicken dinner');
                    break
                print('looser looser salad lunch');
                break


        except:
            print('please enter the coresponding number');

        print(positions[0],"|",positions[1],"|",positions[2]);
        print(positions[3],"|",positions[4],"|",positions[5]);
        print(positions[6],"|",positions[7],"|",positions[8]);
main();