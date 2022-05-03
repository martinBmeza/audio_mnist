import glob
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from tqdm import tqdm

def dataset_info(dataset_path):
    dataset_files = glob.glob(dataset_path+'/**/*.wav', recursive=True)
    
    samplerate = set()
    formats = set()
    durations = []

    for path in tqdm(dataset_files):
        info = sf.info(path)
        samplerate.add(info.samplerate)
        formats.add(info.format)
        durations.append(info.duration)
        
    plt.figure(figsize=(10,5))
    plt.hist(durations, bins=20)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Cantidad de audios')
    plt.show()
    
    print('Formatos de audio:', formats)
    print('Frecuencias de muestreo:', samplerate)
    print('Cantidad de archivos:', len(dataset_files))
