funny‐startup
================

![gif](output.gif)

A simple setup script that configures your shell (Bash or Zsh) to automatically launch a Python ASCII‑art message on each interactive session.

## Features

- Detects whether you use Bash (`.bashrc`) or Zsh (`.zshrc`).
- Prepends environment variables (`FUNNY_START_HOME`, `FIGLET_FONTS_DIR`) to your shell rc‑file.
- Adds an interactive hook to run your Python ASCII‑art script (`colorfiglet.py`) on every new shell session.
- Ensures the setup code is placed at the top of the rc‑file, preventing later overrides.

## Prerequisites

- macOS or Linux with Bash or Zsh.
- Python 3.7+ with a virtual environment containing your ASCII‑art script (`colorfiglet.py`).
- `pyfiglet` and `art` packages installed in that virtualenv.


## Installation

Clone this repository to your home directory (or any folder):

```sh
git clone https://github.com/su-mt/funny-startup.git
cd funny-startup

python3 -m venv .venv # You must use .venv as the exact directory name.
pip install pyfiglet art

chmod +x init.sh
./init.sh

```


## Configuration & Usage

Run the installer once to configure your shell:

```sh
chmod +x init.sh
./init.sh
```

You will be prompted:

    Which shell are you using? (b for bash / z for zsh):

Enter `b` for Bash or `z` for Zsh.

The script will prepend the following snippet to the top of `~/.bashrc` or `~/.zshrc`:

```sh
# --- asciiart startup added by select_shell.sh ---
export FIGLET_FONTS_DIR="/path/to/asciiart-startup"
export FUNNY_START_HOME="/path/to/asciiart-startup"
if [[ $- == *i* ]]; then
    "/path/to/asciiart-startup/.venv/bin/python" "/path/to/asciiart-startup/colorfiglet.py"
fi
# --- end asciiart startup ---
```

Restart your terminal or source the rc‑file to apply changes:

```sh
source ~/.bashrc   # or source ~/.zshrc
```

## Customization

**Change execution path**  
Edit `init.sh` if your virtualenv or script location differs.

**Modify color/font settings**  
Tweak `colorfiglet.py` to add new ANSI colors, fonts, or message files.

## Uninstallation

Remove the prepended block from your `~/.bashrc` or `~/.zshrc`.

(Optional) Delete the asciiart-startup directory:

```sh
rm -rf ~/asciiart-startup
```

## License

This project is released under the MIT License.
