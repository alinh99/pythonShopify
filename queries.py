order_query = """
    query OrdersQuery($cursor: String)   {
        orders(first: 1, after: $cursor) {
            edges {
                node {
                    id
                    name
                    
                    displayFinancialStatus
                    displayFulfillmentStatus
                    customerAcceptsMarketing
                    currencyCode
                    subtotalPrice
                    discountCode
                    note
                    phone
                    subtotalLineItemsQuantity
                    tags
                    
                    customer {
                        displayName
                    }
                    
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
                        title
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

product_query = """
query ProductsQuery($cursor: String) {
    inventoryItems(first: 1, after: $cursor) {
        edges {
            node {
                id
                sku
                variant {
                    id
                    displayName
                    image {
                        url
                    }
                    inventoryQuantity
                    inventoryItem {
                        id
                    }
                }
                inventoryLevels(first: 1) {
                    edges {
                        node {
                            id
       											quantities(names: ["available", "on_hand", "committed", "quality_control"]){
                            	name
                            	quantity
                          }
                        }
                    }
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
