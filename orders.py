order_query = """
    query OrdersQuery($cursor: String)   {
        orders(first: 1000, after: $cursor) {
            edges {
                node {
                    id
                    name
                    email
                    displayFinancialStatus
                    displayFulfillmentStatus
                    customerAcceptsMarketing
                    currencyCode
                    subtotalPrice
                    discountCode
                    note
                    phone
                    
                    app {
                        id
                        name    
                    }
                    
                    totalTax
                    totalPrice
                    createdAt
                    
                    totalDiscountsSet {
                        shopMoney {
                            amount
                        }
                    }
                    
                    shippingLine {
                        price
                        code
                    }
                    

                    
                    lineItems {
                        edges {
                            node {
                                name
                                quantity
                                
                            }
                        }
                    }
                    
                    billingAddress {
                        address1
                        address2
                        city
                        province
                        countryCode
                        zip
                        provinceCode
                    }
                    
                    channelInformation {
                        channelId
                        channelDefinition {
                        handle
                        channelName
                        }
                    }
                    
                    shippingAddress {
                        address1
                        address2
                        city
                        province
                        countryCode
                        zip
                        provinceCode
                    }
                
                }
            }
            pageInfo {
                hasNextPage
                endCursor
            }
        }
    }
"""