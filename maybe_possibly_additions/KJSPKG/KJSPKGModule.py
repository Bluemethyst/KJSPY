import requests
import json
import os
import git
import shutil

class KJSPKGScripts():
    def __init__(self, instance_path):
        self.instance_path = instance_path
        self.kjspkg_scripts = {"kjspkg": []}
        
    def install(self, package):
        self.kjspkg_scripts = {"kjspkg": []}
        r = requests.get('https://raw.githubusercontent.com/Modern-Modpacks/kjspkg/main/pkgs.json')
        pkgs = r.json()
        for pkg in pkgs:
            if pkg == package:
                self.kjspkg_scripts["kjspkg"].append(pkgs[pkg])
                requests.put(f"https://tizudev.vercel.app/automatin/api/1025316079226064966/kjspkg?stat=downloads&id={pkg}")
        print(json.dumps(self.kjspkg_scripts, indent=4))
        for link in self.kjspkg_scripts["kjspkg"]:
            # Create a new directory for the package
            repo_path = f'{self.instance_path}/kubejs/kjspkg/{link.split("/")[1]}'
            os.makedirs(repo_path, exist_ok=True)
            # Clone the repository
            git.Repo.clone_from(f'https://github.com/{link}.git', repo_path)
            for folder in ['server_scripts', 'client_scripts', 'startup_scripts', 'assets', 'data']:
                src_folder = os.path.join(repo_path, folder)
                dst_folder = os.path.join(self.instance_path, 'kubejs', folder)
                if os.path.exists(src_folder):
                    for filename in os.listdir(src_folder):
                        shutil.copy(os.path.join(src_folder, filename), dst_folder)
        # Delete the contents of the kjspkg directory
        for filename in os.listdir(f'{self.instance_path}/kubejs/kjspkg'):
            file_path = os.path.join(f'{self.instance_path}/kubejs/kjspkg', filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path) # remove file
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path) # remove directory
            except PermissionError:
                print(f'Permission denied to delete {file_path}. Skipping...')
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')