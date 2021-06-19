# IMPORTS
from constants import *
import pyqrcode as qr
import sys


# METHODS

# Create Qr Code
def create_qrcode(data: str) -> qr.QRCode:

    # Return Qr Code
    return qr.create(data)

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
if __name__ == '__main__':

    # INITIALIZATION

    # Get System
    if sys.platform == "win32": system = S_WINDOWS
    elif sys.platform == "darwin": system = S_MACOS
    elif sys.platform == "linux": system = S_LINUX
    else: system = S_UNKNOWN

    # Set the Output Path for the right System
    if system == S_WINDOWS: output_path = ".\\QrCodes\\"
    else: output_path = r"./QrCodes/"

    # Set the Default Qr Code Scale
    qr_code_scale = 2

    # Print Welcome Message
    print("\nQr Code Generator\n----------------\n\nCreated for the MAKER SPACE Project:\n'Race Video Analyse'\n\nAuthor: Nikocraft, Magnus\nVersion: Beta 1.1\n\n")

    # ROUTINE
    while True:

        # Menu Routine

        # Get Input from User
        user_input = get_input("What want you do?", ("'C' = Create new Qr Code", "'Q' = Exit Program")).lower()

        # If User Input is C
        if user_input == 'c':

            # Create Routine

            # Get Qr Code Data Input
            user_input = get_input("\nPlease type your Qr Code data:", ("Any",))

            # Create the Qr Code
            print("\nCreate Qr Code ...")
            qr_code = create_qrcode(user_input)

            # Get Qr Code Image Name
            user_input = get_input("\nPlease type your filename to save as PNG:", ("Filename",))

            # Open new File
            print("\nOpen Qr Code file ...")
            with open(f"{output_path}{user_input}", "wb") as file:

                # Save Qr Code
                print("Save Qr Code ...")
                qr_code.png(file, qr_code_scale)

            # Print Completed Message
            print(f"\nQr Code saved completed at file '{output_path}{user_input}'!\n")

        # Else If User Input is Q
        elif user_input == 'q':

            # Exit Program
            print("\nExit Program ...")
            break

        # Else
        else:

            # Print Warning and Continue
            print("WARNING! Invalid Input. Try it again!\n")
