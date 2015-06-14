import itertools
import statistics
from collections import Counter

from war import WarRunner

games = []
for i in range(0,100 0):
	game = WarRunner(False)
	games.append(game.play())

# depths = [game['war_depths'] for game in games]
# print('War depths:')
# print(Counter(itertools.chain(*depths)))
# print('')



turns = [game['turn_count'] for game in games]

endless_games = turns.count(5000)
print('Unending games: %d/100' % endless_games)
print('')

print('Turn count (without endless games):')
ending_games = [x for x in turns if x < 5000]
print('Mean: %d' % statistics.mean(ending_games))
print('Median: %d' % statistics.median(ending_games))
print('Min: %d' % min(ending_games))
print('Max: %d' % max(ending_games))
print('')

# wars = [game['war_count'] for game in games]
# print('War count per game:')
# print('Mean: %d' % statistics.mean(wars))
# print('Median: %d' % statistics.median(wars))
# print('Min: %d' % min(wars))
# print('Max: %d' % max(wars))
