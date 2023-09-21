from pizza import PizzaRecipe

def test_recipe_inputs():
    custom_inputs = PizzaRecipe(num_pizzas=42, ball_weight_g=42, hydration=42)
    assert custom_inputs.num_pizzas == 42

def test_writetofile(tmpdir):
    saved = PizzaRecipe(num_pizzas=42, ball_weight_g=42, hydration=42)
    file = tmpdir.join('output.txt')
    saved.save(file.strpath)
    assert file.read() == '{"num_pizzas": 42, "ball_weight_g": 42, "hydration": 42}'
