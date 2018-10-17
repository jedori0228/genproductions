import os

WhicihDir = 'logs_PairN'

os.system('ls -1 '+WhicihDir+'/*.log > tmp.txt')
Files = open('tmp.txt').readlines()
os.system('rm tmp.txt')

for File in Files:
  File = File.strip('\n')
  alias = File.replace(WhicihDir+'/','').replace('.log','').replace('xsec_','')

  lines = open(File).readlines()

  for i in range(0,len(lines)):
    line = lines[len(lines)-1-i].strip('\n')
       #After filter: final cross section = 1.718e-05 +- 1.642e-08 pb
    if "After filter: final cross section" in line:
      line = line.replace('After filter: final cross section = ','')

      endindex=0
      for a in range(0,len(line)):
        if line[a]==" ":
          endindex = a
          break
      xsec = line[:a]
      print alias+'\t'+xsec
      break
