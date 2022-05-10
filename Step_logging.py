from datetime import datetime

master_instruction_list = []
list_letters = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)', '(j)', '(k)', '(l)', '(m)', '(n)', '(o)', '(p)', '(q)', '(r)', '(s)', '(t)'] 
roman_numerals = ['(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)', '(vii)', '(viii)', '(ix)', '(x)', '(xi)', '(xii)', '(xiii)', '(xiv)', '(xv)', '(xvi)', '(xvii)', '(xviii)', '(xix)', '(xx)']
blnDebugging = True

def fCreate_Instruction():
    bln_code_still_running = True
    int_CurrentInstruction = -1

    while bln_code_still_running == True:
        new_instruction_list = []

        # prepare display message
        int_CurrentInstruction += 1
        print(list_letters[int_CurrentInstruction])

        # run the step input function and add the result to the master list
        new_instruction_list = fInput_Steps(int_CurrentInstruction)
        master_instruction_list.append(list(new_instruction_list))

        # ask user to complete job, otherwise repeat loop
        input_string = fRestrict_User_Input(["Y","N"],"Complete Job? Y/N")
        if input_string == "Y":
            bln_code_still_running = False
        if input_string == "N":
            bln_code_still_running = True
            new_instruction_list.clear()


def fInput_Steps(letter_list_position):
    item_list = []
    bln_repeat_loop = True
    int_CurrentStep = -1

    # depending on what step, generate the letter relevant to that step and add it to the list (should be first item)
    current_letter = list_letters[letter_list_position]
    item_list.append(current_letter)

    while bln_repeat_loop == True:

        # prepare user input message string
        int_CurrentStep += 1
        step_roman_numerals = roman_numerals[int_CurrentStep]
        input_message = "Input User Step {0}: ".format(step_roman_numerals)

        # take user input
        user_input = input(input_message)

        # exit loop if user uses "<"
        if user_input == "<":
            bln_repeat_loop = True
            return item_list
        else:
            string = step_roman_numerals + "," + user_input
            item_list.append(string)


def fPrepare_Export():

    # adjust filename if debugging
    if blnDebugging == True:
        str_filename = "(DEBUGGING) Python Output " + fPrepareDateTime() + ".csv"
    elif blnDebugging == False:
        str_filename = "Python Output " + fPrepareDateTime() + ".csv"

    enumerate(master_instruction_list,0)

    with open(str_filename,"w") as output_file:

        for each_list in master_instruction_list:

            output_file.writelines("\n".join(each_list))
            output_file.write("\n\n")


def fPrepareDateTime():
    # current time using datetime object
    now = datetime.now()

    date_string = now.strftime("%Y-%m-%d")
    time_string = now.strftime("%H_%M_%S")

    date_string = "d" + date_string
    time_string = "t" + time_string
    dt_string = date_string + " " + time_string
    return dt_string


def fRestrict_User_Input(user_can_only_type, input_message):
    list_upper_case = [each_string.upper() for each_string in user_can_only_type]
    while True:
        try:
            user_input = input(input_message + ": ")
            if str(user_input).upper() in list_upper_case:
                return user_input
            raise ValueError()
        except ValueError:
            print("    Error: You are required to enter one of the following: {}".format(user_can_only_type))
            print("    Please try again\n")


#Start Code, Check if user is debugging
user_input = fRestrict_User_Input(["Y","N"],"Are you Debugging? Y/N")
if user_input == "Y":
    blnDebugging = True
elif user_input == "N":
    blnDebugging = False

#User to create the instructions. Will loop until exited
fCreate_Instruction()

#Combine instructions into a filename (filename will be todays date/time)
fPrepare_Export()




















