import pytest

from gestion import anadir_cancion, listar_por_estilo



def test_anadir_cancion(monkeypatch, capsys):
    # Simulamos la entrada del usuario
    input_values = iter(["Titulo de la cancion\n", "Interprete\n", "120\n", "Estilo\n", "*****"])
    monkeypatch.setattr('builtins.input', lambda _: next(input_values))

    lista_canciones = []
    anadir_cancion(lista_canciones)
    captured = capsys.readouterr()
    assert "Canción añadida correctamente." in captured.out


def test_listar_por_estilo(monkeypatch, capsys):
    lista_canciones = [
        ["Cancion1", "Interprete1", 120, "Estilo1", "*****"],
        ["Cancion2", "Interprete2", 180, "Estilo2", "***"],
        ["Cancion3", "Interprete3", 150, "Estilo1", "****"]
    ]

    # Simulamos la entrada del usuario
    input_values = iter(["Estilo1", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(input_values))

    listar_por_estilo(lista_canciones)

    captured = capsys.readouterr()
    assert "Cancion1" in captured.out
    assert "Cancion3" in captured.out
    assert "Cancion2" not in captured.out
