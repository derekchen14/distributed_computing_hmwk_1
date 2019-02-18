import requests
import json

def make_request(action):
  url = "http://18.218.116.164:8000/admin/djangoApp/studentinfo/"

  if action == "create":
    payload = {"student_id": 10, "student_year": 2017,
               "student_name": "John Smith",
               "registered_courses": "distributed computing"}
    result = requests.post(url, params)
  elif action == "read ":
    result = requests.get(url)
  elif action == "update":
    payload = {"student_id": 10,
               "student_name": "Barack Obama"}
    result = requests.put(url, params)
  elif action == "delete":
    params = {"student_id": 10}
    result = requests.delete(url, params)

  return result.json() if result.status_code == 200 else result.error_message


if __name__ == "__main__":
  for action in ["read ", "create", "update", "delete"]:
    result = make_request(action)
    gerund_form = action[:-1] + "ing"
    print("result from {}:".format(gerund_form))
    print(json.dumps(result, indent=4))
