import cv2
import os, sys
import time, datetime
import serial

WEBCAM_DEVICE = 0
STORAGE_DIR = 'storage'

ArduinoUnoSerial = serial.Serial('/dev/ttyACM1', 9600)

def putText(img, text, location, positive=True):

    font = cv2.FONT_HERSHEY_DUPLEX
    fsize = 2
    colour = (0, 255, 0) if positive else (255, 0, 0)
    if location == 'left_button':
        cv2.putText(img, text, (0, img.shape[0] - 10),
                    font, fsize, colour)
    elif location == 'right_button':
        cv2.putText(
            img, text,
            (int(img.shape[1] - 40*len(text)), int(img.shape[0] - 10)),
            font, fsize, colour)
    elif location == 'centre':
        cv2.putText(
            img, text,
            (int(img.shape[1] / 2 - 20*len(text)), int(img.shape[0] / 2)),
            font, fsize, colour)


if __name__ == '__main__':
    # open webcam and UI
    cap = cv2.VideoCapture(WEBCAM_DEVICE)
    screen = 'Som na Rural'
    cv2.namedWindow(screen, cv2.WND_PROP_FULLSCREEN)

    # show webcam and wait for user input
    while True:
        ret, frame = cap.read()
        img = frame
        img_ui = img.copy()
        putText(img_ui, "TIRAR", 'left_button', True)
        cv2.imshow(screen, img_ui)
        keypress = cv2.waitKey(10)

        if ArduinoUnoSerial.read(1) == b'1': # serial read 1: take photo
            # take snapshot, wait for user input
            img_ui = img.copy()
            putText(img_ui, "SALVAR", 'left_button', True)
            putText(img_ui, "REPETIR", 'right_button', False)
            cv2.imshow(screen, img_ui)
            keypress = cv2.waitKey(0)

            if ArduinoUnoSerial.read(1) == b'1': # serial read 1: print

                datestr = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = os.path.join(os.getcwd(), STORAGE_DIR, datestr + ".jpg")
                cv2.imwrite(filename, img)

                for i in range(10, 0, -1):
                    time.sleep(1)
                    img_ui = img.copy()
                    putText(img_ui, "SALVANDO({})".format(i), 'centre', True)
                    cv2.imshow(screen, img_ui)
                    cv2.waitKey(1)
            else:
                continue # retake

        if ArduinoUnoSerial.read(1) == b'2': # serial read 2: exit
            break
