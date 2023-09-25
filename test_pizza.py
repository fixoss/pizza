from pizza import PizzaRecipe
import json

def test_recipe_inputs():
    custom_inputs = PizzaRecipe(num_pizzas=42, ball_weight_g=42, hydration=42)
    assert custom_inputs.num_pizzas == 42
    assert custom_inputs.ball_weight_g == 42
    assert custom_inputs.hydration == 42

def test_writetofile(tmpdir):
    saved = PizzaRecipe(num_pizzas=42, ball_weight_g=42, hydration=42)
    file = tmpdir.join('output.json')
    saved.save(file.strpath)
    assert file.read() == '{"num_pizzas": 42, "ball_weight_g": 42, "hydration": 42}'

def test_readfromfile(tmpdir):
    recipe_dict = {
        "num_pizzas": 42,
        "ball_weight_g": 42,
        "hydration": 42
    }
    file = tmpdir.join('input.json')
    with open(file.strpath, 'w') as f:
        json.dump(recipe_dict, f, ensure_ascii=True)

    testload = PizzaRecipe()
    testload.load(file.strpath)
    assert testload.num_pizzas == 42
    assert testload.ball_weight_g == 42
    assert testload.hydration == 42


def test_ingredient_calculations():
    pie = PizzaRecipe(num_pizzas=10, ball_weight_g=250, hydration=70)
    ingredients = pie.ingredients()
    assert ingredients['flour'] == 1444.4187658886062
    assert ingredients['water'] == 1011.0931361220245
    assert ingredients['salt'] == 43.33256297665819
    assert ingredients['yeast'] == 1.155535012710885
