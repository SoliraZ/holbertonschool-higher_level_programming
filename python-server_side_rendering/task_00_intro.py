#!/usr/bin/python3
""" Task 00: Basic Server-Side Rendering """


import os


# Define the function generate_invitations
def generate_invitations(template, attendees):
    """ Generate invitations using the template and attendees list """
    try:
        if not isinstance(template, str):
            raise TypeError("Template is not a string")
        if not isinstance(attendees, list) or not \
                all(isinstance(attendee, dict) for attendee in attendees):
            raise TypeError("Attendees is not a list of dictionaries")
    except TypeError as e:
        print(f"Error : {e}")
        return

    try:
        if not template.strip():
            raise ValueError("Template is empty, no output files generated.")
        if not attendees:
            raise ValueError("No data provided, no output files generated.")
    except ValueError as e:
        print(f"Error : {e}")

    for i, attendee in enumerate(attendees, start=1):
        output_content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            placeholder = "{" + key + "}"
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            output_content = output_content.replace(placeholder, value)
        filename = f"output_{i}.txt"
        if os.path.exists(filename):
            print(f"Warning [{filename}] already exists")
            continue

    with open(filename, 'w') as file:
        file.write(output_content)
