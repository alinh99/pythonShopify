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
    
    total_tax_attr_checking = check_existed_attr(data, "totalTax")
    total_tax_existed = check_existed_value(total_tax_attr_checking)
    
    total_price_attr_checking = check_existed_attr(data, "totalPrice")
    total_price_existed = check_existed_value(total_price_attr_checking)
    
    total_discounts_attr_checking = check_existed_attr(data, "totalDiscounts")
    total_discounts_existed = check_existed_value(total_discounts_attr_checking)
    
    created_at_attr_checking = check_existed_attr(data, "createdAt")
    created_at_existed = check_existed_value(created_at_attr_checking)
    
    note_attr_checking = check_existed_attr(data, "note")
    note_existed = check_existed_value(note_attr_checking)
    
    cancelled_at_attr_checking = check_existed_attr(data, "cancelledAt")
    cancelled_at_existed = check_existed_value(cancelled_at_attr_checking)
    
    refunds_attr_checking = check_existed_attr(data, "refunds")
    refunds_existed = check_existed_value(refunds_attr_checking)
    
    payment_method_attr_checking = check_existed_attr(data, "paymentGatewayNames")
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
    
    payment_terms_name_attr_checking = check_existed_attr(data, "paymentTerms")
    payment_terms_name_existed = check_existed_value(payment_terms_name_attr_checking)
    
    discount_code_attr_checking = check_existed_attr(data, "discountCode")
    discount_code_existed = check_existed_value(discount_code_attr_checking)

    subtotal_line_items_quantity_attr_checking = check_existed_attr(data, "subtotalLineItemsQuantity")
    subtotal_line_items_quantity_existed = check_existed_value(subtotal_line_items_quantity_attr_checking)
    
    return name_existed, email_existed, financial_status_existed, fulfillment_status_existed, \
           buyer_accepts_marketing_existed, currency_existed, subtotal_price_existed, total_tax_existed, \
           total_price_existed, total_discounts_existed, created_at_existed, note_existed, \
           cancelled_at_existed, payment_method_existed, refunds_existed, payment_reference_existed, \
           id_existed, tags_existed, source_existed, phone_existed, duties_existed, payment_terms_name_existed, \
           discount_code_existed, subtotal_line_items_quantity_existed