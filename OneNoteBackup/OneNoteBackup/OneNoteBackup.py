import FolderCopier

#instantiate new FolderCopier
oneNoteBackup = FolderCopier.FolderCopier()

# Set prefix
oneNoteBackup.set_source_folder("C:\OneNoteNotebooks")
oneNoteBackup.set_destination_folder(prefix="OneNote", 
                                     dest_location="C:\OneNoteBackups")
oneNoteBackup.copy_folder()

# Still to do:
## How to deal with MyDocuments, and get that to work (e.g. errors when using "\\CLTFILE" etc.)
## If number of backups > 5, then delete the oldest backups starting with Prefix such that only 5 are remaining.
## Create batch file.
## Bonus - Create executable, annotate, and ensure PEP8 compliant.
