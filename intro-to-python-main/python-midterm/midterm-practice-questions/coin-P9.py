import random
results = {
    'heads': 0,
    'tails': 0,
}
sides = list(results.keys())
for i in range(1000):
    results[random.choice(sides)] += 1
print('Heads:', results['heads'])
print('Tails:', results['tails'])