# coding: utf-8


import json

try:
    from ru.curs.showcase.core.jython import JythonDTO
except:
    from ru.curs.celesta.showcase import JythonDTO
from ru.curs.celesta.showcase.utils import XMLJSONConverter
from security._security_orm import loginsCursor
from security._security_orm import subjectsCursor
from security.functions import Settings

def cardData(context, main, add, filterinfo=None, session=None, elementId=None):
    xformsdata = {"schema":{"@xmlns":""}}
    xformssettings = {"properties":{"event":{"@name":"single_click",
                                             "@linkId": "1",
                                             "action":{"#sorted":[{"main_context": "current"},                                                       
                                                                  {"datapanel": {"@type": "current",
                                                                         "@tab": "current",
                                                                         "element": [{"@id":"usersGrid",
                                                                                     "add_context": ""
                                                                                     },
                                                                                     {"@id":"employeesGrid",
                                                                                     "add_context": ""
                                                                                     }]
                                                                     }
                                                       }]}
                                             }
                                    }
                      }
    jsonData = XMLJSONConverter.jsonToXml(json.dumps(xformsdata))
    jsonSettings = XMLJSONConverter.jsonToXml(json.dumps(xformssettings))
    return JythonDTO(jsonData, jsonSettings)

def cardDelete(context, main=None, add=None, filterinfo=None, session=None, elementId=None, xformsdata=None):
    currentRecordId = json.loads(session)['sessioncontext']['related']['gridContext']['currentRecordId']
    settings=Settings()
    user = loginsCursor(context)
    user.get(currentRecordId)
    if settings.loginIsSubject():
        subject = subjectsCursor(context)
        subject.get(user.subjectId)
        user.delete()
        subject.delete()
    else:
        user.delete()