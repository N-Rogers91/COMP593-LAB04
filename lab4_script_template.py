import sys
import os
import re as re
import pandas as pd


def main():
    log_file = get_log_file_path_from_cmd_line()
    filter_log_by_regex(log_file, 'SRC=(.*?) DST(.*?) LEN=(.*?)', print_summary=True, print_records=True)
    dpt_tally = tally_port_traffic(log_file)

    for dpt, count in dpt_tally.items():
        if count > 100
        generate_port_traffic_report(log_file, dpt)



    pass

# TODO: Step 3
def get_log_file_path_from_cmd_line():
    num_params = len(sys.argv) - 1
    if num_params >= 1:
        log_file_path = sys.argv[1]
        if os.path.isfile(log_file_path):
            return os.path.abspath(log_file_path)
        else: 
            print("Error: Log file does not exist")
            sys.exit(1)
    else:
        print("Error: Missing Log file.")
        sys.exit(1)                 



# TODO: Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    """Gets a list of records in a log file that match a specified regex."""

    records = []
    captured_data = []
    
    regex_flags = re.IGNORECASE if ignore_case else 0

    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(regex, line, regex_flags)
            if match: 
                records.append(line)
                if match.lastindex:
                    captured_data.append(match.groups())
        

    if print_records is True:
        print(*records, sep='')


    if print_summary is True:
        
        print(f' The log file contains {len(records)} records that case-{"in"if ignore_case else ""}senstive math the regex. "{regex}"')


    
    
    
    
    return records, captured_data

# TODO: Step 8
def tally_port_traffic(log_file):
    dest_port_logs = filter_log_by_regex(log_file, 'DPT=(.+?) ')[1]
    
    dpt_tally = {}
    for dpt_tuple in dest_port_logs:
        dpt_num = dpt_tuple[0]
        dpt_tally[dpt_num] = dpt_tally.get(dpt_num, 0) + 1

    return

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):

    regex = r"^({6}) (.{8}).*SRC=(.+?) DST=(.+?) .*SPT=(.+?)"

    captured_data = filter_log_by_regex(log_file, regex)[1]

    report_df = pd.DataFrame(captured_data)
    report_header = ('Date', 'Time', 'Source IP Address', 'Source port', 'Destination port')
    report_df.to_csv(f'destination_port_{port_number}_report.csv', index=False, header=report_header)

# TODO: Step 11
def generate_invalid_user_report(log_file):
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()