import os

rawdir = "/data/cephfs-2/unmirrored/groups/ritter/MR_processing/HCP-EP/HCP-EP_2025/HCPEP2025-full_dataset"

for fname in os.listdir(os.path.join(rawdir, "imagingcollection01")):
    if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "T1w_MPR", f"{fname}_T1w_MPR.nii.gz")):
        print(fname[:4], " no T1w")
    if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST1_AP", f"{fname}_rfMRI_REST1_AP.nii.gz")):
        print(fname[:4], " no fMRI 1AP")
    if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST1_AP", f"{fname}_rfMRI_REST1_AP_SBRef.nii.gz")):
        print(fname[:4], " no fMRI 1AP sbref")
    if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST1_PA", f"{fname}_rfMRI_REST1_PA.nii.gz")):
        print(fname[:4], " no fMRI 1PA")
    if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST1_PA", f"{fname}_rfMRI_REST1_PA_SBRef.nii.gz")):
        print(fname[:4], " no fMRI 1PA sbref")
    if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST2_AP", f"{fname}_rfMRI_REST2_AP.nii.gz")):
        print(fname[:4], " no fMRI 2AP")
    if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST2_AP", f"{fname}_rfMRI_REST2_AP_SBRef.nii.gz")):
        print(fname[:4], " no fMRI 2AP sbref")
    if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST2_PA", f"{fname}_rfMRI_REST2_PA.nii.gz")):
        print(fname[:4], " no fMRI 2PA")
    if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST2_PA", f"{fname}_rfMRI_REST2_PA_SBRef.nii.gz")):
        print(fname[:4], " no fMRI 2PA sbref")
    if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "T1w_MPR", "OTHER_FILES", f"{fname}_SpinEchoFieldMap1_AP.nii.gz")):
        print(fname[:4], " no echo field map 1 AP in T1w")
    if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "T1w_MPR", "OTHER_FILES", f"{fname}_SpinEchoFieldMap1_PA.nii.gz"))
        print(fname[:4], " no echo field map 1 PA in T1w")
    print('-------------------------')