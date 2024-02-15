import requests

API_URL = "http://localhost:8000"


def add_stakeholder(name, role):
    url = f"{API_URL}/stakeholder"
    data = {"name": name, "role": role}
    response = requests.post(url, json=data)
    return response.json()


def get_stakeholders():
    url = f"{API_URL}/stakeholders"
    response = requests.get(url)
    return response.json()


def update_stakeholder(stakeholder_id, updated_data):
    url = f"{API_URL}/stakeholder/{stakeholder_id}"
    response = requests.put(url, json=updated_data)
    return response.json()


def delete_stakeholder(stakeholder_id):
    url = f"{API_URL}/stakeholder/{stakeholder_id}"
    response = requests.delete(url)
    return response.json()


def delete_all_stakeholders():
    stakeholders = get_stakeholders()  # Retrieve all stakeholders
    for stakeholder in stakeholders:
        delete_stakeholder(stakeholder['id'])  # Delete each stakeholder by ID




delete_all_stakeholders()

print(get_stakeholders())