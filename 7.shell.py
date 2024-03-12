import subprocess
import sys

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def main():
    while True:
        user_input = input("$ ")
        if user_input.lower() == "exit":
            break
        elif ">" in user_input:
            # Output redirection
            command, output_file = user_input.split(">")
            command = command.strip()
            output_file = output_file.strip()
            with open(output_file, "w") as f_out:
                try:
                    subprocess.run(command, shell=True, check=True, stdout=f_out)
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")
        elif "<" in user_input:
            # Input redirection
            command, input_file = user_input.split("<")
            command = command.strip()
            input_file = input_file.strip()
            with open(input_file, "r") as f_in:
                try:
                    subprocess.run(command, shell=True, check=True, stdin=f_in)
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")
        else:
            execute_command(user_input)

if __name__ == "__main__":
    main()