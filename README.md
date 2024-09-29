# ntu_admissions

Install python from here: https://www.python.org/downloads/

On Windows, to create a python environment, run following command in cmd:

python -m venv env

Then run following command to activate virtual environment:

env\Scripts\activate

Then run following command to install all requirements:

pip install -r requirements.txt

To run the chatbot, run following command:

python rag.py

To scrap data from the ntu website, run following command and wait to for it to complete:

python scrapping.py

Fresh data will be stored in the output.txt file which is further used by the chatbot as a knowledge base for RAG(Retrieval Augmented Generation)
