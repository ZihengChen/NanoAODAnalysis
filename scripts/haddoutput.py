# python haddoutput.py /eos/uscms/store/user/zchen/batchout/WBrAnalyzer_YYYYMMDD_HHMMSS /eos/uscms/store/user/zchen/bltFiles/
# python haddoutput.py ./WBrAnalyzer_YYYYMMDD_HHMMSS ../bltFiles/

import sys, os, glob
from collections import defaultdict


if __name__ == "__main__":
    sourceDir = sys.argv[1]
    targetDir = sys.argv[2]
    targetDir += sourceDir.split("/")[-1]
    

    sourceLists = defaultdict(list)

    for src in glob.glob(sourceDir+"/*.root"):
        fname = os.path.basename(src)
        fnameSplit = fname.split("_")
        key = "{}_{}".format(fnameSplit[1],fnameSplit[2])
        sourceLists[key].append(fname)

    for key in sourceLists.keys():
        print "\n \n", key
        os.system('mkdir -p '+targetDir)
        cmd = "hadd {}/{}.root ".format(targetDir, key)
        for fname in sourceLists[key]:
            src = "{}/{} ".format(sourceDir, fname)
            cmd += src
        os.system(cmd)