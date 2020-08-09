def msgchecker(msg):

    args = ['12','24']
    command = msg[0].lower()

    if len(msg) >= 1:
        args = msg[1:]

    response = 'Invalid  command'
        

    if command == 'hello':
        response = 'hello babu!'

    if command == 'repeat':
        response = ' '.join(args)

    if command == 'challenge':
        if args[0] == 'push':
            chal = ' '.join(args[1:-1])
            flag = str(args[-1])

            if flag[:7] == 'pieCTF{' and flag[-1] == '}':
                with open('chal.txt' ,'a') as chalfile:
                    chalfile.write('Challenge: ' + chal + ' ' + flag + '\n')
                response = 'Hurray\nNew challenge added.'
            else:
                response = 'Sorry, the challenge is not added.\nIt must be in the form \"!challenge   push   challenge_statement  flag\" \nand the flag must be in form pieCTF\{flag_with_no_spaces\}'


        if args[0] == 'all':
            with open('chal.txt' ,'r') as chalfile:
                challine = chalfile.readlines()
            
            response = ''
            num = 0
            # print(challine)
            for line in challine:
                # print(line)
                line = line.split()
                text = ' '.join(line[1:-1])
                num += 1
                # print(text)
                response += f'Challenge #{num}: {text}\n'


        if args[0] == 'look':
            line = int(args[1])-1
            with open('chal.txt' ,'r') as chalfile:
                challine = chalfile.readlines()[line].split()
                chaltext = ' '.join(challine[1:-1])
            response = f'Challenge #{line+1}: {chaltext}'

        if args[0] == 'submit':
            line = int(args[1])-1
            with open('chal.txt' ,'r') as chalfile:
                challine = chalfile.readlines()[line].split()
                flag = challine[-1]
                if args[2] == flag:
                    response = 'Wow! You are right!'
                else:
                    response = 'Sorry! Try again!'
            
    if command == 'help':
        print(args)
        if args[0] == 'hello':
            response = "> Hi! Yesko baarema tah vannu naparla ni"
            
        elif args[0] == 'repeat':
            response = "> I will repeat what you say"

        elif args[0] == 'challenge':
            response =  '> Add new challenge:    baje  challenge   push    challenge_statment   flag(in form pieCTF\{\})\n'
            response += '> Look at a challenge:  baje  challenge   look    challenge_no\n'
            response += '> Submit a flag:        baje  challenge   submit  challenge_no  flag'

        else:
            response =   '> To know abbout different commands, enter baje  help  command_name  \n'
            response +=  '> The commands available are:\n'
            response +=  '> hello\n' 
            response +=  '> repeat\n' 
            response +=  '> submit\n'                                                                                                                                                          

    return response