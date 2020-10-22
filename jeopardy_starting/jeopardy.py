
import pandas as pd
import datetime as dt
import random
pd.set_option('display.max_colwidth', None)

# read in csv
jeopardy = pd.read_csv('jeopardy.csv')
# inspect first rows
# print(jeopardy.head())

# rename columns
jeopardy.rename(
	columns = {
		'Show Number': 'show_number', 
		' Air Date': 'air_date', 
		' Round': 'round', 
		' Category': 'category', 
		' Value': 'value', 
		' Question': 'question', 
		' Answer': 'answer'}, 
	inplace=True)

# convert value column to floats
jeopardy['value_float'] = jeopardy.value.apply(
	lambda x: float(x[1:].replace(',', '')) 
		if x != 'None' else 0
	)

# convert dates to date times
jeopardy['date'] = jeopardy.air_date.apply(
	lambda x: pd.to_datetime(x)
	)

# create filter function
def word_filter(data, words):
  filter_function = lambda x: all(word.lower() in x.lower() 
  	for word in words)
  return data.loc[data['question'].apply(filter_function)]

# test
# print(word_filter(jeopardy, ['king']))

# count unique answers
def unique_answers(data, words):
	filtered_data = word_filter(data, words)
	unique_data = filtered_data.groupby('answer').value.count().reset_index()
	return unique_data.sort_values(by=['value'], ascending = False)

# test
# print(unique_answers(jeopardy, ['women']))

# use of word computer over time
"""
filtered_computer = word_filter(jeopardy, ['computer'])
computer_90s = filtered_computer[
	(filtered_computer['date'] > dt.datetime(1990, 1, 1)) 
		& (filtered_computer['date'] < dt.datetime(2000, 1, 1))
	]
computer_90s_count = computer_90s.question.nunique()
computer_00s = filtered_computer[
	(filtered_computer['date'] > dt.datetime(2000, 1, 1)) 
		& (filtered_computer['date'] < dt.datetime(2010, 1, 1))
	]
computer_00s_count = computer_00s.question.nunique()
"""

# examine
#print("Computer was mentioned " + str(computer_90s_count) + " times in the 90s")
#print("Computer was mentioned " + str(computer_00s_count) + " times in the 00s")

# build a game
def jeopardy_game(df = jeopardy):
	correct = 0
	incorrect = 0
	random_index = random.randint(0, len(df))
	question = df.question.iloc[random_index]
	answer = df.answer.iloc[random_index]
	print(question)
	user_input = input('Give it your best shot: ')
	if (user_input.lower() == answer.lower()):
		print('Well done!')
		correct += 1
	else: 
		print('Bad luck')
		incorrect += 1
	return 'You scored: ' + str(score)

jeopardy_game()