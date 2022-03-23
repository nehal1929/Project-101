import dropbox
import os
import shutil

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        # enumerate local files recursively
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                 # construct the full local path
                local_path = os.path.join(root, filename)
                # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'P30uBDIGlusAAAAAAAAAAaLDo9vafr8A33SAZacgsSe4_Yk_k9UhbcCDMBOjb_qe'
    file_from = input("Enter the file name to transferred:")
    file_to= input("Enter the full path to be upload to dropbox:")
    transferData = TransferData(access_token)
    transferData.upload_file(file_from, file_to)
    print("File is moved to dropbox!")
main()