import stripe
from forex_python.converter import CurrencyRates
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    """ Создает продукт в страйпе """

    # return stripe.Product.create(
    #     name=instance.get('name'),
    #     description=instance.get('description'),
    #     images=[instance.get('image')],
    # )
    title_product = f"{instance.paid_course}" if instance.paid_course else instance.paid_lesson
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get("id")


def convert_rub_to_dollars(payment_sum):
    """ Конвертирует рубли в доллары """

    c = CurrencyRates()
    rate = c.get_rate('RUB', 'USD')
    return int(payment_sum * rate)


def create_stripe_price(payment_sum):
    """ Создает цену в страйпе """

    return stripe.Price.create(
        currency="usd",
        unit_amount=payment_sum * 100,
        product_data={"name": "Payment"},
    )


def create_stripe_session(price):
    """ Создает сессию На оплату в страйпе """

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')

    # return stripe.checkout.Session.create(
    #     payment_method_types=['card'],
    #     line_items=[{
    #         'price': price.get('id'),
    #         'quantity': 1,
    #     }],
    #     mode='payment',
    #     success_url='http://127.0.0.1:8000/success/',
    #     cancel_url='http://127.0.0.1:8000/cancel/',
    # )
