#!/usr/bin/env python

from sys import argv
from os import system
import matplotlib.pyplot as plt
import numpy as np

# function whose orbit is to be found
def function_for_orbit(x):
		return 4*x*(1-x)

system('clear')
print '-----'

# check arguments in case something went wrong
if len(argv) != 6:
	print 'Something went wrong while passing the arguments.'
	print 'An incorrect number of arguments was received.'
	print '-----'
	raise SystemExit

# obtain the start horizontal coordinate
try:
	left = float(argv[1])
except ValueError:
	print '\'%s\' is not a valid X-axis coordinate.' % argv[1]
	print '-----'
	raise SystemExit

# obtain the seed
try:
	seed = float(argv[2])
except ValueError:
	print '\'%s\' is not a valid floating-point value.' % argv[2]
	print '-----'
	raise SystemExit

# obtain the end horizontal coordinate
try:
	right = float(argv[3])
except ValueError:
	print '\'%s\' is not a valid X-axis coordinate.' % argv[3]
	print '-----'
	raise SystemExit

# if the seed is not in (left, right), do nothing
if seed <= left or seed >= right:
	print 'The seed %.2f does not lie between %.2f and %.2f, the two extreme points.' % (seed, left, right)
	print '-----'
	raise SystemExit

# obtain the number of points to plot
try:
	iterations = abs(int(argv[4]))
except ValueError:
	print '\'%s\' is not a valid number of points.' % argv[4]
	print '-----'
	raise SystemExit

# obtain the annotation flag
try:
	annotation_flag = int(argv[5])
except ValueError:
	print '\'%s\' is not a valid flag.' % argv[5]
	print '-----'
	raise SystemExit

# set the function
x = np.linspace(left, right, 39482)
y = function_for_orbit(x)

# set plot window title
plt.figure().canvas.set_window_title('orbit of a function')

# make coordinate axes thick
plt.axhline(linewidth = 1, color = 'k')
plt.axvline(linewidth = 1, color = 'k')

# plot given function and identity function with thin line
plt.plot(x, y, 'r-', label = 'your function', linewidth = 0.8)
plt.plot(x, x, 'g-', label = r'$y=x$', linewidth = 0.8)

# initialize array for orbit elements and to simplify the loop
current_point = seed
next_point = function_for_orbit(seed)
orbit = [current_point, next_point]

# draw the first line (vertical line from X-axis to function) of the cobweb
initial_cobweb_x = [current_point, current_point]
initial_cobweb_y = [0, next_point]
plt.plot(initial_cobweb_x, initial_cobweb_y, 'b-', linewidth = 0.8)
plt.plot(current_point, 0, 'ko', label = 'seed')
plt.plot(current_point, next_point, 'r.', label = 'orbits')
annotation_flag and plt.annotate('(%.2f, 0.00)' % seed, xy = (seed, 0))
annotation_flag and plt.annotate('(%.2f, %.2f)' % (current_point, next_point), xy = (current_point, next_point))

# plot each element in a loop
for count in range(1, iterations):

	# draw horizontal line of staircase
	horizontal_x = [current_point, next_point]
	horizontal_y = [next_point, next_point]
	plt.plot(horizontal_x, horizontal_y, 'b-', linewidth = 0.8)
	plt.plot(next_point, next_point, 'g.')

	# obtain the next point of the orbit
	current_point = next_point
	next_point = function_for_orbit(orbit[count])
	orbit.append(next_point)	

	# draw vertical line of staricase
	vertical_x = [current_point, current_point]
	vertical_y = [current_point, next_point]
	plt.plot(vertical_x, vertical_y, 'b-', linewidth = 0.8)
	plt.plot(current_point, next_point, 'r.')
	annotation_flag and plt.annotate('(%.2f, %.2f)' % (current_point, next_point), xy = (current_point, next_point))

# display result
print 'iteration\torbit point'
for index, item in enumerate(orbit):
	print '\t %s\t' % str(index).rjust(len(str(iterations))),
	print '%s' % str('%f' % item).rjust(10)

# make the graph plot useful
plt.title('last orbit element = %f' % orbit[count + 1])
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.grid(True)
plt.legend()
# plt.show() # commented to show both plots simultaneously

# figure to show the successive orbits
plt.figure().canvas.set_window_title('successive orbits')

# make coordinate axes thick
plt.axhline(linewidth = 1, color = 'k')
plt.axvline(linewidth = 1, color = 'k')

# plot the points against index
plt.plot(orbit, 'r.--', label = 'orbit points', linewidth = 0.8)
plt.title('orbit plot')
plt.xlabel('iteration')
plt.ylabel('orbit')
plt.grid(True)
plt.legend()
plt.show()

print '-----'
