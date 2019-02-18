def locationer(dir, json_file):

    import re
    import json
    if re.match('/.+/', dir):
        new_dir = re.sub("(?<=\B)/|/(?!\w)", '' , dir)
        path = re.split('/', new_dir)

    else:

        path = dir

    with open(json_file, 'r', encoding='utf-8') as container:

        js = json.load(container)
        fold_holder = path
        curr_dir = js
        if isinstance(path, list):

            for folder in path:
                curr_dir = curr_dir[folder]
                fold_holder = folder
        else:
            curr_dir = js[path]

        return {fold_holder: curr_dir}

if __name__ == '__main__':


    json_file = input('Please enter a valid json file: ')
    dir = input('Please enter a valid key or key path, formatted as /nodename/nodename/: ')
    locationer(dir, json_file)