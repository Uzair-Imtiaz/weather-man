import argparse
import re
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

    year_month_pattern = r'^\d{4}/\d{1,2}$'
    year_pattern = r'^\d{4}$'
    if args.year_and_month_for_a is not None and not re.match(pattern=year_month_pattern,
                                                              string=args.year_and_month_for_a):
        parser.error('Argument must be of the format yyyy/mm')
    if args.year_and_month_for_c is not None and not re.match(pattern=year_month_pattern,
                                                              string=args.year_and_month_for_c):
        parser.error('Argument must be of the format yyyy/mm')
    if args.year is not None and not re.match(pattern=year_pattern, string=args.year):
        parser.error('Argument must be of the format yyyy')

    rg = ReportGenerator()
    rg.generate_report(args.files_dir, args.year_and_month_for_a, args.year_and_month_for_c, args.year)


if __name__ == '__main__':
    # Call the main function.
    main()
