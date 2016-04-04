from selenium import webdriver
import threading
import tutorial

def before_all(ctx):

    ctx.server = tutorial
    ctx.address = tutorial.address
    ctx.thread = threading.Thread(target=ctx.server.serve_forever)
    ctx.thread.start()
    ctx.browser = webdriver.Firefox()

def after_all(ctx):
    ctx.browser.get("{0}/shutdown".format(ctx.address))
    ctx.thread.join()
    ctx.browser.quit()
