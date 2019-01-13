import requests

cookies = {
    'WTSesIDHx': '35g0il04pqo4fcptt4vgwholu-18yyzmt-56483s',
    'WTSesIDx': '35g1dvj1pbw5574vto2gnwe6r-rlyd7n-182a5h4',
    'WTSesIDxC': '56e8136d6ad095af1fbe7f4758bb3b02-b4e67ef5d5cffbe39d020f840e563cc8-93a81d8a03fee8c0a1554ae6c5dcd580-078b088c46c1fedadae61539dcf41ed7',
}

headers = {
    'Origin': 'https://rei.gov.ro',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ro;q=0.8,de;q=0.7,ru;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'text/html, */*; q=0.01',
    'Referer': 'https://rei.gov.ro/index.php?&ddpN=1396056689&we=fa012412589ad4b7e6996102b1bddeb5&wf=dGFCall&wtok=355e9bc2a5ebe22d32c1fbf31dfef3aa981167d2&wtkps=FYxBCoAgEAD/snehNTdj/UN/MIyyokJFiejv2W1ghrHc8hOZGEra9gjGMzadkhpNrAqid1BJNQwtzejyitdYiLTK6ZTzUaYuiLDfTh8Ce2lpUX8v628CM5j3Aw==&wchk=318d9f0735c4fc07a1b252d47493291922029f57',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = {
  'wtok': '',
  'wlist': '#Y#.YTowOnt9#Y#.5452c2af6d8a7e89b9597a5398d75b2d257d1b2e',
  'wtvnl': 'UzdReXNLcXVCUUE9#6c1a92b4c7082e953eee1652cd318cb0d10f6ec4',
  'we': 'module.main.map.heat.nasterevsdomiciuliu',
  'wtkps': 'hYxNDoIwFITv0j1IS3/gcQdi4gmqr4FqKYQWiDHe3ULixo2byWTmm9Eg4BWSkC0+XCCNBVpIzhRtApRAgkWSHC+AlKKjuN7pdN2EUHyNI+v8ZuScze6Jyme0Ylr0fOdZ+jPf4TDi4kw+aOuTTHlvdMy9DtHMZg04DvZmF2eXnacKCOLkz5cTLWtZCCmr+ijS0U8iDrT9A74/',
  'filters': '{"universitate":"5","facultate":"","cicluStudiu":"","domeniuStudiu":""}',
  'wf': 'aGFCall',
  'igfm': 'arFindData',
  'ddpN': '1396056689',
  'igfmV': 'aCall:data',
  'igfm_sa': '#Y#.dGhpcy5wcmUoKTtDb3JlLmFDYWxsKHRoaXMsJ2FyRmluZERhdGEnKTs=#Y#.09b03de603450d47f0bb16657dfa132070a0433b',
  'oS': '#Y#.dGhpcy5wcmUoKTtDb3JlLmFDYWxsKHRoaXMsJ2FyRmluZERhdGEnKTs=#Y#.09b03de603450d47f0bb16657dfa132070a0433b'
}
import json;

for i in range(0,50):
    if i != 1:
        data['filters'] = '{"universitate":"'+str(i)+'","facultate":"","cicluStudiu":"","domeniuStudiu":""}';
        # print(data['filters']);
        response = requests.post('https://rei.gov.ro/a.php', headers=headers, cookies=cookies, data=data);
        data1 = json.loads(response.text);
        data2 = json.loads(data1['content']);
        # print (data2);

import pymongo;

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# print(myclient.list_database_names());

mydb = myclient["StudentDB"];

university = mydb['university'];

# university.delete_many({})
#
# university.insert_one(data1);
#
# print(myclient.list_database_names());

for x in university.find():
    print (x);