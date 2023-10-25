import PySimpleGUI as sg
from route_query import is_valid_route
from data_assembler import Data_assembler

class Gui:
  
  def __init__(self, assembler: Data_assembler):
    layout = [  [sg.Text('Enter a route\'s short name (e.g.\"520\" to calculate predictions)')],
                [sg.Text('', key='notification')],
                [sg.InputText()],
                [sg.Button('Calculate')] ]
    self.window = sg.Window('TimelyTransit', layout)
    self.assembler = assembler
  
  def start_GUI(self):
    while True:
      event, values = self.window.read()
      input = values[0]
      if event == sg.WIN_CLOSED:
        break
      if (is_valid_route(input)):
        self.window['notification'].update('Generating graph for route ' + input)
        self.assembler.construct_graph(route = input)
      else:
        self.window['notification'].update(input + ' is not a valid route')
      