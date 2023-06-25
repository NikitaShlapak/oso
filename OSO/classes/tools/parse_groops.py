import re

import requests
from bs4 import BeautifulSoup as bs

def __main__():
    print('Groups parsing initiated...')

    groups = get_all_groups()
    groups_dict = []
    types = []
    for id, group_name in groups:
        type = re.match(r'[а-яА-Я]*', group_name).group(0)
        types.append(type)
        course = re.search(r'-[А-Я]\d', group_name).group(0)[1]
        year = '20'+re.search(r'-[А-Я]\d\d', group_name).group(0)[-2:]

        numgroup_re = re.match(r'[а-яА-Я]*\d', group_name)
        if numgroup_re:
            numgroup = numgroup_re.group(0)[-1]
        else:
            numgroup=0

        is_foreigns = group_name[-1]=='и'

        groups_dict.append({
            'group_name': group_name,
            'type':  type,
            'course': course,
            'year':year,
            'numgroup': numgroup,
            'is_foreigns':is_foreigns
        })
        # print(group_name, type, course, year,numgroup, is_foreigns)
        print(groups_dict[-1])
    print('Всего групп:', len(groups_dict))
    types = list(set(types))
    print(types, len(types))

def get_all_groups():
    data = requests.get('http://timetable.iate.obninsk.ru/')
    soup = bs(data.text, 'html.parser')
    links = soup.findAll(href=re.compile("group"))
    resp = []
    for link in links:
        resp.append((link['href'].split('/')[-1],link.text))
    return resp

__main__()