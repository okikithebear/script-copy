import paramiko

def copy_file(source_path, destination_path, hostname, username, password):
    try:
        # Create SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to  remote server
        ssh_client.connect(hostname, username=username, password=password)

        # Use SFTP to copy  file
        with ssh_client.open_sftp() as sftp:
            sftp.put(source_path, destination_path)
            print(f"File copied successfully from {source_path} to {destination_path}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close  SSH connect
        if ssh_client:
            ssh_client.close()


source_path = "/path/to/local/file.txt"
destination_path = "/path/to/remote/file.txt"
hostname = "remote_server_ip"
username = "your_username"
password = "your_password"

print("Starting the file copy process...")
copy_file(source_path, destination_path, hostname, username, password)
print("File copy process completed.")