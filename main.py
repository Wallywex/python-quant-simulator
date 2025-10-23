import random
import matplotlib.pyplot as plt
import numpy as np

# --- Part 1: The Simulator ---

# --- Part 1: The Simulator ---

def simulate(num_trials):
    """
    Runs a simulation of the 'Two-Dice Game' for a given number of trials.
    Returns a list of the net profit/loss from each trial.
    """
    
    # This list will store the net result ($) of each individual game
    results_per_game = []
    
    # The cost to play one round
    cost_to_play = 2 

    print(f"--- Running Simulation ({num_trials:,} trials) ---")

    for _ in range(num_trials):
        
        # Start with the cost to play
        net_result_this_game = -cost_to_play
        
        # Roll two dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        
        # Check for wins
        if roll_sum == 7 or roll_sum == 11:
            # Win $5
            net_result_this_game += 5
        elif die1 == 1 and die2 == 1:
            # "Snake Eyes" win $20
            net_result_this_game += 20
        # Any other roll wins $0 (which is already accounted for in the net_result)
        
        # Add this game's final result to our list
        results_per_game.append(net_result_this_game)
    
    # --- Print Simulation Report ---
    total_net_profit_loss = sum(results_per_game)
    avg_profit_loss_per_game = total_net_profit_loss / num_trials
    
    print(f"Total Net Profit/Loss:   ${total_net_profit_loss:,.2f}")
    print(f"Avg Profit/Loss per Game: ${avg_profit_loss_per_game:,.4f}")
    
    # Return the full list of results for plotting
    return results_per_game

    # --- Part 2: The Calculator (Expected Value) ---

def calculate_ev():
    """
    Calculates the precise mathematical Expected Value (EV) of one round.
    """
    
    print("\n--- Calculating Mathematical EV ---")

    # 1. Define Costs and Payouts
    cost_to_play = 2
    win_7_or_11_payout = 5
    win_snake_eyes_payout = 20

    # 2. Define Probabilities (There are 36 possible outcomes for 2 dice)
    
    # Probability of rolling a 7 (1-6, 6-1, 2-5, 5-2, 3-4, 4-3) = 6 ways
    p_roll_7 = 6 / 36
    
    # Probability of rolling an 11 (5-6, 6-5) = 2 ways
    p_roll_11 = 2 / 36
    
    # Probability of 7 or 11
    p_win_7_or_11 = p_roll_7 + p_roll_11 # 8/36
    
    # Probability of rolling "snake eyes" (1-1) = 1 way
    p_win_snake_eyes = 1 / 36
    
    # 3. Calculate Expected Value
    # EV = (Probability_of_Win_A * Payout_A) + (Probability_of_Win_B * Payout_B) - Cost
    
    expected_winnings = (p_win_7_or_11 * win_7_or_11_payout) + (p_win_snake_eyes * win_snake_eyes_payout)
    
    # The Expected Value (EV) is the expected winnings minus the cost to play
    ev = expected_winnings - cost_to_play
    
    print(f"Total combinations: 36")
    print(f"P(Win $5):  {p_win_7_or_11*100:,.2f}% (8/36)")
    print(f"P(Win $20): {p_win_snake_eyes*100:,.2f}% (1/36)")
    print(f"Expected Winnings per game: ${expected_winnings:,.4f}")
    print("------------------------------------------")
    print(f"Cost to Play: ${cost_to_play:,.2f}")
    print(f"NET Expected Value (EV): ${ev:,.4f}")


# --- Part 3: The Plotter ---

def create_histogram(results):
    """
    Takes a list of simulation results and creates a histogram.
    """
    
    print("\n--- Generating Plot ---")

    # Convert results to a NumPy array for easier plotting
    results_array = np.array(results)
    
    # Get the unique outcomes and their counts
    # The possible outcomes are: -$2 (loss), +$3 (win $5), +$18 (win $20)
    unique_outcomes, counts = np.unique(results_array, return_counts=True)
    
    # Create a bar chart (better than a histogram for discrete outcomes)
    plt.figure(figsize=(10, 6))
    plt.bar(unique_outcomes, counts, color=['#d9534f', '#5cb85c', '#428bca'], edgecolor='black')
    
    # Add titles and labels
    plt.title(f'Outcome Distribution of {len(results):,} "Two-Dice" Games', fontsize=16)
    plt.xlabel('Net Profit/Loss per Game ($)', fontsize=12)
    plt.ylabel('Frequency (Number of Times Occurred)', fontsize=12)
    
    # Set x-axis ticks to only show our specific outcomes
    plt.xticks(unique_outcomes)
    
    # Add the text labels on top of the bars
    for i in range(len(unique_outcomes)):
        plt.text(unique_outcomes[i], counts[i] + (0.01 * max(counts)), f'{counts[i]:,}', ha='center', fontsize=11)

    # Save the plot as an image file in your project folder
    output_filename = 'game_outcome_distribution.png'
    plt.savefig(output_filename)
    
    print(f"Plot successfully saved as '{output_filename}'")
    # plt.show() # Optional: un-comment this line if you want the plot to pop up


    # --- Run the Program ---
# --- Run the Program ---
# --- Run the Program ---
if __name__ == "__main__":
    
    # Set the number of trials you want to run
    trials_to_run = 1_000_000
    
    # Run Part 1
    # This now returns the list of all game results
    all_game_results = simulate(trials_to_run)
    
    # Run Part 2
    calculate_ev()
    
    # Run Part 3
    create_histogram(all_game_results)