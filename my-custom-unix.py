import sys
import subprocess
import argparse

is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")
        G = Y = B = R = W = G = Y = B = R = W = ''
else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white

def no_color():
    global G, Y, B, R, W
    G = Y = B = R = W = ''

def parser_error(errmsg):
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()

def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -v")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-v', '--verbose', help='Enable Verbosity and display results in realtime', nargs='?', default=False)
    parser.add_argument('-o', '--output', help='Save the results to text file')
    parser.add_argument('-n', '--no-color', help='Output without color', default=False, action='store_true')
    return parser.parse_args()

def banner():
    print("""%s
        ▄▄       ▄▄  ▄         ▄       ▄         ▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄ 
        ▐░░▌     ▐░░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌
        ▐░▌░▌   ▐░▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀  ▐░▌   ▐░▌ 
        ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌▐░▌    ▐░▌     ▐░▌       ▐░▌ ▐░▌  
        ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌     ▐░▌        ▐░▐░▌   
        ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌     ▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌     ▐░▌         ▐░▌    
        ▐░▌   ▀   ▐░▌ ▀▀▀▀█░█▀▀▀▀      ▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌     ▐░▌        ▐░▌░▌   
        ▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌     ▐░▌       ▐░▌ ▐░▌  
        ▐░▌       ▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄  ▐░▌   ▐░▌ 
        ▐░▌       ▐░▌     ▐░▌          ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌
        ▀         ▀       ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀ %s
    # Coded By David Munoz - @davidmunoz-dev%s
    """ % (G, Y, W))

def install_apt_program(program, verbose):
    try:
        print(f"{B}Installing {program}...")
        command = ["sudo", "apt", "install", "-y"]
        if not verbose:
            command.append("-q")
        command.append(program)
        print(f"{W}")
        subprocess.check_call(command)
        print(f"{B}")
        subprocess.check_call([program, '--version'])
        print(f"{G}{program} installed successfully")
        print(f"{W}")
    except subprocess.CalledProcessError as e:
        print(f"{R}Failed to install {program}: {e}{W}")
        sys.exit(1)

def configure_zshrc():
    file_path = 'aliases.txt'
    lines_of_text = [
    'alias ne="emacs -nw"\n',
    'alias pbcopy=\'xsel --input --clipboard\'\n',
    'alias pbpaste=\'xsel --output --clipboard\'\n',
    'alias ..="cd .."\n',
    'alias ...="cd ../.."\n'
    ]
    existing_lines = []

    try:
        with open(file_path, 'r') as file:
            existing_lines = file.readlines()
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Creating new file.")
    lines_to_add = [line for line in lines_of_text if line not in existing_lines]

    if lines_to_add:
        with open(file_path, 'a') as file:
            file.writelines(lines_to_add)
        print(f'Lines appended to {file_path} successfully.')
    else:
        print('All lines already exist in the file. Nothing appended.')

def install_oh_my_zsh():
    try:
        subprocess.check_call(["sh", "-c", "'$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'"])
        print(f"{G}Oh My Zsh installed successfully{W}")
        configure_zshrc()
    except subprocess.CalledProcessError as e:
        print(f"{R}Failed to install Oh My Zsh: {e}{W}")
        sys.exit(1)

def install_nvm():
    try:
        subprocess.check_call(["curl", "-o-", "https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh", "|", "zsh"])
        print(f"{G}NVM installed successfully{W}")
        subprocess.check_call(["nvm", "install", "--lts"])
        subprocess.check_call(["node", "--version"])
    except subprocess.CalledProcessError as e:
        print(f"{R}Failed to install NVM: {e}{W}")
        sys.exit(1)

def install_apt_programs(verbose):
    programs = ['curl', 'git', 'htop', 'btop', 'zsh', 'emacs', 'xsel', 'terminator']
    for program in programs:
        print('--------\n')
        install_apt_program(program, verbose)
    print('--------\n')

def install_custom_programs():
    install_oh_my_zsh()
    install_nvm()

def main(domain, threads, savefile, ports, silent, verbose, enable_bruteforce, engines):
    print("hell world")

def interactive():
    args = parse_args()
    verbose = args.verbose
    if verbose or verbose is None:
        verbose = True
    if args.no_color:
        no_color()
    banner()
    # Update package lists
    #subprocess.check_call(["sudo", "apt", "update"])
    install_apt_programs(verbose)
    install_custom_programs()

if __name__ == "__main__":
    interactive()
