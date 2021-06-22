from datetime import datetime
from cisco_pm import get_hosts_file, hosts_to_yaml, ios_pm, result_parsing, create_worksheet, report


def main(excel_file, site, role):
    commands = [
        'show hardware',
        'show env all', 'show env',
        'show processes cpu',
        'show processes mem',
        'show run | inc hostname',
    ]
    now = datetime.now()
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(f'Starting proactive maintenance: {now}')
    hosts = get_hosts_file(excel_file)
    # hosts_to_yaml(hosts)
    result = ios_pm(hosts, commands=commands, vendors='cisco', site=site, role=role)
    chk_list = result_parsing(result)
    create_worksheet(excel_file)
    report(chk_list, excel_file)
    now = datetime.now()
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    print(f'End proactive maintenance: {now}')


if __name__ == '__main__':
    excel_file = input('Type excel file: [cisco.xlsx] ')
    if not excel_file:
        excel_file = 'cisco.xlsx'
    site = input('Type site: [ALL] ')
    if site.upper() == 'ALL':
        site = ''
    role = input('Type role: [ALL] ')
    if role.upper() == 'ALL':
        role = ''

    main(excel_file, site, role)




