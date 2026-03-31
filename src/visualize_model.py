import pandas as pd                                                 # Import pandas for data manipulation
import matplotlib.pyplot as plt                                     # Import matplotlib for data visualization
import numpy as np                                                  # Import numpy for numerical operations
from sklearn.ensemble import RandomForestRegressor                  # Import Random Forest machine learning algorithm
from sklearn.model_selection import train_test_split                # Import function to split data into train/test

def generate_ml_visuals():                                          # Define main function to create ML charts
# 1. MATCH EXACT WINDOWS PATH TO DATA
    data_path = r"E:\s23002167\Data Analytics\Projects\audience-sentiment-predictor\Data\Processed\the_audience_cleaned.csv" # Set path to cleaned dataset
    
    print("Loading data and training Random Forest...")             # Print status message to the terminal
    df = pd.read_csv(data_path)                                     # Load the CSV data into a pandas DataFrame
    
    features = ['RT_Score', 'IMDb_Rating', 'IMDb_Votes']            # Define the input variables (features) for the AI
    target = 'Box_Office'                                           # Define the output variable (target) to predict
    
    X = df[features]                                                # Create the Feature Matrix (X)
    y = df[target]                                                  # Create the Target Vector (y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # Split data (80% train, 20% test)

    model = RandomForestRegressor(random_state=42)                  # Initialize the Random Forest algorithm with a fixed seed
    model.fit(X_train, y_train)                                     # Train the AI model using the training data


# CHART 1: FEATURE IMPORTANCE

    print("Generating Feature Importance Chart...")                 # Print status message to the terminal
    importances = model.feature_importances_                        # Extract the mathematical importance score of each feature
    feature_names = ['Rotten Tomatoes', 'IMDb Rating', 'IMDb Votes']# Define human-readable names for the chart labels
    indices = np.argsort(importances)                               # Sort the features from least to most important

    plt.figure(figsize=(10, 5))                                     # Create a new chart canvas of size 10x5 inches
    plt.style.use('dark_background')                                # Apply a dark theme to match the Power BI aesthetic
    plt.barh(range(len(indices)), importances[indices], color='#f5c518', align='center') # Draw horizontal bars for each feature
    plt.yticks(range(len(indices)), [feature_names[i] for i in indices], fontsize=12, color='white') # Label the Y-axis
    plt.xlabel('Relative Importance (Contribution to Prediction)', fontsize=12, color='white') # Label the X-axis
    plt.title('Random Forest Feature Importance', fontsize=14, fontweight='bold', pad=15, color='white') # Add a bold title
    
    plt.gca().spines['top'].set_visible(False)                      # Hide the top border line for a cleaner look
    plt.gca().spines['right'].set_visible(False)                    # Hide the right border line for a cleaner look
    plt.gca().spines['bottom'].set_color('#333333')                 # Darken the bottom border line
    plt.gca().spines['left'].set_color('#333333')                   # Darken the left border line
    plt.grid(axis='x', color='#333333', linestyle='--', alpha=0.5)  # Add subtle vertical grid lines to help read values
    plt.tight_layout()                                              # Auto-adjust spacing so no text gets cut off
    
    plt.savefig(r"E:\s23002167\Data Analytics\Projects\audience-sentiment-predictor\Images\feature_importance.png", dpi=300, facecolor='#121212') # Save chart 1 to Images folder
    plt.close()                                                     # Close the canvas to free up computer memory


# CHART 2: TARGET SKEWNESS DISTRIBUTION

    print("Generating Box Office Skewness Chart...")                # Print status message to the terminal
    plt.figure(figsize=(10, 5))                                     # Create a new chart canvas of size 10x5 inches
    plt.hist(df['Box_Office'] / 1e6, bins=30, color='#4da6ff', edgecolor='white', alpha=0.8) # Draw a histogram scaling dollars to millions
    plt.xlabel('Global Box Office Revenue ($ Millions)', fontsize=12, color='white') # Label the X-axis
    plt.ylabel('Number of Movies', fontsize=12, color='white')      # Label the Y-axis
    plt.title('Box Office Revenue Distribution (Target Skewness)', fontsize=14, fontweight='bold', pad=15, color='white') # Add a bold title
    
    plt.gca().spines['top'].set_visible(False)                      # Hide the top border line for a cleaner look
    plt.gca().spines['right'].set_visible(False)                    # Hide the right border line for a cleaner look
    plt.grid(axis='y', color='#333333', linestyle='--', alpha=0.5)  # Add subtle horizontal grid lines
    plt.tight_layout()                                              # Auto-adjust spacing so no text gets cut off
    
    plt.savefig(r"E:\s23002167\Data Analytics\Projects\audience-sentiment-predictor\Images\target_skew.png", dpi=300, facecolor='#121212') # Save chart 2 to Images folder
    plt.close()                                                     # Close the canvas to free up computer memory

# CHART 3: ACTUAL VS PREDICTED PLOT

    print("Generating Actual vs Predicted Chart...")                # Print status message to the terminal
    predictions = model.predict(X_test)                             # Ask the trained AI to predict revenues for the test set
    plt.figure(figsize=(8, 8))                                      # Create a square chart canvas of size 8x8 inches
    plt.scatter(y_test / 1e6, predictions / 1e6, color='#fa320a', alpha=0.7, edgecolor='white', s=80) # Draw a scatter plot of true vs predicted
    
    max_val = max(y_test.max(), predictions.max()) / 1e6            # Find the highest dollar amount to scale the reference line
    plt.plot([0, max_val], [0, max_val], color='white', linestyle='--', lw=2, label='Perfect Prediction') # Draw the 45-degree perfect accuracy line
    
    plt.xlabel('Actual Box Office ($ Millions)', fontsize=12, color='white') # Label the X-axis
    plt.ylabel('Predicted Box Office ($ Millions)', fontsize=12, color='white') # Label the Y-axis
    plt.title('Actual vs. Predicted Box Office Revenue', fontsize=14, fontweight='bold', pad=15, color='white') # Add a bold title
    plt.legend(facecolor='#121212', edgecolor='#333333', labelcolor='white') # Add a legend explaining the white dotted line
    plt.grid(color='#333333', linestyle='--', alpha=0.5)            # Add a subtle grid to the background
    plt.gca().spines['top'].set_visible(False)                      # Hide the top border line
    plt.gca().spines['right'].set_visible(False)                    # Hide the right border line
    plt.gca().spines['bottom'].set_color('#333333')                 # Darken the bottom border line
    plt.gca().spines['left'].set_color('#333333')                   # Darken the left border line
    plt.tight_layout()                                              # Auto-adjust spacing so no text gets cut off
    
    plt.savefig(r"E:\s23002167\Data Analytics\Projects\audience-sentiment-predictor\Images\actual_vs_predicted.png", dpi=300, bbox_inches='tight', facecolor='#121212') # Save chart 3 to Images folder
    plt.close()                                                     # Close the canvas to free up computer memory

    print("All ML visuals successfully saved to your Images/ folder!") # Print final success message

if __name__ == "__main__":                                          # Check if script is being run directly from the terminal
    generate_ml_visuals()                                           # Execute the main visual generation function