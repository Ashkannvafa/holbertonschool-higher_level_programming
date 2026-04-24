#!/usr/bin/python3
"""Generate invitation files from template and attendee data."""


def generate_invitations(template, attendees):
    """Generates personalized invitation files."""
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, 1):
        name = attendee.get("name") or "N/A"
        title = attendee.get("event_title") or "N/A"
        date = attendee.get("event_date") or "N/A"
        location = attendee.get("event_location") or "N/A"

        content = template
        content = content.replace("{name}", str(name))
        content = content.replace("{event_title}", str(title))
        content = content.replace("{event_date}", str(date))
        content = content.replace("{event_location}", str(location))

        filename = "output_{}.txt".format(i)
        with open(filename, "w") as f:
            f.write(content)
