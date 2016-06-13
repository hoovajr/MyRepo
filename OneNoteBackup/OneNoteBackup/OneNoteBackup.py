# specifically will use shutil.copytree()  

#instantiate new FolderCopier
oneNoteBackup = FolderCopier()

# Set prefix
oneNoteBackup.set_prefix("OneNote")
oneNoteBackup.set_source_folder("C:\OneNoteNotebooks")

# Set Source Folder, destination folder
# Create Backup subfolder (prefix + current datetimestamp)
# Copy Folders from source folder to newly created backup folder
# If number of backups > 5, then delete the oldest backup

