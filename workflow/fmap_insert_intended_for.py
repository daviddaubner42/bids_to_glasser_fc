import os
import json
import argparse

parser = argparse.ArgumentParser(description="Insert the IntendeFor attribute to fmap json sidecar.")
parser.add_argument("--subid", type=str, help="ID of the subject to be converted (without the 'sub-' prefix)")
parser.add_argument("--target_dir", type=str, help="Path to BIDS folder.")
args = parser.parse_args()

bids_dir = args.target_dir
subdir = f"sub-{args.subid}"

os.chmod(os.path.join(bids_dir, subdir, "ses-1", "fmap", f"{subdir}_ses-1_task-rest_dir-AP_epi.json"), 0o664)
with open(os.path.join(bids_dir, subdir, "ses-1", "fmap", f"{subdir}_ses-1_task-rest_dir-AP_epi.json"), 'r') as f:
    data = json.load(f)
    data["IntendedFor"] = f"bids::{subdir}/ses-1/func/{subdir}_ses-1_task-rest_dir-AP_bold.nii.gz"
    f.close()
with open(os.path.join(bids_dir, subdir, "ses-1", "fmap", f"{subdir}_ses-1_task-rest_dir-AP_epi.json"), "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)
    f.close()

os.chmod(os.path.join(bids_dir, subdir, "ses-1", "fmap", f"{subdir}_ses-1_task-rest_dir-PA_epi.json"), 0o664)
with open(os.path.join(bids_dir, subdir, "ses-1", "fmap", f"{subdir}_ses-1_task-rest_dir-PA_epi.json"), 'r') as f:
    data = json.load(f)
    data["IntendedFor"] = f"bids::{subdir}/ses-1/func/{subdir}_ses-1_task-rest_dir-PA_bold.nii.gz"
    f.close()
with open(os.path.join(bids_dir, subdir, "ses-1", "fmap", f"{subdir}_ses-1_task-rest_dir-PA_epi.json"), "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)
    f.close()

os.chmod(os.path.join(bids_dir, subdir, "ses-2", "fmap", f"{subdir}_ses-2_task-rest_dir-AP_epi.json"), 0o664)
with open(os.path.join(bids_dir, subdir, "ses-2", "fmap", f"{subdir}_ses-2_task-rest_dir-AP_epi.json"), 'r') as f:
    data = json.load(f)
    data["IntendedFor"] = f"bids::{subdir}/ses-2/func/{subdir}_ses-2_task-rest_dir-AP_bold.nii.gz"
    f.close()
with open(os.path.join(bids_dir, subdir, "ses-2", "fmap", f"{subdir}_ses-2_task-rest_dir-AP_epi.json"), "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)
    f.close()

os.chmod(os.path.join(bids_dir, subdir, "ses-2", "fmap", f"{subdir}_ses-2_task-rest_dir-PA_epi.json"), 0o664)
with open(os.path.join(bids_dir, subdir, "ses-2", "fmap", f"{subdir}_ses-2_task-rest_dir-PA_epi.json"), 'r') as f:
    data = json.load(f)
    data["IntendedFor"] = f"bids::{subdir}/ses-2/func/{subdir}_ses-2_task-rest_dir-PA_bold.nii.gz"
    f.close()
with open(os.path.join(bids_dir, subdir, "ses-2", "fmap", f"{subdir}_ses-2_task-rest_dir-PA_epi.json"), "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)
    f.close()

# os.chmod(os.path.join(bids_dir, subdir, "fmap", f"{subdir}_magnitude2.json"), 0o664)
# with open(os.path.join(bids_dir, subdir, "fmap", f"{subdir}_magnitude2.json"), 'r') as f:
#     data = json.load(f)
#     data["IntendedFor"] = f"bids::{subdir}/func/{subdir}_task-rest_bold.nii.gz"
#     f.close()
# with open(os.path.join(bids_dir, subdir, "fmap", f"{subdir}_magnitude2.json"), "w") as f:
#     json.dump(data, f, indent=4, sort_keys=True)
#     f.close()

# os.chmod(os.path.join(bids_dir, subdir, "fmap", f"{subdir}_phasediff.json"), 0o664)
# with open(os.path.join(bids_dir, subdir, "fmap", f"{subdir}_phasediff.json"), 'r') as f:
#     data = json.load(f)
#     data["IntendedFor"] = f"bids::{subdir}/func/{subdir}_task-rest_bold.nii.gz"
#     f.close()
# with open(os.path.join(bids_dir, subdir, "fmap", f"{subdir}_phasediff.json"), "w") as f:
#     json.dump(data, f, indent=4, sort_keys=True)
#     f.close()