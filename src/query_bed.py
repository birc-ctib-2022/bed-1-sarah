"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    parse_line, print_line
)
from query import Table


def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',  # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    
    # Create empty table
    table = Table()

    # Add each line from the BED file to a table
    for bed_line in args.bed:
        new_line = parse_line(bed_line)
        table.add_line(new_line)
    
    # Access the query and itterate over each line
    for query_line in args.query:
        # Get chrom, chromStart and chromEnd
        query_chrom, query_chromStart, query_chromEnd = query_line.split()
        # Get all BED lines that match chrom from the query line
        list_chrom_match = table.get_chrom(query_chrom)
        # Itterate over the list of BED lines matching the query chromosome
        for chrom_match in list_chrom_match:
        # If chromStart and chromEnd match the querry, add to outfile
            if int(query_chromStart) <= chrom_match[1] and chrom_match[2] <= int(query_chromEnd):
                print_line(chrom_match, args.outfile)

if __name__ == '__main__':
    main()

# looked at bed-1-grupo-loco & bed-1-capibaras when getting stuck