from colors import *
import socket

def help_command():
    help_text = (
        f"{light_blue}╔════════════════════════════════════════════╗\n"
        "║              Available Commands            ║\n"
        "╠════════════════════════════════════════════╣\n"
        "║  help      - Show this help message        ║\n"
        "║  info      - Show information about program║\n"
        "║  exit      - Exit the program              ║\n"
        "║  nslookup  - Lookup IP for a domain        ║\n"
        f"╚════════════════════════════════════════════╝{reset}"
    )
    return help_text

def info_command():
    info = (
        f"{light_blue}╔════════════════════════════════════════════╗\n"
        "║           Divinity CLI Utility             ║\n"
        "╠════════════════════════════════════════════╣\n"
        "║  Version : 1.0.0                           ║\n"
        "║  Author  : CodeByMed                       ║\n"
        "║  Purpose : Command-line Cyber-Security     ║\n"
        "║  GitHub  : https://github.com/repo         ║\n"
        f"╚════════════════════════════════════════════╝{reset}"
    )
    return info

def exit_command():
    return (
        f"{red}╔════════════════════════════════════════════╗\n"
        f"║         Program is shutting down...        ║\n"
        f"╚════════════════════════════════════════════╝{reset}"
    )

def nslookup():
    try:
        domain = input(f"{yellow}Enter Domain: {reset}")
        ip = socket.gethostbyname(domain)
        print(f"{green}IP address of {domain}: {ip}{reset}")
    except Exception as e:
        print(f"{red}Error: {e}{reset}")

def execute_command(command):
    cmd = command.strip().lower()
    if cmd == "help":
        print(help_command())
    elif cmd == "info":
        print(info_command())
    elif cmd == "exit":
        print(exit_command())
        exit(0)
    elif cmd == "nslookup":
        nslookup()
    else:
        print(f"{red}Unknown command. Type 'help' for a list of commands.{reset}")