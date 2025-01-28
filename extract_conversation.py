import json
from pathlib import Path

def process_transcript(json_file, output_file):
    """
    Process a JSON file containing audio segments and generate a transcript.

    Args:
        json_file (str): Path to the input JSON file.
        output_file (str): Path to save the processed transcript.
    """
    # Load the JSON data
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extract audio segments
    audio_segments = data["results"]["audio_segments"]

    # Initialize variables for processing
    merged_transcript = []
    current_speaker = None
    current_text = []

    # Iterate through each audio segment
    for segment in audio_segments:
        speaker = segment["speaker_label"]
        text = segment["transcript"]

        if speaker != current_speaker:
            # Save the previous speaker's text block
            if current_speaker:
                merged_transcript.append(f"{current_speaker}: {' '.join(current_text)}")
            current_speaker = speaker
            current_text = [text]
        else:
            # Append text to the current speaker's block
            current_text.append(text)

    # Append the last speaker's block
    if current_speaker:
        merged_transcript.append(f"{current_speaker}: {' '.join(current_text)}")

    # Combine conversation into a single text block with spaces between speakers
    conversation_text = "\n\n".join(merged_transcript)

    # Save the processed transcript to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(conversation_text)

    print(f"Processed transcript saved to {output_file}")

# Example usage
if __name__ == "__main__":
    input_json_file = Path("D:/Dropbox/McCallieFamilyStories/ZoomFest-Jan2025/zoomfest-video-jan-2025.json") 
    output_transcript_file = "output_transcript.txt"  # Replace with desired output file path
    process_transcript(input_json_file, output_transcript_file)
