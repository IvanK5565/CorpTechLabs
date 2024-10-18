from controller import Controller
from appJar import gui

controller = Controller()
app = gui('Converter', '400x200')
app.addLabelEntry('value')
app.addLabel('result')

def set(result: str):
    app.setLabel('result', result)

def press(button):
    if button == 'Convert':
        value = app.getEntry('value')
        from_format = app.getOptionBox('from')
        to_format = app.getOptionBox('to')
        controller.input(value, from_format, to_format, set)


listbox = app.addOptionBox('from',controller.get_currencies())
listbox = app.addOptionBox('to',controller.get_currencies())


app.addButton('Convert',press)

app.go()