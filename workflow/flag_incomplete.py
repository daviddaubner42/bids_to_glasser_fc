import os

rawdir = "/data/cephfs-2/unmirrored/groups/ritter/MR_processing/HCP-EP/HCP-EP_2025/HCPEP2025-full_dataset/2026"
outdir = "/data/cephfs-2/unmirrored/groups/ritter/MR_processing/HCP-EP/HCP-EP_2025/HCPEP2025-full_dataset/derivatives"

for fname in os.listdir(os.path.join(rawdir, "imagingcollection01")):
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "T1w_MPR", f"{fname}_T1w_MPR.nii.gz")):
    #     print(fname[:4], " no T1w")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "T2w_SPC", f"{fname}_T2w_SPC.nii.gz")):
    #     print(fname[:4], " no T2w")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST1_AP", f"{fname}_rfMRI_REST1_AP.nii.gz")):
    #     print(fname[:4], " no fMRI 1AP")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST1_AP", f"{fname}_rfMRI_REST1_AP_SBRef.nii.gz")):
    #     print(fname[:4], " no fMRI 1AP sbref")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST1_PA", f"{fname}_rfMRI_REST1_PA.nii.gz")):
    #     print(fname[:4], " no fMRI 1PA")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST1_PA", f"{fname}_rfMRI_REST1_PA_SBRef.nii.gz")):
    #     print(fname[:4], " no fMRI 1PA sbref")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST2_AP", f"{fname}_rfMRI_REST2_AP.nii.gz")):
    #     print(fname[:4], " no fMRI 2AP")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST2_AP", f"{fname}_rfMRI_REST2_AP_SBRef.nii.gz")):
    #     print(fname[:4], " no fMRI 2AP sbref")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST2_PA", f"{fname}_rfMRI_REST2_PA.nii.gz")):
    #     print(fname[:4], " no fMRI 2PA")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST2_PA", f"{fname}_rfMRI_REST2_PA_SBRef.nii.gz")):
    #     print(fname[:4], " no fMRI 2PA sbref")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST1_AP", f"{fname}_SpinEchoFieldMap1_AP.nii.gz")):
    #     print(fname[:4], " no echo field map 1 AP in rfMRI_REST1_AP")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST1_AP", f"{fname}_SpinEchoFieldMap1_PA.nii.gz")):
    #     print(fname[:4], " no echo field map 1 PA in rfMRI_REST1_AP")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST2_AP", f"{fname}_SpinEchoFieldMap2_AP.nii.gz")):
    #     print(fname[:4], " no echo field map 1 AP in rfMRI_REST2_AP")
    # if not os.path.exists(os.path.join(rawdir, "imagingcollection01", fname, "unprocessed", "rfMRI_REST2_AP", f"{fname}_SpinEchoFieldMap2_PA.nii.gz")):
    #     print(fname[:4], " no echo field map 1 PA in rfMRI_REST2_AP")
    if not (os.path.exists(os.path.join(outdir, "xcp_d", f"sub-{fname[:4]}", "ses-1", "func", f"sub-{fname[:4]}_ses-1_task-rest_dir-AP_space-fsLR_seg-Glasser_den-91k_stat-pearsoncorrelation_boldmap.pconn.nii"))
    and os.path.exists(os.path.join(outdir, "xcp_d", f"sub-{fname[:4]}", "ses-1", "func", f"sub-{fname[:4]}_ses-1_task-rest_dir-PA_space-fsLR_seg-Glasser_den-91k_stat-pearsoncorrelation_boldmap.pconn.nii"))
    and os.path.exists(os.path.join(outdir, "xcp_d", f"sub-{fname[:4]}", "ses-2", "func", f"sub-{fname[:4]}_ses-2_task-rest_dir-AP_space-fsLR_seg-Glasser_den-91k_stat-pearsoncorrelation_boldmap.pconn.nii"))
    and os.path.exists(os.path.join(outdir, "xcp_d", f"sub-{fname[:4]}", "ses-2", "func", f"sub-{fname[:4]}_ses-2_task-rest_dir-PA_space-fsLR_seg-Glasser_den-91k_stat-pearsoncorrelation_boldmap.pconn.nii"))):
        print(f"{fname[:4]} - Incomplete processing")
    print('-------------------------')