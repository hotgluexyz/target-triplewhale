from target_triplewhale.clients import TriplewhaleSink


class OrdersSink(TriplewhaleSink):

    name = "Orders"
    endpoint = "/data-in/orders"



class SubscriptionsSink(TriplewhaleSink):

    name = "Subscriptions"
    endpoint = "/data-in/subscriptions"
    