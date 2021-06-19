# IMPORTS
from pyzbar import pyzbar
import cv2 as cv
import pygame as pg
import color


# CLASSES

# Application
class Application:

    # CONSTRUCTOR
    def __init__(self):

        # Definiere App Titel
        self.title = "MAKER Space - Race Video Analyse"

        # Definiere App Größe
        self.width = 900
        self.height = 700

        # Definiere Kamerasignal
        self.video_cap = cv.VideoCapture(0, cv.CAP_DSHOW)

        # Initialisiere Pygame
        pg.init()

        # Definiere Running
        self.running = True


    # METHODS

    # Run
    def run(self):

        # Definiere Fenster
        self.screen = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
        pg.display.set_caption(self.title)

        # App Routine
        while self.running:

            # Aktualisiere Frame
            self.update_frame()

            # Aktualisiere Fenster Größe
            self.update_window_size()

            # Aktualisiere Fenster Inhalt
            self.update_screen()

            # Behandle Events
            self.handel_events()

        # Löse das Kamerasignal
        self.video_cap.release()

        # Beende Pygame
        pg.quit()

    # Aktualisiere Fenster Inhalt
    def update_screen(self):

        # Setze den Hintergrund auf Türkis
        self.screen.fill(color.AQUA)

        # Zeichne Frame auf dem Fenster (In der Mitte)
        self.screen.blit(self.pg_frame, ((self.screen.get_width() - self.pg_frame.get_width()) // 2, (self.screen.get_height() - self.pg_frame.get_height()) // 2))

        # Aktualisiere Fenster
        pg.display.flip()

    # Behandle Events
    def handel_events(self):

        # Gehe durch alle Events durch
        for event in pg.event.get():

            # Wenn das Fenster schließen Event gefunden wurde
            if event.type == pg.QUIT:

                # Setze Running auf Falsch
                self.running = False

    # Aktualisiere Frame
    def update_frame(self):

        # Hole aktuellen Frame
        _, self.frame = self.video_cap.read()

        # Lade Qr Codes
        self.load_qr_codes()

        # Konvertiere OpenCV Bild zu Pygame Bild
        self.pg_frame = pg.image.frombuffer(self.frame.tobytes(), self.frame.shape[1::-1], "BGR")

    # Lade Qr Codes
    def load_qr_codes(self):

        # Endcode Frame
        self.qr_codes = pyzbar.decode(self.frame, [pyzbar.ZBarSymbol.QRCODE])

        # Gehe durch jeden Qr Code durch
        for code in self.qr_codes:

            # Hole Position und Größe des Qr Codes
            x_pos, y_pos, width, height = code.rect

            # Zeichne roten Rahmen um Qr Code
            cv.rectangle(self.frame, (x_pos, y_pos), (x_pos + width, y_pos + height), (0, 0, 255), 2)

            # Endcode den Inhalt des Qr Codes
            data = code.data.decode("utf-8")

            # Schreibe den Inhalt in grün über den Qr Code
            cv.putText(self.frame, data, (x_pos, y_pos - 5), cv.QT_FONT_NORMAL, 0.4, (0, 255, 0), 1)

    # Aktualisiere Fenster Größe
    def update_window_size(self):

        # Hole Größe
        self.width, self.height = pg.display.get_window_size()

        # Kontrolliere, ob die Größe zu klein ist
        if self.width < self.pg_frame.get_width():
            self.width = self.pg_frame.get_width()
        if self.height < self.pg_frame.get_height():
            self.height = self.pg_frame.get_height()

        # Setze die neue Größe auf das Fenster
        self.screen = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)


# MAIN
if __name__ == "__main__":

    # Initialisiere App
    app = Application()

    # Starte App
    app.run()
