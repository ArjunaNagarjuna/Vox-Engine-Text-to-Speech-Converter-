VoxEngine – Text-to-Speech Converter
**Overview**

         VoxEngine is a Python-based Text-to-Speech (TTS) application that converts text and PDF files into natural-sounding speech. Designed with a user-friendly GUI using Tkinter, it supports multiple languages, real-time audio playback, and interactive features for an enhanced user experience. This project demonstrates hands-on experience in speech technology, audio processing, and product-oriented software development.


**Features:**

                  Multi-language support: English, Hindi, French, Spanish, Tamil, Telugu.
                  
                  Real-time playback: Low-latency audio streaming using playsound.
                  
                  File upload: Convert text files (.txt) or PDFs (.pdf) to speech.
                  
                  Adjustable speed: Normal or Slow playback options.
                  
                  Fun Mode Emojis: Replaces certain keywords with emojis for interactive speech output.
                  
                  Save audio: Export TTS output as .mp3 files.
                  
                  Replay option: Quickly replay last read text.

**Technologies Used:**


                Python – Core programming language
                
                gTTS – Google Text-to-Speech library for audio generation
                
                Tkinter – GUI development
                
                PyPDF2 – PDF text extraction
                
                playsound – Real-time audio playback

**Installation:**


Clone the repository:

        git clone https://github.com/yourusername/VoxEngine.git


Navigate to the project directory:

        cd VoxEngine


**Install dependencies:**

        pip install gTTS playsound PyPDF2
        


**Run the application:**

            python voxengine.py
            
            
            Enter text in the text area or upload a .txt/.pdf file.
            
            Select language and speed.
            
            Click Convert & Play to hear the audio.
            
            Optionally, save the audio as an .mp3 file.

            Enable Fun Mode for emojis in speech output.



**Future Improvements**

          Add speech-to-text (STT) functionality for bidirectional voice interaction.
          
          Deploy as a web application for cloud accessibility.
          
          Include voice modulation and multiple voice options
