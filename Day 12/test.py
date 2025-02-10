
def update_server_config(file_path, key, value):

    with open(file_path, 'r') as file:   # Open the file in read mode
        lines = file.readlines()

    with open(file_path, 'w') as file:   # Open the file in write mode

        for line in lines:
            if key in line:
                file.write(key + '=' + value + '\n')
            else:
                file.write(line)

update_server_config("server.conf", "MAX_CONNECTIONS", "500")
update_server_config("server.conf", "TIMEOUT", "60")

# Another way to do the same thing
file_path = "server.conf"
key = "PORT"
value = "8081"
update_server_config(file_path, key, value)