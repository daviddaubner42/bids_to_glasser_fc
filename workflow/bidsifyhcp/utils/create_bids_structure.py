import os

def create_bids_structure(subject_id, target_dir):
    """
    Create the BIDS directory structure for the given subject.
    """
    os.makedirs(os.path.join(target_dir, f"sub-{subject_id}", "ses-1", "anat"), exist_ok=True)
    os.makedirs(os.path.join(target_dir, f"sub-{subject_id}", "ses-1", "fmap"), exist_ok=True)
    os.makedirs(os.path.join(target_dir, f"sub-{subject_id}", "ses-1", "func"), exist_ok=True)
    os.makedirs(os.path.join(target_dir, f"sub-{subject_id}", "ses-2", "fmap"), exist_ok=True)
    os.makedirs(os.path.join(target_dir, f"sub-{subject_id}", "ses-2", "func"), exist_ok=True)
