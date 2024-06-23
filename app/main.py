import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        x = input()
        print(x+": command not found")


if __name__ == "__main__":
    main()
