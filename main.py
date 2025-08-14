import webview

def set_scale(window):
    window.evaluate_js("document.body.style.zoom='60%'")
    window.resize(600, 900)

window = webview.create_window('EasyShare', 'https://easyshare--markizoo.on.websim.com/')
webview.start(set_scale, window, gui='qt')
