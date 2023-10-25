from cancelled_times_query import Cancelled_times_query
from data_assembler import Data_assembler
from gui import Gui
import sys




data_assembler_object = Data_assembler()
gui_object = Gui(assembler = data_assembler_object)
cancelled_times_query_object = Cancelled_times_query()

while True:
    print('\n What do you want to do?')
    print('(s) Start the application')
    print('(w) Write data to file')
    print('(p) Print data')
    print('(c) Compile all data to a .csv file')
    print('(e) Exit')
    response = input()
    
    if response == 's':
        gui_object.start_GUI()
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
