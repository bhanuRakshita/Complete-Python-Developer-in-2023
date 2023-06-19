# with: No need to close

with open('08_File\sample.txt', mode='r+') as  my_file:
    my_file.seek(0,2)
    my_file.write('\nndukewi')
