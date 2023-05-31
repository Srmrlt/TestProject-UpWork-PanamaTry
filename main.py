import os
from azure.storage.blob import BlobServiceClient

# Azure Blob Storage credentials
connection_string = "DefaultEndpointsProtocol=https;AccountName=panama1try;" \
                    "AccountKey=lR97CJG2AgaWtUnNPisKeUfBpvJODqW7zC4GjUmzQVfO" \
                    "vvqxZBoNGMqwL8i3fWCVnhAc9KA+0v7K+AStLMxz2g==;EndpointSu" \
                    "ffix=core.windows.net"
container_name = "connection1test"

# Directory path to fetch the latest file from
directory_path = "files"

# Fetch the latest file from the directory
files_path = []
for dir_file in os.listdir(directory_path):
    files_path.append(os.path.join(directory_path, dir_file))
latest_file = max(files_path, key=os.path.getctime)
print(latest_file)

# Rename the file
new_file_name = "sending2test.txt"  # Replace with your desired new file name
new_file_path = os.path.join(directory_path, new_file_name)
os.rename(latest_file, new_file_path)

# Upload the renamed file to Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=new_file_name)

containers = blob_service_client.list_containers()
for container in containers:
    print(container.name)

with open(new_file_path, "rb") as data:
    blob_client.upload_blob(data)

# Print success message
print(f"File '{new_file_name}' uploaded to Azure Blob Storage successfully.")
