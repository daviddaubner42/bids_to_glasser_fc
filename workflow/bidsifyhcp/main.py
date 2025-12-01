import os
import logging
# from utils.import_data import pre_source_dir, target_dir
from utils.create_bids_structure import create_bids_structure
from utils.copy_rename import copy_and_rename_files
from utils.logger import logger
# from dotenv import load_dotenv

import argparse

parser = argparse.ArgumentParser(description="BIDSify and HCP dataset.")
parser.add_argument("--hcp_dir", type=str, help="Path to folder containing the HCP data.")
parser.add_argument("--target_dir", type=str, help="Path to folder where the new BIDS dataset should be stored.")
args = parser.parse_args()

pre_source_dir = args.hcp_dir
target_dir = args.target_dir


# List all the subject folders in the pre_source_dir 
# (disregarding the manifest folder, which does not contain subject data)
list_dir = [d for d in os.listdir(pre_source_dir) if not d.startswith('.') and d != 'manifest']

for l in list_dir:
    source_dir = os.path.join(pre_source_dir, l, 'unprocessed')


    subject_id = l[:4]
    # print(f"Extracted subject ID: {subject_id}")
    logging.debug(f"Extracted subject ID: {subject_id}")

    # Define the files to copy from the HCP subject files
    # The files are listed in the order: json files first, then nifti files
    files_to_copy_anat = [
        f'{subject_id}_01_MR_T1w_MPR.json', f'{subject_id}_01_MR_T2w_SPC.json',
        f'{subject_id}_01_MR_T1w_MPR.nii.gz', f'{subject_id}_01_MR_T2w_SPC.nii.gz'
    ]

    files_to_copy_fmap = [
        f'{subject_id}_01_MR_SpinEchoFieldMap1_AP.json', f'{subject_id}_01_MR_SpinEchoFieldMap1_PA.json',
        f'{subject_id}_01_MR_SpinEchoFieldMap1_AP.nii.gz', f'{subject_id}_01_MR_SpinEchoFieldMap1_PA.nii.gz'
    ]

    files_to_copy_func = [
        f'{subject_id}_01_MR_rfMRI_REST1_AP.json', f'{subject_id}_01_MR_rfMRI_REST1_PA.json',
        f'{subject_id}_01_MR_rfMRI_REST1_AP.nii.gz', f'{subject_id}_01_MR_rfMRI_REST1_PA.nii.gz',
        f'{subject_id}_01_MR_rfMRI_REST1_AP_SBRef.json', f'{subject_id}_01_MR_rfMRI_REST1_PA_SBRef.json',
        f'{subject_id}_01_MR_rfMRI_REST1_AP_SBRef.nii.gz', f'{subject_id}_01_MR_rfMRI_REST1_PA_SBRef.nii.gz'
    ]

    files_to_copy_fmap_ses2 = [
        f'{subject_id}_01_MR_SpinEchoFieldMap2_AP.json', f'{subject_id}_01_MR_SpinEchoFieldMap2_PA.json',
        f'{subject_id}_01_MR_SpinEchoFieldMap2_AP.nii.gz', f'{subject_id}_01_MR_SpinEchoFieldMap2_PA.nii.gz'
    ]

    files_to_copy_func_ses2 = [
        f'{subject_id}_01_MR_rfMRI_REST2_AP.json', f'{subject_id}_01_MR_rfMRI_REST2_PA.json',
        f'{subject_id}_01_MR_rfMRI_REST2_AP.nii.gz', f'{subject_id}_01_MR_rfMRI_REST2_PA.nii.gz',
        f'{subject_id}_01_MR_rfMRI_REST2_AP_SBRef.json', f'{subject_id}_01_MR_rfMRI_REST2_PA_SBRef.json',
        f'{subject_id}_01_MR_rfMRI_REST2_AP_SBRef.nii.gz', f'{subject_id}_01_MR_rfMRI_REST2_PA_SBRef.nii.gz'
    ]

    # Define the rename maps:  old_name (HCP): new_name (BIDS)
    anat_rename_map = {
        f'{subject_id}_01_MR_T1w_MPR.json': f'sub-{subject_id}_ses-1_T1w.json',
        f'{subject_id}_01_MR_T2w_SPC.json': f'sub-{subject_id}_ses-1_T2w.json',
        f'{subject_id}_01_MR_T1w_MPR.nii.gz': f'sub-{subject_id}_ses-1_T1w.nii.gz',
        f'{subject_id}_01_MR_T2w_SPC.nii.gz': f'sub-{subject_id}_ses-1_T2w.nii.gz'
    }

    fmap_rename_map_ses1 = {
        f'{subject_id}_01_MR_SpinEchoFieldMap1_AP.json': f'sub-{subject_id}_ses-1_task-rest_dir-AP_epi.json',
        f'{subject_id}_01_MR_SpinEchoFieldMap1_PA.json': f'sub-{subject_id}_ses-1_task-rest_dir-PA_epi.json',
        f'{subject_id}_01_MR_SpinEchoFieldMap1_AP.nii.gz': f'sub-{subject_id}_ses-1_task-rest_dir-AP_epi.nii.gz',
        f'{subject_id}_01_MR_SpinEchoFieldMap1_PA.nii.gz': f'sub-{subject_id}_ses-1_task-rest_dir-PA_epi.nii.gz'
    }

    func_rename_map_ses1 = {
        f'{subject_id}_01_MR_rfMRI_REST1_AP.json': f'sub-{subject_id}_ses-1_task-rest_dir-AP_bold.json',
        f'{subject_id}_01_MR_rfMRI_REST1_PA.json': f'sub-{subject_id}_ses-1_task-rest_dir-PA_bold.json',
        f'{subject_id}_01_MR_rfMRI_REST1_AP.nii.gz': f'sub-{subject_id}_ses-1_task-rest_dir-AP_bold.nii.gz',
        f'{subject_id}_01_MR_rfMRI_REST1_PA.nii.gz': f'sub-{subject_id}_ses-1_task-rest_dir-PA_bold.nii.gz',
        f'{subject_id}_01_MR_rfMRI_REST1_AP_SBRef.json': f'sub-{subject_id}_ses-1_task-rest_dir-AP_sbref.json',
        f'{subject_id}_01_MR_rfMRI_REST1_PA_SBRef.json': f'sub-{subject_id}_ses-1_task-rest_dir-PA_sbref.json',
        f'{subject_id}_01_MR_rfMRI_REST1_AP_SBRef.nii.gz': f'sub-{subject_id}_ses-1_task-rest_dir-AP_sbref.nii.gz',
        f'{subject_id}_01_MR_rfMRI_REST1_PA_SBRef.nii.gz': f'sub-{subject_id}_ses-1_task-rest_dir-PA_sbref.nii.gz'
    }

    fmap_rename_map_ses2 = {
        f'{subject_id}_01_MR_SpinEchoFieldMap2_AP.json': f'sub-{subject_id}_ses-2_task-rest_dir-AP_epi.json',
        f'{subject_id}_01_MR_SpinEchoFieldMap2_PA.json': f'sub-{subject_id}_ses-2_task-rest_dir-PA_epi.json',
        f'{subject_id}_01_MR_SpinEchoFieldMap2_AP.nii.gz': f'sub-{subject_id}_ses-2_task-rest_dir-AP_epi.nii.gz',
        f'{subject_id}_01_MR_SpinEchoFieldMap2_PA.nii.gz': f'sub-{subject_id}_ses-2_task-rest_dir-PA_epi.nii.gz'
    }

    func_rename_map_ses2 = {
        f'{subject_id}_01_MR_rfMRI_REST2_AP.json': f'sub-{subject_id}_ses-2_task-rest_dir-AP_bold.json',
        f'{subject_id}_01_MR_rfMRI_REST2_PA.json': f'sub-{subject_id}_ses-2_task-rest_dir-PA_bold.json',
        f'{subject_id}_01_MR_rfMRI_REST2_AP.nii.gz': f'sub-{subject_id}_ses-2_task-rest_dir-AP_bold.nii.gz',
        f'{subject_id}_01_MR_rfMRI_REST2_PA.nii.gz': f'sub-{subject_id}_ses-2_task-rest_dir-PA_bold.nii.gz',
        f'{subject_id}_01_MR_rfMRI_REST2_AP_SBRef.json': f'sub-{subject_id}_ses-2_task-rest_dir-AP_sbref.json',
        f'{subject_id}_01_MR_rfMRI_REST2_PA_SBRef.json': f'sub-{subject_id}_ses-2_task-rest_dir-PA_sbref.json',
        f'{subject_id}_01_MR_rfMRI_REST2_AP_SBRef.nii.gz': f'sub-{subject_id}_ses-2_task-rest_dir-AP_sbref.nii.gz',
        f'{subject_id}_01_MR_rfMRI_REST2_PA_SBRef.nii.gz': f'sub-{subject_id}_ses-2_task-rest_dir-PA_sbref.nii.gz'
    }


    # Main Execution

    # Create the BIDS structure
    create_bids_structure(subject_id, target_dir)

    # Define the target subdirectories
    anat_subdir = os.path.join(target_dir, f"sub-{subject_id}", "ses-1", "anat")
    fmap_subdir_ses1 = os.path.join(target_dir, f"sub-{subject_id}", "ses-1", "fmap")
    func_subdir = os.path.join(target_dir, f"sub-{subject_id}", "ses-1", "func")
    fmap_subdir_ses2 = os.path.join(target_dir, f"sub-{subject_id}", "ses-2", "fmap")
    func_subdir_ses2 = os.path.join(target_dir, f"sub-{subject_id}", "ses-2", "func")

    # Copy and rename the files
    print("-------- ANAT --------")
    copy_and_rename_files(source_dir, target_dir, files_to_copy_anat, anat_subdir, anat_rename_map)
    # print("-------- FMAP --------")
    # copy_and_rename_files(source_dir, target_dir, files_to_copy_fmap, fmap_subdir_ses1, fmap_rename_map_ses1)
    print("-------- FUNC --------")
    copy_and_rename_files(source_dir, target_dir, files_to_copy_func, func_subdir, func_rename_map_ses1)
    # print("-------- FMAP-2 --------")
    # copy_and_rename_files(source_dir, target_dir, files_to_copy_fmap_ses2, fmap_subdir_ses2, fmap_rename_map_ses2)
    print("-------- FUNC-2 --------")
    copy_and_rename_files(source_dir, target_dir, files_to_copy_func_ses2, func_subdir_ses2, func_rename_map_ses2)

    logging.debug(f"File copying and renaming completed.")
    #print("File copying and renaming completed.")
    


logging.critical("All subjects have been processed.")