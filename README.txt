This program is used to download all the fsl format files from 
TrackOn XNAT: https://xnat.hdni.org/xnat.
These fsl files were converted from DWI_QCed.nrrd files to 
DWI_QCed.nii.gz, DWI_QCed.bval, and DWI_QCed.bvec files by using DWIConvert program. 

It will download all the fsl files in the given file 2012DWI.csv. 


How to Run this program?

Install python 2.7 or 2.6
easy_install pip

sudo pip install --user httplib2
Install the latest pyxnat. 
git clone https://github.com/pyxnat/pyxnat 
cd pyxnat 
pip install 
sudo pip install --user pydicom

If you have already had a account, then you can skip the following get account steps. 
Get a TrackOn XNAT account as following:
1. go to https://xnat.hdni.org/xnat
2. click Register
3. fill the registration form with detailed information
4. wait for the account to be enabled.

git clone https://github.com/healthonrails/TrackOn.git
cd TrackOn

Then run program like this. 

python download_track_data.py -u xnat_user_name -p password -f /base_output_directory_path/ -c /xnat_cache_directory_path/ -l 2012DWI.csv
e.g 
python download_track_data.py -u tester -p secret -f /hjohnson/HDNI/20130214_TEST_DOWNLOAD/ -c /hjohnson/HDNI/20130214_TEST_DOWNLOAD/

This program will download 2280 files in the given file 2012DWI.csv.
to my local machine /hjohnson/HDNI/20130214_TEST_DOWNLOAD/ folder with the following folder structure.
 /hjohnson/HDNI/20130214_TEST_DOWNLOAD/
 ....HDNI_001
     ....015955315/
         ....015955315_20090622_30/
             ....2012DWI/
                 ....20121019_DTIPrep_HDNI_001_015955315_015955315_20090622_30_DWI_CONCAT_QCed.bval
                 ....20121019_DTIPrep_HDNI_001_015955315_015955315_20090622_30_DWI_CONCAT_QCed.bvec
                 ....20121019_DTIPrep_HDNI_001_015955315_015955315_20090622_30_DWI_CONCAT_QCed.nii.gz

Note the given path and folders like /scratch/DWI2012/ should be created if they does not 
exist before run this program.
XNAT cache path and folders will be created by xnat program too.

The download.py script will download all the file into one folder like  the following structure. 
 /hjohnson/HDNI/20130214_TEST_DOWNLOAD/
 ....20121019_DTIPrep_HDNI_001_015955315_015955315_20090622_30_DWI_CONCAT_QCed.bval
 ....20121019_DTIPrep_HDNI_001_015955315_015955315_20090622_30_DWI_CONCAT_QCed.bvec
 ....20121019_DTIPrep_HDNI_001_015955315_015955315_20090622_30_DWI_CONCAT_QCed.nii.gz
 .....
 
 How to run download.py? 
 
 python download.py -u xnat_user_name -p password -f /output_folder_path/ -c /xnat_cache_path/
 e.g.
 python download.py -u tester -p secret -f /scratch/DWI2012/ -c /scratch/xnat_cache/