# Disaster Response Pipeline Project

This project demonstrates a simple pipeline for features from audio files.



### Installation:

To setup this project in your own environment, the following libraries need to be installed with python 3.*.:

- Librosa
- Numpy
- pytest
- setuptools

Run the following commands in your project's root directory:
1. Setup a virtual environment and select as interpreter

    ```
    $ python -m venv
    ```
2. Activate the virtual environment

    ```
    $ .venv\Scripts\activate
    ```

3. run pip install -r requirements.txt in your shell


### Instructions:
1. Run the following commands in the project's  preprocessor directory to run the pipeline.

    - To run ETL pipeline that loads the audio data, extracts fetures and stores in another directory
        `python bin/preprocessor/Preprocessor.py preprocessor melspectrograms /path/to/dataset /path/to/save/directory`



### Files

- bin
| - preprocessor
| |- __init__.py  
| |- command_line.py 
| |- Preprocessor.py   # pipeline class for preprocessing
| |- test_pipeline.py  # unit test class 
|- setup.py  # package setup


- README.md



### Licensing, Authors, Acknowledgements

Many thanks to Valerio Velardo for this task. 


