from hotglue_singer_sdk.target_sdk.client import HotglueSink


class TriplewhaleSink(HotglueSink):
    
    base_url = "https://api.triplewhale.com/api/v2"
    
    @property
    def name(self) -> str:
        return self.stream_name
    
    @property
    def http_headers(self) -> dict:
        return {
            "x-api-key": f"{self.config.get('api_key')}",
            "Content-Type": "application/json",
        }

    def preprocess_record(self, record: dict, context: dict) -> dict:
        # add shop and platform_account_id to the record from config
        record["shop"] = self.config.get("shop")
        record["platform_account_id"] = self.config.get("platform_account_id")
        return record
    
    def upsert_record(self, record: dict, context: dict):
        state_updates = {}
        record_id = record.get("id")
        method = "POST"
        response = self.request_api(method, self.endpoint, request_data=record)
        return record_id, response.ok, state_updates