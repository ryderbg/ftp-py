def get_dir_name(path):
    path_split = path.split('\\')
    last_index = path_split.__len__()
    dir_name = path_split[last_index - 1]
    return dir_name