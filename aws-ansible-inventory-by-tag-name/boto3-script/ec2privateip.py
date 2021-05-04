#!/usr/local/bin/python3

import boto3
import sys, getopt

def main(argv):
    gpname = ''
    typ = ''
    try:
        opts, args = getopt.getopt(argv,"hg:",["gpname=", "typ="])
    except getopt.GetoptError:
        print('ec2groupinv.py -g <alpha|bravo> ')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('ec2groupinv.py -g <alpha|bravo>')
            sys.exit()
        elif opt in ("-g", "--gpname"):
            gpname = arg
        else:
            print('ec2groupinv.py -g <alpha|bravo>')
            sys.exit(1)

    typ = 'public'    
    instlist = get_inst_info(gpname)
    prnt_instaddr(gpname, typ, instlist) 

def prnt_instaddr(gpname,typ,instlist):
    hd = '[' + gpname + '_' + typ + ']'
    print(hd)
    for inst in instlist:
        print(inst) 

def get_inst_info(gn):
    #ec2 = boto3.resource('ec2')
    ec2client = boto3.client('ec2')
    response = ec2client.describe_instances(
        Filters = [
            {
                'Name': 'tag:'+'Group',
                 'Values': [gn]
            }

	]
    )
    instanceIPlist = []
    ipaddr = 'PrivateIpAddress'    
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            if instance.get(ipaddr) is not None:
                instanceIPlist.append(instance[ipaddr])

    return instanceIPlist 



if __name__ == "__main__":
    main(sys.argv[1:])
