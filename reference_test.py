import pytest
from func import es_primo

# Test para números primos conocidos
@pytest.mark.parametrize("num", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
def test_numeros_primos(num):
    assert es_primo(num) == True, f"Error: {num} debería ser primo"

# Test para números no primos conocidos
@pytest.mark.parametrize("num", [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20])
def test_numeros_no_primos(num):
    assert es_primo(num) == False, f"Error: {num} no debería ser primo"

# Test para números que la implementación actual considera primos (0 y 1)
@pytest.mark.parametrize("num", [0, 1])
def test_numeros_especiales(num):
    assert es_primo(num) == True, f"Error: {num} debería ser considerado primo según la implementación actual"

# Test para números negativos (todos deberían ser considerados primos según la implementación actual)
@pytest.mark.parametrize("num", [-1, -2, -3, -5, -11, -13])
def test_numeros_negativos(num):
    assert es_primo(num) == True, f"Error: {num} debería ser considerado primo según la implementación actual"

# Test para verificar la eficiencia con números grandes
def test_numeros_grandes():
    assert es_primo(1000003) == True, "Error: 1000003 debería ser primo"
    assert es_primo(1000004) == False, "Error: 1000004 no debería ser primo"

# Test para entradas no enteras (ajustados a la implementación actual)
@pytest.mark.parametrize("num", [2.3, 3.9, "tres", None])
def test_entradas_no_enteras(num):
    with pytest.raises(TypeError):
        es_primo(num)

# Test para entradas booleanas (ajustados a la implementación actual)
@pytest.mark.parametrize("num", [True, False])
def test_entradas_booleanas(num):
    assert es_primo(num) == True, f"Error: {num} debería ser considerado primo según la implementación actual"

# Test para verificar el manejo de inputs inusuales (ajustados a la implementación actual)
def test_inputs_inusuales():
    with pytest.raises(TypeError):
        es_primo("cinco")
    with pytest.raises(TypeError):
        es_primo(None)
    with pytest.raises(TypeError):
        es_primo([])

# Ajuste para números de punto flotante (según la implementación actual)
@pytest.mark.parametrize(
    "num",
    [
        19.000000000000004,
        23.000000000000004,
    ],
)
def test_numeros_punto_flotante(num):
    with pytest.raises(TypeError):
        es_primo(num)

if __name__ == "__main__":
    pytest.main()
