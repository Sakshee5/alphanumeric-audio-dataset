import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Function to plot age distribution
def plot_age_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Age'], kde=False, color='skyblue', bins=5)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.show()

# Function to plot gender distribution (Donut Chart)
def plot_gender_distribution(df):
    gender_counts = df['Gender'].value_counts()
    plt.figure(figsize=(7, 7))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, 
            colors=sns.color_palette("pastel"))
    plt.title('Gender Distribution')
    plt.gca().set_aspect('equal')
    plt.show()

# Function to plot nationality distribution
def plot_nationality_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(y=df['Nationality'], palette='coolwarm')
    plt.title('Nationality Distribution')
    plt.gca().set_aspect('equal')
    plt.show()

# Function to plot native language distribution
def plot_native_language_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(y=df['Native Language'], palette='coolwarm')
    plt.title('Native Language Distribution')
    plt.gca().set_aspect('equal')
    plt.show()

# Function to plot familiarity with English distribution
def plot_familiarity_with_english(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(y=df['Familiarity with English'], palette='coolwarm')
    plt.title('Familiarity with English')
    plt.xlabel('Count')
    plt.ylabel('Familiarity Level')
    plt.show()

# Function to plot recording duration distribution
def plot_duration_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Duration (secs)'], kde=False, color='coral', bins=10)
    plt.title('Recording Duration Distribution')
    plt.xlabel('Duration (seconds)')
    plt.ylabel('Count')
    plt.show()


def main():
    # Load the dataset
    df = pd.read_csv("metadata.csv")
    
    # Plot the distributions
    plot_age_distribution(df)
    plot_gender_distribution(df)
    plot_nationality_distribution(df)
    plot_native_language_distribution(df)
    plot_familiarity_with_english(df)
    plot_duration_distribution(df)


if __name__ == "__main__":
    main()
