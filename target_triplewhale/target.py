"""Triplewhale target class."""

from hotglue_singer_sdk import typing as th
from hotglue_singer_sdk.target_sdk.target import TargetHotglue

from target_triplewhale.sinks import OrdersSink, SubscriptionsSink


class TargetTriplewhale(TargetHotglue):
    """Sample target for Triplewhale."""

    name = "target-triplewhale"
    reference_data = {}

    config_jsonschema = th.PropertiesList(
        th.Property("access_token", th.StringType, required=True),
        th.Property("shop", th.StringType, required=True),
        th.Property("platform_account_id", th.StringType, required=True),
    ).to_dict()

    SINK_TYPES = [OrdersSink, SubscriptionsSink]

if __name__ == "__main__":
    TargetTriplewhale.cli()
