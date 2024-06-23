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
            sys.stdout.write(x[5:]+"\n")
        elif (x[:4]=="type"):
            if (x[5:] in builtin):
                sys.stdout.write(x[5:]+" is a shell builtin\n")
            else:
                found = 0;
                for path in paths:
                    if os.path.isfile(path+"/"+x[5:]):
                        found = 1;
                        sys.stdout.write(x[5:]+" is "+path+"/"+x[5:]+"\n")
                if (found == 0):
                    sys.stdout.write(x[5:]+": not found\n")
        else:
            sys.stdout.write(x+": command not found\n")


if __name__ == "__main__":
    main()
