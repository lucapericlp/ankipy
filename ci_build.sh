pip install uv
uv venv
source .venv/bin/activate
# uv pip compile requirements.in --universal --output-file requirements.txt
uv pip sync requirements.txt
