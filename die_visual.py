from die import Die
import pygal

# Create a d6
die = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

# Analysis
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#TODO: Demonstrate Counter

print(frequencies)

# Visualize
hist = pygal.Bar()
hist.title = "Results of rolling a d6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.y_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
