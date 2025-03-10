def update_server_config(file_path, key, value):
    # Read the existing content of the server configuration file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Update the configuration value for the specified key
    with open(file_path, 'w') as file:
        for line in lines:
            # Check if the line starts with the specified key
            if key in line:
                # Update the line with the new value
                file.write(key + "=" + value + "\n")
            else:
                # Keep the existing line as it is
                file.write(line)

# Path to the server configuration file
file_path = 'server.conf'

# Key and new value for updating the server configuration
key = 'MAX_CONNECTIONS'
value = '1000'  

# Update the server configuration file

update_server_config(file_path, key, value)

# Another way to update the config

file_path = "server.conf"
key = "PORT"
value = "8081"
update_server_config(file_path, key, value)
