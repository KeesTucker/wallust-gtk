import os
import shutil
import subprocess

from scripts.patches import recreate_xfwm4_assets
from scripts.recolor import recolor
from scripts.utils import replacetext, zip_multiple_folders
from scripts.var import repo_dir, src_dir, theme_name, work_dir
from scripts.wallust import WallustDark, WallustLight

def create_theme(style: str, dest: str, link: bool = False, name: str = theme_name, size: str = "standard", tweaks=[], zip = False, recreate_assets = False) -> None:

    try:
        os.makedirs(dest)  # Create our destination directory
    except FileExistsError:
        pass

    if recreate_assets:
        recreate_xfwm4_assets()

    theme = WallustDark
    if style == "light":
        theme = WallustLight
    recolor(theme)
    install_cmd: str = f"./install.sh -c {style} -s {size} -n {name} -d {dest} -t default"
    if tweaks:
        install_cmd += f" --tweaks {' '.join([tweak for tweak in tweaks])}"
    shutil.rmtree(f"{repo_dir}/chrome", ignore_errors=True)
    shutil.copytree(f"{src_dir}/other/firefox/chrome", f"{repo_dir}/chrome")
    os.chdir(work_dir)
    subprocess.call("./build.sh", shell=True) # Rebuild all scss
    subprocess.call(install_cmd, shell=True) # Install the theme globally for you
    subprocess.call("git reset --hard HEAD", shell=True)  # reset colloid repo to original state

    try:
        # Rename colloid generated files as per soggy-wallust
        new_filename = dest + \
            f"/{name}-{size.capitalize()}-{style}"
        filename = f"{name}"
        filename += f"-{style.capitalize()}"
        if size == 'compact':
            filename += '-Compact'
        try:
            shutil.rmtree(new_filename + '-hdpi')
            shutil.rmtree(new_filename + '-xhdpi')
            shutil.rmtree(new_filename)
        except:
            pass
        os.rename(dest + "/" + filename + '-hdpi',
                new_filename + '-hdpi')
        os.rename(dest + "/" + filename + '-xhdpi',
                new_filename + '-xhdpi')
        os.rename(dest + "/" + filename, new_filename)
        replacetext(new_filename + '/index.theme', filename, new_filename.split("/")[-1])
        print("Successfully renamed file")
    except Exception as e:
        print("Failed to rename the files due to:", e)

    if link:
        try:
            # Attempte relinking all the libadvaita files
            subprocess.call(
                'rm -rf "${HOME}/.config/gtk-4.0/"{assets,gtk.css,gtk-dark.css}', shell=True)
            HOME = os.path.expanduser('~')

            try:
                os.makedirs(f"{HOME}/.config/gtk-4.0")
            except FileExistsError:
                pass
            os.symlink(f"{new_filename}/gtk-4.0/assets",
                    f"{HOME}/.config/gtk-4.0/assets")
            os.symlink(f"{new_filename}/gtk-4.0/gtk.css",
                    f"{HOME}/.config/gtk-4.0/gtk.css")
            os.symlink(f"{new_filename}/gtk-4.0/gtk-dark.css",
                    f"{HOME}/.config/gtk-4.0/gtk-dark.css")
            print("Successfully created symlinks for libadvaita")
        except Exception as e:
            print("Failed to link due to :", e)

    if zip:
        foldernames = [new_filename, new_filename + '-xhdpi', new_filename + '-hdpi']
        zip_multiple_folders(foldernames, new_filename + ".zip", not link)
