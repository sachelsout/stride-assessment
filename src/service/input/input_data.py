import logging
import os
import streamlit as st
import string

class input_class:

    def __init__(self):
        
        """
        This class returns inputs (obtained from Streamlit web app) like text input and pdf input, which are further required.
        LOG_FILE_PATH - the path for log file where logs will be stored.
        Paths set for different operating systems, so that the code can work for different OS.
        """

        try:

            if os.name == 'nt':
                LOG_FILE_PATH = '/'.join(
                    (os.path.abspath(__file__).replace('\\', '/')).split('/')[:-2]) + '/logFile'
                os.makedirs(LOG_FILE_PATH, exist_ok=True)

            elif os.name == 'posix':
                LOG_FILE_PATH = '/'.join(os.path.abspath(
                    __file__).split('/')[:-2]) + '/logFile'
                os.makedirs(LOG_FILE_PATH, exist_ok=True)
            else:
                raise OSError('untested OS')

        except Exception as file_dir_ERR:
            logging.error('file_dir_ERR', exc_info=file_dir_ERR)

        try:
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s.%(msecs)-3d:%(filename)s:%(funcName)s:%(levelname)s:%(lineno)d:%(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S',
                                filename=LOG_FILE_PATH + '/logger.log',
                                force=True)

        except Exception as config_ERR:
            logging.error('config_ERR', exc_info=config_ERR)


    def text_input(self):

        """
        This function takes user text input on the web app.
        text_area() function is simply a bigger box to enter the text.
        Only string data is considered. Digits not allowed. Punctuation marks removed as well.
        """

        try:
            st.title('1. Text Processing 🔤')

            text_input = st.text_area('Enter the input text (string format) for text processing')

            if text_input and not text_input.strip().isdigit():

                translator = str.maketrans('', '', string.punctuation)
                text_without_punctuation = text_input.translate(translator)
                
                return text_without_punctuation
            
            elif text_input:
                st.write('Invalid input, please enter a valid string.')
            
        except Exception as text_input_ERR:
            logging.error('failed to take user text input for text processing', exc_info=text_input_ERR)


    def pdf_input(self):

        """
        This function takes pdf file as an input on the web app.
        Only PDF file will be uploaded from local storage.
        """

        try:
            st.title('2. PDF Processing 📒')

            pdf_input = st.file_uploader('Upload a PDF file', type=["pdf"])

            return pdf_input
            
        except Exception as pdf_input_ERR:
            logging.error('failed to take pdf input for pdf processing', exc_info=pdf_input_ERR)