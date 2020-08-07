import joke_api.py

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
                    chalfile.write('Challenge: ' + chal + ' ' + flag + '\n')
                response = 'Hurray\nNew challenge added.'
            else:
                response = 'Sorry, the challenge is not added.\nIt must be in the form \"!challenge   add   challenge_statement  flag\" \nand the flag must be in form pieCTF\{flag_with_no_spaces\}'


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
                
    if command == 'joke':
        joke = joke_api.get_joke()
        print(joke)

        if joke == False:
            await message.channel.send("Uh-oh...I couldn't get a joke. Try again later. ;)")
        else:
            await message.channel.send(joke['setup'] + '\n' + joke['punchline'])
    
    return response
