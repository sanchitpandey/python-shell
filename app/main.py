import sys
import os
import subprocess

def main():
    builtin = ["echo", "exit", "type", "pwd"]

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        paths = os.getenv("PATH").split(":")

        x = input()
        if x == "exit 0":
            exit(0)
        elif x == "exit 1":
            exit(1)
        elif x[:4] == "echo":
            sys.stdout.write(x[5:] + "\n")
        elif x[:3]== "pwd":
            sys.stdout.write(os.getcwd() + "\n")
        elif x[:4] == "type":
            command = x[5:]
            if command in builtin:
                sys.stdout.write(command + " is a shell builtin\n")
            else:
                found = False
                for path in paths:
                    executable_path = os.path.join(path, command)
                    if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                        found = True
                        sys.stdout.write(command + " is " + executable_path + "\n")
                        break
                if not found:
                    sys.stdout.write(command + ": not found\n")
        else:
            command_parts = x.split()
            command = command_parts[0]
            args = command_parts[1:]
            found = False
            for path in paths:
                executable_path = os.path.join(path, command)
                if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                    found = True
                    try:
                        subprocess.run([executable_path] + args)
                    except Exception as e:
                        sys.stdout.write(f"Error executing {command}: {e}\n")
                    break
            if not found:
                sys.stdout.write(command + ": command not found\n")

if __name__ == "__main__":
    main()
