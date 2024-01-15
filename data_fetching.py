import json
import shopify
import urllib.request
import shopify #https://github.com/Shopify/shopify_python_api
from constants import BULK_OPERATION_COMPLETED, BULK_OPERATION_RUNNING

def shopify_client(shop_url, api_version, private_app_password):
    api_session = shopify.Session(shop_url, api_version, private_app_password)
    shopify.ShopifyResource.activate_session(api_session)
    client = shopify.GraphQL()
    return client
def bulk_operation(query):
    try:
        if not isinstance(query, str):
            return f"Please replace {query} into String Datatype"
        bulk_operation_query = f"""
        mutation {{
            bulkOperationRunQuery(
                query: "{query}"
            ) {{
                bulkOperation {{
                    id
                    status
                }}
                userErrors {{
                    field
                    message
                }}
            }}
        }}
        """
        return bulk_operation_query
    except Exception as e:
        return str(e)

    
q_bulk_status = """
    query bulkStatus($id: ID!) {
        node(id: $id) {
            ... on BulkOperation {
                id
                status
                errorCode
                createdAt
                completedAt
                objectCount
                url
                partialDataUrl
            }
        }
    }
"""

def bulk_status(client, bulk):
    try:
        status = {}
        
        if not isinstance(bulk, str):
            return f"Please replace {bulk} into String Datatype"
        
        if "data" in bulk:
            bulk_id = json.loads(bulk)["data"]["bulkOperationRunQuery"]["bulkOperation"]["id"]
            
            while True:
                bulk_query_executed = client.execute(q_bulk_status, {"id": bulk_id})
                status = json.loads(bulk_query_executed)
                if status["data"]["node"]["status"] != BULK_OPERATION_RUNNING:                
                    return status
    
        return "Cannot get status of bulk operation"
    except Exception as e:
        return str(e)

def get_bulk_data(bulk_status):
    try:        
        if "data" in bulk_status and "node" in bulk_status["data"] \
        and "status" in bulk_status["data"]["node"]:
            orders = []
            if bulk_status['data']['node']['status'] == BULK_OPERATION_COMPLETED: 
                url = bulk_status['data']['node']['url']
                order_data = urllib.request.urlopen(url)
                for line in order_data:
                    l = json.loads(line.decode('utf8'))
                    if 'id' in l:
                        orders.append(l)

            return orders or []
    except Exception as e:
        return str(e)