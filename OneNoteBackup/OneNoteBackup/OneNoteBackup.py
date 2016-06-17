import FolderCopier

#instantiate new FolderCopier
oneNoteBackup = FolderCopier.FolderCopier()

# Set prefix
oneNoteBackup.set_source_folder()
oneNoteBackup.set_destination_folder(prefix="OneNote", 
                                     dest_location="")
oneNoteBackup.copy_folder()

# Still to do:
## (done) (use r for raw strings) How to deal with MyDocuments, and get that to work (e.g. double backslash etc.)
## If source_folder = dest_location, exit with custom exception.
## Have source / destination folders passed in as arguments.
## If number of backups > 5, then delete the oldest backups starting with Prefix such that only 5 are remaining.
## Create batch file.
## Bonus - Create executable, annotate, and ensure PEP8 compliant.
