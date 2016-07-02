import FolderCopier
import sys

#instantiate new FolderCopier
oneNoteBackup = FolderCopier.FolderCopier()

# Remove next two lines after calling this from comman line.

# Set prefix
oneNoteBackup.set_source_folder(sys.argv[1])
oneNoteBackup.set_destination_folder(prefix="OneNote", 
                                     dest_location=sys.argv[2])
oneNoteBackup.copy_folder()
oneNoteBackup.purge_old_backups()

# Still to do:
## (done) (use r for raw strings) How to deal with MyDocuments, and get that to work (e.g. double backslash etc.)
## (done) If source_folder = dest_location, exit with exception.
## (done) Have source / destination folders passed in as arguments.
## (done)If number of backups starting with prefix > 5 (use os.listdir() to start), 
## (done)...then delete the oldest (os.stat()?) backups starting with Prefix such that only 5 are remaining.
## (done)Create batch file.
## (deferred) Bonus - Create executable, annotate, and ensure PEP8 compliant.
