BIDSifyHCP

This tool automatically converts data from the Human Connectome Project (HCP) standard to the Brain Imaging Data Standard (BIDS). 

For this tool to work in your environment, you will need to install the required packages (see: BIDSifyHCP/requirements.txt)
and you will need to create your own ".env" file. 
For this you can use the provided "dotenv_template" and just adapt the follwing:
- The pre_source_dir should be set to where the HCP MR data is saved in a structue complying with the HCP standard - e.g. ".../imagingcollection01"
- The target_dir is where the BIDS formatted data will be saved - e.g. ".../BIDSified"

You can then run the code using the command /path/to/python /path/to/main.py

This tool will
1. create the BIDS directory structure for each subject,
2. then it will copy the necessary files from the HCP data to the BIDS directory structure. 
3. Afterwards the files will be renamed according to the BIDS file naming specifications. 
4. Finally the pipeline will loop through all the subject folders in the pre_source_dir.

Please note that this tool is set up to convert the HCP MR data of the following types to the BIDS format: T1 and T2 from one session as well as resting state fMRI from two sessions.
The output will be structured as follows:

```
sub-{subject_id}/
├── ses-1/
│   ├── anat/
│   ├── fmap/
│   └── func/
└── ses-2/
    ├── fmap/
    └── func/
```

This tool also includes a non-sensitive test dataset enabeling you to get hands-on right away without the need to aquire additional data. 

If you need to convert other types of data, you can adapt this tool according to your needs due to its modular structure.

If the requirements are satisfied, you are ready to go. Just run main.py and the BIDS formatted data will be saved in the target directory.
    
I hope this tool will be useful for you. 
    
To make the output of this conversion fully BIDS compliant, you may need to manually need to add a "dataset_description.json" file e.g.: {"Name": "Example dataset", "BIDSVersion": "1.0.2"} to the root of the BIDS directory.
Further details on BIDS can be found here: https://bids-specification.readthedocs.io/en/stable/
and for more information on the HCP please refer to: https://www.humanconnectome.org

#happyBIDSifying

Authors: 
Christoph V. M. Huettl, Luise da Costa Zemsch, Leon Martin, Rico A. Schmitt, Michael Schirner and Petra Ritter

Copyright © 2025 Charité Universitätsmedizin Berlin.
