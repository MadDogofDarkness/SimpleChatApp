import requests
import sys

#print(len(sys.argv))

def help():
    s = """
    syntax:
    python simpleclient.py signin username ------ sets your username
    python simpleclient.py get ---- returns posts from server
    python simpleclient.py post message to send... ------ sends message to server
    """
    return s

def main():
    username = ""
    try:
        f = open('user.pog', 'r')
        username = f.readline()
        f.close()
        print(username, " signed in.")
    except FileNotFoundError:
        pass
    message = ""
    if len(sys.argv) >= 3:
        cmd = sys.argv[1].lower()
        message = ""
        if cmd == 'post':
            for i in range(2, len(sys.argv)):
                message += sys.argv[i] + ' '
            #print('yes', cmd, message)
            r = requests.post('http://<insert ip and port of server here>', data={'username':username,'message':message})
            print('sent!')
        elif cmd == 'signin':
            newusername = sys.argv[2]
            try:
                f = open('user.pog', 'w')
                f.write(username)
                f.close()    
            except FileExistsError:
                inds = input("do you want to change your username? y/n ").lower()
                if inds == 'y':
                    f = open('user.pog', 'w')
                    f.write(newusername)
                    f.close()
                    print('username updated to ', newusername)
                else:
                    print("username not changed")        
        else:
            print('incorrect syntax')
            print(help())
    elif len(sys.argv) == 2:
        cmd = sys.argv[1].lower()
        if cmd == 'get':
            r = requests.get('http://<insert ip and port of server here>')
            print(r.text)
        #print('response')
        else:
            print('incorrect syntax')
            print(help())
    else:
        print(help())

if __name__ == '__main__':
    main()
    exit()
#r = requests.post('<insert ip here>', data={'message':'onodera is best girl'})

#print(r.text)