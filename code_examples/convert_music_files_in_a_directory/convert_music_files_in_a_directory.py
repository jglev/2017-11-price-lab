# =============================================================================
# Import libraries
# =============================================================================

import glob  # For listing files with a wildcard ('*') search
import os  # For interacting with our filesystem
from pydub import AudioSegment  # For converting between formats, using ffmpeg

# =============================================================================
# Settings
# =============================================================================

directory_of_music_files = 'music'

# This should be either mp3 or wav:
convert_from_mp3 = 'mp3'  # We will use this to search for files in
# the directory_of_music_files

# =============================================================================
# Convert the files in the directory
# =============================================================================

# List the files in the directory that match the music_format_to_convert_from:
# os.listdir(directory_of_music_files)  # See all files in the directory

# Get just the files that end in '.mp3' (for example):
files_to_convert = glob.glob(os.path.join(
        directory_of_music_files,
        f'*.{music_format_to_convert_from}'))

for file_to_convert in files_to_convert:
    print(f'Processing "{file_to_convert}"...')

    # Get just the filename, not the directories it's in:
    file_name = os.path.basename(file_to_convert)
    
    if music_format_to_convert_from == 'mp3':
        conversion_process = AudioSegment.from_mp3(file_to_convert)
        file_extension_to_convert_to = 'wav'
        
    elif music_format_to_convert_from == 'wav':
        conversion_process = AudioSegment.from_wav(file_to_convert)
        file_extension_to_convert_to = 'mp3'
    
    # Convert the file:
    AudioSegment.from_wav("/input/file.wav")
