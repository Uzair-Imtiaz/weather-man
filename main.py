import sys
import argparse
from ReportGenerator import ReportGenerator


def main():
    '''The main function'''

    parser = argparse.ArgumentParser(prog='Weather Man.', description='Generates a report for the specified month and'
                                                                      'year for Murree.')
    parser.add_argument('files_dir', help='Path to the files directory')
    parser.add_argument('-a', '--year_and_month_for_a', help='Report a requires year ad month in yyyy/mm format')
    parser.add_argument('-c', '--year-and-month-for-c', help='Report c requires year ad month in yyyy/mm format')
    parser.add_argument('-e', '--year', help='Report e requires year yyyy format')
    args = parser.parse_args()
    if not any([args.year_and_month_for_a, args.year_and_month_for_c, args.year]):
        parser.error('At least one of the report types must be given.')

    rg = ReportGenerator()
    rg.generate_report(args.files_dir, args.year_and_month_for_a, args.year_and_month_for_c, args.year)

# Run the program
if __name__ == '__main__':
    main()
