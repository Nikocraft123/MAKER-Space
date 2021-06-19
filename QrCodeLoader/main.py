# IMPORTS
import cv2
from pyzbar import pyzbar
import os


# METHODS

# Load Image
def load_image(path: str):

    # Lade Bild
    image = cv2.imread(path)

    # Lade Qr Codes
    print("\nQr Code data:")
    codes = pyzbar.decode(image)

    # Gehe durch jeden Qr Code durch
    for code in codes:

        # Hole Position und Größe des Qr Code
        x_pos, y_pos, width, height = code.rect

        # Zeichne Rahmen um Qr Code
        cv2.rectangle(image, (x_pos, y_pos), (x_pos + width, y_pos + height), (0, 0, 255), 2)

        # Decode Qr Code Data
        qr_data = code.data.decode("utf-8")
        print(f"- {qr_data}")

        # Write the Data above the Qr Code
        cv2.putText(image, qr_data, (x_pos, y_pos - 8), cv2.QT_FONT_NORMAL, 0.4, (0, 255, 0), 1)

    # Zeige Bild in einem Fenster
    cv2.imshow("Qr Code Image Scanner", image)

    # Warte auf Taste
    cv2.waitKey(0)

    # Zerstöre alle Fenster
    print("\nImage closed.\n")
    cv2.destroyAllWindows()

# Get User Input
def get_input(message: str, options: tuple) -> str:

    # Print the Message
    print(message)

    # Build Options
    option_str = "["
    if (len(options) == 0):
        option_str += "Alles]"
    else:
        for option, value in enumerate(options):
            if option == len(options) - 1:
                option_str += f"{value}]"
            else:
                option_str += f"{value} | "

    # Print Options
    print(option_str)

    # Return Input
    return input("> ")


# MAIN
if __name__ == "__main__":

    # Pfadeingabe
    while True:

        # Get path from user
        user_input = get_input("Please type the path of the image:", ("Path", "#EXIT#"))

        # If the User Input is #exit#
        if user_input.lower() == "#exit#":

            # Print Exit Message and Break
            print("Exit Program ...")
            break

        # Check, if the path exist
        if not os.path.exists(user_input):

            # Print Warning Message and Continue
            print("WARNING! Can't find this Image. Try it again!\n")
            continue

        # Load the Image
        print("\nLoad the Image ...")
        load_image(user_input)
