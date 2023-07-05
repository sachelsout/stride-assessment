import logging
import os
import streamlit as st

# importing other required .py files/classes
from input.input_data import input_class
from text_processing.text_process import text_process_class
from pdf_processing.pdf_process import pdf_process_class

class MergerService:

    def __init__(self):
        
        """
        This class merges all the other classes/functions of .py files using considered logic.

        Here we will merge input, text process and pdf process related classes/functions/.py files.

        LOG_FILE_PATH - the path for log file where logs will be stored.
        paths set for different operating systems, so that the code can work for different OS.
        Required classes called and self variable assigned to them.
        """
        
        try:
            
            if os.name == 'nt':
                LOG_FILE_PATH = '/'.join(
                    (os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1]) + '/logFile'
                os.makedirs(LOG_FILE_PATH, exist_ok=True)

            elif os.name == 'posix':
                LOG_FILE_PATH = '/'.join(os.path.abspath(
                    __file__).split('/')[:-1]) + '/logFile'
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

            self.input = input_class()
            self.text = text_process_class()
            self.pdf = pdf_process_class()

        except Exception as config_ERR:
            logging.error('config_ERR', exc_info=config_ERR)

    
    def merge(self):
        
        """
        This function basically executes the code from different .py files in a way we want. 
        e.g. here we consider 2 inputs (text and pdf) and then processing of those respective inputs

        In the below code, the buttons for performing different processing tasks (for both text and pdf) will be visible
        in the web app once the user enters the required input data (string text or pdf file).
        """
        
        try:
            
            image_url = "https://stride.ai/static/media/stride-logo.2c005be3d07610026e385714dbd0445b.svg"
            st.image(image_url, width=200)
            
            ########### TEXT #############
            st.title('Stride NLP Assessment')
            st.markdown("<hr>", unsafe_allow_html=True)

            text_input = self.input.text_input()

            if text_input and not text_input.strip().isdigit():
                if st.button("Generate Word Tokens"):
                    tokens = self.text.tokenize(input=text_input)
                    st.header("Word Tokens")
                    st.write(tokens)
                
                if st.button("Generate POS Tags"):
                    pos_tags = self.text.pos_tagging(input=text_input)
                    st.header("POS (Parts of Speech) Tags")
                    st.write(pos_tags)
                
                if st.button("Generate NER Tags"):
                    ner_tags = self.text.named_entity_recognition(input=text_input)
                    st.header("NER (Named Entity Recognition) Tags")
                    st.write(ner_tags)

                if st.button("Generate NER Tags Frequency"):
                    ner_freq = self.text.named_entity_frequency(input=text_input)
                    st.header("NER (Named Entity Recognition) Tags Frequency")
                    st.write(ner_freq)

            ########## PDF ##############
            st.markdown("<hr>", unsafe_allow_html=True)
            pdf_input = self.input.pdf_input()

            if pdf_input is not None:
                if st.button("Extract text from PDF"):
                    extracted_text = self.pdf.extract_text_from_pdf(input=pdf_input)
                    st.header("Extracted Text from PDF File")
                    if len(extracted_text) == 0:
                        st.write('Text is not present in this PDF.')
                    else:
                        st.write(extracted_text)

                if st.button("Extract tables from PDF"):
                    extracted_tables = self.pdf.extract_tables_from_pdf(input=pdf_input)
                    st.header("Extracted Tables from PDF File")
                    if len(extracted_tables) == 0:
                        st.write('Table is not present in this PDF.')
                    else:
                        st.write(extracted_tables)

                if st.button("Extract headings from PDF"):
                    extracted_headings = self.pdf.extract_headings_from_pdf(input=pdf_input)
                    st.header("Extracted Headings from PDF File")
                    if len(extracted_headings) == 0:
                        st.write('Heading is not present in this PDF.')
                    else:
                        st.write(extracted_headings)      

        except Exception as merge_ERR:
            logging.error('failed to merge the classes and the functions', exc_info=merge_ERR)
            return False