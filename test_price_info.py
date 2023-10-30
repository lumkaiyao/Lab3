import price_info


def test_total_cost_shopping():
    result = []
    price_lists = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear': 0.90}
    quantity_lists = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2, 'pear': 10}
    result=price_info.total_cost_shopping(price_lists,quantity_lists)
    assert result==33.9


def test_cost_of_fruits():
    result=[]
    result=price_info.cost_of_fruits("apple",10)
    assert(result==12)
