import pycob as pc
import pandas as pd

app = pc.App('Test App')

def test_page(server_request: pc.Request) -> pc.Page:
    name = server_request.get_query_parameter('name')
    page = pc.Page('Test Page')
    page.add_header('Test Header', "2")
    page.add_text('Test Text')
    page.add_alert('Test Alert')
    page.add_hero('Hello ' + name, 'Test Subtitle', 'https://source.unsplash.com/random/800x600')
    
    form = pc.FormComponent(action="/")
    form.add_formtext('Name', 'name', 'Enter your name')
    form.add_formsubmit('Submit')

    page.add_component(form)

    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }

    df = pd.DataFrame(data)

    page.add_pandas_table(df)

    return page

app.add_page('/', test_page)

app.run()
