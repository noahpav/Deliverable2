import os
import csv

# Paths to the team folders, events folder, images folder, and HTML file
mens_team_folder = '/Users/noahpav/Desktop/SI339/deliverable2/data/athletes/mens_team'
womens_team_folder = '/Users/noahpav/Desktop/SI339/deliverable2/data/athletes/womens_team'
events_folder = '/Users/noahpav/Desktop/SI339/deliverable2/data/meets'
images_folder = '/Users/noahpav/Desktop/SI339/deliverable2/images'
html_file_path = '/Users/noahpav/Desktop/SI339/deliverable2/index.html'

# Base URL for images relative to the HTML file location
image_base_path = '/images/'

# Function to get the first line (athlete's name) from each CSV file
def get_athlete_names(folder):
    athlete_names = []
    for filename in os.listdir(folder):
        if filename.endswith('.csv'):
            with open(os.path.join(folder, filename), 'r') as csv_file:
                reader = csv.reader(csv_file)
                athlete_name = next(reader)[0]  # Get the first line, first column (athlete's name)
                athlete_names.append(athlete_name)
    return athlete_names

# Function to parse the meet name, event name, and event date from the CSV files
def get_meet_and_event_details(folder):
    meets = {}
    for filename in os.listdir(folder):
        if filename.endswith('.csv'):
            with open(os.path.join(folder, filename), 'r') as csv_file:
                reader = csv.reader(csv_file)
                meet_name = next(reader)[0].strip()  # First line contains the meet name
                event_name = next(reader)[0].strip()  # Second line contains the event name
                event_date = next(reader)[0].strip()  # Third line contains the event date

                if meet_name not in meets:
                    meets[meet_name] = []
                meets[meet_name].append((event_name, event_date))  # Store events under the meet name

    return meets

# Function to generate HTML list of athlete names
def generate_athlete_list_html(team_names):
    list_html = ""
    for name in team_names:
        list_html += f"<tr><td>{name}</td></tr>\n"
    return list_html

# Function to generate the event section dynamically
def generate_event_section_html(meets):
    html_content = ""
    for meet_name, events in meets.items():
        table_html = f"""
        <table>
          <caption>Events from {meet_name}</caption>
          <tr>
            <th>Event Name</th>
            <th>Event Date</th>
          </tr>
        """
        for event_name, event_date in events:
            table_html += f"""
            <tr>
              <td>{event_name}</td>
              <td>{event_date}</td>
            </tr>
            """
        table_html += "</table>\n"
        html_content += table_html

    return html_content

# Function to generate the photo gallery for events with inline styles
def generate_gallery_html(events_folder):
    gallery_html = ""

    # Iterate over each folder in the images folder (each folder corresponds to an event)
    for event_name in os.listdir(events_folder):
        event_path = os.path.join(events_folder, event_name)

        if os.path.isdir(event_path):  # Ensure it's a directory
            # Start creating a section for each event
            gallery_html += f"""
            <div class="event-gallery">
              <h2>{event_name}</h2>
              <div class="photos">
            """

            # Add images for this event with inline styles for size
            for image_file in os.listdir(event_path):
                if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    # Use the base image path and event folder name to build the full path
                    image_path = f"{image_base_path}{event_name}/{image_file}"
                    # Add inline styles to the img tag
                    gallery_html += f"""
                    <img src="{image_path}" alt="Photo from {event_name}" class="gallery-image" style="width: 150px; height: auto; margin: 5px;">
                    """

            gallery_html += "</div></div>\n"  # Close the event gallery section

    return gallery_html

# Get athlete names from men's and women's teams
mens_team_names = get_athlete_names(mens_team_folder)
womens_team_names = get_athlete_names(womens_team_folder)

# Get meet and event details from the CSV files
meets_data = get_meet_and_event_details(events_folder)

# Generate the athlete list, event section, and photo gallery
mens_team_html = generate_athlete_list_html(mens_team_names)
womens_team_html = generate_athlete_list_html(womens_team_names)
events_html = generate_event_section_html(meets_data)
gallery_html = generate_gallery_html(images_folder)

# Read the HTML file
with open(html_file_path, 'r') as html_file:
    html_content = html_file.read()

# Replace placeholders in the HTML
html_content = html_content.replace("{athlete_name}", mens_team_html, 1)  # Replace for men's team
html_content = html_content.replace("{athlete_name}", womens_team_html, 1)  # Replace for women's team
html_content = html_content.replace("{event_section}", events_html)  # Replace event section
html_content = html_content.replace("{gallery_section}", gallery_html)  # Replace gallery section

# Save the updated HTML file
with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)

print("Athlete names, event details, and photo gallery with inline styles have been inserted into the HTML file.")
