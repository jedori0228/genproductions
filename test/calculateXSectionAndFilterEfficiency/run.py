import os

WhicihDir = 'filelist_PairN'
OutDir = 'logs_PairN'

os.system('mkdir -p '+OutDir)

os.system('ls -1 '+WhicihDir+'/*.txt > tmp.txt')
lines = open('tmp.txt').readlines()
os.system('rm tmp.txt')

for line in lines:
  line = line.strip('\n')
  alias = line.replace(WhicihDir+'/','').replace('.txt','')

  Files = open(line).readlines()

  cmd = 'cmsRun genXsec_cfg.py inputFiles='

  for i in range(0,len(Files)):
    File = Files[i]
    File = File.strip('\n').replace('root://cluster142.knu.ac.kr//','dcap://cluster142.knu.ac.kr//pnfs/knu.ac.kr/data/cms/')
    cmd += File
    if i!=len(Files)-1:
      cmd +=','

  cmd += ' &> '+OutDir+'/xsec_'+alias+'.log'

  print alias
  os.system(cmd)
