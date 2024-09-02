import requests
import json


def make_api_request(url: str, output_file: str = None, return_data=False):
    headers = {
        'Access-Token': "54d68e2c854b693dd235ffa5c38b9f888961178e8e69e05f54774df34a18cf14"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        resp_data = response.json()
        if return_data:
            return resp_data
        with open(output_file, 'w') as f:
            json.dump(resp_data, f, indent=4)
    else:
        raise Exception(f"Could not fetch response: {response.status_code}")


def get_questions():
    for i in range(1000):
        api_url = f"https://api1.heycoach.in//api/code_problems/{i}"
        make_api_request(api_url, f"problems/q{i}.json")


api_map = {
    "classes_sessions.json": "https://api1.heycoach.in//api/programs/sessions",
    "placement_pools.json": "https://api1.heycoach.in//api/placement_pools",
    "user_progression.json": "https://api1.heycoach.in//api/users/11339/learner_progress_details",
    "user_details.json": "https://api1.heycoach.in//api/users/11339",
    "resources.json": "https://api1.heycoach.in//api/programs/resources"
}


def fetch_updated_data():
    for file_name, url in api_map.items():
        make_api_request(url, file_name)


data = make_api_request("https://api1.heycoach.in//api/programs/resources", None, True)
for item in data:
    temp_item = {
        "id": 1926,
        "title": "Time Complexity",
        "link": None,
        "resource_type": "file",
        "session_id": 5296,
        "added_by": 30,
        "created_at": "2024-05-02T06:34:11.282Z",
        "resource_context": "pre_read",
        "completed": True,
        "topics_entities": []
    }
    if item["resource_type"] == "file":
        get_resource_url = f"https://api1.heycoach.in//api/resources/{item['id']}/resource_file"
        resp = make_api_request(api_map['resources.json'], None, True)
        print(resp)
        break
