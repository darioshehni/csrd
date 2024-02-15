from manage import add_stakeholder, get_stakeholders, update_stakeholder, delete_stakeholder, delete_all_stakeholders


def test_1():
    # Adding stakeholders
    add_stakeholder("John Doe", "Project Manager")
    add_stakeholder("Jane Smith", "Software Developer")

    # Getting all stakeholders
    stakeholders = get_stakeholders()
    print(stakeholders)

    # Updating a stakeholder
    update_stakeholder(1, {"name": "John Doe Updated", "role": "Senior Project Manager"})

    # Deleting a stakeholder
    delete_stakeholder(2)

    # Getting all stakeholders to verify deletion
    stakeholders = get_stakeholders()
    print(stakeholders)