from pizza import PizzaRecipe

def test_recipe_inputs():
    custom_inputs = PizzaRecipe(num_pizzas=42, ball_weight_g=42, hydration=42)
    assert custom_inputs.num_pizzas == 42
    assert custom_inputs.ball_weight_g == 42
    assert custom_inputs.hydration == 42

def test_writetofile(tmpdir):
    saved = PizzaRecipe(num_pizzas=42, ball_weight_g=42, hydration=42)
    file = tmpdir.join('output.txt')
    saved.save(file.strpath)
    assert file.read() == '{"num_pizzas": 42, "ball_weight_g": 42, "hydration": 42}'

def test_ingredient_calculations():
    pie = PizzaRecipe(num_pizzas=10, ball_weight_g=250, hydration=70)
    ingredients = pie.ingredients()
    assert ingredients['flour'] == 1444.4187658886062
    assert ingredients['water'] == 1011.0931361220245
    assert ingredients['salt'] == 43.33256297665819
    assert ingredients['yeast'] == 1.155535012710885
