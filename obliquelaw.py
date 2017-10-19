#a random strategy generator for lawyers who have hit mental roadblocks, modeled after Brian Eno's Oblique Strategies deck.

import random

strategies = [
    'What would the dissenting opinion say?',
    'Make your argument using only pictures and diagrams.',
    'What\'s the second best policy argument to make on this point?',
    'How would Atticus Finch make this point?',
    'Assume you lost. Why\'d it happen & how should you have stopped it?',
    'If the precedent/statute did not exist, how would this be decided?',
    'It\'s due in an hour. Write the most important thing in the time left.',
    'Write your opponent\'s best argument.',
    
]

if __name__ == '__main__':
    strategy = random.choice(strategies)
    print(strategy)

#figure out how to put online using django or flask
#figure out how to show it in nicer font
#figure out how to change background colors
#figure out how to allow people to choose another
