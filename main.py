import sh

server = "192.168.1.238"
remote_dir = "/mnt/2tb/kabads-films"
# remote_dir = "/home/adam"

"""
This module provides a menu-driven program that allows the user to list files in a remote directory. 
It assumes that you already have a working SSH connection to the server, without a password.
"""

def ssh_object(server):
    """
    Connects to the specified server using SSH.
    Args:
        server (str): The server address.
    Returns:
        ssh: An SSH object representing the connection to the server, or None if an error occurred.
    Raises:
        Exception: If an error occurred while connecting to the server.
    """

    try:
        ssh = sh.ssh.bake(f"{server}")
        print(f"connected to {server}")
        return ssh
    except Exception as e:
        print(f"Error: {e}")
    return None


def list_remote_files(ssh, server, remote_dir):
    """
    Lists the files in a remote directory using SSH.
    Args:
        ssh (function): A function that executes SSH commands.
        server (str): The server address.
        remote_dir (str): The path to the remote directory.
    Returns:
        list: A list of files in the remote directory.
    """

    file_list = list(ssh("ls " + remote_dir).split())
    return file_list


def delete_a_remote_file(ssh, file):
    """
    Deletes a file from a remote directory.
    Args:
        ssh (SSHClient): The SSH client object used to connect to the remote server.
        file (str): The name of the file to be deleted.
    Returns:
        list: A list of files in the remote directory after the deletion.
    Raises:
        Exception: If an error occurs while deleting the file.
    """

    try:
        ssh.rm(remote_dir + "/" + file)
        print(f"Deleted {file}")
        file_list = list_remote_files(ssh, server, remote_dir)
        return file_list
    except Exception as e:
        print(f"Error: {e}")


def menu():
    """
    Displays a menu and prompts the user for a choice.
    Returns:
        str: The user's choice as a string. Possible choices are:
            - "1" for listing files
            - "2" for deleting a file
            - "3" for listing files with size
            - "4" for searching a file
            - "0" for exiting
            - None if an invalid choice is entered
    """
    print()
    print("What would you like to do?")
    print("1. List files")
    print("2. Delete a file")
    print("3. List files with size")
    print("4. Search for a file")
    print("0. Exit")

    choice = input("Enter your choice: ")
    if choice in ["1", "2", "3", "4", "0"]:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return None


def print_file_list(file_list):
    """
    Prints the list of files with their corresponding index.
    Args:
        file_list (list): A list of files.
    Returns:
        None
    """
    
    digit = 1
    for file in file_list:
        print(f"{digit}: {file}")
        digit += 1

def file_list_and_size(ssh):
    """
    Prints the list of files with their corresponding index and size.
    Args:
        ssh (SSHClient): The SSH client object used for remote file operations.
        file_list (list): A list of files.
    Returns:
        None
    """
    global remote_dir
    try:
        print(ssh(f"ls -lh {remote_dir}"))
    except Exception as e:
        print(f"Error: {e}")

def search_remote_file(file_list):
    """
    Searches for a specific file in the list of remote files.
    Args:
        file_list (list): A list of files in the remote directory.
    Returns:
        str: The name of the file if found, or None if not found.
    """
    filename = input("Enter the name of the file you want to search for: ")
    if filename in file_list:
        print(f"File '{filename}' found.")
        return filename
    else:
        print(f"File '{filename}' not found.")
        return None


def direct_choice(ssh, choice, file_list):
    """
    Executes a specific action based on the user's choice.
    Parameters:
    - ssh (SSHClient): The SSH client object used for remote file operations.
    - choice (str): The user's choice.
    - file_list (list): The list of files.
    Returns:
    - None
    Raises:
    - None
    """

    if choice == "1":
        print_file_list(file_list)
    elif choice == "2":
        file = input("Enter the number of the file you want to delete: ")
        delete_a_remote_file(ssh, file_list[int(file) - 1])
    elif choice == "3":
        file_list_and_size(ssh)
    elif choice == "4":
        search_remote_file(file_list)
    elif choice == "0":
        exit = True
        return

def main():
    """
    Entry point of the program.
    This function establishes an SSH connection to a server and performs various operations on remote files.
    It prompts the user with a menu to choose an action, such as creating files, deleting 
    files, or disconnecting from the server.
    The function continues to loop until the user chooses to exit the program.
    Parameters:
    None
    Returns:
    None
    """
    ssh = ssh_object(server)

    exit_program = False

    while exit_program == False:
        choice = None
        while choice is None:
            choice = menu()
            if choice == "0":
                print(f"Disconnecting from {server}.....")
                exit_program = True
        file_list = list_remote_files(ssh, server, remote_dir)
        direct_choice(ssh, choice, file_list)


if __name__ == '__main__':
    main()
