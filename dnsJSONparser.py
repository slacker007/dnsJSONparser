#!/usr/bin/env python
# @real_slacker007
# http://cybersyndicates.com
# http://huntools.org

import sys
import os
import argparse
import json

def main(args):
    if args.filename:
            try:
                    f = open(args.filename)
            except:
                    print "Unable to open {0}".format(args.filename)
                    return 1
    else: 
        print "Error, No file supplied"
        return 1

    if args.queries:
        for line in iter(f):
            json_d = json.loads(line)
            h = json_d["header"]
            jq = json_d["questions"]
            if (h["type"] == "QUERY"):
                try:
                    query = "[Q] {0}, {1}, {2}, {3}, {4}".format(h["type"], h["flags"], h["rcode"], jq[0]["qtype"], jq[0]["qname"])
                    print query
                except:
                    pass
            else:
                pass

    elif args.responses:
        for line in iter(f):
            json_d = json.loads(line)
            r = json_d["header"]
            jr = json_d["rr"]
            if (r["type"] == "RESPONSE"):
                try:
                    response = "[R] {0}, {1}, {2}, {3}, {4}, {5}".format(r["type"], r["flags"], r["rcode"], str(jr[0]["ttl"]), jr[0]["rdata"], jr[0]["rname"])
                    print response
                except:
                    pass
            else:
                pass

    else:
        print "Error: must include -q or -r"
        print "<command> --help"
        return 1
    return 0
    
if __name__ == "__main__":
    #parse arguments from cli
    if len(sys.argv) < 2:
        print "Error: Too Few Arguments"
        print "<command> --help"
        sys.exit()
    else:
        parser = argparse.ArgumentParser()        
        parser.add_argument('-f', '--filename', type=str)
        parser.add_argument('-q', '--queries', help= '\tshow all dns queries', action='store_true')
        parser.add_argument('-r', '--responses', help='\tshow all dns responses', action='store_true')
        args = parser.parse_args()
        main(args)

