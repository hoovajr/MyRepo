import FolderCopier
import sys

#instantiate new FolderCopier
oneNoteBackup = FolderCopier.FolderCopier()

# Remove next two lines after calling this from comman line.
sys.argv[0] = 
sys.argv[1] = 


# Set prefix
oneNoteBackup.set_source_folder(sys.argv[0])
oneNoteBackup.set_destination_folder(prefix="OneNote", 
                                     dest_location=sys.argv[1])
oneNoteBackup.copy_folder()

# Still to do:
## (done) (use r for raw strings) How to deal with MyDocuments, and get that to work (e.g. double backslash etc.)
## (done) If source_folder = dest_location, exit with exception.
## Have source / destination folders passed in as arguments.
## If number of backups > 5, then delete the oldest backups starting with Prefix such that only 5 are remaining.
## Create batch file.
## Bonus - Create executable, annotate, and ensure PEP8 compliant.
