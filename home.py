#from time import sleep
import streamlit as st
import pandas as pd
import oci
#import pydub
#from pathlib import Path
#from datetime import date, datetime
import ocifs
#import json

def main():
    st.title("Faça Upload do seu arquivo de áudio")
    #st.sidebar.image('oracle.png')

    fileObject = st.file_uploader(label = "Faça upload do seu arquivo aqui ", 
    type=['mp4'])

    if fileObject is not None:
        audio_bytes = fileObject.read()
        st.video(audio_bytes, format='video/mp4')

    if fileObject is not None:
        if fileObject.name.endswith('wav'):
            audio = pydub.AudioSegment.from_wav(fileObject)
            file_type = 'wav'

        #save_path = Path("C:/Users/ffsantos/Documents/AI_Services/Speech_App")/fileObject.name
        #audio.export(save_path, format=file_type)

        nome_arquivo = f'{"Video"}-{datetime.now()}'

        

        config = oci.config.from_file('config')

        object_storage_client = oci.object_storage.ObjectStorageClient(config)

        put_object_response = object_storage_client.put_object(
        namespace_name="id3kyspkytmr",
        bucket_name="DemoHotBucket",
        object_name=nome_arquivo,
        put_object_body = fileObject.getvalue(),
        content_type="video/mp4")



    
    
        
        
        
            
    

if __name__ == '__main__':
    main()

