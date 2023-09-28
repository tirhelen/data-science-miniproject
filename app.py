from cancelled_times_query import Cancelled_times_query

cancelled_times_query_object = Cancelled_times_query()
while(True):
    print('What do you want to do?')
    print('(w) Write data to file')
    print('(p) Print data')
    response = input()
    if (response == 'w'):
        cancelled_times_query_object.write()
    if (response == 'p'):
        cancelled_times_query_object.print()