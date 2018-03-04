import web

urls = (
    '/(.*)', 'recipe'
)
app = web.application(urls, globals())

db = web.database(dbn='sqlite', db='recipes.db')
templates = web.template.render('templates')

class recipe:
    def GET(self, name):
        vars = {'url':name}

        recipe = db.select('recipes', where="url = $url", vars=vars).first()

        if recipe:
            return templates.recipe(recipe)
        else:
            return web.notfound()

if __name__ == "__main__":
    app.run()
