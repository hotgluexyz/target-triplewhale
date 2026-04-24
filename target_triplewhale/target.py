"""Triplewhale target class."""

from hotglue_singer_sdk import typing as th
from hotglue_singer_sdk.target_sdk.target import TargetHotglue

from target_triplewhale.sinks import OrdersSink


class TargetTriplewhale(TargetHotglue):
    """Sample target for Triplewhale."""

    name = "target-triplewhale"
    reference_data = {}

    config_jsonschema = th.PropertiesList(
        th.Property("api_key", th.StringType, required=True),
    ).to_dict()

    SINK_TYPES = [OrdersSink]

if __name__ == "__main__":
    TargetTriplewhale.cli()
