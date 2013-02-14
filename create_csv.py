import csv

def fsl_list(fsl_file='2012DWIQCed_nrrd_to_fsl_list.txt'):
    """

    Create a CSV file of 2012DWI files.
    >>>cat 2012DWI_list.csv
    RESOURCE_NAME,SESSION,FILE_PATTERN
    2012DWI,106115590_20120417_30,*.nii.gz
    2012DWI, 106115590_20120417_30,*.bvec
    2012DWI, 106115590_20120417_30,*.bval

    """
    dwi_list = []
    with open(fsl_file, 'rU') as fls:
        dwi_year = '2012DWI'
        for fl in fls:
            fll = fl.split(',')
            sps = eval([','.join(fll[1:])][0].rstrip())
            dwi_list.append([dwi_year, sps[0], sps[1], sps[2], fll[0]])

    return dwi_list


def fsl_csv(fsls, file_name='2012DWI.csv'):

    with open(file_name, 'a') as fn:
        csvwriter = csv.writer(fn, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        header = ['RESOURCE_NAME', 'PROJECT', 'SUBJECT', 'SESSION', 'FILE_PATTERN']
        csvwriter.writerow(header)
        for fsl in fsls:
            csvwriter.writerow(fsl)



if __name__ == "__main__":
    fsls = fsl_list()
    fsl_csv(fsls)
