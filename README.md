# Setup

```bash
pip install uv
uv venv
source .venv/bin/activate.fish
uv pip compile requirements.in --universal --output-file requirements.txt
uv pip sync requirements.txt
```
