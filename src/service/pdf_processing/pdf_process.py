import logging
import os
import pdfplumber
import tabula
import json

class pdf_process_class:

    def __init__(self):
        
        """
        This class processes the PDF input data and does the following :-
        a) Extracts all the text from the PDF.
        b) Identifies and extracts tables from the document.
        c) Identifies and extracts all headings in the document.

        2 packages named pdfplumber and tabula are used for the above purposes.

        LOG_FILE_PATH - the path for log file where logs will be stored.
        paths set for different operating systems, so that the code can work for different OS.
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


    def extract_text_from_pdf(self, input):

        """
        function defined to extract all the text from the PDF input
        Function extract_text() extracts the text from the PDF.
        """

        try:

            with pdfplumber.open(input) as pdf_input:

                all_text = ''

                for page in pdf_input.pages:
                    text = page.extract_text()
                    all_text += text + '\n'

            return all_text

        except Exception as extract_text_ERR:
            logging.error('failed to extract the text from the PDF file', exc_info=extract_text_ERR)


    def extract_tables_from_pdf(self, input):

        """
        function defined to extract all the tables from the PDF input
        Function read_pdf() of tabula reads the pdf and returns the tables present in it
        """

        try:

            tables = tabula.read_pdf(input, pages='all')

            return tables


        except Exception as extract_tables_ERR:
            logging.error('failed to extract tables from the PDF file', exc_info=extract_tables_ERR)


    def extract_headings_from_pdf(self, input):

        """
        function defined to extract all the headings from the PDF input
        Reference - https://stackoverflow.com/questions/70802394/extract-pdf-pages-based-on-header-text-in-python
        In this function, I am asuming text headings as bold texts present in the corpus. 
        (This assumption is not enough to extract headings as not all bold texts are heading. I did considered text size as attribute in
        which I will return the text(s) with max fontsize but the corpus might contain text with fontsize bigger but may not be a heading.
        I considered frequency of the texts sizes as well, wherein I will consider text(s) with lowest frequency, considering number of headers
        are less than the normal size text. But this can also bu ruled out as text with lower size might be very less in corpus.)
        """

        try:
            
            with pdfplumber.open(input) as pdf_input:

                all_headings = []

                for i in range(len(pdf_input.pages)):
                    word_data = pdf_input.pages[i].extract_words(extra_attrs = ['fontname'])
                    json_text = json.loads(json.dumps(word_data))
                    headings = [item['text'] for item in json_text if '-B' in (item['fontname'])]

                    for heading in headings:
                        all_headings.append(heading)

            return all_headings


        except Exception as extract_headings_ERR:
            logging.error('failed to extract headings from the PDF file', exc_info=extract_headings_ERR)