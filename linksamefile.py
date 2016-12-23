import sys
import os
import codecs
import ctypes

def find(rootdir):
  filelist={}
  count=0
  for pt,dlist,flist in os.walk(rootdir):
    for f in flist:
      p = os.path.join(pt,f)
      if os.path.exists(p):
        s=os.lstat(p)
        qf=0
        if s.st_size > 0:
          if s.st_size in filelist:
            if s.st_mtime in filelist[s.st_size]:
              """
              st = "del %s\nln %s %s" % (p,filelist[s.st_size][s.st_mtime],p)
              print(st)
              """
              os.remove(p)
              os.link(filelist[s.st_size][s.st_mtime],p)
              #print(filelist[s.st_size][s.st_mtime],p)
              count += 1
              if count % 1000 == 0:
                print("%d %s" % (count,pt))
              qf=1
          else:
            filelist[s.st_size] = {}
          if qf == 0:
            filelist[s.st_size][s.st_mtime] = p
  print("Total:%d" % count)

if __name__ == '__main__':
  find(sys.argv[1])

