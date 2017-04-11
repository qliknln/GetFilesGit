# The information below is used as input for getting repos from GitHub
#
#   Parameter description:

#    The username for the Bitbucket user
#    'username': 'JohnDoe',

#    Password for the previously specified user
#    'password': 'FooBar',

#    Name of the repository to retrieve
#    'reponame': 'myRepo',

#    Target folder on local drive
#    'local_repo_dir': 'C:\myTestRepo',

#    List of folders that contains files with % in the their names.
#    Files in folders listed here, will have their names changed if the contain a % character. % will be replaced by _
#    'data_file_folders': [
#        'Folder_name1',
#        'Folder_name2,
#        'Folder_name3'

git_input = {
    'git_url': 'bitbucket.org/mycompany/mygit.git',
    'username': 'myusername',
    'password': 'mypassword',
    'repo_dir': 'C:/myTestRepo',
    'data_file_folders': [
        'myRepoFolder/myRepoSubFolder',
        'myRepoFolder1/myRepoSubFolder1',
        'myRepoFolder2/myRepoSubFolder2'
    ]
}
