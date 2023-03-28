# import sys
import argparse

VERSION = "0.0.0"


def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-v", "--version", help="Show version", action="version", version = f'Version : {VERSION}')

    args = argParser.parse_args()



if __name__ == "__main__":
    main()

