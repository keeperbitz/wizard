
from enum import Enum
import random

NUM_TOTAL_CARDS = 60
NUM_PLAYING_CARDS = 52

class Suit(Enum):
	HEARTS = 0
	DIAMONDS = 1
	SPADES = 2
	CLUBS = 3
	NO_SUIT = -1

class Value(Enum):
	JOKER = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	JACK = 11
	QUEEN = 12
	KING = 13
	ACE = 14
	WIZARD = 15
	INVALID_VALUE = -1

class Card():

	suit = Suit.NO_SUIT
	value = Value.INVALID_VALUE

	name = 'null'

	def __init__(self, suit, value, name):
		self.suit = suit
		self.value = value
		self.name = name

class User():

	score = 0
	hand = []

	def __init__(self):
		print('pizza')

	def add_card(self, card):
		self.hand.append(card)

	def place_card(index):
		print('pizza')

	def print_hand():
		print('hi')

class ComputerPlayer():

	score = 0
	hand = []

	def __init__(self):
		print('pizza')

	def add_card(self, card):
		self.hand.append(card)

	def print_hand():
		print('hi')

class Deck():
	card_list = []
	num_cards = 60

	def __init__(self):
		self.card_list = self.initialize_deck()
		for i in self.card_list:
			print(i.name)
		self.num_cards = len(self.card_list)

	def initialize_deck(self):
		card_list = []
		possible_suits = ['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS']
		possible_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
		for i in range(0, 4):
			for j in range(1, 14):
				name = possible_values[j - 1] + ' of ' + possible_suits[i] 
				new_card = Card(Suit(i), Value(j), name)
				card_list.append(new_card)

		for i in range(0, 4):
			new_card = Card(Suit.NO_SUIT, Value.WIZARD, 'WIZARD')
			card_list.append(new_card)
			new_card = Card(Suit.NO_SUIT, Value.JOKER, 'JOKER')
			card_list.append(new_card)

		random.shuffle(card_list)
		return card_list



class Game():

	num_total_players = 3
	num_computer_players = 2
	num_users = 1
	deck = None
	round_num = 1
	user = None
	computer_players = []

	def __init__(self, num_players):
		self.deck = Deck()
		self.num_total_players = num_players
		self.num_computer_players = num_players - 1
		self.num_users = 1
		self.user = User()
		for i in range(0, self.num_computer_players):
			self.computer_players.append(ComputerPlayer())

	def perform_round(self, round_num):
		self.deal(round_num)
		self.score()
		self.distribute_scores()
		self.reset_deck()

	def deal(self, round_num):
		num_cards_per_player = round_num
		for i in range(0, self.num_total_players):
			for j in range(0, round_num):
				card = self.deck.card_list.pop()
				if i == 0:
					self.user.add_card(card)
				else:
					self.computer_players[i - 1].add_card(card)

	def score(self):
		print('hi')

	def distribute_scores(self):
		print('hi')

	def reset_deck(self):
		self.deck = Deck()

print('Welcome to the Wizard Game')
num_players = -1

while True:

	num_players = int(input('Enter number of players (3 to 6): '))
	if num_players == 3 or num_players == 4 or num_players == 5 or num_players == 6:
		break

	print('Invalid number')

game = Game(num_players)
game.perform_round(1)

# Idea use reinforcement learning to win this game

# Decision Tree

# Minimax






