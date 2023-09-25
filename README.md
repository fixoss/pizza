# Pizza!

The most over-engineered pizza calculator ever!

## Requirements
* Python3
* PyTest
* Hunger for 🍕

## Usage:

Run

```
$ python3 pizza.py
```

Enter your inputs to the recipe:
 * number of dough balls
 * ball weight
 * hydration amount
 * etc...

It will print out the appropriate measurements to make the best tasting pizza pie.

Example output

```
Number of pizzas (8): 4
Size grams (250g): 240
Hydration (65%): 65
---
Flour (100%): 571g
Water (65%): 371g
Salt (3%): 17.13g
Yeast (0.08%): 0.46g
```

It will also remember the previous inputs provided to make it easier to tweak a good recipe.

## Tests

[Install pytest](https://docs.pytest.org/en/7.4.x/getting-started.html#getstarted)
```
$ cd pizza/
$ pytest
================================================== test session starts ===================================================
platform linux -- Python 3.11.2, pytest-7.2.1, pluggy-1.0.0+repack
rootdir: /your/path/to/pizza
collected 4 items                                                                                                        

test_pizza.py ....                                                                                                 [100%]

=================================================== 4 passed in 0.02s ====================================================
```

## Roadmap

- [x] Save previous recipe 
- [x] Customise hydration %
- [ ] Timestamped recipes, rolling history
- [ ] Customise yeast %
- [ ] Customise salt %
- [ ] Proving time calculation ?
- [ ] Different yeast types ?
- [ ] Adjust for room temperature ?
