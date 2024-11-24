import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Ensure the 'assets' directory exists
if not os.path.exists('assets'):
    os.makedirs('assets')

# Function to plot age distribution
def plot_age_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Age'], kde=False, color='skyblue', bins=5)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plot_filename = 'assets/age_distribution.png'
    plt.savefig(plot_filename)
    plt.show() 
    plt.close()
    return plot_filename

# Function to plot gender distribution (Donut Chart)
def plot_gender_distribution(df):
    gender_counts = df['Gender'].value_counts()
    plt.figure(figsize=(7, 7))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, 
            colors=sns.color_palette("pastel"))
    plt.title('Gender Distribution')
    plt.gca().set_aspect('equal')
    plot_filename = 'assets/gender_distribution.png'
    plt.savefig(plot_filename)
    plt.show() 
    plt.close()
    return plot_filename

# Function to plot nationality distribution
def plot_nationality_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(y=df['Nationality'], hue=df['Nationality'], palette='coolwarm', legend=False)
    plt.title('Nationality Distribution')
    plt.gca().set_aspect('equal')
    plot_filename = 'assets/nationality_distribution.png'
    plt.savefig(plot_filename)
    plt.show()  
    plt.close()
    return plot_filename

# Function to plot native language distribution
def plot_native_language_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(y=df['Native Language'], hue=df['Native Language'], palette='coolwarm', legend=False)
    plt.title('Native Language Distribution')
    plt.gca().set_aspect('equal')
    plot_filename = 'assets/native_language_distribution.png'
    plt.savefig(plot_filename)
    plt.show() 
    plt.close()
    return plot_filename

# Function to plot familiarity with English distribution
def plot_familiarity_with_english(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(y=df['Familiarity with English'], hue=df['Familiarity with English'], palette='coolwarm', legend=False)
    plt.title('Familiarity with English')
    plt.xlabel('Count')
    plt.ylabel('Familiarity Level')
    plot_filename = 'assets/familiarity_with_eng.png'
    plt.savefig(plot_filename)
    plt.show() 
    plt.close()
    return plot_filename

# Function to plot recording duration distribution
def plot_duration_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Duration (secs)'], kde=False, color='coral', bins=10)
    plt.title('Recording Duration Distribution')
    plt.xlabel('Duration (seconds)')
    plt.ylabel('Count')
    plot_filename = 'assets/recording_duration_distribution.png'
    plt.savefig(plot_filename)
    plt.show() 
    plt.close()
    return plot_filename


def main():
    # Load the dataset
    df = pd.read_csv("metadata.csv")
    
    # Plot the distributions and save files
    plot_files = [
        plot_age_distribution(df),
        plot_gender_distribution(df),
        plot_nationality_distribution(df),
        plot_native_language_distribution(df),
        plot_familiarity_with_english(df),
        plot_duration_distribution(df)
    ]
    
    # Testing
    for plot_file in plot_files:
        assert os.path.exists(plot_file), f"Plot {plot_file} was not saved."
        print(f"Assertion passed for {plot_file}")


if __name__ == "__main__":
    main()
