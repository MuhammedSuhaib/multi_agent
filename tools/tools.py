from agents import function_tool
from data.data import FAQS, ORDERS

# ---------------------- FAQ Tool ----------------------
# This tool answers frequently asked questions about products, shipping, returns, and contact info.
# It uses a simple keyword match to find the answer.

def faq_is_enabled(query: str) -> bool:
    # Enable only if query contains 'faq', 'question', or matches a known FAQ
    keywords = ["faq", "question"] + list(FAQS.keys())
    return any(k in query.lower() for k in keywords)

def faq_error_function(user_query: str) -> str:
    # Return a friendly error if the question is not found
    return "Sorry, I couldn't find an answer to your question. Please contact support."

@function_tool(name_override="faq_tool",description_override="Answer FAQ about products, shipping, returns, and contact info.")
def faq_tool(user_query: str) -> str:
    """
    FAQ tool: Answers common customer questions.
    Returns a canned answer if a match is found, otherwise a friendly error.
    """
    if not faq_is_enabled(user_query):
        return "Tool not enabled for this query."
    for k, v in FAQS.items():
        if k in user_query.lower():
            return v
    return faq_error_function(user_query)

# ---------------------- Order Status Tool ----------------------
# This tool simulates fetching order status for a given order ID.
# It only activates if the query is about an order.

def error_function(order_id: str) -> str:
    # Return a friendly error if the order ID is not found
    return f"Sorry, order ID '{order_id}' was not found. Please check and try again."

def is_enabled(query: str) -> bool:
    # Only enable this tool if the query contains the word "order"
    return "order" in query.lower()

@function_tool(name_override="lookup_order",description_override="Fetch order status by ID",)
def lookup_order(order_id: str, user_query: str) -> str:
    """
    Order status tool: Looks up the status of an order by ID.
    Returns the status if found, otherwise a friendly error.
    """
    if not is_enabled(user_query):
        return "Tool not enabled for this query."
    status = ORDERS.get(order_id)
    if not status:
        return error_function(order_id)
    return f"Order {order_id} status: {status}"
