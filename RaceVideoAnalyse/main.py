# IMPORTS
import cv2
import pyqrcode


# CLASSES


# METHODS

# Run
def run():

    # Unendliche Schleife
    while True:

        # Hole aktuellen Frame
        _, frame = video_cap.read()

        # Zeige Video in einem Fenster
        cv2.imshow("Test", frame)

        # Schaue ob eine die Taste 'q' gedrückt worden ist
        if cv2.waitKey(1) & 0xff == ord("q"):

            # Breche ab
            break


# MAIN
if __name__ == "__main__":
    
    video_cap = cv2.VideoCapture(0)
    #run()

    i = pyqrcode.create("test")
    print(i.terminal())
