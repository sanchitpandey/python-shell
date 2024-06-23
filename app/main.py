import sys
import os

def main():
    builtin = ["echo", "exit", "type"]
    exec = []
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        paths = os.getenv("PATH").split(":")

        x = input()
        if (x == "exit 0"):
            exit(0)
        elif (x == "exit 1"):
            exit(1)
        elif (x[:4]=="echo"):
            sys.stdout.write(x[5:])
        elif (x[:4]=="type"):
            if (x[5:] in builtin):
                sys.stdout.write(x[5:]+" is a shell builtin")
            else:
                for path in paths:
                    for cmd in os.listdir(path):
                        if (x[5:] == cmd):
                            sys.stdout.write(x[5:]+" is "+path+cmd)
                sys.stdout.write(x[5:]+"is ")
        else:
            sys.stdout.write(x+": command not found")


if __name__ == "__main__":
    main()
