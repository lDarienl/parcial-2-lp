from nosql_dsl import InMemoryCrudInterpreter


def test_crud_flujo_basico():
    src = """
        INSERT INTO motos VALUES { "id": "m1", "marca": "Yamaha", "cc": 600 };
        INSERT INTO motos VALUES { "id": "m2", "marca": "Honda", "cc": 500 };
        UPDATE motos SET cc = 650 WHERE id == "m1";
        GET FROM motos WHERE marca == "Yamaha";
    """
    vm = InMemoryCrudInterpreter()
    vm.run(src)
    assert len(vm.last_read) == 1
    assert vm.last_read[0]["cc"] == 650
    assert vm.last_read[0]["marca"] == "Yamaha"


def test_delete_where():
    src = """
        INSERT INTO c VALUES { "n": 1 };
        INSERT INTO c VALUES { "n": 2 };
        DELETE FROM c WHERE n == 1;
        GET FROM c;
    """
    vm = InMemoryCrudInterpreter()
    vm.run(src)
    assert len(vm.last_read) == 1
    assert vm.last_read[0]["n"] == 2
