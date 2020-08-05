def msgchecker(msg):

    command = msg[0].lower()
    args = msg[1:]
    response = 'Invalid  command'

    if command == 'hello':
        response = 'World!'

    if command == 'repeat':
        response = ' '.join(args)

    if command == 'challenge':
        if args[0] == 'add':
            chal = ' '.join(args[1:-1])
            flag = str(args[-1])

            if flag[:7] == 'pieCTF{' and flag[-1] == '}':
                with open('chal.txt' ,'a') as chalfile:
                    chalfile.write('Challenge: ' + chal + ' ' +flag)
                response = 'Hurray\nNew challenge added.'
            else:
                response = 'Sorry, the challenge is not added.\nIt must be in the form \"!challenge   add   challenge_statement  flag\" \nand the flag must be in form pieCTF\{flag_with_no_spaces\}'


        if args[0] == 'look':
            with open('chal.txt' ,'r') as chalfile:
                response = chalfile.readline(int(args[[1]]))[1:-1]

        if args[0] == 'submit':
            with open('chal.txt' ,'r') as chalfile:
                flag = chalfile.readline(int(args[[1]]))[-1]
                if args[2] == flag:
                    response = 'Wow! You are right!'
                else:
                    response = 'Sorry! Try again!'
                


    return response