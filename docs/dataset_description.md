# Dataset Description

This document provides a detailed description of the dataset's contents, structure, and the significance of each component.

## 1. Audio Recordings
The dataset includes audio recordings of participants spelling out a randomized full name, a phone number, and an address. Each participant's audio files are stored in separate folders under the `audio/` directory.

### Audio Files Naming Convention
- `name_spellout.wav`: Audio of the participant spelling out their randomized name letter by letter.
- `phone_number.wav`: Audio of the participant reading out their randomized phone number digit by digit.
- `address.wav`: Audio of the participant stating their randomized address clearly.

## 2. Metadata
The accompanying metadata file `metadata.csv` contains essential information about each participant. The columns in the metadata file include:

| Column Name                | Description                                                                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------|
| **Response_ID**            | Unique identifier for each participant's response.                                                   |                                                             |
| **Age**                    | Age of the participant in years.                                                                     |
| **Gender**                 | Gender of the participant (e.g., Male, Female, Non-binary).                                          |
| **Nationality**            | Participant's nationality.                                                                           |
| **Native_Language**        | The language the participant primarily speaks.                                                       |
| **Familiarity_with_English** | Self-reported level of familiarity with English       |
| **Accent_Strength**        | Self-reported strength of the participant's accent on a scale from 0 (no noticeable accent) to 10.   |
| **Difficulties**           | Self-reported frequency of difficulty with automated systems |
| **Recording_Machine**      | Device used by the participant for recording (e.g., phone recorder, external microphone).            |
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
