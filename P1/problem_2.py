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
    
    # paths to return
    list_of_paths = []

    # Listing files and directories in path
    current_dir = os.listdir(path)
    
    # iterating through files and directories
    for item in current_dir:
        new_path = os.path.join(path,item)
        
        if os.path.isdir(new_path):
            list_of_paths.extend(find_files(suffix, new_path))
        else:
            if new_path.endswith(suffix):
                list_of_paths.append(new_path)

    return list_of_paths


suffix = ".c"
path = './testdir'

print(find_files(suffix,path))