from __future__ import division
from __future__ import absolute_import
import random
from node import Room
from io import open
from monster import Monster


new_dict = {}
mons, hole, gold, wall, teleport, wind, smell = 0, 0, 0, 0, 0, 0, 0
listparam = [mons, gold, hole, wall, teleport, wind, smell]

main_dict = {}

#global_clock = 0


# This is used for loading the maze
def generate_pre_dictonary_2(lst):
	for el in lst:
		main_dict.update({el: []})


# This is used for creating the maze
# Generate an empty dictionary
def generate_pre_dictonary(lst):
	for el in lst:
		new_dict.update({el: []})


def print_dict(dict):
	for el in dict:
		stri = el.toString() + u": { "
		tmplst = dict[el]
		for val in tmplst:
			if val != tmplst[0]:
				stri += u", "
			stri += u"\"" + u"Room " + unicode(val.id) + u"\""
		stri += u" }"
		print stri


def print_list(lst):
	stri = u"["
	for el in lst:
		stri += u" \"" + el.toString() + u"\" "
	stri += u"]"
	print stri


def has_duplicates(listObj):
	return len(listObj) != len(set(listObj))


# Check if graph can be constructed with the given number of nodes and edges
def check(N, K, p, k):
	lst = []
	for i in xrange(N - K):
		lst.append(p)
	for i in xrange(K):
		lst.append(k)

	# If negative integer is present or sum is not even
	if min(lst) < 0 or (sum(lst) % 2 == 1):
		return False

	while (len(lst) > 0):

		lst.sort(reverse=True)
		x = lst.pop(0)

		if x == 0:
			return True
		if x < 0  or x > len(lst):
			return False

		for i in xrange(x):
			lst[i] -= 1

	return False

def distribute_items(lst):

	added = []
	cpy_mons = listparam[0]
	randints = range(1, cpy_mons + 1)

	# Time to distribute monsters!!!
	while (cpy_mons > 0):

		tmp = random.choice(lst)
		if tmp in added:
			continue

		monsId = randints.pop(0)
		monster = Monster(monsId)                   # Create new monster object
		tmp.monsters.append(monster)

		tmp.pres_monster = 1
		tmp.pres_smell = 1
		cpy_mons -= 1
		added.append(tmp)
	del added
	del cpy_mons

	# Time to distribute holes!
	added = []
	cpy_holes = listparam[1]

	while (cpy_holes > 0):
		tmp = random.choice(lst)
		if tmp in added:
			continue
		# If there is a monster, then moving to the next room
		if tmp.pres_monster == 1:
			added.append(tmp)
			continue

		tmp.pres_hole = 1
		tmp.pres_wind = 1
		cpy_holes -= 1
		added.append(tmp)
	del added
	del cpy_holes

	# Time to distribute walls!
	added = []
	cpy_walls = listparam[3]

	while (cpy_walls > 0):
		tmp = random.choice(lst)
		if tmp in added:
			continue

		# If there is a monster or hole in the room, skip it
		if tmp.pres_monster == 1 or tmp.pres_hole == 1:
			added.append(tmp)
			continue

		tmp.pres_wall = 1
		cpy_walls -= 1
		added.append(tmp)
	del added
	del cpy_walls

	# Time to distribute gold!
	added = []
	cpy_gold = listparam[2]
	while (cpy_gold > 0):
		tmp = random.choice(lst)
		if tmp in added:
			continue

		# if there is a hole or monster or wall in the room , skip it
		if tmp.pres_hole == 1 or tmp.pres_monster == 1 or tmp.pres_wall == 1:
			added.append(tmp)
			continue

		tmp.pres_gold = 1
		cpy_gold -= 1
		added.append(tmp)
	del added
	del cpy_gold

	#Time to distribute teleportation gates!
	added = []
	cpy_tg = listparam[4]
	while (cpy_tg > 0):
		tmp = random.choice(lst)
		if tmp in added:
			continue

		# if there is a hole or monster or wall or gold in the room , skip it
		if tmp.pres_hole == 1 or tmp.pres_monster == 1 or tmp.pres_wall == 1 or tmp.pres_gold == 1:
			added.append(tmp)
			continue

		tmp.pres_teleport = 1
		cpy_tg -= 1
		added.append(tmp)
	del added
	del cpy_tg

def generate(N, K, p, k):

	normal = []
	border = []

	templist = range(1, N + 1)

	# Fill list of normal nodes
	for i in xrange(N - K):
		x = random.choice(templist)
		templist.remove(x)
		nroom = Room(x)
		nroom.isNormal = True
		nroom.conn_remained = p
		normal.append(nroom)

	# Fill list of border nodes
	for i in xrange(N - K, N):
		x = random.choice(templist)
		templist.remove(x)
		nroom = Room(x)
		nroom.isNormal = False
		nroom.conn_remained = k
		border.append(nroom)

	new_lst = normal + border
	generate_pre_dictonary(new_lst)
	copylst = new_lst[:]

	while(True):
		#This works!!!!
		new_lst.sort(key=lambda x: x.conn_remained, reverse=True)

		curr_node = new_lst.pop(-1)
		degree = curr_node.conn_remained

		if degree == 0 or len(new_lst) == 0:
			break

		toConnect = []
		for i in range(degree):
			toConnect.append(new_lst[i])


		for ngb in toConnect:
			new_dict[curr_node].append(ngb)
			new_dict[ngb].append(curr_node)
			curr_node.conn_remained -= 1
			ngb.conn_remained -=  1

			curr_node.neighbors.append(ngb)
			ngb.neighbors.append(curr_node)

	distribute_items(copylst)


def read_generator(file, teta, omega):
	f = open(file, u"r+")  # open file
	count = 0  # count the number of lines ~ rooms
	room_list = []
	list_of_rooms_nbrs = []  # list of rooms neighbors is used to figure out what is maximum num of neighbors

	for line in f:
		id = int(line[0])
		ww = int(line[2])
		hh = int(line[4])
		mm = int(line[6])
		gg = int(line[8])
		tt = int(line[10])
		neighbors_list = line.split(u" ")
		neighbors_list.remove(neighbors_list[0])  # list with ids of current room's neighbors

		room = Room(id)
		room.pres_monster = mm
		room.pres_gold = gg
		room.pres_wall = ww
		room.pres_hole = hh
		room.pres_teleport = tt

		#print(neighbors_list)

		# Convert all ids to int
		for i in xrange(len(neighbors_list)):
			if neighbors_list[i] != "\n":
				neighbors_list[i] = int(neighbors_list[i])

		room.neighbors = neighbors_list[:]  # copy neighbor list

		# appending to the lists of rooms and neighbors
		room_list.append(room)
		list_of_rooms_nbrs.append(room.neighbors)

		count += 1
	# Get max number of neighbors
	max = 0
	for el in list_of_rooms_nbrs:
		if len(el) > max:
			max = len(el)
	# print(max)

	# Figure out if room is normal or border
	for el in room_list:
		if len(el.neighbors) == max:
			el.isNormal = True
		else:
			el.isNormal = False

	for el in room_list:
		if el.pres_monster == 1:
			el.pres_smell = 1
		if el.pres_hole == 1:
			el.pres_wind = 1

	# Create new dictionary that represents the maze
	generate_pre_dictonary_2(room_list)

	for el in room_list:
		for nl in room_list:
			if nl.id in el.neighbors:
				main_dict[el].append(nl)

	# print_list(room_list)
	allocate_smell(main_dict, teta, omega)
	allocate_wind(main_dict, teta, omega)
	print_maze(main_dict)


def allocate_wind(graph, teta, omega):
	# if teta = 0; wind does not spread
	if teta == 0 or omega <= 0:
		return
	# going through all graph elements
	for el in graph:
		if el.pres_wind == 0:  # if no wind in current room, move to next room
			continue
		bfs_wind(graph, el, teta, omega)


def allocate_smell(graph, teta, omega):
	# if teta = 0; wind does not spread
	if teta == 0 or omega <= 0:
		return
	# going through all graph elements
	for el in graph:
		if el.pres_smell == 0:  # if no wind in current room, move to next room
			continue
		bfs_smell(graph, el, teta, omega)


def calculate_limit(teta, omega):
	res = 1
	for i in xrange(teta):
		res /= omega
	return res


# These function was implemented using https://stackoverflow.com/a/46383689/9901274
def bfs_wind(graph, start, theta, omega):
	# print("Start is : {}".format(start.id))
	# keep track of all visited nodes
	explored = []
	# keep track of nodes to be checked
	queue = [start]

	levels = {}  # this dict keeps track of levels
	levels[start] = 0  # depth of start node is 0
	limit = calculate_limit(theta, omega)

	visited = [start]  # to avoid inserting the same node twice into the queue
	new_wind = start.pres_wind
	# keep looping until there are nodes still to be checked
	while queue:
		# pop shallowest node (first node) from queue
		if new_wind < limit:
			return

		node = queue.pop(0)
		explored.append(node)
		neighbours = graph[node]
		new_wind = new_wind / omega
		# add neighbours of node to queue
		for neighbour in neighbours:
			if neighbour not in visited:
				# HERE!!!
				if new_wind < limit:
					return

				if new_wind > neighbour.pres_wind:
					neighbour.pres_wind = new_wind
				queue.append(neighbour)
				visited.append(neighbour)

				levels[neighbour] = levels[node] + 1
				if levels[neighbour] > theta:  # Theta defines 'depth'
					return
				# print(neighbour, ">>", levels[neighbour])
	return explored


# These function was implemented using https://stackoverflow.com/a/46383689/9901274
def bfs_smell(graph, start, theta, omega):
	# print("Start is : {}".format(start.id))
	# keep track of all visited nodes
	explored = []
	# keep track of nodes to be checked
	queue = [start]

	levels = {}  # this dict keeps track of levels
	levels[start] = 0  # depth of start node is 0
	limit = calculate_limit(theta, omega)

	visited = [start]  # to avoid inserting the same node twice into the queue
	new_smell = start.pres_smell
	# keep looping until there are nodes still to be checked
	while queue:
		if new_smell < limit:
			return

		# pop shallowest node (first node) from queue
		node = queue.pop(0)
		explored.append(node)
		neighbours = graph[node]
		new_smell = new_smell / omega
		# add neighbours of node to queue
		for neighbour in neighbours:
			if neighbour not in visited:
				# HERE!!!
				if new_smell < limit:
					return

				if new_smell > neighbour.pres_smell:
					neighbour.pres_smell = new_smell
				queue.append(neighbour)
				visited.append(neighbour)

				levels[neighbour] = levels[node] + 1
				if levels[neighbour] > theta:  # Theta defines 'depth'
					return
				# print(neighbour, ">>", levels[neighbour])

	return explored

def reset_smell():

	for room in new_dict:
		if room.pres_monster == 1:
			room.pres_smell = 1
			continue
		else:
			room.pres_smell = 0


def main_input():
	while(True):
		inp = raw_input("To create a maze, type: initMaze N K k p M W H G T sigma omega tau\n"
						"To load a maze, type: loadMaze filename sigma omega\n\n")
		sinp = inp.split()

		if sinp[0] == "initMaze":

			N, K, k, p, M, W, H, G, T, sigma, omega, tau = int(sinp[1]), int(sinp[2]), int(sinp[3]), int(sinp[4]),\
													 int(sinp[5]), int(sinp[6]), int(sinp[7]), int(sinp[8]), int(sinp[9]),\
													 int(sinp[10]), int(sinp[11]), int(sinp[12])

			if N <= K or p <= k:
				print u"Invalid number of nodes of edges. N should be > K, p should be > k\n"
				continue

			if check(N, K, p, k) == False:
				print("Maze cannot be constructed with these values of N, K, p, k. Try again\n")
				continue

			if M < 0 or W < 0 or H < 0 or G < 0 or T < 0:
				print("Number of items cannot be negative. Try again \n")
				continue
			if M + W + H + G + T > N:
				print("Total number of monsters, walls, holes and gold are greater than number of rooms. Try again \n")
				continue
			if sigma < 0 or omega < 0:
				print ("Spread and decay cannot be negative. Try again \n")
				continue



			listparam[0] = M
			listparam[1] = W
			listparam[2] = H
			listparam[3] = G
			listparam[4] = T
			listparam[5] = sigma
			listparam[6] = omega

			generate(N, K, p, k)
			allocate_wind(new_dict, sigma, omega)
			allocate_smell(new_dict, sigma, omega)
			output()
			final_output_with_cycles(tau)

			break

		elif sinp[0] == "loadMaze":
			fname, sigma, omega = sinp[1], int(sinp[2]), int(sinp[3])
			read_generator(fname, sigma, omega)
			if sigma < 0 or omega < 0:
				print ("Spread and decay cannot be negative. Try again \n")
				continue
		else:
			print("Input cannot be recognized. Try again\n")
			continue


def print_maze(dict):
	# FOR PYTHON 2.7 CHANGE TO: for key, value in d.iteritems():
	print("\n")
	for key, value in dict.items():
		stri = u""
		stri = unicode(key.id) + u": " + unicode(key.pres_monster) + u", " + unicode(key.pres_wall) + u", " + unicode(key.pres_hole
			) + u", " + \
			   unicode(key.pres_gold) + u", " + unicode(key.pres_teleport) + u", " + unicode(key.pres_wind) + u", " + unicode(key.pres_smell) + u"     "

		for el in value:
			stri += unicode(el.id) + u" "
		stri += "   Number of Monsters: " + unicode(len(key.monsters)) + u"    \n"
		print(stri)
	print("\n\n===================================================================\n\n")

def print_one_room(key):

	stri = u""
	stri = unicode(key.id) + u": " + unicode(key.pres_monster) + u", " + unicode(key.pres_wall) + u", " + unicode(
		key.pres_hole) + u", " + \
			unicode(key.pres_gold) + u", " + unicode(key.pres_teleport) + u", " + unicode(
		key.pres_wind) + u", " + unicode(key.pres_smell) + u"   "

	for el in new_dict[key]:
		stri += unicode(el.id) + u" "
	stri += u"\n"
	print(stri)

#Write generated maze to the file
def output():
	file = open(u"output.txt", u"r+")
	file.truncate(0)
	# FOR PYTHON 2.7 CHANGE TO: for key, value in d.iteritems():
	for el in new_dict:
		if el.pres_smell < 1:
			el.pres_smell = 0
		if el.pres_wind < 1:
			el.pres_wind = 0

	for key, value in new_dict.items():
		stri = u""
		stri = unicode(key.id) + u":" + unicode(key.pres_wall) + u"," + unicode(key.pres_hole) + u"," + unicode(
			key.pres_monster) + u"," + \
			   unicode(key.pres_gold) + u"," + unicode(key.pres_wind) + u"," + unicode(key.pres_smell) + u" "

		for el in value:
			stri += unicode(el.id) + u" "
		stri += u"\n"
		file.write(stri)



ff = 0
monstersToReturn = []           # Queue of monsters that need to return
teleportQueue = []
globalClock = [0]

def tick():

	sigma = listparam[5]
	omega = listparam[6]

	# Return monsters back home from rooms with walls and holes
	for currRoom in new_dict:

		# No need to return monstrers in the first cycle
		if globalClock[0] == 0:
			break

		# If monsters need to return here
		if currRoom.numOfMonstersToReturn > 0:

			size = currRoom.numOfMonstersToReturn
			for i in range(size):

				monster = monstersToReturn.pop(0)
				monster.hasMoved = True                                             # Blocking monster for one cycle
				currRoom.monsters.append(monster)                                   # Return monster back
				currRoom.pres_monster += 1                                          # Update naumber of monsters
				currRoom.numOfMonstersToReturn -= 1                                 # Decrement number of monsters to return

				currRoom.isChanged = True

				#del monster

		# If monsters need to move away fro here
		if currRoom.numOfMonstersToLeave > 0:

			size = currRoom.numOfMonstersToLeave
			for i in range(size):

				currRoom.monsters.pop(0)                            # Remove monster
				currRoom.numOfMonstersToLeave -= 1
				currRoom.pres_monster -= 1

				currRoom.isChanged = True

	del monstersToReturn[:]

	# Iterating throung maze rooms to make monsters move
	for currRoom in new_dict:

		# If current room has 1 monster
		if currRoom.pres_monster == 1:

			if currRoom.monsters[0].isBlocked > 0 or currRoom.monsters[0].hasMoved == True:          # If monster is blocked, skip this room
				continue

			moveTo = random.choice(new_dict[currRoom])      # Randomly choosing destination room from its neighbors
			monster = currRoom.monsters.pop(0)              # If monster is not blocked, remove it from the room
			currRoom.pres_monster -= 1                      # Decrement number of monsters in the start

			if moveTo.pres_wall == 1 or moveTo.pres_hole == 1:

				moveTo.pres_monster += 1                    # Increment number of monsters in the destination

				moveTo.numOfMonstersToLeave += 1            # Increment number of monsters that should leave destination
				currRoom.numOfMonstersToReturn += 1         # Increment number of monsters that should return to the start

				monster.hasMoved = True
				monstersToReturn.append(monster)            # Add monster to the queue of returning monsters
				moveTo.monsters.append(monster)             # Move monster to the destination

			else:
				monster.hasMoved = True
				moveTo.pres_monster += 1                    # Increment number of monsters in the destination
				moveTo.monsters.append(monster)             # Move monster to the destination

			currRoom.isChanged = True                       # Both rooms are changed
			moveTo.isChanged = True
			del monster
	  
		# If there are several monsters in the room:
		elif currRoom.pres_monster > 1:
			size = len(currRoom.monsters)
			for i in range(size):
																			 # Iterating through all monsters in this room
				if currRoom.monsters[0] == True:         # If monster is blocked, skip this room
					continue
				monster = currRoom.monsters[0]
				moveTo = random.choice(new_dict[currRoom])  # Randomly choosing destination room from its neighbors
				currRoom.monsters.remove(monster)         # If monster is not blocked, remove it from the room
				currRoom.pres_monster -= 1                  # Decrement number of monsters in the start

				if moveTo.pres_wall == 1 or moveTo.pres_hole == 1:

					monster.hasMoved = True
					moveTo.pres_monster += 1

					moveTo.numOfMonstersToLeave += 1
					currRoom.numOfMonstersToReturn += 1

					monstersToReturn.append(monster)        # Add monster to the queue of returning monsters
					moveTo.monsters.append(monster)         # Move monster to the destination

				else:

					monster.hasMoved = True
					moveTo.pres_monster += 1
					moveTo.monsters.append(monster)         # Move monster to the destination

				del monster


	# Unblock monsters in the end
	for currRoom in new_dict:
		if currRoom.pres_monster > 0:
			for m in currRoom.monsters:
				m.hasMoved = False

	globalClock[0] += 1

	# Print changed rooms
	print ("Cycle " + unicode(globalClock[0]) + "\n")
	for room in new_dict:
		if room.isChanged == True:
			#print_one_room(room)
			room.isChanged = False
	print_maze(new_dict)



def final_output_with_cycles(tau):

	for i in range(tau + 1):
		if i == 0:
			print_maze(new_dict)
			continue
		tick()



main_input()

# initMaze 10 5 3 5 3 1 1 0 0 2 2 5




