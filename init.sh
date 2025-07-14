#!/bin/bash

# This script asks the user which shell they use (b for bash, z for zsh),
# then appends the necessary environment setup and startup call to the appropriate rc file.

# Determine the directory where this script resides
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -n "Which shell are you using? (b for bash / z for zsh): "
read -r shell_choice

# Choose the rc file based on input
case "$shell_choice" in
    b|B)
        rc_file="$HOME/.bashrc"
        ;;
    z|Z)
        rc_file="$HOME/.zshrc"
        ;;
    *)
        echo "Invalid input: '$shell_choice'. Expected 'b' or 'z'."
        exit 1
        ;;
esac

echo "Adding configuration to $rc_file ..."

{
    echo ""
    echo "# --- asciiart startup added by select_shell.sh ---"
    echo "export FIGLET_FONTS_DIR=\"$script_dir\""
    echo "export FUNNY_START_HOME=\"$script_dir\""
    echo "if [[ \$- == *i* ]]; then"
    echo "    \"$script_dir/.venv/bin/python\" \"$script_dir/colorfiglet.py\""
    echo "fi"
    echo "# --- end asciiart startup ---"
} >> "$rc_file"

echo "Done. Please restart your shell or run 'source $rc_file' to apply changes."
