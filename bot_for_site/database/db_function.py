from database.data_base import CATEGORIES, SUBCATEGORIES, GOODS


class Goods:
    def __init__(self, goods_id: int) -> None:
        self._goods_id = goods_id

    def get_info(self):
        if self._goods_id in GOODS:
            goods_info = GOODS[self._goods_id]
            subcategory_id = goods_info[1]
            category_id = SUBCATEGORIES[subcategory_id][1]
            category_name = CATEGORIES[category_id]
            subcategory_name = SUBCATEGORIES[subcategory_id][0]
            goods_name = goods_info[0]
            price = goods_info[2]
            item_type = goods_info[3]

            return {
                'Category': category_name,
                'Subcategory': subcategory_name,
                'GoodsName': goods_name,
                'Price': price,
                'ItemType': item_type
            }
        else:
            return None


# Тест вывода товара по ключу GOODS
goods_1 = Goods(27)
goods_info = goods_1.get_info()
if goods_info:
    print("Категория:", goods_info['Category'])
    print("Подкатегория:", goods_info['Subcategory'])
    print("Название товара:", goods_info['GoodsName'])
    print("Цена:", goods_info['Price'])
    print("Тип товара:", goods_info['ItemType'])
else:
    print("Товар не найден.")