import requests
import json
import pdb

def make_request(action):
  url = "http://18.218.116.164:8000/djangoApp/"

  if action == "create":
    payload = {"STUDENT_ID": 8, "STUDENT_YEAR": 2019,
               "STUDENT_NAME": "Ishan Ishikawa",
               "REGISTERED_COURSES": "Intelligence of an Artificial Nature"}
    result = requests.post(url, data=payload)
  elif action == "read":
    student_id = 3
    url = url + str(student_id)
    result = requests.get(url)
  elif action == "update":
    student_id = 8
    url = url + str(student_id)
    payload = {
    "STUDENT_ID": 8,
    "STUDENT_NAME": "Ishan Ishikawa",
    "STUDENT_YEAR": 2019,
    "REGISTERED_COURSES": "Artificial Intelligence"}
    result = requests.put(url, data=payload)
  elif action == "destroy":
    student_id = 8
    url = url + str(student_id)
    result = requests.delete(url)
  elif action == "list":
    result = requests.get(url)

  if result.status_code in [200, 201, 202, 203, 204]:
    return result
  else:
    result.raise_for_status()

action_mapping = {
    "create": "creating",
    "read": "reading",
    "update": "updating",
    "destroy": "deleting",
}

if __name__ == "__main__":
  for action in ["read", "create", "update", "destroy"]:
    result = make_request(action)
    print("Raw result from {}: ".format(action_mapping[action]) )
    print(result.text)

    action = "read"
    listing = make_request("list")
    print("Full table after {}: ".format(action_mapping[action]) )
    print(json.dumps(listing.json(), indent=4))
