import os
import pandas as pd
from datasets import Dataset, Audio

def load_metadata(metadata_path):
    """Load the metadata CSV file."""
    return pd.read_csv(metadata_path)

def generate_dataset_dict(metadata, audio_folder):
    """
    Generate the dataset dictionary by mapping metadata to corresponding audio files.
    """
    data = {
        "file_name_id": [],
        "audio": [],
        "text": [],
        "age": [],
        "gender": [],
        "nationality": [],
        "native_language": [],
        "familiarity_with_english": [],
        "accent_strength": [],
        "difficulties": [],
        "recording_machine": [],
    }
    
    for id in metadata['Response_ID'].unique():

        df_subset = metadata[metadata['Response_ID']==id]
        
        # Collect audio paths for different categories
        name_audio_path = df_subset['file_name'].iloc[0]
        number_audio_path = df_subset['file_name'].iloc[2]
        address_audio_path = df_subset['file_name'].iloc[1]
        
        row = df_subset.iloc[0]

        # Only include data if all three audio files exist
        if name_audio_path and number_audio_path and address_audio_path:
            data["file_name_id"].append(id)
            data["audio"].append({
                "name_audio": name_audio_path,
                "number_audio": number_audio_path,
                "address_audio": address_audio_path,
            })
            data["text"].append({
                "name": row["Name"],
                "number": row["Number"],
                "address": row["Address"],
            })
            data["age"].append(row["Age"])
            data["gender"].append(row["Gender"])
            data["nationality"].append(row["Nationality"])
            data["native_language"].append(row["Native Language"])
            data["familiarity_with_english"].append(row["Familiarity with English"])
            data["accent_strength"].append(row["Accent Strength (Self reported)"])
            data["difficulties"].append(row["Difficulties"])
            data["recording_machine"].append(row["Recording Machine"])
    
    return data

def load_dataset(metadata_path="metadata.csv", audio_folder="audio_data"):
    """
    Load the dataset, mapping metadata to audio and other fields.
    """
    metadata = load_metadata(metadata_path)
    dataset_dict = generate_dataset_dict(metadata, audio_folder)
    
    # Use the Audio feature from the Hugging Face Datasets library
    return Dataset.from_dict(dataset_dict).cast_column("audio", Audio())

if __name__ == "__main__":
    # Load the dataset and print a sample
    dataset = load_dataset()
    print(dataset)