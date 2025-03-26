import json

def check_creativity_score(project_data):
    creativity_score = 0

    # with open(project_json, "r") as json_file:
    #     project_data = json.load(json_file)


    for type in project_data:
        if(type == "motion"):
            creativity_score += 0.5 * project_data[type]

        if(type == "looks"):
            creativity_score += 0.5 * project_data[type]

        if(type == "sound"):
            creativity_score += 1 * project_data[type]
        
        if(type == "events"):
            creativity_score += 1 * project_data[type]
    
    return creativity_score
