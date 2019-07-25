import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    paths = []
    list_of_paths = []

    current_dir = os.listdir(path)
    paths.append(path)
    
    for item in current_dir:
        new_path = os.path.join(path,item)

        print(new_path)

        if os.path.isdir(new_path):
            find_files(suffix, new_path)
            paths.append(new_path)
        else:
            paths.append(new_path)
    
    return paths

suffix = ".c"
path = './testdir'

print(find_files(suffix,path))