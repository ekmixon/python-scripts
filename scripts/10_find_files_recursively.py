import fnmatch
import os

# constants
PATH = './'
PATTERN = '*.md'


def get_file_names(filepath, pattern):
    if os.path.exists(filepath):
        matches = []
        for root, dirnames, filenames in os.walk(filepath):
            matches.extend(
                os.path.join(filename)
                for filename in fnmatch.filter(filenames, pattern)
            )

        if matches:
            print(f"Found {len(matches)} files:")
            output_files(matches)
        else:
            print("No files found.")
    else:
        print("Sorry that path does not exist. Try again.")


def output_files(list_of_files):
    for filename in list_of_files:
        print(filename)


if __name__ == '__main__':
    get_file_names(PATH, PATTERN)
