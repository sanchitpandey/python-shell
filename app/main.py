import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        x = input()
        if (x == "exit 0"):
            exit(0)
        print(x+": command not found")


if __name__ == "__main__":
    main()
