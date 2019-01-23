#!/bin/bash

# check arguments
if [ $# -ne 6 ]; then
	echo '-----'

	# explain correct usage
	echo 'correct usage:'
	echo -en "\t./generate_orbit '<function>' "
	echo '<start horizontal coordinate> <seed> <end horizontal coordinate> <number of orbit points> <annotation flag>'
	echo

	# explain the terms
	echo -e '<function>\t\t\tNumPy (np) function or any function with valid Python syntax (enter it without spaces)'
	echo -e '<start horizontal coordinate>\tsmallest coordinate on the X-axis that must be plotted'
	echo -e '<seed>\t\t\t\tseed of the orbit of the function'
	echo -e '<end horizontal coordinate>\tgreatest coordinate on the X-axis that must be plotted'
	echo -e '<number of orbit points>\thow many elements of the orbit of <function> to plot'
	echo -e '<annotation flag>\t\twhether the orbit points should be annonated (0 means no, 1 means yes)'
	echo

	# examples
	echo 'examples:'
	echo -e "\t./generate_orbit.sh 'x**2-1' -1.6 0.3 1.42 14 0"
	echo -e "\t./generate_orbit.sh 'np.sqrt(x)' 0.036 0.14 1.89 4 1"
	echo -e "\t./generate_orbit.sh 'np.cos(x)' -0.46 0 1.1 6 1"
	echo -e "\t./generate_orbit.sh 'x**2.043' 0 1.1 2.47 4 1 "
	echo '-----'

	exit
fi

# set the function in the Python script
# searches for the line containing 'return'
# replaces that entire line by 'return <user function>'
sed -i '/return/c\\t\treturn '"$1" orbit.py

# on failure, display error message
if !(./orbit.py $2 $3 $4 $5 $6); then
	echo 'The function you entered is either invalid or inappropriate.'
fi
