#!/usr/bin/python
import os
import urllib
import zipfile
import shutil


def zip_downloader(file_url, file_path):
    urllib.urlretrieve(file_url, file_path)


def github_repo_downloader(repo_url, file_path):
    '''
    :type repo_url: str
    '''
    zip_downloader(repo_url, file_path)


def delete_temporary_files(path_to_script_directory=None):
    if not path_to_script_directory:
        path_to_script_directory = os.path.dirname(os.path.realpath(__file__))
    files_to_remove = ["bloat-master", "webtreemap-gh-pages"]
    for e in files_to_remove:
        shutil.rmtree(os.path.join(path_to_script_directory, e))
    os.remove(os.path.join(path_to_script_directory, "bloat-repo.zip"))
    os.remove(os.path.join(path_to_script_directory, "webtreemap-repo.zip"))


def get_rl_bloat_files(path_to_script_directory=None):
    if not path_to_script_directory:
        path_to_script_directory = os.path.dirname(os.path.realpath(__file__))
    rl_bloat_link = "https://github.com/rainlabs-eu/bloat.git"
    rl_bloat_link = rl_bloat_link.replace(".git", "/archive/master.zip")
    rl_bloat_zip_path = os.path.join(path_to_script_directory, "bloat-repo.zip")
    github_repo_downloader(rl_bloat_link, rl_bloat_zip_path)
    with zipfile.ZipFile(rl_bloat_zip_path, 'r') as rl_bloat_zip_file:
        rl_bloat_zip_file.extract("bloat-master/bloat.py", path_to_script_directory)
        rl_bloat_zip_file.extract("bloat-master/index.html", path_to_script_directory)
    shutil.copy(os.path.join(path_to_script_directory, "bloat-master/bloat.py"), os.path.join(path_to_script_directory, "bloat.py"))


def get_rl_webtreemap_files(path_to_script_directory=None):
    if not path_to_script_directory:
        path_to_script_directory = os.path.dirname(os.path.realpath(__file__))
    rl_webtreemap_link = "https://github.com/rainlabs-eu/webtreemap.git"
    rl_webtreemap_link = rl_webtreemap_link.replace(".git", "/archive/gh-pages.zip")
    rl_webtreemap_zip_path = os.path.join(path_to_script_directory, "webtreemap-repo.zip")
    github_repo_downloader(rl_webtreemap_link, rl_webtreemap_zip_path)
    with zipfile.ZipFile(rl_webtreemap_zip_path, 'r') as rl_bloat_zip_file:
        rl_bloat_zip_file.extract("webtreemap-gh-pages/webtreemap.css", path_to_script_directory)
        rl_bloat_zip_file.extract("webtreemap-gh-pages/webtreemap.js", path_to_script_directory)


def make_zip_file(path_to_script_directory):
    if not path_to_script_directory:
        path_to_script_directory = os.path.dirname(os.path.realpath(__file__))
    bloat_folder_path = os.path.join(path_to_script_directory, "bloat")
    bloat_zip = zipfile.ZipFile(bloat_folder_path + ".zip", 'w')
    bloat_zip.write(os.path.join(path_to_script_directory, "bloat-master/index.html"), "index.html")
    bloat_zip.write(os.path.join(path_to_script_directory, "webtreemap-gh-pages/webtreemap.css"), "webtreemap\\webtreemap.css")
    bloat_zip.write(os.path.join(path_to_script_directory, "webtreemap-gh-pages/webtreemap.js"), "webtreemap\\webtreemap.js")
    bloat_zip.close()


if __name__ == "__main__":
    path_to_script_directory = os.path.dirname(os.path.realpath(__file__))
    get_rl_bloat_files(path_to_script_directory)
    get_rl_webtreemap_files(path_to_script_directory)
    make_zip_file(path_to_script_directory)
    delete_temporary_files(path_to_script_directory)
