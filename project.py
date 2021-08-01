import os
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_folder(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = 'x0cCL9KciOgAAAAAAAAAAU3vq2NpmXEuNa6saWYR617cARzrSb-IqzQ34PP3PRF0'
    transferData = TransferData(access_token)

    file_from = input("Enter the folder path to upload  - ")
    file_to = input("enter the full path that you want to upload ")
    transferData.upload_folder(file_from, file_to)
    print('Folder has been moved')

main()