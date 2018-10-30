import argparse
import step3
import sys
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-c','--countChar', help="Output character frequencies",action = "store_true")
group.add_argument('-f','--countWords', help="Output word frequencies",action = "store_true")
group.add_argument('-p','--phraseNum',type = int, help="Output phrase frequencies",default=2)
group.add_argument('-q','--preName', help="Output PREPOSITION pair frequencies")
parser.add_argument('-d','--dirFlag', help="Treat the <file name> as an directory",action = "store_true")
parser.add_argument('-s','--reFlag', help="Verb file to normalize the veb tenses",action = "store_true")
parser.add_argument('-v','--verbFile', help="Verb file to normalize the veb tenses",default=None)
parser.add_argument('-n','--num',type = int, help="Output only the top <num> iterms",default=10)
parser.add_argument('-x','--stopFile', help="Use <stop word> as a list of stop words, which are ignored in the count",default=None)
parser.add_argument('path', help="The file/directory to be operated with")
if(__name__ == '__main__'):
    args = parser.parse_args()
    if args.phraseNum < 0:
        print("Error: The num of words in a phrase should not be negative!!")
        sys.exit()
    if args.num < 0:
        print("Error: The num of the iterms output should not be negative!!")
        sys.exit()
    if (args.countChar):
        if (args.dirFlag):
            step3.OperateInDir(step3.CountLetters, args.path, int(args.num), args.stopFile, args.verbFile, args.reFlag)
        else:
            step3.CountLetters(args.path, int(args.num), args.stopFile, args.verbFile)
    if (args.countWords):
        if(args.dirFlag):
            step3.OperateInDir(step3.CountWords,args.path, int(args.num), args.stopFile, args.verbFile,args.reFlag)
        else:
            step3.CountWords(args.path, int(args.num), args.stopFile, args.verbFile)
    if (args.phraseNum):
        if (args.dirFlag):
            step3.OperateInDir(step3.CountPhrases, args.path, int(args.num), args.stopFile, args.verbFile, args.reFlag,int(args.phraseNum))
        else:
            step3.CountPhrases(args.path, int(args.num), args.stopFile, args.verbFile,int(args.phraseNum))
    else:
        print("Error: Please input the operation type (-f|-q|-p|-c)")

