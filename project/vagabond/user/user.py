"""

"""

import os
import getpass


class User:

    def __init__(self):
        """
        Instantiates a new instance of User.
        """
        self.username1 = os.getlogin()
        self.username1 = getpass.getuser()
        self.home = os.path.expanduser("~")
        # self.history = []/deque()

    def create_settings_dir(self):
        """
        Creates a
        """
        dir_path = os.path.join(self.home, ".vagabond")

        # Check if the folder already exists and create it if not
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print(f"Created folder: {dir_path}")
        else:
            print(f"Folder already exists: {dir_path}")

