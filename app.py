"""Console-based Rock, Paper, Scissors minigame."""

import random

CHOICES = ("rock", "paper", "scissors")


def get_player_choice() -> str:
	"""Prompt the player until a valid option is provided."""
	while True:
		choice = input("Choose rock, paper, or scissors: ").strip().lower()
		if choice in CHOICES:
			return choice
		print("Invalid option. Please type rock, paper, or scissors.")


def determine_outcome(player: str, computer: str) -> str:
	"""Return win/lose/tie from the player's perspective."""
	if player == computer:
		return "tie"
	wins_against = {
		"rock": "scissors",
		"paper": "rock",
		"scissors": "paper",
	}
	return "win" if wins_against[player] == computer else "lose"


def play_round(score: dict[str, int]) -> bool:
	"""Run a single round and update the score; return False to stop playing."""
	player_choice = get_player_choice()
	computer_choice = random.choice(CHOICES)
	print(f"Computer chose {computer_choice}.")

	result = determine_outcome(player_choice, computer_choice)
	if result == "win":
		score["wins"] += 1
		print("You win!")
	elif result == "lose":
		score["losses"] += 1
		print("You lose!")
	else:
		score["ties"] += 1
		print("It's a tie!")

	again = input("Play again? (y/n): ").strip().lower()
	return again == "y"


def main() -> None:
	"""Game loop entry point."""
	score = {"wins": 0, "losses": 0, "ties": 0}
	print("Welcome to Rock, Paper, Scissors!")

	while play_round(score):
		pass

	print(
		"Final score - Wins: {wins}, Losses: {losses}, Ties: {ties}".format(
			**score
		)
	)


if __name__ == "__main__":
	main()