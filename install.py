"""
Main script to clone, recolor and install the theme.
Run this from the root of the repo.

Usage:
    python install.py [options]
"""
import argparse
import os
import subprocess

from scripts.create_theme import create_theme
from scripts.var import theme_name, work_dir

parser = argparse.ArgumentParser(description="Soggy Wallust GTK theme")

parser.add_argument("--name", "-n",
                    metavar="theme name",
                    type=str,
                    default=theme_name,
                    dest="name",
                    help="Name of the theme to apply. Defaults to Soggy Wallust")

parser.add_argument("--style", "-s",
                    metavar="Style of the theme",
                    type=str,
                    default="dark",
                    dest="style",
                    choices=["dark", "light"],
                    help="Style variant of the theme. Can be dark or light.")

parser.add_argument("--dest", "-d",
                    metavar="destination",
                    type=str,
                    dest="dest",
                    help="Destination of the files. defaults to releases folder inside the root")

parser.add_argument("--size", "-z",
                    metavar="Size of the theme",
                    type=str,
                    default="standard",
                    dest="size",
                    choices=["standard", "compact"],
                    help="Size variant of the theme. Can be standard or compact")

parser.add_argument("--tweaks",
                    metavar="Colloid specific tweaks",
                    type=str,
                    default=[],
                    nargs="+",
                    dest="tweaks",
                    choices=["black", "rimless", "normal", "float"],
                    help="Some specifc tweaks. like black, rimless, normal buttons")

parser.add_argument("-l", "--link",
                    help="Link advaita themes to our soggy wallust theme",
                    type=bool,
                    default=False,
                    action=argparse.BooleanOptionalAction,
                    dest="link")

parser.add_argument("--zip",
                    help="Zip soggy wallust theme",
                    type=bool,
                    default=False,
                    action=argparse.BooleanOptionalAction,
                    dest="zip")

parser.add_argument("--recreate-asset",
                    help="Recreate assets for xfwm4 and such",
                    type=bool,
                    default=False,
                    action=argparse.BooleanOptionalAction,
                    dest="rec_asset")

args = parser.parse_args()

if args.dest:
    dest = args.dest
elif os.geteuid() == 0: # Sudo
    dest = "/usr/share/themes"
else:
    dest = os.path.expanduser('~') + "/.themes"

if not os.listdir(work_dir):
    subprocess.call("git submodule update --init --recursive", shell=True)

filename = create_theme(args.style, dest, args.link, args.name, args.size, args.tweaks, args.zip, args.rec_asset)
