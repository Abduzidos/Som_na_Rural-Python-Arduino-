import serial
import time
import cv2
import facebook
from PIL import Image

graph = facebook.GraphAPI(access_token="EAADXkI2RPRABABOFQ4Lm0b595kvZADjw9hhGL7cCWo08uaIDVXGPaH222xPVnF2amBxANpf98JN0f0IylhAblmjIjLalZBvNZBrClVoYOqTRFxZCeXSli9mWVNkc8yVc1ci7iIhw2qzdaD1QuUVJoZCXISTXVfYUCU7h2GHjs2JBYd87HWU8CYZCK7fSAAdB1ZBJ6KnuxYkVM5GWWeXQVVO", version="2.7")

ArduinoUnoSerial = serial.Serial('/dev/ttyACM1', 9600)

cap = cv2.VideoCapture(0)

counter = 0

def show_webcam(mirror=False): 
    cv2.namedWindow('Som na Rural',cv2.WINDOW_AUTOSIZE)
    while True:
        ret_val, frame = cap.read()                 
        if mirror:
            frame = cv2.flip(frame, 1)
            cv2.imshow('Som na Rural', frame)                               
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
 
def imgedit(foto): 
       
    background = Image.open(foto)
    foreground = Image.open("fg.png")
    background.paste(foreground, (0, 0), foreground)
    background.save('editado'+str(counter)+'.jpg')
    graph.put_photo(image=open('editado'+str(counter)+'.jpg', 'rb'),
                                       message='Look at this cool photo!')


def tirarfoto():
    global counter
    global cap
    ret, frame = cap.read()

    print("Counter {}".format(counter))
    counter += 1
        
    out = cv2.imwrite('capture'+ str(counter) +'.jpg', frame)
    print ("SORRIA PRO LED")
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('0')
    print("Imagem salva")
    print('//--'*10)


# tirarfoto()
# imgedit('capture'+ str(counter) +'.jpg')
show_webcam(mirror=True)
# while True:
    # if ArduinoUnoSerial.read(1) == b'1':
        # tirarfoto()
        # imgedit()
