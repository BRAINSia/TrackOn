#!/usr/bin/env python
'''
This program is used to download all the fsl format files from
TrackOn XNAT: https://xnat.hdni.org/xnat.
These fsl files where converted from DWI_QCed.nrrd files to
DWI_QCed.nii.gz, DWI_QCed.bval, and DWI_QCed.bvec files DWIConvert program.

Created on Feb 13, 2013

@author: Chen Yang
@email: chen-yang@uiowa.edu

'''
import os
import argparse
import getpass

from XNAT import get_XNAT

def get_fsl_dict(fsl_file='2012DWI.csv'):
    """
    (str) -> dict

    Return a dcitionary of DWI QCed fsl files.

    """
    fsl_dict = {}
    with open(fsl_file, 'rU') as fl:
        fl.next()
        for f in fl:
            fs = f.split(',')
            value = (fs[0], fs[1], fs[2], fs[3])
            fsl_dict[fs[4].rstrip()] = value
    return fsl_dict



def download_fsl_file(XNAT, fsl_dict,
                      resource_folder='2012DWI',
                      base_output_directory_path='/hjohnson/HDNI/20130214_TEST_DOWNLOAD/'):
    """
    (XNAT instance, dict, string,string) -> files in the dest folder

    Download all the given file from XNAT to the dest folder.

    """
    for k, v in fsl_dict.items():
        resource_folder = eval(v[0])
        proj_path = os.path.join(base_output_directory_path, eval(v[1]))
        if not os.path.exists(proj_path):
            os.mkdir(proj_path)

        subj_path = os.path.join(proj_path, eval(v[2]))
        if not os.path.exists(subj_path):
            os.mkdir(subj_path)

        sess_path = os.path.join(subj_path, eval(v[3]))
        if not os.path.exists(sess_path):
            os.mkdir(sess_path)

        resource_path = os.path.join(sess_path, resource_folder)
        if not os.path.exists(resource_path):
            os.mkdir(resource_path)
        session = XNAT.select.project(eval(v[1])).subject(eval(v[2])).experiment(eval(v[3]))
        try:
            session.resource(resource_folder).file(eval(k)).get(os.path.join(resource_path, eval(k)))
        except IndexError:
            print "Failed to download %s " % resource_path + "/" + eval(k)
            print "Check and download this file manually."
            continue

        print "Download %s" % resource_path + "/" + eval(k)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description="This program is used to download QCed fsl files from XNAT.")
    parser.add_argument('-u', '--user', action='store', dest='username',
                        help='XNAT Account', required=True)
    parser.add_argument('-p', '--password', action='store', dest='password', default='missing',
                         help='password')
    parser.add_argument('-f', '--base_output_directory_path', action='store',
                        dest='base_output_directory_path', default='/hjohnson/HDNI/20130214_TEST_DOWNLOAD/',
                         help='destination folder for downloaded files')
    parser.add_argument('-c', '--xnat_cache', action='store', dest='xnat_cache',
                        default='/hjohnson/HDNI/20130214_TEST_DOWNLOAD/')
    parser.add_argument('-l', '--file_list', action='store', dest='file_list',
                        default='2012DWI.csv')

    args = parser.parse_args()

    if not os.path.exists(args.base_output_directory_path):
        os.makedirs(args.base_output_directory_path)

    if args.password == 'missing':
        args.password = getpass.getpass("Enter password for " + args.username + ": ")

    XNAT = get_XNAT(username=args.username, password=args.password, xnat_cache=args.xnat_cache)
    fsl_dict = get_fsl_dict(args.file_list)
    download_fsl_file(XNAT, fsl_dict, base_output_directory_path=args.base_output_directory_path)

    pass



