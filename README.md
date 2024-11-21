# Speech Recognition Bias Reduction Project

## Overview
Welcome to the Speech Recognition Bias Reduction Project! My data collection project aims to build a more inclusive and representative dataset to improve the accuracy of automated speech recognition systems, particularly for speakers with non-native English accents. Through this data collection, I seek to address the challenges I faced when I first moved to the US in 2024 when interacting with automated voice systems that often misinterpret alphanumeric information, leading to delays and ineffective communication.

## Objective
The primary goal of this project is to create a diverse dataset of alphanumeric audio inputs. This dataset will focus on audio recordings from speakers with various accents, starting with the vibrant community of international students at Duke University.

## Dataset Description

### Data Collection
Participants will record themselves spelling out:
- **Full Names:** Participants will clearly spell out randomly generated or chosen full names (e.g., “J-O-H-N D-O-E”).
- **Phone Numbers:** Participants will read out randomly generated phone numbers digit by digit (e.g., “Five, Five, Five, One, Two, Three, Four”).
- **Addresses:** Participants will recite randomized addresses, including street numbers, names, and cities (e.g., “One, Two, Three, Maple Street, Durham”).

In addition to the audio recordings, participants will provide metadata, including:
- Age
- Gender
- Familiarity with English
- Native language
- Accent strength (self-reported)

### Unique Aspects of the Dataset
- **Focus on Alphanumeric Data:** The dataset specifically targets the recognition of letters and numbers, critical for automated systems that handle personal information.
- **Diverse Accent Representation:** The dataset will prioritize non-native English speakers, enabling a nuanced understanding of how various accents influence recognition accuracy.
- **Rich Metadata:** Detailed demographic information allows for in-depth analysis and helps identify patterns in recognition challenges faced by different accent groups.

### Metadata File Structure
The `metadata.csv` file will include the following columns:

| Column                   | Description                                                          |
|-------------------------|----------------------------------------------------------------------|
| participant_id          | Unique identifier for each participant                                |
| age                     | Participant's age                                                    |
| gender                  | Participant's gender                                                 |
| native_language         | Participant's native language                                        |
| english_familiarity     | Level of familiarity with English                                    |
| accent_strength         | Self-reported accent strength (1 to 10)                             |                                 |
| experience_difficulty   | Yes/No answer if they faced difficulties with automated systems      |

## Data Collection Protocol
- **IRB Review:** Approved through Duke University - IRB review to ensure ethical compliance.
- **Participant Recruitment:** Participants are from Duke University and were recruited through email lists, student groups, and social media platforms, ensuring a diverse representation.
- **Informed Consent:** Participants consent to the use of their recordings and demographic information through a survey tick box.
- **Recording Platform:** Audio recordings were collected using the Qualtrics Survey App, accessible on various devices (laptop, phone).
- **Recording Conditions:** Participants were encouraged to record in their natural environments to reflect real-world conditions (background noise, varying sound levels).
- **Data Anonymization:** All recordings and metadata is anonymized to protect participant privacy.

## License

This dataset is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share, remix, and build upon the dataset for any purpose, even commercially, as long as you provide proper attribution.

## Contact Information
For any questions or further information, please contact:

**Sakshee Patil**  
Email: [sakshee.patil@duke.edu](mailto:sakshee.patil@duke.edu)

**Advisor: Dr. Brinnae Bent**  
Email: [brinnae.bent@duke.edu](mailto:brinnae.bent@duke.edu)

