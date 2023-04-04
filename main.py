# import modules
import time

# intro explaining the program and how it works
time.sleep(.5)
print("This is a simple program that measures your typing speed.")
time.sleep(.5)
print("It does not check for accuracy and relies on space hits to increase the word count.")
time.sleep(.5)
print("Start typing and hit enter when you're done.")
time.sleep(.5)

# set start time
start_time = time.time()

# allow user input
user_input = input('Start now: ')

# save time of when user hits enter
end_time = time.time()

# set word_count to 1 to account for the fact that people naturally don't end texts with a space hit
word_count = 1

# increase word_count by 1 for every space hit
for character in user_input:
    if character == ' ':
            word_count += 1

# check whether the user typed at least 1 word, else set to 0 to avoid a count of 1
if user_input == '':
    word_count = 0

# substract end_time from start_time to get overall time passed in seconds
seconds = round(end_time - start_time,2)

# calculate word count per minute
per_minute = round(word_count/(seconds/60),2)

# prints "word" as either singular or plural in the result
s = 's'

# this is "==1" instead of ">=1" because 0 uses the plural as well
if word_count == 1:
    s = ''

# print results
time.sleep(.5)
print(f"You typed {word_count} word{s} in {seconds} seconds. "
      f"This translates to a typing speed of {per_minute} words per minute.")


