# IMPORTS
from pyzbar import pyzbar as zbar
import cv2 as cv
import numpy as np

from main import Application
import color


# METHODS

# Lade Qr Codes
def load_qr_codes(app: Application) -> None:

    # Endcode Frame
    app.qr_codes = zbar.decode(app.frame, [zbar.ZBarSymbol.QRCODE])

    # Gehe durch jeden Qr Code durch
    for code in app.qr_codes:

        # Hole Position und Größe des Qr Codes
        x_pos, y_pos, width, height = code.rect

        # Zeichne roten Rahmen um Qr Code
        cv.rectangle(app.frame, (x_pos, y_pos), (x_pos + width, y_pos + height), color.rgb_to_bgr(color.DARK_RED), 2)

        # Endcode den Inhalt des Qr Codes
        data = code.data.decode("utf-8")

        # Schreibe den Inhalt in grün über den Qr Code
        cv.putText(app.frame, data, (x_pos, y_pos - 5), cv.QT_FONT_NORMAL, 0.4, color.rgb_to_bgr(color.DARK_LIME), 1)


# Skaliere Bild
def resize_img(frame: np.ndarray, scale: float) -> np.ndarray:

    # Definiere die neue Größe des Bildes
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    # Berechne das neue Bild und gebe es zurück
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)
