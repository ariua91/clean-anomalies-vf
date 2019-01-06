from datetime import datetime, timedelta
import requests
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from secret_keys import ENV, CLIENT_ID, CLIENT_SECRET
from polygons import POLYGON_DICT

LOGFN = 'logs/' + datetime.strftime(datetime.utcnow() + timedelta(hours=8),
                                    '%y-%U-logs.txt')
VERBOSE = True


class task(object):
    def __init__(self, task_json):
        '''
        Accepts task_JSON from VF Public API
        '''
        self.task_id = task_json['id']
        self.tags    = task_json['tags']
        self.invoice = task_json['invoice_number']
        self.lat     = task_json['address']['latitude']
        self.lng     = task_json['address']['longitude']

    def archive_task(self, variables):
        'archives task'
        env, c_id, c_secret = variables['env'], variables['c_id'], variables['c_secret']
        cnt, status = 0, 400
        while cnt < 3 and status != 200:
            tmp = requests.put(
                "https://{!s}.versafleet.co/api/tasks/{!s}/archive?"
                "client_id={!s}&client_secret={!s}".format(
                    env,
                    self.task_id,
                    c_id,
                    c_secret
                )
            )
            status = tmp.status_code
            cnt += 1
            print tmp


    def tag_task(self, variables, tag):
        'tags a task with provided tag'
        env, c_id, c_secret = variables['env'], variables['c_id'], variables['c_secret']
        cnt, status = 0, 400
        while cnt < 3 and status != 200:
            tmp = requests.put(
                "https://{!s}.versafleet.co/api/tasks/{!s}?"
                "client_id={!s}&client_secret={!s}".format(
                    env,
                    self.task_id,
                    c_id,
                    c_secret
                ),
                json={
                    'task_attributes':{
                        'tag_list':[
                            tag
                        ]
                    }
                }
            )
            status = tmp.status_code
            cnt += 1

    def get_zone(self, polygon_dict):
        '''
        Find the zone of a task
        Return in text format
        '''
        p = Point(self.lat, self.lng)
        for zone, plygn in polygon_dict.iteritems():
            if plygn.contains(p):
                break
        return zone.split('-')[0]

    def deconflict_tags(self, variables, polygon_dict):
        'worker task to remove and retag task'
        self.tag_task(variables, '')
        zone = self.get_zone(polygon_dict)
        self.tag_task(variables, zone)


def write_to_log(logfn, logtext):
    with open(logfn, 'a') as f:
        f.write(datetime.strftime(
            datetime.utcnow() + timedelta(hours=8),
            '%y-%m-%dT%H:%M:%S+08:00 | '
        ))
        f.write(logtext + '\n')


def get_times(tzoffset):
    '''
    Given a tzoffset int in hours (6hours for this client)
    return a FROM time object & TO time object

    KNOWN BUGS: Negative Time Zones
    '''
    current_dt = datetime.utcnow() + timedelta(hours=tzoffset)
    return (datetime.strftime(current_dt,
                              '%Y-%m-%dT06:00:00+08:00'),
            datetime.strftime(current_dt + timedelta(days=1),
                              '%Y-%m-%dT05:59:59+08:00'))


def get_all_tasks(varibales, time_from, time_to, per_pg, archived):
    '''
    Get all tasks
    '''
    env, c_id, c_secret = variables['env'], variables['c_id'], variables['c_secret']
    task_list = []
    pg = 1
    acted_on, total_tasks = 0, 999999999
    while acted_on < total_tasks:
        tmp = requests.get(
            "https://{!s}.versafleet.co/api/tasks?"
            "client_id={!s}&client_secret={!s}"
            "&page={!s}&per_page={!s}"
            "&from_datetime={!s}&to_datetime={!s}&archived={!s}".format(
                env,
                c_id,
                c_secret,
                pg,
                per_pg,
                time_from,
                time_to,
                archived
            )
        )
        for t in tmp.json()['tasks']:
            task_list.append(task(t))
        acted_on += len(tmp.json()['tasks'])
        total_tasks = tmp.json()['meta']['total']
        pg += 1
        if acted_on != 0 and VERBOSE:
            print "GOT {!s} / {!s} tasks".format(acted_on, total_tasks)
            print tmp
    return task_list



variables = {
    'env': ENV,
    'c_id': CLIENT_ID,
    'c_secret': CLIENT_SECRET
}
time_from, time_to = get_times(2)
task_list = get_all_tasks(variables, time_from, time_to, 20, 0)

invoice_dict = {}
retag_log = []
duplicate_log = []

for t in task_list:
    try:
        invoice_dict[t.invoice] += [t]
    except KeyError:
        invoice_dict[t.invoice] = [t]
    if len(t.tags) > 1:
        t.deconflict_tags(variables, POLYGON_DICT)
        retag_log.append(t.task_id)

for k,v in invoice_dict.iteritems():
    if len(v) > 1 and k != None:
        task_dict = {}
        for t in v:
            task_dict[t.task_id] = t
        task_ids = sorted(task_dict.keys())[:-1]
        print task_ids
        for archive_t_id in task_ids:
            task_dict[archive_t_id].archive_task(variables)
        duplicate_log.append(', '.join(str(n) for n in task_dict.keys()))


write_to_log(LOGFN, 'Processed {0} tasks'.format(len(task_list)))

if len(retag_log) > 0:
    write_to_log(LOGFN, 'Retagged {!s}'.format(len(retag_log)))
    write_to_log(LOGFN, 'Retagged the following: {!s}'.format(', '.join(
        str(n) for n in retag_log)))

if len(duplicate_log) > 0:
    write_to_log(LOGFN, 'Archived {!s}'.format(len(duplicate_log)))
    write_to_log(LOGFN, 'Archived all but the last of the following: {!s}'.format(
        '\n'.join(duplicate_log)
    ))

write_to_log(LOGFN, '\n')
