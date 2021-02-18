# AI Audio task

This project demonstrates a simple pipeline for extracting features from audio files.



## Installation:

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

3. run  the below to install the libraries
    ```
    pip install -r requirements.txt in your shell
    ```





## Instructions:


1. Run the following commands in the project's  preprocessor directory to run the pipeline.

    - To run ETL pipeline that loads the audio data, extracts fetures and stores in another directory

        ```$ python bin/preprocessor/Preprocessor.py preprocessor melspectrograms /path/to/dataset /path/to/save/directory```

2. To run the unnit test:
   - Locate the test_pipeline.py file in the preprocessor directory
   - Make sure to update the dataset path and the output path. below shows where and how:
        ```
            
            @pytest.fixture(scope='module')
            def pipeline():
                print('------------------setup-------------------')
           
                pipeline = Pipeline(dataset_path='ABSOLUTE PATH TO DATA SOURCE DIRECTORY GOES HERE',
                                output_path='ABSOLUTE PATH TO OUTPUT SOURCE DIRECTORY GOES HERE',
                                sample_rate=22050,
                                mel_bands=10,
                                n_mfcc=10,
                                hop_length=512)


        ```
   - Go to your terminal and make sure to cd into the preprocessor directory and run the below command:
        ```
            pytest -k test_pipeline.py 
        ```

3. To install the package locally, make sure you cd into the bin directory or locate the setup.py file. Then run the below in the terminal.
    ```
        $ pip install .
    ```



4. To use the installed package in the terminal or batch, example is as shown below

    ```
        # you can change the feature type to mfccs or melspectrograms
        $ preprocessor melspectrograms /path/to/dataset /path/to/save/directory
    ```

### Files

- bin
  - preprocessor
    - __init__.py  
    - command_line.py 
    - Preprocessor.py   # pipeline class for preprocessing
    - test_pipeline.py  # unit test class 
  - setup.py  # package setup

- music_dataset
- output
- README.md
- requirements.txt



### Licensing, Authors, Acknowledgements

Many thanks to Valerio Velardo for this task. 


