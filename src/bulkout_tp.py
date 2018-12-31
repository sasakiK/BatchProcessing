import os
import sys
import pandas as pd

def formatGBtoB(arg):
    # arg : "1GB" - "100GB" character
    # return : target filesize
    num = int(arg.split("G")[0])
    if arg.find("G")>=1:
        return 1073741824 * num
    else:
        return "target file size is too small"

if __name__ == '__main__':

    os.chdir("/home/sskk/BatchProcessing/")

    # load df
    df = pd.read_csv("data/breast-cancer-wisconsin.csv", header=None)
    df.columns = ["ID"] + ["V" + str(n) for n in range(len(df.columns)-1)]

    # put sample csv
    args_filename = sys.argv[2]
    df.to_csv("data/" + args_filename, index=False)

    # get commancline flag
    args = sys.argv[1]
    target_filesize = formatGBtoB(args)

    # bulkout csv
    df_appended = df.append(df).append(df).append(df).append(df)
    while os.stat("data/" + args_filename).st_size<=target_filesize:
        df_appended.to_csv("data/" + args_filename, mode='a', header=False)
    print("process is done ...")
