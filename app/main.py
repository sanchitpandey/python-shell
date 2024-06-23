import sys

def main():
    builtin = ["echo", "exit", "type"]
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        x = input()
        if (x == "exit 0"):
            exit(0)
        elif (x == "exit 1"):
            exit(1)
        elif (x[:4]=="echo"):
            print(x[5:])
        elif (x[:4]=="type"):
            if (x[5:] in builtin):
                print(x[5:]+" is a shell builtin")
            else:
                print(x[5:]+": not found")
        else:
            print(x+": command not found")


if __name__ == "__main__":
    main()
