from Tkinter import *
from re import *
from math import *

###
# Variables initialization
###
calc_input = ''
_sizex = 5
_sizey = 3
_padding = 2
_green = 'green'
result = 0
operatorsList = ['+', '-', '/', '*', '**', 'sin', 'cos', 'tan']


#Test operator priority
def priorite(op1, op2):
    prio = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 2}
    if prio[op1] > prio[op2]:
        return True
    else: 
        return False


#Test is number
def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def npi(calcul):
    output = []
    operators = []
    tokens = re.findall("[+-/*()^|\d+]|(?:cos|sin|tan)", calcul)
    # [+-/*()|\d+]
    ope = 0

    # While there are tokens to be read:
    for token in tokens:
        print("token = " + token)
        if is_number(token):
            # If it's a number add it to queue
            if len(output) > 0 and is_number(output[-1]) and ope == 0:
                nb1 = str(output[-1]) + token
                print ("nb = " + nb1)
                output[-1] = int(nb1)
                ope = 0
            else:
                output.append(int(token))
                ope = 0
        elif token == '(':
            #If it's a left bracket push it onto the stack
            operators.append(token)
            ope = 1
        elif token == ')':
            ope = 1
            # If it's a right bracket
            
            # While there's not a left bracket at the top of the stack:
            while operators[-1] != '(':
                # Pop operators from the stack onto the output queue.
                output.append(operators.pop())
            # Pop the left bracket from the stack and discard it
            operators.pop()

        # If it's an operator
        elif token =='+' or token == '-' or token == '/' or token == '*' or token == '^' or token == 'sin' or token == 'cos' or token == 'tan':
        # elif token in operatorsList:
            ope = 1
            # While there's an operator on the top of the stack with greater precedence:
            # Check if first operator
            if len(operators) > 0:
                while len(operators) > 0 and priorite(token, operators[-1]) == False:
                    # Pop operators from the stack onto the output queue
                    output.append(operators.pop())
                # Push the current operator onto the stack
                operators.append(token)
            else:
               operators.append(token) 

    while len(operators) > 0:
        # While there are operators on the stack, pop them to the queue
        output.append(operators.pop())

    return output


def decodenpi(tab):
    # operatorsList = ['+', '-', '/', '**']
    i = 0
    while i < (len(tab)-2):
        if isinstance(tab[i], int) and isinstance(tab[i + 1], int) and tab[i + 2] in operatorsList:
            return [tab[i], tab[i+1], tab[i+2]]
        else:
            i+=1
    
    return False




# Rcuperation de la valeur cliquee dans l'interface
def digit(value): 
    global calc_input 
    calc_input += value 
    calc_input_text.set(calc_input)
    # print(calc_input)


def equal():
    # operatorsList = ['+', '-', '/', '*', '**', 'sin', 'cos', 'tan']
    global calc_input

    # calc_input = '1 + 1'

    calcul = npi(calc_input)
    result = 0
    # print(calcul)

    if len(calcul) > 1:
        while len(calcul) > 3:
            # print(calcul)
            # print(len(calcul))
            i = 0
            while i <= (len(calcul) - 2):
                # print(i)
                # print(calcul)
                if isinstance(calcul[i], int) and isinstance(calcul[i + 1], int) and calcul[i + 2] in operatorsList:
                    if calcul[i + 2] == '+':
                        calc = calcul[i] + calcul[i + 1]
                        calcul[i] = calc
                        del calcul[i + 1]
                        del calcul[i + 1]
                        # print(calcul)
                        break

                    elif calcul[i+2] == '-':
                        calc = calcul[i] - calcul[i + 1]
                        calcul[i] = calc
                        del calcul[i+1]
                        del calcul[i+1]
                        # print(calcul)
                        break

                    elif calcul[i+2] == '*':
                        calc = calcul[i] * calcul[i + 1]
                        calcul[i] = calc
                        del calcul[i + 1]
                        del calcul[i + 1]
                        # print(calcul)
                        break

                    elif calcul[i+2] == '^':
                        calc = calcul[i] ** calcul[i + 1]
                        calcul[i] = calc
                        del calcul[i + 1]
                        del calcul[i + 1]
                        # print(calcul)
                        break

                    elif calcul[i + 2] == '/':
                        if calcul[i + 1] == 0:
                            # print("Err divide by 0")
                            result_text.set("Err divide by 0")
                            break
                        else:
                            calc = calcul[i] / calcul[i + 1]
                            calcul[i] = calc
                            del calcul[i + 1]
                            del calcul[i + 1]
                            # print(calcul)
                            break
                else:
                    i+=1
            
        i = 0
        if len(calcul) == 2 and isinstance(calcul[i], int) and calcul[i + 1] in operatorsList:
            if calcul[i + 1] == 'sin':
                result = sin(calcul[i])

            if calcul[i + 1] == 'cos':
                result = cos(calcul[i])
            
            if calcul[i + 1] == 'tan':
                result = tan(calcul[i])

        else :
            print(calcul)
            i = 0
            if calcul[i + 2] == '+':
                # print(calcul)
                result = calcul[i] + calcul[i + 1]

            elif calcul[i+2] == '-':
                # print(calcul)
                result = calcul[i] - calcul[i + 1]

            elif calcul[i+2] == '*':
                # print(calcul)
                result = calcul[i] * calcul[i + 1]

            elif calcul[i+2] == '^':
                # print(calcul)
                result = calcul[i] ** calcul[i + 1]

            elif calcul[i+2] == '/':
                # print(calcul)
                if calcul[i + 1] == 0:
                    # print("Err divide by 0")
                    result = "Err divide by 0"
                    result_text.set(result)
                
                else:
                    result = calcul[i] / calcul[i + 1]
            

        calc_input = ""
        calc_input_text.set(calc_input)
        result_text.set(result)


def efface():
    global calc_input
    calc_input = ''
    result = ''
    calc_input_text.set(calc_input)
    result_text.set(result)


# UI Window initialization
window = Tk()
window.title("Ultimate Calculator")
window.minsize(196, 282)
window.config(background = '#24305E')

# UI Buttons definition
calc_input_text = StringVar()
entree = Label(window, textvariable=calc_input_text, width=_sizex*5, height = _sizey, bg="#24305E", fg="white", anchor='e', font=("Courier", 14)).grid(row = 1, column = 0, columnspan=5)
result_text = StringVar()
sortie = Label(window, textvariable=result_text, width=_sizex*5, height = _sizey, bg="#24305E", fg="yellow", anchor='e', font=("Courier", 14)).grid(row=2, column = 0, columnspan=5)
Button(window, text="Close", command=window.quit).grid(row=0, column=4)
Button(window, text=" 0 ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("0")).grid(row=7, column=0)
Button(window, text=" 1 ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("1")).grid(row=6, column=0)
Button(window, text=" 2 ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("2")).grid(row=6, column=1)
Button(window, text=" 3 ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("3")).grid(row=6, column=2)
Button(window, text=" 4 ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("4")).grid(row=5, column=0)
Button(window, text=" 5 ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("5")).grid(row=5, column=1)
Button(window, text=" 6 ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("6")).grid(row=5, column=2)
Button(window, text=" 7 ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("7")).grid(row=4, column=0)
Button(window, text=" 8 ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("8")).grid(row=4, column=1)
Button(window, text=" 9 ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("9")).grid(row=4, column=2)
Button(window, text=" / ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("/")).grid(row=3, column=4)
Button(window, text=" x ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("*")).grid(row=4, column=4)
Button(window, text=" - ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("-")).grid(row=5, column=4)
Button(window, text=" + ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("+")).grid(row=6, column=4)
Button(window, text=" ( ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("(")).grid(row=7, column=1)
Button(window, text=" ) ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit(")")).grid(row=7, column=2)
Button(window, text=" C ", height = _sizey, width = _sizex, pady = _padding, command=lambda:efface()).grid(row=3, column=0)
Button(window, text=" = ", height = _sizey, width = _sizex, pady = _padding, bg = _green, command=lambda:equal()).grid(row=7, column=4)

Button(window, text=" ^ ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("^")).grid(row=7, column=3)

Button(window, text=" sin ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("sin")).grid(row=4, column=3)
Button(window, text=" cos ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("cos")).grid(row=5, column=3)
Button(window, text=" tan ", height = _sizey, width = _sizex, pady = _padding, command=lambda:digit("tan")).grid(row=6, column=3)


window.mainloop()
