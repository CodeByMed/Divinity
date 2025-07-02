from colors import *
from commands import execute_command

def main():
    print(f"{green}[+] Welcome to XS13 CLI! Type 'help' for a list of commands.\n{reset}")

    while True:
        try:
            user_input = input(f"{light_green}$ {reset}")
            execute_command(user_input)
        except KeyboardInterrupt:
            print(f"\n{red}[-] Exiting XS13. Goodbye!{reset}")
            break
        except Exception as e:
            print(f"{red}[-] An error occurred: {e}{reset}")

if __name__ == "__main__":
    main()