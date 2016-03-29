'''
Created on 2016年3月24日

@author: lyt
'''
import optparse

from optparse import OptionParser
MSG_USAGE = "myprog[ -f <filename>][-s <xyz>] arg1[,arg2..]"
optParser = OptionParser(MSG_USAGE)
optParser.add_option("-f","--file",action = "store",type="string",dest = "fileName")
optParser.add_option("-v","--vison", action="store_false", dest="verbose",default='gggggg',
                     help="make lots of noise [default]")
fakeArgs = ['-f','file.txt','-v','good luck to you', 'arg2', 'arge']
options, args = optParser.parse_args(fakeArgs)
print (options.fileName)
print (options.verbose)
print (options)
print (args)
print (optParser.print_help())


usage = "usage: %prog [options] arg1 arg2"  
parser = OptionParser(usage=usage)  
parser.add_option("-v", "--verbose",  
                  action="store_true", dest="verbose", default=True,  
                  help="make lots of noise [default]")  
parser.add_option("-q", "--quiet",  
                  action="store_false", dest="verbose",  
                  help="be vewwy quiet (I'm hunting wabbits)")  
parser.add_option("-f", "--filename",  
                  metavar="FILE", help="write output to FILE"),  
parser.add_option("-m", "--mode",  
                  default="intermediate",  
              help="interaction mode: novice, intermediate, "  
                   "or expert [default: %default]")  