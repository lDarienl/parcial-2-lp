import pytest

from nosql_dsl.parser import ParseError, parse_program


def test_insert_values_objeto():
    src = r'''
        INSERT INTO motos VALUES { "marca": "Yamaha", cc: 600, ok: true };
    '''
    tree = parse_program(src)
    assert tree.getChildCount() >= 1


def test_get_from_sin_where():
    src = "GET FROM motos;"
    tree = parse_program(src)
    assert tree is not None


def test_get_from_con_where_and_or_not():
    src = """
        GET FROM motos WHERE (precio < 10000 AND marca == \"Yamaha\") OR NOT (activa == false);
    """
    tree = parse_program(src)
    assert tree is not None


def test_update_set_where():
    src = """
        UPDATE motos SET cilindrada = 650 WHERE id == \"m1\";
    """
    tree = parse_program(src)
    assert tree is not None


def test_delete_from_where():
    src = 'DELETE FROM motos WHERE id == "m1";'
    tree = parse_program(src)
    assert tree is not None


def test_comentario_linea_ignorado():
    src = """
        // comentario
        GET FROM x;
    """
    assert parse_program(src) is not None


def test_varias_instrucciones():
    src = """
        INSERT INTO c VALUES { "a": 1 };
        GET FROM c WHERE a == 1;
    """
    tree = parse_program(src)
    assert len(tree.instruccion()) == 2


def test_operadores_comparacion():
    src = 'GET FROM t WHERE x >= 1 AND y <= 2 AND z != 0 AND w == 3;'
    assert parse_program(src) is not None


def test_null_y_boolean_case_insensitive():
    src = """
        INSERT INTO c VALUES { "n": null, "b": False, "t": TRUE };
    """
    assert parse_program(src) is not None


def test_array_anidado():
    src = 'INSERT INTO c VALUES { "arr": [1, 2, { "k": "v" }] };'
    assert parse_program(src) is not None


def test_error_falta_punto_y_coma():
    with pytest.raises(ParseError):
        parse_program("GET FROM x")


def test_string_con_escape():
    src = r'INSERT INTO c VALUES { "t": "dice \"hola\"" };'
    assert parse_program(src) is not None
