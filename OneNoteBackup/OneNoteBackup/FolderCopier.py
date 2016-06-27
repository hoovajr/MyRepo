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
        self.prefix = prefix
        suffix = '_{:%Y-%m-%d_%H.%M.%S}'.format(datetime.datetime.now())
        self.dest_location = dest_location
        self.destination_folder = self.dest_location + "\\" + prefix + suffix
        print("dest=", self.destination_folder)        

    def copy_folder(self):
        if self.source_folder == self.dest_location:
            raise Exception("Source folder and destination folder cannot be the same.")
        shutil.copytree(self.source_folder, self.destination_folder)

    def purge_old_backups(self, num_backups_to_keep=5):
        if not (self.source_folder and self.destination_folder and self.prefix):
            raise Exception("Source folder, destination folder, and prefix all must be populated.")
        if num_backups_to_keep < 1:
            raise Exception("Number of backups to keep must be at least 1.")

        backups_list=[]
        for item in os.listdir(dest_location):
            backups_list.add('\\'.join((dest_location, item)))
