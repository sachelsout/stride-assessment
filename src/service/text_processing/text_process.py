import logging
import os
import nltk

# nltk files download
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

class text_process_class:

    def __init__(self):
        
        """
        This class processes the text input data and does the following :-
        a) Tokenizes the string into words.
        b) Tags parts of speech (POS) for each word.
        c) Performs named entity recognition (NER).
        d) Counts the frequency of each named entity in the text.

        Package named nltk is used for performing text processing.

        LOG_FILE_PATH - the path for log file where logs will be stored
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


    def tokenize(self, input):

        """
        function defined to tokenize the input string into words
        Function word_tokenize() returns the words from the input text
        """

        try:
            
            word_tokens = word_tokenize(text=input)
            
            return word_tokens

        except Exception as tokenize_ERR:
            logging.error('failed to convert input string into word tokens', exc_info=tokenize_ERR)


    def pos_tagging(self, input):

        """
        function defined to tag part of speech (POS) for each word token
        Function pos_tag() returns parts of speech tags, here input is word tokens
        """

        try:

            word_tokens = self.tokenize(input=input)
            pos_tags = pos_tag(tokens=word_tokens)
            
            return pos_tags

        except Exception as pos_tags_ERR:
            logging.error('failed to tag POS for word tokens', exc_info=pos_tags_ERR)


    def named_entity_recognition(self, input):

        """
        function defined to perform NER (Named Entity Recognition) on POS (Parts Of Speech) tags
        Function ne_chunk() returns the NER tags, here POS tags are input
        """

        try:

            pos_tags = self.pos_tagging(input=input)
            ner = ne_chunk(tagged_tokens=pos_tags)
            
            return ner

        except Exception as ner_ERR:
            logging.error('failed to get NER tags for POS tags', exc_info=ner_ERR)


    def named_entity_frequency(self, input):

        """
        function defined to count frequency of each named entity in the text
        
        """

        try:
            
            ner_tags = self.named_entity_recognition(input=input)
            named_entity_count = {}
            for i in ner_tags:
                if hasattr(i, 'label'):
                    named_entity = ' '.join(j[0] for j in i.leaves())
                    named_entity_count[named_entity] = named_entity_count.get(named_entity, 0) + 1
            
            return named_entity_count


        except Exception as ner_freq_ERR:
            logging.error('failed to count the frequency of each named entity in the text', exc_info=ner_freq_ERR)