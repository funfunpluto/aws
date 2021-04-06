#!/usr/local/bin/python3

import boto3
import sys, getopt

def main(argv):
    gpname = ''
    typ = ''
    try:
        opts, args = getopt.getopt(argv,"hg:t:",["gpname=", "typ="])
    except getopt.GetoptError:
        print('ec2groupinv.py -g <alpha|bravo> -t <public|private>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('ec2groupinv.py -g <alpha|bravo> -t <public|private>')
            sys.exit()
        elif opt in ("-g", "--gpname"):
            gpname = arg
        elif opt in ("-t", "--typ"):
            typ = arg
        else:
            print('ec2groupinv.py -g <alpha|bravo> -t <public|private>')
            sys.exit(1)

    if typ == 'public':
        ty = 'yes'
        ipaddr = 'PublicIpAddress'
    else:
        ty = 'no'
        ipaddr = 'PrivateIpAddress'
    
    instlist = get_inst_info(gpname,ty,ipaddr)
    prnt_instaddr(gpname, typ, instlist) 

def prnt_instaddr(gpname,typ,instlist):
    hd = '[' + gpname + '_' + typ + ']'
    print(hd)
    for inst in instlist:
        print(inst) 

def get_inst_info(gn,typ,ipaddr):
    #ec2 = boto3.resource('ec2')
    ec2client = boto3.client('ec2')
    response = ec2client.describe_instances(
        Filters = [
            {
                'Name': 'tag:'+'Group',
                 'Values': [gn]
            },
            {
                 'Name': 'tag:'+'Public',
                 'Values': [typ]
            }

	]
    )
    instanceIPlist = []
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            instanceIPlist.append(instance[ipaddr])
    return instanceIPlist 

if __name__ == "__main__":
    main(sys.argv[1:])
