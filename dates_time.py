import datetime
import json
class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)

def dumps(obj):
    return json.dumps(obj, cls=JSONDateTimeEncoder)

now_str = dumps({'time': datetime.datetime.now()})
print(now_str)

from datetime import datetime
time_str = '2012/01/01 12:32:11'
dt = datetime.strptime(time_str, '%Y/%m/%d %H:%M:%S')
print(dt)

# To convert date fields of a known format into datetimes:
# dt = datetime.strptime('1/2/2012 12:32:11', '%Y/%m/%d %H:%M:%S')
# for d in data:
#     try:
#         d['date'] = datetime.strptime(d['date'],\
#         '%Y/%m/%d %H:%M:%S')
#     except ValueError:
#         print('Oops! - invalid date for ' + repr(d))