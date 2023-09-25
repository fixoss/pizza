import json

class PizzaRecipe:
	recipe_path = "./recipe.json"

	def __init__(self, num_pizzas=4, ball_weight_g=240, hydration=60):
		self.num_pizzas = num_pizzas
		self.ball_weight_g = ball_weight_g
		self.hydration = hydration
	
	def save(self, path=recipe_path):
		recipe_dict = {
			"num_pizzas": self.num_pizzas,
			"ball_weight_g": self.ball_weight_g,
			"hydration": self.hydration
		}
		with open(path, 'w') as f:
			json.dump(recipe_dict, f, ensure_ascii=True)

	def load(self, path=recipe_path):
		with open(path, 'r') as f:
			recipe_dict = json.loads(f.read())

	def ingredients(self):
		dough_weight_g = self.num_pizzas * self.ball_weight_g
		flour_ratio = 100
		water_ratio = self.hydration
		salt_ratio = 3
		yeast_ratio = 0.08
		total_ratio = flour_ratio + water_ratio + yeast_ratio + salt_ratio

		dough_ratio = dough_weight_g / total_ratio
		flour_weight_g = dough_ratio * flour_ratio
		water_weight_g = dough_ratio * water_ratio
		salt_weight_g = dough_ratio * salt_ratio
		yeast_weight_g = dough_ratio * yeast_ratio

		return {
			"flour_ratio": flour_ratio,
			"flour": flour_weight_g,
			"water_ratio": water_ratio,
			"water": water_weight_g,
			"salt_ratio": salt_ratio,
			"salt": salt_weight_g,
			"yeast_ratio": yeast_ratio,
			"yeast": yeast_weight_g
		}



def run():
	# Let there be pizza
	mypizza = PizzaRecipe()

	try:
		# Try to grab the previous pizza recipe
		mypizza.load()
	except IOError as e:
		# If no recipes exist, then we start a new recipe from scratch
		mypizza = PizzaRecipe()

	try:
		mypizza.num_pizzas = int(input(f"Number of pizzas ({mypizza.num_pizzas}): "))
	except:
		pass

	try:
		mypizza.ball_weight_g = int(input(f"Size grams ({mypizza.ball_weight_g}g): "))
	except:
		pass

	try:
		mypizza.hydration = int(input(f"Hydration ({mypizza.hydration}%): "))
	except:
		pass

	ingredients = mypizza.ingredients()

	results = ["---"]
	results += [f"Flour ({ingredients['flour_ratio']}%): {ingredients['flour']:.0f}g"]
	results += [f"Water ({ingredients['water_ratio']}%): {ingredients['water']:.0f}g"]
	results += [f"Salt ({ingredients['salt_ratio']}%): {ingredients['salt']:.2f}g"]
	results += [f"Yeast ({ingredients['yeast_ratio']}%): {ingredients['yeast']:.2f}g"]

	mypizza.save()
	print("\n".join(results))

if __name__ == "__main__":
	run()