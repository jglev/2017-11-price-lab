"""This script converts mp3s to wav files."""

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

# =============================================================================
# Convert the files in the directory
# =============================================================================

# List the files in the directory that match the music_format_to_convert_from:
# os.listdir(directory_of_music_files)  # See all files in the directory

# Get just the files that end in '.mp3' (for example):
files_to_convert = glob.glob(os.path.join(
        directory_of_music_files,
        f'*.mp3'))

for file_to_convert in files_to_convert:
    print(f'Processing "{file_to_convert}"...')

    # Get just the filename, not the directories it's in:
    file_name = os.path.basename(file_to_convert)
    file_name_without_extension = os.path.splitext(file_name)[0]

    # Convert the file:
    conversion_process = AudioSegment.from_mp3(file_to_convert)

    # Save the converted file:
    conversion_process.export(
            os.path.join(
                    directory_of_music_files,
                    f'{file_name_without_extension}.wav'))
