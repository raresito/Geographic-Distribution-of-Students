import json;
import requests;
import pymongo;

cookies = {
    'WTSesIDx': '35g19jhuzlfhqw1p5cmw0li31-127nlj7-1cu67ex',
    'WTSesIDHx': '35g0w816vv3xtlw65ylmwa1n0-4vj2hm-2pmtm0',
    'WTSesIDxC': '0c42ce3a0be691453bee68756c482656-72016b81400227053651aab17b62f366-e7e8dcb86c7fa777cb2466e26843ed04-01fc3041d26b7b6ef924d305a93985f5',
}

headers = {
    'Origin': 'https://rei.gov.ro',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ro;q=0.8,de;q=0.7,ru;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'text/html, */*; q=0.01',
    'Referer': 'https://rei.gov.ro/index.php?&ddpN=1396056689&we=fa012412589ad4b7e6996102b1bddeb5&wf=dGFCall&wtok=cd5c01a632387c75483359231daced34aa31ed0a&wtkps=FYxbCoAgEEX3Mv9Bo9nQuIf2EPbSLAoTo2jv2f06cDi3Y8lPYMWQzsUH0JaxpCpPh6wg2B4yVcgg1YSNm+Ptx/lIuCuzptJbiQUK2ryjAk2sabj+QOTDAXSr3w8=&wchk=e1d96d048c840eb4144086ee2a0615a37ae310ae',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = {
  'wtok': '',
  'wlist': '#Y#.YTowOnt9#Y#.5452c2af6d8a7e89b9597a5398d75b2d257d1b2e',
  'wtvnl': 'UzdReXNLcXVCUUE9#160b41ce20d69dff59a046a3fad2b5847a0a624b',
  'we': 'module.main.map.heat.nasterevsdomiciuliu',
  'wtkps': 'hYxBDsIgFETvwr6VXwrY3zsYE09ACloq0CrFGo13l3bpxllMJv+/GYUc3zEbWeari6S1CFTWWW1EhiRaTXKqAQnjF2iGPr3cub8tMPHOL9RZBgVUMrhBFtAlIc1zLVR50GxNisSPOjlTemVDtqnsjZrLoOJs7uYR9ehtZ5OzaeVBItF6CsfTDlgjKBdi32yPPPRz4Rt6+AN+vg==',
  'filters': '{"universitate":"1","facultate":"","cicluStudiu":"","domeniuStudiu":""}',
  'wf': 'aGFCall',
  'igfm': 'arSelectFilterData',
  'ddpN': '1396056689',
  'igfmV': 'aCall:data',
  'igfm_sa': '#Y#.dGhpcy5wcmUoKTtDb3JlLmFDYWxsKHRoaXMsJ2FyU2VsZWN0RmlsdGVyRGF0YScpOw==#Y#.f05638e0031517ae390f45950225b453ccd7642a',
  'oS': '#Y#.dGhpcy5wcmUoKTtDb3JlLmFDYWxsKHRoaXMsJ2FyU2VsZWN0RmlsdGVyRGF0YScpOw==#Y#.f05638e0031517ae390f45950225b453ccd7642a'
}

# for i in range(0,200):
# data['filters'] = '{"universitate":"'+str(1)+'","facultate":"","cicluStudiu":"","domeniuStudiu":""}';
# response = requests.post('https://rei.gov.ro/a.php', headers=headers, cookies=cookies, data=data);
# data1 = json.loads(response.text);
# data2 = json.loads(data1['content']);

client = pymongo.MongoClient("mongodb+srv://raresito:volkswag3@cluster0-hl3wg.mongodb.net/test?retryWrites=true");
database = client["StudentDB"];
university = database["university"];

for doc in university.find():
    print(doc['_id'])
    data['filters'] = '{"universitate":"'+str(doc['_id'])+'","facultate":"","cicluStudiu":"","domeniuStudiu":""}';
    response = requests.post('https://rei.gov.ro/a.php', headers=headers, cookies=cookies, data=data);
    data1 = json.loads(response.text);
    data2 = json.loads(data1['content']);
    print(type(data2), data2);

    for i in range (0, len(data2['facultate']) - 1):
        fac = {
            '_id': data2['facultate'][i][0],
            'idUniversitate': doc['_id'],
            'denumire': data2['facultate'][i][1]
        }
        if i/10 == 0:
            print (i)
        print(fac);
        # university.insert_one(uni);

# print(type(data2), data2);



#### INSERT UNIVERSITY LIST IN MONGO DB ####
# for i in range (0, len(data2['universitate']) - 1):
#     uni = {
#         '_id': data2['universitate'][i][0],
#         'denumire': data2['universitate'][i][1]
#     }
#     if i/10 == 0:
#         print (i)
#     university.insert_one(uni);
#### INSERT UNIVERSITY LIST IN MONGO DB ####