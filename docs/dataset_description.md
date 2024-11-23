# Dataset Description

This document provides a detailed description of the dataset's contents, structure, and the significance of each component.

## 1. Audio Recordings
The dataset includes audio recordings of participants spelling out a randomized full name, a phone number, and an address. Each participant's audio files are stored in separate folders under the `audio_data/` directory.

### Audio Files Naming Convention
- `audio_data/Names`: Audio of participants spelling out a randomized name letter by letter.
- `audio_data/Numbers`: Audio of participants reading out a randomized phone number digit by digit.
- `audio_data/Addresses`: Audio of participants stating randomized address clearly.

The folders contain raw audio files in multiple formats, such as .wav, .mp3, and .m4a. Each participant is assigned a unique Response_ID, which corresponds to three specific file names in the above folders. The ground truth data, including participant names, phone numbers, and addresses, is stored in the metadata.csv file.

## 2. Metadata
The accompanying metadata file `metadata.csv` contains essential information about each participant. The columns in the metadata file include:

| Column Name                | Description                                                                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------|
| **Response_ID**            | Unique identifier for each participant's response.                                                   |                                                             |
| **Age**                    | Age of the participant in years.                                                                     |
| **Gender**                 | Gender of the participant (e.g., Male, Female, Non-binary).                                          |
| **Nationality**            | Participant's nationality.                                                                           |
| **Native Language**        | The language the participant primarily speaks.                                                       |
| **Familiarity with English** | Self-reported level of familiarity with English       |
| **Accent Strength (Self reported)**        | Self-reported strength of the participant's accent on a scale from 0 (no noticeable accent) to 10.   |
| **Difficulties**           | Self-reported frequency of difficulty with automated systems |
| **Recording Machine**      | Device used by the participant for recording (e.g., phone recorder, external microphone).            |
| **Name**                   | Name recorded by the participant.                                                                             |
| **Number**                 | Number recorded by the participant.                                                                     |
| **Address**                | Address recorded by the participant.                                                                |
| **Duration_secs**          | Time it took to complete the survey.                                                                |

## 3. Significance of the Dataset
The dataset is crucial for:
- Reducing bias in automated speech recognition systems, particularly for non-native speakers.
- Providing researchers and developers with a resource to enhance their understanding of how different accents affect speech recognition accuracy.
- Supporting the development of more inclusive technologies.

## 4. How to Access the Data
To access the dataset, you can download it from ........
