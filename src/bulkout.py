import os
import sys
import pandas as pd

def formatGBtoB(arg):
    # arg : "1-100GB" character, 1GB = 1073741824 byte
    # return :
    num = int(arg.split("G")[0])
    if arg.find("G")>=1:
        print(num)
        return 107374182 * num
    else:
        return "target file size is too small"

if __name__ == '__main__':

    os.chdir("/home/jovyan/BatchProcessing/")

    # load df
    df = pd.read_csv("data/breast-cancer-wisconsin.csv", header=None)
    df.columns = ["ID"] + ["V" + str(n) for n in range(len(df.columns)-1)]

    # put sample csv
    df.to_csv("data/sample.csv")

    # get commancline flag
    args = sys.argv[1]
    target_filesize = formatGBtoB(args)

    # bulkout csv
    df_appended = df.append(df).append(df).append(df).append(df)
    while os.stat("data/sample.csv").st_size<=target_filesize:
        df_appended.to_csv('data/sample.csv', mode='a', header=False)
    print("process is done ...")
