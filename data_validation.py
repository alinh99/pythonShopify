def check_existed_attr(data, attr):
    if not attr in data:
        return ""
    return data

def check_existed_value(val):
    if val is None:
        return ""
    return val

def order_data_checking(data=""):
    name_attr_checking = check_existed_attr(data, "name")
    name_existed = check_existed_value(name_attr_checking)
    
    email_attr_checking = check_existed_attr(data, "email")
    email_existed = check_existed_value(email_attr_checking)
    
    financial_status_attr_checking = check_existed_attr(data, "displayFinancialStatus")
    financial_status_existed = check_existed_value(financial_status_attr_checking)
    
    fulfillment_status_attr_checking = check_existed_attr(data, "displayFulfillmentStatus")
    fulfillment_status_existed = check_existed_value(fulfillment_status_attr_checking)
    
    buyer_accepts_marketing_attr_checking = check_existed_attr(data, "customerAcceptsMarketing")
    buyer_accepts_marketing_existed = check_existed_value(buyer_accepts_marketing_attr_checking)
    
    currency_attr_checking = check_existed_attr(data, "currencyCode")
    currency_existed = check_existed_value(currency_attr_checking)
    
    subtotal_price_attr_checking = check_existed_attr(data, "subtotalPrice")
    subtotal_price_existed = check_existed_value(subtotal_price_attr_checking)
    
    total_tax_attr_checking = check_existed_attr(data, "total_tax")
    total_tax_existed = check_existed_value(total_tax_attr_checking)
    
    total_price_attr_checking = check_existed_attr(data, "total_price")
    total_price_existed = check_existed_value(total_price_attr_checking)
    
    total_discounts_attr_checking = check_existed_attr(data, "total_discounts")
    total_discounts_existed = check_existed_value(total_discounts_attr_checking)
    
    created_at_attr_checking = check_existed_attr(data, "created_at")
    created_at_existed = check_existed_value(created_at_attr_checking)
    
    note_attr_checking = check_existed_attr(data, "note")
    note_existed = check_existed_value(note_attr_checking)
    
    cancelled_at_attr_checking = check_existed_attr(data, "cancelled_at")
    cancelled_at_existed = check_existed_value(cancelled_at_attr_checking)
    
    refunds_attr_checking = check_existed_attr(data, "refunds")
    refunds_existed = check_existed_value(refunds_attr_checking)
    
    payment_method_attr_checking = check_existed_attr(data, "payment_gateway_names")
    payment_method_existed = check_existed_value(payment_method_attr_checking)
    
    payment_reference_attr_checking = check_existed_attr(data, "reference")
    payment_reference_existed = check_existed_value(payment_reference_attr_checking)
    
    tags_attr_checking = check_existed_attr(data, "tags")
    tags_existed = check_existed_value(tags_attr_checking)

    source_attr_checking = check_existed_attr(data, "source_name")
    source_existed = check_existed_value(source_attr_checking)
    
    id_attr_checking = check_existed_attr(data, "id")
    id_existed = check_existed_value(id_attr_checking)
    
    phone_attr_checking = check_existed_attr(data, "phone")
    phone_existed = check_existed_value(phone_attr_checking)
    
    duties_attr_checking = check_existed_attr(data, "current_total_duties_set")
    duties_existed = check_existed_value(duties_attr_checking)
    
    payment_terms_name_attr_checking = check_existed_attr(data, "payment_terms")
    payment_terms_name_existed = check_existed_value(payment_terms_name_attr_checking)
    
    discount_code_attr_checking = check_existed_attr(data, "discountCode")
    discount_code_existed = check_existed_value(discount_code_attr_checking)
    
    return name_existed, email_existed, financial_status_existed, fulfillment_status_existed, \
           buyer_accepts_marketing_existed, currency_existed, subtotal_price_existed, total_tax_existed, \
           total_price_existed, total_discounts_existed, created_at_existed, note_existed, \
           cancelled_at_existed, payment_method_existed, refunds_existed, payment_reference_existed, \
           id_existed, tags_existed, source_existed, phone_existed, duties_existed, payment_terms_name_existed, discount_code_existed
               

def line_item_data_checking(data=""):
    quantity_attr_checking = check_existed_attr(data, "quantity")
    quantity_existed = check_existed_value(quantity_attr_checking)
    
    product_name_attr_checking = check_existed_attr(data, "name")
    product_name_existed = check_existed_value(product_name_attr_checking)
    
    price_attr_checking = check_existed_attr(data, "price")
    price_existed = check_existed_value(price_attr_checking)
    
    sku_attr_checking = check_existed_attr(data, "sku")
    sku_existed = check_existed_value(sku_attr_checking)
    
    requires_shipping_attr_checking = check_existed_attr(data, "requires_shipping")
    requires_shipping_existed = check_existed_value(requires_shipping_attr_checking)
    
    taxable_attr_checking = check_existed_attr(data, "taxable")
    taxable_existed = check_existed_value(taxable_attr_checking)
    
    fulfillment_status_attr_checking = check_existed_attr(data, "fulfillment_status")
    fulfillment_status_existed = check_existed_value(fulfillment_status_attr_checking)
    
    vendor_attr_checking = check_existed_attr(data, "vendor")
    vendor_existed = check_existed_value(vendor_attr_checking)

    
    discount_attr_checking = check_existed_attr(data, "total_discount")
    discount_existed = check_existed_value(discount_attr_checking)
    
    return quantity_existed, product_name_existed, price_existed, sku_existed, requires_shipping_existed, \
           taxable_existed, fulfillment_status_existed, vendor_existed, discount_existed
def shipping_line_data_checking(data=""):
    price_attr_checking = check_existed_attr(data, "price")
    price_existed = check_existed_value(price_attr_checking)
    
    shipping_method_attr_checking = check_existed_attr(data, "code")
    shipping_method_existed = check_existed_value(shipping_method_attr_checking)
    
    return price_existed, shipping_method_existed

def fulfillment_data_checking(data=""):
    fulfillment_at_attr_checking = check_existed_attr(data, "created_at")
    fulfillment_at_existed = check_existed_value(fulfillment_at_attr_checking)
    
    return fulfillment_at_existed

def customer_data_checking(data=""):
    first_name_attr_checking = check_existed_attr(data, "first_name")
    first_name_existed = check_existed_value(first_name_attr_checking)
    
    last_name_attr_checking = check_existed_attr(data, "last_name")
    last_name_existed = check_existed_value(last_name_attr_checking)
    
    address1_attr_checking = check_existed_attr(data, "address1")
    address1_existed = check_existed_value(address1_attr_checking)
    
    address2_attr_checking = check_existed_attr(data, "address2")
    address2_existed = check_existed_value(address2_attr_checking)
    
    company_attr_checking = check_existed_attr(data, "company")
    company_existed = check_existed_value(company_attr_checking)
    
    city_attr_checking = check_existed_attr(data, "city")
    city_existed = check_existed_value(city_attr_checking)
    
    zip_attr_checking = check_existed_attr(data, "zip")
    zip_existed = check_existed_value(zip_attr_checking)

    province_attr_checking = check_existed_attr(data, "province_code")
    province_existed = check_existed_value(province_attr_checking)

    country_attr_checking = check_existed_attr(data, "country_code")
    country_existed = check_existed_value(country_attr_checking)

    phone_attr_checking = check_existed_attr(data, "phone")
    phone_existed = check_existed_value(phone_attr_checking)
    
    province_name_attr_checking = check_existed_attr(data, "province")
    province_name_existed = check_existed_value(province_name_attr_checking)
    
    return first_name_existed, last_name_existed, address1_existed, address2_existed, company_existed, \
           city_existed, zip_existed, province_existed, country_existed, phone_existed, province_name_existed

def note_attributes_data_checking(data=""):
    note_attributes_attr_checking = check_existed_attr(data, "note_attributes")
    note_attributes_existed = check_existed_value(note_attributes_attr_checking)
    
    return note_attributes_existed

def tax_line_data_checking(data=""):
    name_attr_checking = check_existed_attr(data, "title")
    name_existed = check_existed_value(name_attr_checking)
    
    rate_attr_checking = check_existed_attr(data, "rate")
    rate_existed = check_existed_value(rate_attr_checking)
    
    value_attr_checking = check_existed_attr(data, "price")
    value_existed = check_existed_value(value_attr_checking)
    
    return name_existed, rate_existed, value_existed

def assign_value(vals):
    if isinstance(vals, list) and not vals:
        return format(float(0), ".2f")
    elif isinstance(vals, list):
        return format(float(sum(vals)), ".2f")
    else:
        return format(float(sum(vals)), ".2f")
