# IMPORTS
import cv2
import pyqrcode
from pyzbar import pyzbar


# CLASSES


# METHODS

# Run
def run():

    # Unendliche Schleife
    while True:

        # Hole aktuellen Frame
        _, frame = video_cap.read()

        codes = pyzbar.decode(frame)


        # Zeige Video in einem Fenster
        cv2.imshow("MAKER Space - Race Video Analyse", frame)

        # Schaue ob eine die Taste 'q' gedrückt worden ist
        if cv2.waitKey(1) & 0xff == ord("q"):

            # Breche ab
            break

    # Löse das Kamerasignal
    video_cap.release()

    # Zerstöre alle Fenster
    cv2.destroyAllWindows()


# MAIN
if __name__ == "__main__":

    # DEFINE VARIABLES
    video_cap = cv2.VideoCapture(0)
    qrcode_img = cv2.imread(".\qrcode.png")

    # run()
    i = pyqrcode.create("Car_ID_#1")
    f = open(r".\qrcode.png", "wb")
    i.png(f)
    print(i.terminal())
