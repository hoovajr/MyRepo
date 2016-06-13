import datetime


class FileCopier:
    """Utility class for activities such as making backup"""
        
    def create_destination_folder(prefix, dest_location):
        suffix = '_{:%Y-%m-%d_%H.%M.%S}'.format(datetime.datetime.now())



