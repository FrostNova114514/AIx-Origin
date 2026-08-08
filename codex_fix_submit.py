from pathlib import Path

app = Path('/www/wwwroot/aixorigin/frontend/src/App.vue')
text = app.read_text()
text = text.replace('name="github_homepage" type="url"', 'name="github_homepage" type="text"')
app.write_text(text)

views = Path('/www/wwwroot/aixorigin/website/views.py')
text = views.read_text()
old = """    def rating(name):
        raw = value(name)
        if not raw:
            return None
        try:
            score = int(raw)
        except ValueError:
            raise ValueError(f'{name} 必须是 1-4 的数字')
        if score not in (1, 2, 3, 4):
            raise ValueError(f'{name} 必须是 1-4 的数字')
        return score

    required_fields = {
"""
new = """    def rating(name):
        raw = value(name)
        if not raw:
            return None
        try:
            score = int(raw)
        except ValueError:
            raise ValueError(f'{name} 必须是 1-4 的数字')
        if score not in (1, 2, 3, 4):
            raise ValueError(f'{name} 必须是 1-4 的数字')
        return score

    def normalize_url(raw):
        raw = raw.strip()
        if not raw:
            return ''
        if raw.startswith(('http://', 'https://')):
            return raw
        return f'https://{raw}'

    required_fields = {
"""
text = text.replace(old, new)
text = text.replace("github_homepage = value('github_homepage') or value('github')", "github_homepage = normalize_url(value('github_homepage') or value('github'))")
views.write_text(text)
print('patched')
