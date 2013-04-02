# encoding: utf-8

import web
import datetime

urls = ('/', 'Index')
render = web.template.render('templates/')

CATEGORIES = [
    (u'食', u'食'),
    (u'', u'その他'),
]

entry_form = web.form.Form(
    web.form.Dropdown(
        name='month',
        args=range(1,13),
        value=datetime.date.today().month),
    web.form.Dropdown(
        name='day',
        args=range(1,31),
        value=datetime.date.today().day),
    web.form.Dropdown(
        name='category',
        args=CATEGORIES
    )
)

class Index:
  def GET(self):
    print "GET!!!"
    return render.index(entry_form)

if __name__=='__main__':
    print "run"
    app = web.application(urls, globals())
    app.run()


