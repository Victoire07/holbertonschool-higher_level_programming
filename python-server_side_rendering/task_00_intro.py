def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print ("Error: template must be a string!")
    if not isinstance(attendees, list) or not all(isinstance(person, dict) for person in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
