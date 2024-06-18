from page_objects.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from locators.order_history_page_locators import OrderHistoryPageLocators
import allure


class FeedPage(BasePage):
    @allure.step('Получить текст заголовка раздела заказов')
    def get_text_on_title_of_orders_list(self):
        return self.get_text_on_element(FeedPageLocators.title_of_orders_feed)

    @allure.step('Кликнуть по первому (последнему) заказу в ленте')
    def click_on_order_card(self):
        self.wait_visibility_of_element(FeedPageLocators.order_in_feed)
        self.click_on_element(FeedPageLocators.order_in_feed)

    @allure.step('Получить текст заголовка окна с деталями заказа')
    def get_text_on_title_of_modal_order(self):
        return self.get_text_on_element(FeedPageLocators.title_of_modal_order)

    @allure.step('Получить количество заказов, выполненных за все время')
    def get_quantity_of_orders(self):
        self.find_element_with_wait(FeedPageLocators.quantity_of_orders)
        return self.get_text_on_element(FeedPageLocators.quantity_of_orders)

    @allure.step('Получить количество заказов, выполненных за сегодня')
    def get_daily_quantity_of_orders(self):
        self.find_element_with_wait(FeedPageLocators.daily_quantity_of_orders)
        return self.get_text_on_element(FeedPageLocators.daily_quantity_of_orders)

    @allure.step('Проверить наличие номера созданного заказа в списке ленты')
    def check_id_order_in_feed(self, order_id):
        locator = OrderHistoryPageLocators.order_card_id
        xpath_with_order_number = f'{locator[1]}[contains(text(), "{order_id}")]'
        locator_with_order_number = (locator[0], xpath_with_order_number)
        return self.find_element_with_wait(locator_with_order_number)

    @allure.step('Проверить появление номера нового заказа в разделе "В работе"')
    def check_displaying_order_number_in_feed_progress_section(self, order_number):
        locator = FeedPageLocators.number_of_order_in_progress
        xpath_with_order_number = f'{locator[1]}[contains(normalize-space(), "{order_number}")]'
        locator_with_order_number = (locator[0], xpath_with_order_number)
        self.wait_visibility_of_element(locator_with_order_number)
        return self.find_element_with_wait(locator_with_order_number)
