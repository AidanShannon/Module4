"""


"""


def calculate_price(price, cash_coupon, percent_coupon):
    with_cashcoupon = price - cash_coupon
    with_percentcoupon = with_cashcoupon - (with_cashcoupon * percent_coupon/100)
    subtotal_tax = with_percentcoupon * 1.06
    shipping = 0
    if with_percentcoupon < 10:
        shipping = 5.95
    elif with_percentcoupon < 30:
        shipping = 7.95
    elif with_percentcoupon < 50:
        shipping = 11.95
    else:
        shipping = 0
    return subtotal_tax + shipping


if __name__ == '__main__':
    calculate_price(15.99, 5, 30)
