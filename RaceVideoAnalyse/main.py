# IMPORTS
import cv2
from pyzbar import pyzbar


# CLASSES


# METHODS

# Run
def run():

    # Unendliche Schleife
    while True:

        # Hole aktuellen Frame
        _, frame = video_cap.read()

        # Lade Qr Codes
        codes = pyzbar.decode(frame)

        # Gehe durch jeden Qr Code durch
        for code in codes:

            # Hole Position und Größe des Qr Code
            x_pos, y_pos, width, height = code.rect

            # Zeichne Rahmen um Qr Code
            cv2.rectangle(frame, (x_pos, y_pos), (x_pos + width, y_pos + height), (0, 0, 255), 2)

            # Decode Qr Code Data
            qr_data = code.data.decode("utf-8")

            # Write the Data above the Qr Code
            cv2.putText(frame, qr_data, (x_pos, y_pos - 8), cv2.QT_FONT_NORMAL, 0.4, (0, 255, 0), 1)

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

    # Definiere Video Signal
    video_cap = cv2.VideoCapture(0)

    # Run die Webcam
    run()
