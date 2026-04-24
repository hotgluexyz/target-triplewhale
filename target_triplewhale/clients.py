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