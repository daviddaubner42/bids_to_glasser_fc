import os
import argparse

parser = argparse.ArgumentParser(description="Rename the files in this directory from ses-1 to ses-2")
parser.add_argument("--anat_dir", type=str, help="The path to the anat directory in ses-2")
args = parser.parse_args()

anat_dir = args.anat_dir

for f in os.listdir(anat_dir):
    if f.startswith("sub-"):
        new_name = f.replace("ses-1", "ses-2")
        os.rename(f"{anat_dir}/{f}", f"{anat_dir}/{new_name}")
