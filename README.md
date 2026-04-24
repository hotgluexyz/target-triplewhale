# target-triplewhale

`target-triplewhale` is a [Singer](https://www.singer.io/) target for [Triplewhale](https://www.triplewhale.com/). It sends tap records to the Triplewhale HTTP API using the [Hotglue Singer SDK](https://pypi.org/project/hotglue-singer-sdk/) (`hotglue-singer-sdk`).

## What it does

- **Base URL**: `https://api.triplewhale.com/api/v2` (set in `target_triplewhale/clients.py`; change there if you use another environment).
- **Auth**: `api_key` from config is sent as the `x-api-key` header with `Content-Type: application/json`.
- **Sinks**: Each Singer stream is handled by a sink class. Stream names must match the sink’s `name` (case-insensitive per SDK).

## Installation

```bash
pip install .
```

From a clone of this repository:

```bash
cd target-triplewhale
poetry install
```

## Configuration

| Setting   | Description |
|-----------|-------------|
| `api_key` | Triplewhale API key (`x-api-key` header). |

### Example `config.json`

```json
{
  "api_key": "your-triplewhale-api-token"
}
```

## Supported streams

| Singer stream | HTTP method | Path (under base URL) | Notes |
|---------------|-------------|------------------------|--------|
| `Orders`      | `POST`      | `/data-in/orders`      | Record body is sent as JSON; `preprocess_record` may shape the payload before the request. |

## Usage

```bash
target-triplewhale --version
target-triplewhale --help
tap-your-source | target-triplewhale --config config.json
```

Run as a module from the repo root (so imports resolve):

```bash
python -m target_triplewhale.target --config path/to/config.json < tap_output.jsonl
```

## Development

```bash
poetry install
poetry run target-triplewhale --help
```

## License

Apache 2.0
