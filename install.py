#!/usr/bin/python3
import os
import pathlib
import sys


ABLETON_VERSION = 11
CONTROLLER_NAME = "APC40_MKII_9000"


def get_scripts_folder():
    """Get location of MIDI remote scripts folder"""
    # TODO: make windows friendly
    return "Contents/App-Resources/MIDI Remote Scripts"


def discover_ableton_folder() -> pathlib.Path:
    """Find location of ableton application folder
    """
    options = list(
        pathlib.Path("/Applications").glob(f"Ableton Live {ABLETON_VERSION}*"))
    if len(options) == 0:
        print("No Ableton Live application folder could be found.")
        sys.exit(0)
    elif len(options) == 1:
        return options[0]
    else:
        while True:
            print("Multiple Ableton application folders found:")
            for i, option in enumerate(options):
                print(f'\t{i}: "{option}"')
            print("\tq: exit")
            answer = input("Select an option (enter a number): ")
            if answer == "q":
                sys.exit(0)
            else:
                try:
                    return options[int(answer)]
                except (IndexError, TypeError):
                    print("\nInvalid input!\n")
                    pass


def main():
    ableton_folder = discover_ableton_folder()
    install_path = ableton_folder / get_scripts_folder()
    # TODO: make windows friendly
    print(f'copying {CONTROLLER_NAME} to "{install_path}"')
    os.system(f'rm -rf "{install_path}"')
    os.system(f'cp -r {CONTROLLER_NAME} "{install_path}"')
    print("done!")


if __name__ == "__main__":
    if sys.platform != "darwin":
        print("Install script only works for Mac.")
        sys.exit(0)
    main()
