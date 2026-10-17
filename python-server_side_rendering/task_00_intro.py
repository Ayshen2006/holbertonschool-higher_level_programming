#!/usr/bin/python3
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template

        for placeholder in (
            "name",
            "event_title",
            "event_date",
            "event_location",
        ):
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            content = content.replace("{" + placeholder + "}", str(value))

        try:
            with open(f"output_{index}.txt", "w") as file:
                file.write(content)
        except OSError as error:
            print(f"Error writing output_{index}.txt: {error}")
