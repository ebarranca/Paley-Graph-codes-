"""
This program takes in a txt file and
writes the sets in the file of a given size to a
given output file

expects magma output to be formatted like a normal txt file
"""

import optparse
import sys


def main():
    #parse command line for input file and size we want

    parser = optparse.OptionParser(description = "Parse Tight Sets")
    parser.add_option('-i', '--input_filename', type = 'string', help = 'path to input txt file')
    parser.add_option('-c', '--cardinality', type = 'int', help = 'desired cardinality')
    parser.add_option('-o', '--output_filename', type = 'string', help= 'output file name')
    (opts, args) = parser.parse_args()

    mandatories = ['input_filename', 'cardinality', 'output_filename']
    for m in mandatories:
        if not opts.__dict__[m]:
            print('mandatory option ' + m + ' is missing\n')
            parser.print_help()
            sys.exit()

    ifile = opts.input_filename
    ofile = opts.output_filename
    c = opts.cardinality

    #print to terminal number of sets
    ret =[]
    try:
        infile = open(ifile, "r")
    except:
        print("could not open %s" % ifile)
        sys.exit()


    for line in infile:
        # print(line)
        if line != "{" and line != "}":
            lis = line.strip()
            lis = lis.strip("{")
            lis= lis.strip("},")

            lis = lis.split(',')
            # print (lis)
            if len(lis)==c:
                if lis not in ret:
                    ret.append(lis)


    print("Number of sets of size %d: %d" % (c, len(ret)))
    infile.close()

    #create an output file for the sets
    try:
        outfile = open(ofile, "w")
    except:
        print("Could not open %s " % ofile)
        sys.exit()
    #
    # zero_one = []
    # for item in ret:
    #     count = 0
    #     for el in item:
    #         if el == " 0" or el == " 1":
    #             count +=1
    #     if count == 2:
    #         zero_one.append(item)

    # for item in zero_one:
    for item in ret:
        outfile.write("{")
        for el in item:
            if el == item[len(item)-1]:
                outfile.write("%s "% el)
            else:
                outfile.write("%s, "% el)
        if item == ret[len(ret)-1]:
            outfile.write("} \n")
        else:
            outfile.write("}, \n")


main()
