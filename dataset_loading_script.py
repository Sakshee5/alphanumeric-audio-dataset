import os
import pandas as pd
from datasets import Dataset, Audio

def load_metadata(metadata_path):
    # Load the metadata CSV file
    return pd.read_csv(metadata_path)

def generate_dataset_dict(metadata, audio_folder):
    data = {
        "response_id": [],
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
    
    for _, row in metadata.iterrows():
        response_id = row["Response_ID"]
        
        # Collect audio paths
        name_audio_path = os.path.join(audio_folder, "Names", f"{response_id}.wav")
        number_audio_path = os.path.join(audio_folder, "Numbers", f"{response_id}.wav")
        address_audio_path = os.path.join(audio_folder, "Addresses", f"{response_id}.wav")
        
        if os.path.exists(name_audio_path):
            data["response_id"].append(response_id)
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
            data["native_language"].append(row["Native_Language"])
            data["familiarity_with_english"].append(row["Familiarity_with_English"])
            data["accent_strength"].append(row["Accent_Strength"])
            data["difficulties"].append(row["Difficulties"])
            data["recording_machine"].append(row["Recording_Machine"])
    
    return data

def load_dataset(metadata_path="metadata.csv", audio_folder="audio_data/"):
    
    metadata = load_metadata(metadata_path)
    dataset_dict = generate_dataset_dict(metadata, audio_folder)
    
    return Dataset.from_dict(dataset_dict).cast_column("audio", Audio())


if __name__ == "__main__":
    dataset = load_dataset()
    print(dataset)
