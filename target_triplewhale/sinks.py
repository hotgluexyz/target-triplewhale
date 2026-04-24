from target_triplewhale.clients import TriplewhaleSink


class OrdersSink(TriplewhaleSink):

    name = "Orders"
    endpoint = "/data-in/orders"

    def preprocess_record(self, record: dict, context: dict) -> dict:
        return record

    def upsert_record(self, record: dict, context: dict):
        state_updates = {}
        record_id = record.get("id")
        method = "POST"
        response = self.request_api(method, self.endpoint, request_data=record)
        return record_id, response.ok, state_updates
    