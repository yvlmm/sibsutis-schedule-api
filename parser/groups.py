groups_id = {
    "ИВ-421": "483",
    "ИВ-422": "486",
    "ИКС-431" : "235",
    "ИКС-432" : "236",
    "ИКС-433" : "237"
}

def find_group(group):
    group_id = groups_id.get(group)
    if group_id:
        return group_id
    else:
        return None 

def find_group_name(group_id):
    for group, id in groups_id.items():
        if id == group_id:
            return group
    return None