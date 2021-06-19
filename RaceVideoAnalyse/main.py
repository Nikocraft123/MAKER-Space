# IMPORTS
import cv2 as cv
import pygame as pg

import color
import utils


# CLASSES

# Application
class Application:

    # CONSTRUCTOR
    def __init__(self):

        # Definiere Fenster Titel
        self.title = "MAKER Space - Race Video Analyse"

        # Definiere Fenster Größe
        self.width = 900
        self.height = 700

        # Definiere Fenster Mindestgröße
        self.min_width = 850
        self.min_height = 600

        # Definiere Kamerasignal
        self.video_cap = cv.VideoCapture(0, cv.CAP_DSHOW)

        # Initialisiere Pygame
        pg.init()

        # Definiere Running
        self.running = True


    # METHODS

    # Run
    def run(self) -> None:

        # Definiere Fenster
        self.screen = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
        pg.display.set_caption(self.title)

        # App Routine
        while self.running:

            # Aktualisiere Kamera Frame
            self.update_cam_frame()

            # Aktualisiere Fenster Größe
            self.update_window_size()

            # Aktualisiere Fenster Inhalt
            self.update_screen()

            # Behandle Events
            self.handel_events()

        # Beende Pygame
        pg.quit()

        # Löse das Kamerasignal
        self.video_cap.release()

    # Aktualisiere Fenster Inhalt
    def update_screen(self) -> None:

        # Setze den Hintergrund auf Türkis
        self.screen.fill(color.GRAY)

        # Zeichne Kamera Frame auf dem Fenster
        #self.screen.blit(self.pg_frame, ((self.screen.get_width() - self.pg_frame.get_width()) // 2, (self.screen.get_height() - self.pg_frame.get_height()) // 2))
        pg.draw.rect(self.screen, color.BLUE, (10, 10, 10 + self.pg_frame.get_width(), 10 + self.pg_frame.get_height()))
        self.screen.blit(self.pg_frame, (15, 15))

        # Zeichne Infoleiste
        pg.draw.rect(self.screen, color.YELLOW, (self.pg_frame.get_width() + 100, 10, self.screen.get_width() - self.pg_frame.get_width() - 110, self.screen.get_height() - 20))

        # Aktualisiere Fenster
        pg.display.flip()

    # Behandle Events
    def handel_events(self) -> None:

        # Gehe durch alle Events durch
        for event in pg.event.get():

            # Wenn das Fenster schließen Event gefunden wurde
            if event.type == pg.QUIT:

                # Setze Running auf Falsch
                self.running = False

            # Wenn eine Taste gedrückt wurde
            if event.type == pg.KEYDOWN:

                # Wenn die gedrückte Taste ESC ist
                if event.key == pg.K_ESCAPE:

                    # Setze Running auf Falsch
                    self.running = False

    # Aktualisiere Kamera Frame
    def update_cam_frame(self) -> None:

        # Hole aktuellen Frame
        _, self.frame = self.video_cap.read()

        # Lade Qr Codes
        utils.load_qr_codes(app)

        # Skaliere Frame auf 0.8
        self.frame = utils.resize_img(self.frame, 0.8)

        # Konvertiere OpenCV Bild zu Pygame Bild
        self.pg_frame = pg.image.frombuffer(self.frame.tobytes(), (self.frame.shape[1], self.frame.shape[0]), "BGR")

    # Aktualisiere Fenster Größe
    def update_window_size(self) -> None:

        # Hole Größe
        self.width, self.height = pg.display.get_window_size()

        # Kontrolliere, ob die Größe zu klein ist
        if self.width < self.min_width:
            self.width = self.min_width
        if self.height < self.min_height:
            self.height = self.min_height

        # Setze die neue Größe auf das Fenster
        self.screen = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)


# MAIN
if __name__ == "__main__":

    # Initialisiere App
    app = Application()

    # Starte App
    app.run()
