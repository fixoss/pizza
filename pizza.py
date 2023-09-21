import json

def run():
	recipe_dict = {}

	recipe_path = "./recipe.json"

	try:
		with open(recipe_path, "r") as f:
			recipe_dict = json.loads(f.read())
	except Exception as e:
		#print(e)
		pass

	recipe_dict["num_pizzas"] = recipe_dict.get("num_pizzas", 4)
	try:
		recipe_dict["num_pizzas"] = int(input(f"Number of pizzas ({recipe_dict['num_pizzas']}): "))
	except:
		pass

	recipe_dict["ball_weight_g"] = recipe_dict.get("ball_weight_g", 240)
	try:
		recipe_dict["ball_weight_g"] = int(input(f"Size grams ({recipe_dict['ball_weight_g']}g): "))
	except:
		pass

	recipe_dict["hydration"] = recipe_dict.get("hydration", 60)
	try:
		recipe_dict["hydration"] = int(input(f"Hydration ({recipe_dict['hydration']}%): "))
	except:
		pass

	dough_weight_g = recipe_dict["num_pizzas"] * recipe_dict["ball_weight_g"]
	flour_ratio = 100
	water_ratio = recipe_dict["hydration"]
	salt_ratio = 3
	yeast_ratio = 0.15

	total_ratio = flour_ratio + water_ratio + yeast_ratio + salt_ratio

	dough_ratio = dough_weight_g / total_ratio
	flour_weight_g = dough_ratio * flour_ratio
	water_weight_g = dough_ratio * water_ratio
	salt_weight_g = dough_ratio * salt_ratio
	yeast_weight_g = dough_ratio * yeast_ratio

	yeast_tsps_to_g = 1.0 / 2.8
	yeast_tsps = yeast_weight_g * yeast_tsps_to_g

	results = ["---"]
	results += [f"Flour ({flour_ratio}%): {flour_weight_g:.0f}g"]
	results += [f"Water ({water_ratio}%): {water_weight_g:.0f}g"]
	results += [f"Salt ({salt_ratio}%): {salt_weight_g:.2f}g"]
	results += [f"Yeast ({yeast_ratio}%): {yeast_weight_g:.2f}g or {yeast_tsps:.2f} tsps"]

	print("\n".join(results))

	with open(recipe_path, "w") as f:
		json.dump(recipe_dict, f, ensure_ascii=True)

if __name__ == "__main__":
	run()