import json;
import requests;
import pymongo;
import requests
from pymongo.collation import Collation

cookies = {
    'WTSesIDHx': '35g0w816vv3xtlw65ylmwa1n0-4vj2hm-2pmtm0',
    '_ga': 'GA1.2.1358434475.1548575832',
    'WTSesIDx': '35g0iwwzs45qbi4mny20qb5mu-1bphsej-4at7mq',
    'WTSesIDxC': '37d9cf2f6e016ee74acd070d8fd74d47-f08a3eef84fbafde6be8f2ed41fa29ee-a8f7fe1f5ba3b4cfe6bc24d86385eee6-e0ab9300cf0a90b76d0a3f17426fdd62',
}

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://rei.gov.ro',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ro;q=0.8,de;q=0.7,ru;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'text/html, */*; q=0.01',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://rei.gov.ro/index.php?&ddpN=1396056689&we=fa012412589ad4b7e6996102b1bddeb5&wf=dGFCall&wtok=d4988a328784eae4ed23f66e4af054ac6f1bfc13&wtkps=FYxbCoAgEADvsv+CT6T1Dt0hScrKSNaQiu6e/Q3MMAMqfAgNQi3rRuAiCsFFJ62jpoDiCI00R1Bm4rHWm7TJPuq0X5Jnb9LJhD9mCgvTQ7Ep/71svwCud+8H&wchk=6f98fb14211594e5b10d71997f66eaea5e6f484a',
}

data = {
  'wtok': '',
  'wlist': '#Y#.YTowOnt9#Y#.5452c2af6d8a7e89b9597a5398d75b2d257d1b2e',
  'wtvnl': 'UzdReXNLcXVCUUE9#99ff68906ac993737738a049625d7eedae814ae4',
  'we': 'module.main.map.heat.nasterevsdomiciuliu',
  'wtkps': 'hYxBDoIwFETv0j3YQgvyuYMx8QTFNvqVFvC3EjXe3ULixo2byWTmzWhQ8KIkbA7XnliLIAQXTVG3BCUwQsOSkxxYqU4c5/lJUk0dSucfBZ865WImuvFM9pJJHWo3LXyR/ux36AYTe5s7jT7JmJ+tDrnXFOzN3skMDo8Ye4wLL2pgxox+f9iIsqm4qqptsxbp6CdRK7r7A74/',
  'wf': 'aGFCall',
  'igfm': 'arSelectData',
  'ddpN': '1396056689',
  'igfmV': 'aCall:data',
  'igfm_sa': '#Y#.dGhpcy5wcmUoKTtDb3JlLmFDYWxsKHRoaXMsJ2FyU2VsZWN0RGF0YScpOw==#Y#.a1f722ac1cd2b0a0f323dc0ff59bc5376d68eb05',
  'oS': '#Y#.dGhpcy5wcmUoKTtDb3JlLmFDYWxsKHRoaXMsJ2FyU2VsZWN0RGF0YScpOw==#Y#.a1f722ac1cd2b0a0f323dc0ff59bc5376d68eb05'
}



#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://rei.gov.ro/index.php?&ddpN=2559850461&we=739b3c62c1bb313943067e2dbe65cfb3&wf=dGFCall&wtok=2ae3d9f0182505ff216a97c4ba79ee2770bde17d&wtkps=FYxBDoUgDAXv0r2GomBaT2OiXwkgiRVcGO/+YTd58zILD/wKG4bn9kFgdoxqGsnSLFWBuBUaEcNgdpwy3snoEtNxBfK2/DzpLrtCqDqj7Chnu+ua2xqgZYhpzWHr4+LO/kix7t8f&wchk=ad6bc8b0fa43dd9db23d292ad783013c6bcf618a', headers=headers, cookies=cookies, data=data)


# for i in range(0,200):
# data['filters'] = '{"universitate":"","facultate":"","cicluStudiu":"","domeniuStudiu":""}';
# response = requests.post('https://rei.gov.ro/a.php', headers=headers, cookies=cookies, data=data);
# data1 = json.loads(response.text);
# data2 = json.loads(data1['content']);
#
# print(data2['universitate'], len(data2['universitate']));


# def tokenize(str):
#     return str.lower();

client = pymongo.MongoClient("mongodb+srv://@cluster0-hl3wg.mongodb.net/test?retryWrites=true");
database = client["StudentDB"]
domains = database["domains"]
universities = database["university"]

# for uni in data2['universitate']:
#     univ = {
#         '_id': uni[0],
#         'denumire': uni[1]
#     }
#     universities.insert_one(univ);








##### IAU TOATE UNIVERSITATILE SI SCHIMB S-URILE CIUDATE

# import re
# regx = re.compile('.*Ş.*', re.IGNORECASE)
# x = universities.find({"denumire": regx})
# for doc in x:
#     # print(doc["denumire"], doc["denumire"].replace("ş", "ș"));
#     universities.update_one({'_id': doc["_id"]}, {"$set": { "denumire": doc["denumire"].replace("Ş", "Ș") }})



##### IAU TOATE UNIVERSITATILE SI SCHIMB S-URILE CIUDATE



# import re
# regx = re.compile('.*tehn[i,î]c[ă,â,a].*', re.IGNORECASE)
# x = universities.find({"denumire": regx})
#
# for doc in x:
#     print(doc)

# # database.create_collection('university');
# universities.create_index({"denumire": pymongo.TEXT});


# unies = database['universityRO'];

# universities.createIndex({"denumire":"text"});
# print(universities.get_indexes());
# universities.create_index([('denumire', pymongo.TEXT)], name='denumire_index', collation=Collation(locale='ro', strength=1))

# ASTA E CE VREAU: db.TestCollection.find({titlu: {$regex: /.*p[a,â,ă]m.*/i}})

#
# universities.create_index(
#    { 'denumire' : "text" },
#    { 'default_language': "romanian" }
# )

# universities.create_index();


# for doc in universities.find():
#     unies.insert_one(doc);
# for doc in universities.find({"denumire": {"$regex": "ehnică"}}):
#     print(doc, tokenize(doc['denumire']));
#     # newValues = { "$set": {} }
    # universities.update(doc, {$set: {"tokenized": tokenized(doc['denumire'])}})
    # print(doc);



#### INSERT CITY LIST FOR EVERY DOMAIN IN MONGO DB ####
# for doc in domains.find():
#         data['filters'] = '{"universitate":"' + str(doc['idUniversity']) + '","facultate":"' + doc['idFaculty'] + '","cicluStudiu":"' + doc['idCycle'] + '","domeniuStudiu":"' + doc['idDomain'] + '"}'
#         response = requests.post('https://rei.gov.ro/a.php', headers=headers, cookies=cookies, data=data)
#         data1 = json.loads(response.text)
#         data2 = json.loads(data1['content'])
#         print(doc['idUniversity'])
#         dom = {
#             'idUniversity': doc['idUniversity'],
#             'idFaculty': int(doc['idFaculty']),
#             'idCycle': int(doc['idCycle']),
#             'idDomain': int(doc['idDomain']),
#             'listaOrase': data2
#         }
#         studOras.insert_one(dom)
#### INSERT CITY LIST FOR EVERY DOMAIN IN MONGO DB ####


#### INSERT DOMAINS LIST IN MONGO DB ####
# for doc in cycles.find():
#     print(doc['idUniversity'], doc['idFaculty'], doc['id'])
#     # print(doc['_id'], doc['idUniversitate']);
#     data['filters'] = '{"universitate":"' + str(doc['idUniversity']) + '","facultate":"' + doc['idFaculty'] + '","cicluStudiu":"' + doc['id'] + '","domeniuStudiu":""}'
#     response = requests.post('https://rei.gov.ro/a.php', headers=headers, cookies=cookies, data=data)
#     data1 = json.loads(response.text)
#     data2 = json.loads(data1['content'])
#     domenii = data2['domeniuStudiu']
#     for key, value in domenii.items():
#         dom = {
#             'idDomain': key,
#             'idCycle': doc['id'],
#             'idFaculty': doc['idFaculty'],
#             'idUniversity': doc['idUniversity'],
#             'domain': value
#             }
#         domains.insert_one(dom)
#### INSERT DOMAINS LIST IN MONGO DB ####



#### INSERT CYCLES LIST IN MONGO DB ####
# for doc in faculties.find():
#     # print(doc['_id'], doc['idUniversitate']);
#     data['filters'] = '{"universitate":"' + str(doc['idUniversitate']) + '","facultate":"' + doc['_id'] + '","cicluStudiu":"","domeniuStudiu":""}'
#     response = requests.post('https://rei.gov.ro/a.php', headers=headers, cookies=cookies, data=data)
#     data1 = json.loads(response.text)
#     data2 = json.loads(data1['content'])
#     cicluri = data2['cicluStudiu']
#     for key, value in cicluri.items():
#         cic = {
#             'id': key,
#             'idFaculty': doc['_id'],
#             'idUniversity': doc['idUniversitate'],
#             'cycle': value
#         }
#         cycles.insert_one(cic)
#     if doc['idUniversitate'] > 10:
#         print('10');
#     if doc['idUniversitate'] > 20:
#         print('20');
#     if doc['idUniversitate'] > 50:
#         print('50');
#     if doc['idUniversitate'] > 100:
#         print('100');
#### INSERT CYCLES LIST IN MONGO DB ####



#### INSERT FACULTY LIST IN MONGO DB ####
#     for key, value in facultati.items():
#         fac = {
#             '_id': key,
#             'idUniversitate': doc['_id'],
#             'denumire': value
#         }
#         faculties.insert_one(fac)
#### INSERT FACULTY LIST IN MONGO DB ####


