## inTheBagBot

Note: This is a WIP, currently works from [oobabooga webui](https://github.com/oobabooga/text-generation-webui)'s API.  If you don't have that running with the API enabled, this won't work.

---

Setup:

- Install Python 3.10 (pyenv recommended)
- Copy `.env.example` to `.env`
```bash
cp .env.example .env
```
- Add telegram token ([docs](https://core.telegram.org/bots/api))
- Add comma separated list of chat ids `1,-2`
- Setup venv & requirements
```bash
python -m venv .venv
. .venv/Scripts/activate
python -m pip install -r requirements.txt
```
- Run the bot
```bash
python main.py
```

--- 

Todo:
- Use langchain instead of oobabooga api
- Use a conversational model/prompt, not just basic
- Add history of a telegram chat with vector db and json export
- Persist conversations if reply chain is relevant
- Find good base models to use for conversation
- Give a persona? or multiple personas
- Test coverage cause we love test coverage
