import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1,25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4,'печиво','солодке',30)
    product_qnt = db.select_product_qnt_by_id(4)

    assert product_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.database
def test_insert_product():
    db = Database()
    db.insert_product(5,'кукурудза','солона',100)
    product_qnt = db.select_product_qnt_by_id(5)

    assert product_qnt[0][0] == 100

@pytest.mark.database
def test_product_name():
    db = Database()
    product_name = db.get_product_name_by_id(5)
    print(product_name)

    assert product_name[0][0] != 'qwer'
    assert product_name[0][0] == 'кукурудза'
    assert len(product_name) == 1

@pytest.mark.database
def test_product_id():
    db = Database()
    product_id = db.get_product_id_by_name('кукурудза')

    assert product_id[0][0] != 'qw'
    assert product_id[0][0] == 5
    assert product_id[0][0] != 4
    
@pytest.mark.database
def test_new_user():
    db = Database()
    db.insert_new_user(3,'Volodymyr','Sobornosti 25','Dnipro',7777, 'Ukraine')
    new_customer = db.get_user_by_id(3)
    print(new_customer)

    assert new_customer[0][0] == 'Volodymyr'
    assert new_customer[0][1] == 'Sobornosti 25'
    assert new_customer[0][2] == 'Dnipro'
    assert new_customer[0][3] == '7777'
    assert new_customer[0][-1] == 'Ukraine'


@pytest.mark.database
def test_deleted_user():
    db = Database()
    db.insert_new_user(4,'Volodymyr1','Sobornosti 222','Dnipro',7777, 'Ukraine')
    db.delete_user_by_id(3)
    users = db.get_all_users()
    print(users)
    user = db.get_user_by_id(3)

    assert user == []

@pytest.mark.database
def test_data_id():
    db = Database()
    db.insert_new_user(5.5,'Volodymyr1','Sobornosti 222','Dnipro',7777, 'Ukraine')
# sqlite3.IntegrityError: datatype mismatch

@pytest.mark.database
def test_data_name():
    db = Database()
    db.insert_new_user(5,15,'Sobornosti 222','Dnipro',7777, 'Ukraine')
    # sqlite3.OperationalError: database is locked

@pytest.mark.database
def test_data_postcode():
    db = Database()
    db.insert_new_user(5,'Volodymyr2','Sobornosti 222','Dnipro',777.22, 'Ukraine')
    # sqlite3.OperationalError: database is locked

@pytest.mark.database
def test_data_postcode():
    db = Database()
    db.insert_new_user(5,'Volodymyr2','Sobornosti 222','Dnipro',-777, 'Ukraine')
    #sqlite3.OperationalError: database is locked

@pytest.mark.database
def test_data_product_qnt():
    db = Database()
    db.update_product_qnt_by_id(5,2/3)
    product_qnt = db.select_product_qnt_by_id(5)
    assert product_qnt[0][0] == 2/3

    
@pytest.mark.database
def test_data_product_qnt1():
    db = Database()
    db.update_product_qnt_by_id(5,-177)
    product_qnt = db.select_product_qnt_by_id(5)
    assert product_qnt[0][0] == -177


@pytest.mark.database
def test_data_product_qnt2():
    db = Database()
    db.update_product_qnt_by_id(5,'qnt')
    product_qnt = db.select_product_qnt_by_id(5)
    assert product_qnt[0][0] == 'qnt'
    # sqlite3.OperationalError: no such column: qnt

@pytest.mark.database
def test_list_products():
    db = Database()
    products = db.get_distinct_values('products', 'name')
    print("product names:", products)
    assert len(products) >= 4

@pytest.mark.database
def test_get_all_orders_count():
    db = Database()
    orders_count = db.count_rows('orders')
    print("General orders count is", orders_count)
    assert orders_count >= 1

@pytest.mark.database # check of adding new column 'price' to 'products' table
def test_add_price_column_to_products():
    db = Database()
    columns = db.get_table_columns('products')
    print("Current column_names in 'products' table:", columns)
    if 'price' not in columns:
        updated_columns = db.add_new_column('products', 'price', 'REAL')
        print("Updated columns:", updated_columns)
        assert 'price' in updated_columns
    else:
        print("Column 'price' already exists in 'products' table.")
        assert 'price' in columns

@pytest.mark.database # check of setting prices for products
def test_set_products_price():
    db = Database()
    products = db.get_all_products()
    print("Products before setting prices:", products)
    price = 10

    for id, name in products:
        db.set_price_for_each_product(id, name, price)
        price += 10

    prices = db.get_price_column_values()
    print("Product prices after setting:", prices)
    assert len(prices) >= 5
    assert prices[0][0] == 10
    assert prices[1][0] == 20
    assert prices[2][0] == 30
    assert prices[3][0] == 40
    assert prices[4][0] == 50
    assert prices[0][0] != 15

@pytest.mark.database # checking max price after setting prices
def test_check_max_product_price():
    db = Database()
    max_price = db.get_max_product_price()
    print("Max product price is", max_price)
    assert max_price <= 50
    assert max_price != 30

@pytest.mark.database # checking search by pattern in address column of customers table
def test_search_by_pattern_in_customers_address():
    db = Database()
    pattern = '%Nezalezhnosti%'
    records = db.search_by_pattern('customers', 'address', pattern)
    print(f"Customers with address like '{pattern}':", records)
    assert len(records) >= 1
    assert records[0][1] == 'Sergii'
    assert records[0][1] != 'Volodymyr1'

@pytest.mark.database # checking grouping by column in products table
def test_group_by_product_name():
    db = Database()
    grouped_records = db.group_by_column('products', 'name')
    print("Products grouped by name with counts:", grouped_records)
    assert len(grouped_records) >= 4
    assert grouped_records[0][0] == 'солодка вода'
    assert grouped_records[0][1] == 2
    assert grouped_records[0][0] != 'печиво'
    assert grouped_records[1][0] == 'печиво'
    assert grouped_records[1][1] == 1
    assert grouped_records[2][0] == 'молоко'
    assert grouped_records[2][1] == 1
    assert grouped_records[3][0] == 'кукурудза'
    assert grouped_records[3][1] == 1