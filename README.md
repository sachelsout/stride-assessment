# Stride Assessment (Code) 📓
This project has the production grade code service built for solving 2 processing problems - text processing and PDF processing.<br>
The coding files can be run on local machine Streamlit as well as Streamlit Cloud.

## Web App (streamlit)
I have created a streamlit app on streamlit cloud. Here is the link - https://stride-assessment.streamlit.app/ . Do check it out !<br>
<b>NOTE - Everything works well on cloud app except tabula. The app doesn't shows the extracted tabular data on UI. It is visible though on local app. Will dive deep into the issue and resolve soon.</b> 😄

## Project Structure
Here is the Project Structure which I am following, to have a modular code, easy to understand the whole service. It has logFile as well, which will store logs. The code is well documented, followed best python coding practices like logging with timestamp, exception handling, OOPS, OS handling, etc.
![Project Kickoff Team Whiteboard in Pink Green Trendy Stickers Style](https://github.com/sachelsout/stride-assessment/assets/86348193/c21c526c-bc91-451a-afc0-37d6749c473c)


## Running the Code (local Streamlit)
### Open the stride-assessment folder in your favorite IDE and Install the required libraries
```
pip install -r requirements.txt
```

### Run the app (change the directory where app.py is present)
```
streamlit run app.py
```
A new window will be opened up on local url http://localhost:8501/ where you'll see the UI of the app which basically has 2 sections.
1. Text Processing 🔤
2. PDF Processing 📒
![image](https://github.com/sachelsout/stride-assessment/assets/86348193/0bac06c8-244b-4335-9285-6e9e31390c63)

### 1. Text Processing 🔤
Enter the input text and click Ctrl+Enter to apply. If you enter digits, it will shoot a message 'Invalid input, please enter a valid string.'. So, enter a string input. Once you enter the input, 4 buttons will appear, each for a process function, which is given for Text Processing task. Click on these buttons and generate required preprocessed data !! <br>
![image](https://github.com/sachelsout/stride-assessment/assets/86348193/e63dd2b1-a3e0-4d90-8530-f35c75fef41b) <br>
### 2. PDF Processing 📒
Here, you will have an option to upload a PDF File from your local machine. Only PDF Files are allowed to uplaod. You can drag and drop the file as well. After you upload a file, 3 buttons will appear, each for a process function, which is given for PDF Processing task. Click on these buttons and generate required preprocessed data !! <br>
![image](https://github.com/sachelsout/stride-assessment/assets/86348193/ee14ef2c-899b-487a-b64f-b1173d27d679) <br>
## Future changes/improvements 💡
1. The current version of the service works pretty well for processing both text and pdf data. In future, would solve the streamlit cloud issue for tabula-py package.
2. Improving the extraction of tables (when complicated data is involved).
3. Improving headings extraction from pdf file. Currently considering only bold text as headings.
4. Improvements in UI of streamlit web app, exploring buttons, forms more. 
