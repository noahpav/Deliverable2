import os
import csv

# Paths to the team folders, events folder, images folder
mens_team_folder = '/Users/noahpav/Desktop/SI339/deliverable2/data/athletes/mens_team'
womens_team_folder = '/Users/noahpav/Desktop/SI339/deliverable2/data/athletes/womens_team'
events_folder = '/Users/noahpav/Desktop/SI339/deliverable2/data/meets'
images_folder = '/Users/noahpav/Desktop/SI339/deliverable2/images'
html_file_path = '/Users/noahpav/Desktop/SI339/deliverable2/index.html'

# Base URL for images relative to the HTML file location
image_base_path = '/images/'

# HTML template as a multi-line string
html_template = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, intitial-scale=1.0" />
    <title>Organization Home Page</title>
    <!-- <link rel="stylesheet" href="css/reset.css" />
    <link rel="stylesheet" href="/css/styles.css" /> -->
    <!-- <script defer src="/scripts/scripts.js"></script> -->
  </head>
  <body>
    <header>
      <div class="top-banner">
        <a href="index.html">Home Page - Ann Arbor Skyline</a>
      </div>
    </header>
    <nav class="navbar">
      <ul>
        <li><a href="#about">About</a></li>
        <li><a href="#events">Events</a></li>
        <li><a href="#accomplishments">Records</a></li>
        <li><a href="#staff">Staff</a></li>
        <li><a href="#gallery">Media</a></li>
        <li><a href="#search" class="search-icon">🔍</a></li>
      </ul>
    </nav>
    <main class="content-section">
      <!-- Teams Section -->
      <section id="teams-section" class="teams-section">
        <h1>Teams</h1>

        <div class="team-container">
          <!-- Mens Team -->
          <div class="team">
            <h2>Men's Team</h2>
            <table>
              <caption>
                Athlete Name
              </caption>
              <tr>
                <!-- Loop through and add the name of each athlete on mens_team -->
                <!-- Each athlete name will serve as a link that takes you too their individual athlete page -->
                <!-- Each page will include School, Class, Recent Races and times/finishes, accomplishments, progression graph, etc. -->
                <td>{athlete_name}</td>
              </tr>
            </table>
          </div>

          <!-- Womens Team -->
          <div classs="team">
            <h2>Women's Team</h2>
            <table>
              <caption>
                Athlete Name
              </caption>
              <tr>
                <!-- Loop through and add the name of each athlete on womens_team -->
                <!-- Each athlete name will serve as a link that takes you too their individual athlete page -->
                <!-- Each page will include School, Class, Recent Races and times/finishes, accomplishments, progression graph, etc. -->
                <td>{athlete_name}</td>
              </tr>
            </table>
          </div>
        </div>
      </section>

      <!-- Events Section -->
      <section id="events" class="content">
        <div>
            <h2>Season Calendar</h2>
            <ul>
                <li>August 18, 2023 - <a href=https://www.athletic.net/CrossCountry/meet/221431/info>Lamplighter
                        Invite</a></li>
                <li>September 9, 2023 - <a href=https://www.athletic.net/CrossCountry/meet/221738/info>Bret Clemets Bath
                        Invitational</a></li>
                <li>May 15, 2025 - National Meet</li>
                <li>June 20, 2025 - Off-Season Start</li>
            </ul>
        </div>
        <div class="events">
          <h1>Past Events</h1>
          {event_section}
          <!-- Loop through and add the name and date of each event -->
          <!-- <table>
            <caption>
              Events from {meet_name}
            </caption>
            <tr>
              <th>Event Name</th>
              <th>Event Date</th>
            </tr>
            <tr>
              <td>{event_name}</td>
              <td>{event_date}</td>
            </tr>
          </table> -->
        </div>
      </section>

      <section id="accomplishments">
        <h2>Team Accomplishments for the Season</h2>

        <div class="accomplishments" id="top-times">
            <h3>Top 3 Athlete Performances</h3>
                <ul>
                    <li>Athlete 1 - time at Meet A</li>
                    <li>Athlete 2 - time at Meet B</li>
                    <li>Athlete 3 - time at Meet C</li>
                </ul>
        </div>

        <div class="accomplishments" id="best-performance">
            <h3>Best Team Performance of the Season</h3>
            <p>Meet: Championship Meet</p>
            <p>Place: 1st Place</p>
        </div>

        <div class="remarks">
            <h3>Coach's Remarks</h3>
            <p id="coachs-remarks">comments here.</p>
        </div>
    </section>

      <!-- Photo Gallery Section -->
      <section id="gallery" class="content">
        <div class="gallery">
          <h1>Photo Gallery</h1>
          {gallery_section}
        </div>
      </section>
    </main>

    <!-- Contact Section -->
    <footer>
      <div class="contact">
        <h1>Contact Us</h1>
        <p>Email: contact@xcountry.org</p>
        <p>Phone: (123) 456-7890</p>
        <p>Address: 123 XCountry Lane, City, State, ZIP</p>
      </div>
    </footer>
  </body>
</html>

"""

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
                    image_path = f"images/{event_name}/{image_file}"
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

# Insert dynamic content into the HTML template
html_output = html_template.replace("{athlete_name}", mens_team_html + womens_team_html)
html_output = html_output.replace("{event_section}", events_html)
html_output = html_output.replace("{gallery_section}", gallery_html)

# Save the updated HTML content to a file
with open("output.html", 'w') as output_file:
    output_file.write(html_output)

print("HTML template with dynamic data has been generated and saved as 'output.html'.")
