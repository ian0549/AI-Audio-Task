import os

import numpy as np
import librosa 
import pickle



class Pipeline:

 	""" ETL Pipeline class that does the following:

        1. Load audio files from a directory
        2. Extract features for each audio file
        3. Save features as numpy arrays in another directory.
        
	
	Attributes:
        dataset_path (string) representing the path for the dataset
        output_path (string)  representing the path to save all the mfccs or melspect features
		feature_type (string) representing the type of features to extract from the audio dataset. Either MFCCs or Mel-Spectrograms
		mel_bands (int) representing the range of frequencies that are relevant
		n_mfcc (int) 
        n_fft (int) this representing the interval of the number of sample to consider for the fourier transform 
        hop_length (int)
        num_segments (int)



	"""



    def __init__(self, 
                dataset_path,
                output_path,
                feature_type,
                mel_bands=10,
                n_mfcc=13,
                hop_length=512,
                num_segments=5):
        
        # initialize attritubes


    def _loader(self):

        """Function to load audio files from dataset using librosa.
            
            Args: 
                None
            
            Returns: 
                signal (float): list of signals for each audio file
        
        """
        



    def _extract_mfccs(self, loaded_signals):
        
        """Function to extract mfccs from loaded audio files using librosa.
            
            Args: 
                loaded_signals (float): list of signals for each audio file
            
            Returns: 
                features (numpy arrays): list of mfccs extracted from audio signal
        
        """


    def _extract_mel_spectrogram(self, loaded_signals):
    
        """Function to extract mel spectrograms from loaded audio files using librosa.
            
            Args: 
                loaded_signals (float): list of signals for each audio file
            
            Returns: 
                features (numpy arrays): list of mel spectrograms extracted from audio signal
        
        """

    def _save_features(self): 

      """Function to save extracted features from audio signals.
		 filenames to use : "originalfilename_" + feature type + ".npy"
		Args: 
			None
		
		Returns: 
			None
	 """        






def main():
    if len(sys.argv) == 3:


    
    else:



if __name__ == '__main__':
    main()      
