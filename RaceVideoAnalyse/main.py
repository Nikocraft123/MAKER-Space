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

        # Lade Qr Codes
        codes = pyzbar.decode(frame)

        # Gehe durch jeden Qr Code durch
        for code in codes:

            # Hole Position und Größe des Qr Code
            x_pos, y_pos, width, height = code.rect

            # 

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

    # Definiere Video Signale
    video_cap = cv2.VideoCapture(0)
    qrcode_img = cv2.imread(".\qrcode.png")

    # Run die Webcam
    # run()

    # TEMP

    # Load Qr Code Image
    qrcodes = pyzbar.decode(qrcode_img)
    for qrcode in qrcodes:
        x, y, width, height = qrcode.rect
        cv2.rectangle(qrcode_img, (x, y), (x + width, y + height), (0, 255, 0), 4)
        qrdata = qrcode.data.decode("utf-8")
        qrtype = qrcode.type
        cv2.putText(qrcode_img, qrdata, (x, y - 10), cv2.QT_FONT_NORMAL, 0.5, (255, 0, 0), 1)
    cv2.imshow("Qr Code", qrcode_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Create Qr Code
    i = pyqrcode.create("Car_ID_#1")
    f = open(r".\qrcode.png", "wb")
    i.png(f, 10)
    print(i.terminal())
