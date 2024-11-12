# Remote File Management Script

## Overview
This script provides a menu-driven interface for managing files on a remote server via SSH. Users can list files, delete files, and search for specific files in a designated remote directory.

## Requirements
- Python 3.x
- `sh` library for executing shell commands over SSH

## Configuration
Before running the script, ensure that the following variables are set correctly:
- `server`: The IP address or hostname of the remote server.
- `remote_dir`: The path to the remote directory where files are managed.

## Functions
- `ssh_object(server)`: Establishes an SSH connection to the specified server.
- `list_remote_files(ssh, server, remote_dir)`: Lists files in the specified remote directory.
- `delete_a_remote_file(ssh, file)`: Deletes a specified file from the remote directory.
- `menu()`: Displays a menu of options for the user.
- `print_file_list(file_list)`: Prints the list of files with their corresponding index.
- `file_list_and_size(ssh)`: Prints the list of files along with their sizes.
- `search_remote_file(file_list)`: Searches for a specific file in the list of remote files.
- `direct_choice(ssh, choice, file_list)`: Executes the action based on the user's choice.
- `main()`: The entry point of the program that runs the menu loop.

## Usage
1. Run the script using Python.
2. Follow the on-screen prompts to perform file management operations.
3. Choose "0" to exit the program.

## Notes
- Ensure that you have SSH access to the server without a password for seamless operation.
