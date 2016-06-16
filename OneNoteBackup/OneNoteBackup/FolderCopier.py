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
        self.destination_folder = dest_location + "\\" + prefix + suffix
        print("dest=", self.destination_folder)        

    def copy_folder(self):
        shutil.copytree(self.source_folder, self.destination_folder)