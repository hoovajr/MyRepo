import datetime
import os
import shutil

# specifically will use shutil.copytree()  

class FolderCopier:
    """Utility class for activities such as making backup"""
    
    def set_source_folder(self, source_folder):
        self.source_folder = source_folder
        print("source=", self.source_folder)
    
    def set_destination_folder(self, prefix, dest_location):
        suffix = '_{:%Y-%m-%d_%H.%M.%S}'.format(datetime.datetime.now())
        self.dest_location = dest_location
        self.destination_folder = self.dest_location + "\\" + prefix + suffix
        print("dest=", self.destination_folder)        

    def copy_folder(self):
        if self.source_folder == self.dest_location:
                raise Exception("Source folder and destination folder cannot be the same.")
        shutil.copytree(self.source_folder, self.destination_folder)