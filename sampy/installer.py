import sys
import subprocess

def install_package_if_missing(package_name):
    try:
        __import__(package_name)
    except ImportError:
        print(f"`{package_name}` not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"`{package_name}` installed successfully.")
    return __import__(package_name)

# Ensure colorama and tqdm are installed
colorama = install_package_if_missing("colorama")
tqdm = install_package_if_missing("tqdm")

def pip_install(package_name):
    # Display a progress bar during installation
    for _ in tqdm.tqdm(range(100), desc=f"{colorama.Fore.YELLOW}Installing {package_name}", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", ncols=60):
        subprocess.run(["sleep", "0.02"])  # Simulate progress (remove in actual usage)
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def pip_uninstall(package_name):
    # Display a progress bar during uninstallation
    for _ in tqdm.tqdm(range(100), desc=f"{colorama.Fore.YELLOW}Uninstalling {package_name}", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", ncols=60):
        subprocess.run(["sleep", "0.02"])  # Simulate progress (remove in actual usage)
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", package_name])

def install_and_add(package_name):
    pip_install(package_name)
    
    settings_file = './mysite/settings.py'  # Adjust the path as needed
    with open(settings_file, 'r+') as f:
        lines = f.readlines()
        if package_name not in ''.join(lines):
            # Find the INSTALLED_APPS section
            for i, line in enumerate(lines):
                if 'INSTALLED_APPS' in line:
                    break
            # Insert the new package
            for j in range(i, len(lines)):
                if ']' in lines[j]:  # End of the list
                    lines.insert(j, f"    '{package_name}',\n")
                    break
            f.seek(0)
            f.writelines(lines)
            print(colorama.Fore.GREEN + f"`{package_name}` added to INSTALLED_APPS")

def uninstall_and_remove(package_name):
    pip_uninstall(package_name)
    
    settings_file = './mysite/settings.py'  # Adjust the path as needed
    with open(settings_file, 'r+') as f:
        lines = f.readlines()
        package_line = f"    '{package_name}',\n"
        if package_line in lines:
            lines.remove(package_line)
            f.seek(0)
            f.truncate()
            f.writelines(lines)
            print(colorama.Fore.BLUE + f"`{package_name}` removed from INSTALLED_APPS")

if __name__ == "__main__":
    colorama.init(autoreset=True)  # Initialize colorama

    if len(sys.argv) > 2:
        action = sys.argv[1]
        package_name = sys.argv[2]
        if action == 'i':
            print(colorama.Fore.YELLOW + f"Installing `{package_name}`...")
            install_and_add(package_name)
        elif action == 'u':
            print(colorama.Fore.YELLOW + f"Uninstalling `{package_name}`...")
            uninstall_and_remove(package_name)
        else:
            print(colorama.Fore.RED + "Invalid action. Use 'i' for install or 'u' for uninstall.")
    else:
        print(colorama.Fore.RED + "Please provide an action ('i' or 'u') and a package name.")
