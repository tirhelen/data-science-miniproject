from cancelled_times_query import Cancelled_times_query
from data_assembler import Data_assembler
import sys
import PySimpleGUI as sg
from route_query import is_valid_route

cancelled_times_query_object = Cancelled_times_query()
layout = [  [sg.Text('Enter a route\'s short name (e.g.\"520\" to see predictions)')],
            [sg.InputText()],
            [sg.Button('Do the thing')] ]
window = sg.Window('TimelyTransit', layout)
data_assembler_object = Data_assembler()

while True:
    print('\n What do you want to do?')
    print('(s) Start the application')
    print('(w) Write data to file')
    print('(p) Print data')
    print('(c) Compile all data to a .csv file')
    print('(e) Exit')
    response = input()
    
    if response == 's':
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            print(is_valid_route(values[0]))
            print('Entered value was', values[0])
    elif response == 'w':
        cancelled_times_query_object.write()
    elif response == 'p':
        cancelled_times_query_object.print()
    elif response == 'c':
        data_assembler_object.write_to_csv()
    elif response == 'e':
        sys.exit(0)
    else:
        print('Unidentified command')
