import subprocess
import os

xcp_dir = "/data/cephfs-1/scratch/groups/ritter/users/dada15_c/HCP-EP/derivatives_03_26/xcp_d"

destination_dir = "/data/cephfs-2/unmirrored/groups/ritter/MR_processing/HCP-EP/derivatives_2026/xcp_d"

subids = ['4004', '4022', '1020', '3001', '1104', '1094', '1065', '1075', '2049', '2045', '1040', '3039', '4063', '1073', '4038', '4072', '1083', '2029', '4075', '1043', '1027', '1037', '4028', '1015', '4050', '2004', '1084', '3022', '4014', '1074', '1095', '1076', '1077', '4010', '1033', '1072', '3028', '1028', '1034', '1093', '1089', '1031', '3011', '2020', '1009', '1038', '4074', '4049', '1079', '4011', '1099', '1048', '1024', '4088', '2052', '4002', '2042', '4091', '1078', '3017', '1064', '3002', '2040', '2012', '1029', '2028', '1080', '1098', '4048', '1025', '1071', '2001', '2033', '1003', '1010', '3032', '4003', '4036', '1035', '1066', '1070', '4029', '4059', '1056', '1044', '1105', '1050', '2005', '4030', '1018', '1036', '4027', '1026', '4006', '2019', '4047', '4071', '4037', '3009', '1060', '1047', '2044', '4018', '1082', '1021', '2015', '4065', '3029', '2010', '4057', '2016', '1019', '4052', '4066', '2065', '1051', '3034', '2008', '1054', '3025', '1061', '1002', '1069', '2041', '4015', '1053', '4012', '1004', '2007', '4035', '3026', '1091', '1030', '1032', '4031', '1041', '1085', '1057', '4069', '3027', '2031', '1067', '3035', '1001', '1087', '2006', '1086', '1013', '2023', '1045', '3031', '1012', '2062', '1039', '4053', '1052', '1088', '4024', '4005', '1006', '2022', '4023', '4064', '1017']

for subid in subids:
    os.makedirs(f"{destination_dir}/sub-{subid}/ses-1/func", exist_ok=True)
    os.makedirs(f"{destination_dir}/sub-{subid}/ses-2/func", exist_ok=True)

    subprocess.run(f"cp {xcp_dir}/sub-{subid}/ses-1/func/sub-{subid}_ses-1_task-rest_dir-AP_space-fsLR_seg-Glasser_den-91k_stat-mean_timeseries.ptseries.nii {destination_dir}/sub-{subid}/ses-1/func/sub-{subid}_ses-1_task-rest_dir-AP_space-fsLR_seg-Glasser_den-91k_stat-mean_timeseries.ptseries.nii",
        shell = True, executable="/bin/bash")
    subprocess.run(f"cp {xcp_dir}/sub-{subid}/ses-1/func/sub-{subid}_ses-1_task-rest_dir-PA_space-fsLR_seg-Glasser_den-91k_stat-mean_timeseries.ptseries.nii {destination_dir}/sub-{subid}/ses-1/func/sub-{subid}_ses-1_task-rest_dir-PA_space-fsLR_seg-Glasser_den-91k_stat-mean_timeseries.ptseries.nii",
        shell = True, executable="/bin/bash")
    subprocess.run(f"cp {xcp_dir}/sub-{subid}/ses-2/func/sub-{subid}_ses-2_task-rest_dir-AP_space-fsLR_seg-Glasser_den-91k_stat-mean_timeseries.ptseries.nii {destination_dir}/sub-{subid}/ses-2/func/sub-{subid}_ses-2_task-rest_dir-AP_space-fsLR_seg-Glasser_den-91k_stat-mean_timeseries.ptseries.nii",
        shell = True, executable="/bin/bash")
    subprocess.run(f"cp {xcp_dir}/sub-{subid}/ses-2/func/sub-{subid}_ses-2_task-rest_dir-PA_space-fsLR_seg-Glasser_den-91k_stat-mean_timeseries.ptseries.nii {destination_dir}/sub-{subid}/ses-2/func/sub-{subid}_ses-2_task-rest_dir-PA_space-fsLR_seg-Glasser_den-91k_stat-mean_timeseries.ptseries.nii",
        shell = True, executable="/bin/bash")
    
    subprocess.run(f"cp {xcp_dir}/sub-{subid}/ses-1/func/sub-{subid}_ses-1_task-rest_dir-AP_space-fsLR_seg-Glasser_den-91k_stat-pearsoncorrelation_boldmap.json {destination_dir}/sub-{subid}/ses-1/func/sub-{subid}_ses-1_task-rest_dir-AP_space-fsLR_seg-Glasser_den-91k_stat-pearsoncorrelation_boldmap.json",
        shell = True, executable="/bin/bash")
    subprocess.run(f"cp {xcp_dir}/sub-{subid}/ses-1/func/sub-{subid}_ses-1_task-rest_dir-PA_space-fsLR_seg-Glasser_den-91k_stat-pearsoncorrelation_boldmap.json {destination_dir}/sub-{subid}/ses-1/func/sub-{subid}_ses-1_task-rest_dir-PA_space-fsLR_seg-Glasser_den-91k_stat-pearsoncorrelation_boldmap.json",
        shell = True, executable="/bin/bash")
    subprocess.run(f"cp {xcp_dir}/sub-{subid}/ses-2/func/sub-{subid}_ses-2_task-rest_dir-AP_space-fsLR_seg-Glasser_den-91k_stat-pearsoncorrelation_boldmap.json {destination_dir}/sub-{subid}/ses-2/func/sub-{subid}_ses-2_task-rest_dir-AP_space-fsLR_seg-Glasser_den-91k_stat-pearsoncorrelation_boldmap.json",
        shell = True, executable="/bin/bash")
    subprocess.run(f"cp {xcp_dir}/sub-{subid}/ses-2/func/sub-{subid}_ses-2_task-rest_dir-PA_space-fsLR_seg-Glasser_den-91k_stat-pearsoncorrelation_boldmap.json {destination_dir}/sub-{subid}/ses-2/func/sub-{subid}_ses-2_task-rest_dir-PA_space-fsLR_seg-Glasser_den-91k_stat-pearsoncorrelation_boldmap.json",
        shell = True, executable="/bin/bash")
    
subprocess.run(f"cp -r {xcp_dir}/atlases/ {destination_dir}/atlases",
    shell=True, executable="/bin/bash")