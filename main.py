import json;
import requests;
import pymongo;

cookies = {
    'WTSesIDx': '35g19jhuzlfhqw1p5cmw0li31-127nlj7-1cu67ex',
    'WTSesIDHx': '35g0w816vv3xtlw65ylmwa1n0-4vj2hm-2pmtm0',
    'WTSesIDxC': 'b4336e796d89435440dc2b4b86bfc64a-36d80e420b7774f222ce1437cd364730-2be54c41fb79ca4b51b922a40d3fc6f0-eda0d034b81a1512156bee9c2bcf4588',
}

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://rei.gov.ro',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ro;q=0.8,de;q=0.7,ru;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'text/html, */*; q=0.01',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://rei.gov.ro/index.php?&ddpN=1396056689&we=fa012412589ad4b7e6996102b1bddeb5&wf=dGFCall&wtok=cd5c01a632387c75483359231daced34aa31ed0a&wtkps=FYxbCoAgEEX3Mv9Bo9nQuIf2EPbSLAoTo2jv2f06cDi3Y8lPYMWQzsUH0JaxpCpPh6wg2B4yVcgg1YSNm+Ptx/lIuCuzptJbiQUK2ryjAk2sabj+QOTDAXSr3w8=&wchk=e1d96d048c840eb4144086ee2a0615a37ae310ae',
}

data = {
  'wtok': '',
  'wlist': '#Y#.YTowOnt9#Y#.5452c2af6d8a7e89b9597a5398d75b2d257d1b2e',
  'wtvnl': 'UzdReXNLcXVCUUE9#160b41ce20d69dff59a046a3fad2b5847a0a624b',
  'we': 'module.main.map.heat.nasterevsdomiciuliu',
  'wtkps': 'hYxBDsIgFETvwr6VXwrY3zsYE09ACloq0CrFGo13l3bpxllMJv+/GYUc3zEbWeari6S1CFTWWW1EhiRaTXKqAQnjF2iGPr3cub8tMPHOL9RZBgVUMrhBFtAlIc1zLVR50GxNisSPOjlTemVDtqnsjZrLoOJs7uYR9ehtZ5OzaeVBItF6CsfTDlgjKBdi32yPPPRz4Rt6+AN+vg==',
  'wf': 'aGFCall',
  'igfm': 'arSelectData',
  'ddpN': '1396056689',
  'igfmV': 'aCall:data',
  'igfm_sa': '#Y#.dGhpcy5wcmUoKTtDb3JlLmFDYWxsKHRoaXMsJ2FyU2VsZWN0RGF0YScpOw==#Y#.a1f722ac1cd2b0a0f323dc0ff59bc5376d68eb05',
  'oS': '#Y#.dGhpcy5wcmUoKTtDb3JlLmFDYWxsKHRoaXMsJ2FyU2VsZWN0RGF0YScpOw==#Y#.a1f722ac1cd2b0a0f323dc0ff59bc5376d68eb05'
}

# for i in range(0,200):
data['filters'] = '{"universitate":"","facultate":"","cicluStudiu":"","domeniuStudiu":""}';
response = requests.post('https://rei.gov.ro/a.php', headers=headers, cookies=cookies, data=data);
data1 = json.loads(response.text);
data2 = json.loads(data1['content']);

client = pymongo.MongoClient("mongodb+srv://raresito:volkswag3@cluster0-hl3wg.mongodb.net/test?retryWrites=true");
database = client["StudentDB"];
university = database["university"];
# database.authenticate('raresio', 'volkswag3');

print(type(data2['universitate']), data2['universitate']);
for i in range (0, len(data2['universitate']) - 1):
    uni = {
        '_id': data2['universitate'][i][0],
        'denumire': data2['universitate'][i][1]
    }
    if i/10 == 0:
        print (i)
    university.insert_one(uni);