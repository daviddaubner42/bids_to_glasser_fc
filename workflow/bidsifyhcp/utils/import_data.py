import os
import shutil
import re
import dotenv

#### Define the source and target directories ####

#this path ends with ".../imagingcollection01" and contains all the subject folders e.g.: 1001_01_MR, 1002_01_MR, etc. (e.g.: HCP Early Psychosis Dataset)
pre_source_dir = dotenv.get_key(dotenv.find_dotenv(), "pre_source_dir")

#this path is the target directory where the BIDS formatted data will be saved
target_dir = dotenv.get_key(dotenv.find_dotenv(), "target_dir")