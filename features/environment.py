from selenium import webdriver

def before_all(ctx):
    ctx.browser = webdriver.Firefox()

def after_all(ctx):
    ctx.browser.quit()
