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
        # Sets destination backup folder to start with prefix and end with timestamp.
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

        # Create a list of absolute paths to all backups with this prefix
        backups_list=[]
        for item in os.listdir(self.dest_location):
            if item.startswith(self.prefix):
                    backups_list.append('\\'.join((self.dest_location, item)))

        # while there are more than num_backups_to_keep, delete the folder and contents.
        length = len(backups_list)        
        while length > num_backups_to_keep:
            shutil.rmtree(backups_list.pop(0))
            length-=1
