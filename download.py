#!/usr/bin/env python
'''
This program is used to download all the fsl format files from
TrackOn XNAT: https://xnat.hdni.org/xnat.
These fsl files where converted from DWI_QCed.nrrd files to
DWI_QCed.nii.gz, DWI_QCed.bval, and DWI_QCed.bvec files DWIConvert program.

Created on Jan 3, 2013

@author: Chen Yang
@email: chen-yang@uiowa.edu

'''
import os
import re
import argparse
import getpass
from XNAT import get_XNAT

def get_fsl_dict(fsl_file='2012DWIQCed_nrrd_to_fsl_list.txt'):
    """
    (str) -> dict

    Return a dcitionary of DWI QCed fsl files.

    """
    fsl_dict = {}
    with open(fsl_file, 'rU') as fl:
        for f in fl:
            fs = f.split(',')
            fsl_dict[fs[0]] = eval(','.join(fs[1:]))
    return fsl_dict


def download_fsl_file(XNAT, fsl_dict,
                      resource_folder='2012DWI',
                      dest_folder='/scratch/DWIConvert20120919/'):
    """
    (XNAT instance, dict, string,string) -> files in the dest folder

    Download all the given file from XNAT to the dest folder.

    """
    for k, v in fsl_dict.items():
        session = XNAT.select.project(v[0]).subject(v[1]).experiment(v[2])
        session.resource(resource_folder).file(k).get(dest_folder + k)


def verify_download(dest):
    """
    (string of path for the downloaded files) -> number

    Check and return how many files have been downloaded in the given list.

    >>>verify_download('/scratch/DWIConvert20120919/')
    2280

    """
    count = 0
    for f in os.listdir(dest):
        if re.search('.*(?:.nii.gz|.bval|.bvec)', f):
            print f
            count += 1
    return count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description="This program is used to download QCed fsl files from XNAT.")
    parser.add_argument('-u', '--user', action='store', dest='username',
                        help='XNAT Account', required=True)
    parser.add_argument('-p', '--password', action='store', dest='password', default='missing',
                         help='password')
    parser.add_argument('-f', '--output_folder', action='store',
                        dest='output_folder', default='/scratch/DWIConvert20120919/',
                         help='destination folder for downloaded files')
    parser.add_argument('-c', '--xnat_cache', action='store', dest='xnat_cache',
                        default='/scratch/DWIConvert20120919/')

    args = parser.parse_args()

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    if args.password == 'missing':
        args.password = getpass.getpass("Enter password for " + args.username + ": ")

    XNAT = get_XNAT(username=args.username, password=args.password, xnat_cache=args.xnat_cache)
    fsl_dict = get_fsl_dict()
    download_fsl_file(XNAT, fsl_dict, dest_folder=args.output_folder)

    print 'Checking downloads......'

    # check how many files have been downloaded
    num_downloaded = verify_download(args.output_folder)
    print '{0} out of {1} files have been successfully downloaded!'.format(num_downloaded, len(fsl_dict))
    pass



