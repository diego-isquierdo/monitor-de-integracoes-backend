import json


def json_converts(obj_json):
    response_json=[]
    obj={"ticket":"","status":"","last_action":"","actions":"","title":"","pendency":"","pending_time":""}
    
    for x in obj_json:
        obj['actions'] = x['actionCount']
        obj['status'] = x['status']
        obj['title'] = x['subject']
        obj['ticket'] = x['id']
        
