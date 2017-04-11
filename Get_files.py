import git
import os
import shutil
from Repository_data import git_input


# Retrieve the repository and then rename the files that contains % located in the folders specified in
def get_files():
    clone_url = 'https://' + git_input['username'] + ':' + git_input['password'] + '@' + git_input['git_url']
    local_repo_path = git_input['repo_dir']
    shutil.rmtree(local_repo_path, True)
    git_info_folder = os.path.join(local_repo_path, '.git/info')
    repo = git.Repo.init(local_repo_path)
    origin = repo.create_remote('origin', clone_url)
    config = repo.config_writer('repository')
    config.set('core', 'sparseCheckout', 'true')
    info_file = open(os.path.join(git_info_folder, 'sparse-checkout'), 'w')
    s = ''
    for folder_str in git_input['data_file_folders']:
        s = folder_str + '\n' + s
        info_file.write(s[:-1])
        info_file.close()
    fetch_kwargs = {'depth': 1}
    origin.fetch('master', **fetch_kwargs)
    origin.pull(origin.refs[0].remote_head)


def rename_files(fldr):
    new_root_fldr = fldr + '_renamed'
    clean_up_renamed_dir(new_root_fldr)
    copy_directory_content(fldr, new_root_fldr)
    replace_string_in_file_names_in_tree(new_root_fldr, '%', '_')
    replace_string_in_file_names_in_tree(new_root_fldr, '.profile', '.profile.xml')


def replace_string_in_file_names_in_tree(base_fldr, from_chr, to_chr):
    sub_dirs = [x[0] for x in os.walk(base_fldr)]
    for sub_dir in sub_dirs:
        files = os.walk(sub_dir).next()[2]
        if len(files) > 0:
            for f in files:
                to_file = os.path.join(sub_dir, f)
                new_name = to_file.replace(from_chr, to_chr)
                os.rename(to_file, new_name)


def clean_up_renamed_dir(fldr):
        if os.path.exists(fldr):
            shutil.rmtree(fldr)
        os.makedirs(fldr)


def copy_and_rename_folders_a(dirs):
    for sub_dir in dirs:
        new_name = sub_dir + '_renamed'
        if not os.path.exists(new_name):
            os.makedirs(new_name)
        copy_directory_content(sub_dir, new_name)


def copy_directory_content(src, dst):
    os.chdir(dst)
    dir_list = os.listdir(src)
    nom = src + '.txt'
    fit_x = open(nom, 'w')

    for item in dir_list:
        fit_x.write("%s\n" % item)

    fit_x.close()

    f = open(nom, 'r')
    for line in f.readlines():
        if "." in line:
            shutil.copy(src+'/'+line[:-1], dst+'/'+line[:-1])
        else:
            if not os.path.exists(dst+'/'+line[:-1]):
                os.makedirs(dst+'/'+line[:-1])
                copy_directory_content(src + '/' + line[:-1], dst + '/' + line[:-1])
            copy_directory_content(src + '/' + line[:-1], dst + '/' + line[:-1])
    f.close()
    os.remove(nom)
    os.chdir('..')


def create_renamed_folder(folder):
    target_folder = os.path.join(folder, '_renamed')
    if not os.path.exists(target_folder):
        os.makedirs(target_folder, 0)
    return target_folder


get_files()

for folder in git_input['data_file_folders']:
    rename_files(os.path.join(git_input['repo_dir'], folder))
