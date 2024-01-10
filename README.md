# web_app_stat

This web application utilizes the ISRO Stats RESTful API to display launch history statistics in graphical format.

## Features
1. **Launches History - Per Year**: Stacked bar graph showing the year vs mission status (unsuccessful and successful).
2. **Launches History - Per Rocket**: Pie chart showing launches count per rocket.
3. **Launches History - Overall Success Rate**: Doughnut chart displaying the success and unsuccessful rates.

## Getting Started

### Prerequisites
- Python 3.x
- Flask (`pip install Flask`)

### Installation
1. Clone the repository:
    git clone https://github.com/cswapnali/web_app_stat.git
2. Change into the project directory:
    cd web_app_stat
3. Install dependencies:
    pip install -r requirements.txt
   
### Running the Application

1. Run the Flask application:
    python app.py

2. Open your web browser and navigate to http://localhost:5000.

## Documentation
The web application uses Chart.js for rendering graphs. The API endpoint is expected to return JSON data in a specific format. Adjust the Chart.js configurations in `index.html` based on the structure of the ISRO Stats API response.

## Screenshots:
Please refer to the following Google Drive link to access screenshots and a demo video of the application: https://drive.google.com/file/d/1rqVs6zPlZIPSL-iWzfCcRnjdD7I96gOR/view?usp=drive_link
