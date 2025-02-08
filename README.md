The project is a web application that uses Flask to interact with prediction data extracted from a Teachable Machine model. The goal is to display these predictions in a simple user interface using an interactive HTML page.

Project Structure
The project consists of:
- Flask Backend: Processes data and displays predictions from the SQLite database.
- HTML Pages: For displaying the user interface (split into pages to show predictions and the home page).
- Teachable Machine: Used a Teachable Machine model to analyze images in real-time.

Workflow
1. Setting up Flask:
   - Flask was used to create a simple web application.
   - A server was created to serve HTML pages and interact with the user.
   - A main route (/) was created to display the home page, and another route (/get_predictions) was created to display predictions.

2. Database:
   - An SQLite database called detections.db was created to store predictions.
   - A table called predictions was added with the following columns: id, label, probability.

3. Adding Data:
   - Some sample data was added to the database using a Python script.
   - The data includes the label (e.g., iPhone, Laptop) and the probability (e.g., 99%).

4. HTML Pages:
   - index.html: A welcome page with a button to trigger predictions.
   - predictions.html: A page to display the results of predictions stored in the database, with a table showing id, label, and probability.
   - app.html: A page with a webcam to capture images and analyze them using the Teachable Machine model, then send predictions to the server.

5. Interacting with Teachable Machine:
   - The Teachable Machine model was used to analyze images in real-time.
   - Predictions from the model were sent to the server via POST requests using JavaScript.

6. Back to Home Button:
   - In the predictions.html page, a "Back to Home" button is located at the bottom of the page.
   - This button is used to return to the home page (which displays the button to open predictions).
   - When clicked, it redirects the user back to the first page (/), providing an easy way to navigate between pages in the app.

 7: I ran the application using Python by typing python app.py in the command prompt. After running, the application can be accessed through the local link 
 http://127.0.0.1:5000

![alt](https://github.com/aishah8/Flask-Web-App-for-Teachable-Machine/blob/630bfb6c25d9400266da775193973304fb97d227/im1.png)
![alt](https://github.com/aishah8/Flask-Web-App-for-Teachable-Machine/blob/74c7e3fa91dd565a4b6b3d80ff14354d27e711b6/ime2.png)
