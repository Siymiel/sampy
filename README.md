
# Package Installer and Uninstaller

This script provides functionalities to install and uninstall Python packages while updating the `INSTALLED_APPS` in a Django `settings.py` file. It uses progress bars for visual feedback during installation and uninstallation processes.

## Problem Statement

Managing Python packages in a Django project can be cumbersome, especially when it comes to ensuring that newly installed packages are added to the `INSTALLED_APPS` list, or when removing packages that are no longer needed. This script aims to streamline the process by:

- Automatically installing missing packages.
- Uninstalling packages that are no longer required.
- Updating the `INSTALLED_APPS` list in a Django project's `settings.py` file to reflect these changes.
- Providing visual feedback through progress bars during these operations.

## Features

- Installs missing Python packages.
- Uninstalls specified Python packages.
- Adds installed packages to Django's `INSTALLED_APPS` list.
- Removes uninstalled packages from Django's `INSTALLED_APPS` list.
- Displays progress bars during installation and uninstallation.

## Dependencies

Ensure the following packages are installed:
- `colorama`
- `tqdm`

You can install the dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

1. **Install a package and add it to Django's `INSTALLED_APPS` list:**

   ```bash
   python script.py i <package_name>
   ```

   Replace `<package_name>` with the name of the package you want to install.

2. **Uninstall a package and remove it from Django's `INSTALLED_APPS` list:**

   ```bash
   python script.py u <package_name>
   ```

   Replace `<package_name>` with the name of the package you want to uninstall.

## Examples

To install `requests` and add it to `INSTALLED_APPS`:

```bash
python script.py i requests
```

To uninstall `requests` and remove it from `INSTALLED_APPS`:

```bash
python script.py u requests
```

## Notes

- Make sure to adjust the path to your `settings.py` file in the `install_and_add` and `uninstall_and_remove` functions if it's not located at `./mysite/settings.py`.
- The progress bars simulate progress and may not reflect the actual time taken for installation/uninstallation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
