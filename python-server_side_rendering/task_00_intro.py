def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print ("Error: template must be a string!")
        return
    # vérifie que 'attendees' est une liste de dico
    if not isinstance(attendees, list) or not all(isinstance(person, dict) for person in attendees):
        print("Error: attendees must be a list of dictionaries!")
        return
    # vérifie si le template est vide 
    if template.strip() == "":
        print ("The model is empty, no output file is generated")
        return
    # vérifie si la liste attendees est vide
    if not attendees:
        print ("No data is supplied and no output file is generated")
        return
    
    replace_fields = ["name", "event_title", "event_date", "event_location"]
    # Boucle sur chaque invité avec son index
    for index, person in enumerate(attendees, start=1):
        invitation_text = template

        # Remplacement de chaque champ
        for key in replace_fields:
            value = person.get(key)  # récupère la valeur dans le dictionnaire !
            if not value:  # si None ou vide ou absent
                value = "N/A"
            invitation_text = invitation_text.replace("{" + key + "}", value)

        