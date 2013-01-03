This program is used to download all the fsl format files from 
TrackOn XNAT: https://xnat.hdni.org/xnat.
These fsl files were converted from DWI_QCed.nrrd files to 
DWI_QCed.nii.gz, DWI_QCed.bval, and DWI_QCed.bvec files by using DWIConvert program. 

It will download all the fsl files in the given file 2012DWIQCed_nrrd_to_fsl_list.txt. 


How to Run this program?

Install python 2.7 or 2.6
easy_install pip

sudo pip install --user httplib2
sudo pip install --user pyxnat
sudo pip install --user pydicom

Get a TrackOn XNAT account as following:
1. go to https://xnat.hdni.org/xnat
2. click Register
3. fill the registration form with detailed information
4. wait for the account to be enabled.

git clone https://github.com/healthonrails/TrackOn.git
cd TrackOn

Then run program like this. 

python download.py -u xnat_user_name -p password -f /output_folder_path/ -c /xnat_cache_path/
e.g 
python download.py -u tester -p secret -f /scratch/DWI2012/ -c /scratch/xnat_cache/

This program will download 2280 files in the given file 2012DWIQCed_nrrd_to_fsl_list.txt
to my local machine /scratch/DWI2012/ folder. 

Note the given path and folders like /scratch/DWI2012/ should be created if they does not 
exist before run this program.
XNAT cache path and folders will be created by xnat program too.