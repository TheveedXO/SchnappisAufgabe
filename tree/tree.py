import os

def print_directory(path, indentation_level=0):

    h_line = chr(9472) # -
    v_line = chr(9474) # |
    left_high_corner = chr(9500) # |-
    left_low_corner = chr(9492) # |_

    files = 0
    directories = 0

    with os.scandir(path) as entries:

        sorted_entries = sorted(entries, key=lambda f: f.name.lower())
        entries_list = list(sorted_entries)

        for index, entry in enumerate(entries_list):

            is_last = index == len(entries_list) - 1
            corner = left_low_corner if is_last else left_high_corner

            indent = "  " * indentation_level
            if indentation_level > 0:
                indent = indent[:-4] + (v_line + "  " if not is_last else "  ")

            print(f"{indent}{corner}{h_line}{entry.name}")
            if entry.is_dir():
                directories += 1
                subdir_files, subdir_dirs = print_directory(entry.path, indentation_level + 1)
                files += subdir_files
                directories += subdir_dirs
            else:
                files+= 1

    if indentation_level == 0:
        print(f"\n{directories} directories, {files} files")
    return files, directories
if __name__ == "__main__":
    print_directory(".")
