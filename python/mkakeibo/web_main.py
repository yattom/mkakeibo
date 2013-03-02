import web

urls = ('/', 'Index')

class Index:
  def GET(self):
    print "GET!!!"
    return "<html><head><title>mkakeibo</title></head><body><h1>Hi</h1></body></html>"

if __name__=='__main__':
    print "run"
    app = web.application(urls, globals())
    app.run()


