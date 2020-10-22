
import pandas as pd
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

