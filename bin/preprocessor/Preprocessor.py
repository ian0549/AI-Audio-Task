import os
import sys
import numpy as np
import librosa
import pickle
import functools
from pathlib import Path




class Pipeline:
     """ ETL Pipeline class that does the following:

        1. Load audio files from a directory
        2. Extract features for each audio file
        3. Save features as numpy arrays in another directory.


     Attributes:
        dataset_path (string) representing the path for the dataset
        output_path (string)  representing the path to save all the mfccs or melspect features
        sample_rate (int) representing the sample rate to use in preprocessing the audio files
        mel_bands (int) representing the range of frequencies that are relevant
        n_mfcc (int) number of MFCCs to return
        n_fft (int) this representing the interval of the number of sample to consider for the fourier transform
        hop_length (int) The number of samples between successive frames

        



     """

     def __init__(self,
                dataset_path,
                output_path,
                sample_rate=22050,
                mel_bands=10,
                n_mfcc=13,
                n_fft=2048,
                hop_length=512):
                

            # init attritubes

            self.dataset_path=dataset_path
            self.output_path=output_path
            self.mel_bands=mel_bands
            self.n_mfcc=n_mfcc
            self.n_fft=n_fft
            self.hop_length=hop_length

            self.sample_rate = sample_rate

     def __getitem__(self,key):
        return getattr(self,key)


     def __setattr__(self, name, value):
         super().__setattr__(name, value)    
          
     @functools.lru_cache(maxsize = None)
     def loader(self):

        """Function to load audio files from dataset using librosa.
            
            Args: 
                None
            
            Returns: 
                signal (float): list of signals for each audio file
        
        """

        try:
            audio_signals=[]
            path, dirs, files = next(os.walk(self.dataset_path))

            
            for f in files:

                # check if file is a wav and load
                _, extention = os.path.splitext(f)
            
                if extention in ['.wav']:

                        file_path = os.path.join(path, f)

                        signal, _ = librosa.load(file_path, sr=self.sample_rate)
                        audio_signals.append(signal)
                else:
                    print("Error: cannot load file type. Please ensure that your file is a wav.")


            return  audio_signals   

 
        except StopIteration:
            print("No more suggesstions.")
       




     def extract_mfccs(self, loaded_signals):
        
        """Function to extract mfccs from loaded audio files using librosa.
            
            Args: 
                loaded_signals (array list): list of signals for each audio file
            
            Returns: 
                features (arrays list): list of mfccs extracted from audio signal
        
        """

        featrue_list=[]

        for signal in loaded_signals:

            # extract mfccs
            mfcc = librosa.feature.mfcc(signal,
                                         sr=self.sample_rate,
                                          S=None, 
                                          n_fft= self.n_fft,
                                          n_mfcc= self.n_mfcc)

            featrue_list.append(mfcc)                              

        return featrue_list


     def extract_mel_spectrogram(self, loaded_signals):
    
        """Function to extract mel spectrograms from loaded audio files using librosa.
            
            Args: 
                loaded_signals (arrya list): list of signals for each audio file
            
            Returns: 
                features ( arrays list): list of mel spectrograms extracted from audio signal
        
        """

        featrue_list=[]

        for signal in loaded_signals:
    
            sftt = librosa.stft(signal, center=False, n_fft=self.n_fft, hop_length=self.hop_length)
            S = np.abs(sftt) ** 2
            S = librosa.feature.melspectrogram(S=S, n_mels=self.mel_bands, sr=self.sample_rate)
 
            featrue_list.append(S)


        return featrue_list


     def save_features(self, feature, feature_type):
        
        """Function to save extracted features from audio signals.
            filenames to use : "originalfilename_" + feature type + ".npy"
            Args: 
                feature_type(string): representing the feature type
                feature( arrays list): list of extracted feature from audio signal
            Returns: 
                None
        """  

        path, dirs, files = next(os.walk(self.dataset_path))


        if feature_type == "melspectrograms":

            
            for i,f in enumerate(files):


                file_path = os.path.join(path, f)
                original_filename = Path(file_path).stem

                melspectrograms = feature[i]
                
                save_filename = f"{original_filename}_{feature_type}"

                save_file_path = os.path.join(self.output_path, save_filename)
              
                # save the feature as numpy array
                np.save(save_file_path,melspectrograms)

        elif feature_type == "mfccs":


            
            for i,f in enumerate(files):


                file_path = os.path.join(path, f)
                original_filename = Path(file_path).stem

                mfcc = feature[i]
                
                save_filename = f"{original_filename}_{feature_type}"

                save_file_path = os.path.join(self.output_path, save_filename)
                # save the feature as numpy array

                np.save(save_file_path,mfcc)


        print("extracted features saved successfully in {} direcotry"\
            .format(self.output_path))






def main():



    if len(sys.argv) > 2:

        feature_type = sys.argv[1]
        dataset_dir = sys.argv[2]
        save_output_dir = sys.argv[3]


        check_data_dir_exists = os.path.exists(dataset_dir)

        check_save_output_dir_exists = os.path.exists(save_output_dir)

        if(check_data_dir_exists and check_save_output_dir_exists):

            # setup the pipeline

            print('.................starting pipline and extracting {} features........................'\
                .format(feature_type))

            pipeline = Pipeline(dataset_path=dataset_dir,
                                output_path=save_output_dir)

            loaded_signals = pipeline.loader()

            if loaded_signals != []:
            
                if feature_type == "melspectrograms":  
                    # extract mel spectrograms
                    mel_spectrogram = pipeline.extract_mel_spectrogram(loaded_signals)
                    # save the feature
                    pipeline.save_features(mel_spectrogram,feature_type)

                elif feature_type == "mfccs":
                        # extract mfccs
                        mfccs = pipeline.extract_mfccs(loaded_signals)
                        # save the mfccs feature as numpy array
                        pipeline.save_features(mfccs,feature_type)
        else:

            if (check_data_dir_exists== False): print("Error: data directory not found" )
            if (check_save_output_dir_exists== False): print("Error: save output data directory not found" )

            

    else:

        print(" Please set the arguments for the following:\n\
               1.  Feature type ( enter either mfccs or melspectrograms)\n\
               2.  The Absolute path for the audio dataset\n\
               3.  The Absolute path to save the extract features\n\
               Example:  preprocessor melspectrograms \"/path/to/dataset" "/path/to/save/directory\" ")












if __name__ == '__main__':
    main()      
