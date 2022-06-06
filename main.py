from speedy_client.proxy import JsProxy as API
import os
import webview

def get_entrypoint():

    def exists(path: str) -> bool:
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    if exists('./speedy_frontend/dist/index.html'):  # unfrozen development
        return './speedy_frontend/dist/index.html'

    if exists('../dist/index.html'):  # frozen py2app
        return '../dist/index.html'

    if exists('./ui/index.html'):
        return './ui/index.html'

    raise Exception('No index.html found')

entry = get_entrypoint()

if __name__ == '__main__':
    api = API()
    # webview.create_window('Wuxmail', entry, width=800, height=600, resizable=True, debug=True)
    window = webview.create_window('SpeedyMP v0.1.0a', entry, js_api=api, min_size=(1200, 850), resizable=True)
    webview.start(debug=True, gui='gtk')