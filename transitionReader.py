import pandas as pd

# Load the CSV file
file_path = './DFA.csv'
df = pd.read_csv(file_path)

# Initialize an empty dictionary for the transition table
transition_table = {}

# Iterate over each row in the DataFrame to build the transition table
for _, row in df.iterrows():
    current_state = row['DFA']  # The current state (e.g., 'D0')
    
    # Initialize a dictionary for the current state transitions
    state_transitions = {}
    
    # Iterate over each column (input symbols) except the first column (state names)
    for column in df.columns[1:]:
        next_state = row[column]  # The state to which it transitions
        state_transitions[column] = next_state  # Add the transition to the dictionary

    # Add the current state's transitions to the transition table
    transition_table[current_state] = state_transitions

# The transition table is now in a dictionary format
print(transition_table)
