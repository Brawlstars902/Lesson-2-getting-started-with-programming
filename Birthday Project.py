Mom=input('When was was your mother born? \n')
Dad=input('When was your father born? \n')
# Yes bro
if input('Do you have a brother? please answer yes or no. \n')== 'Yes':
 Bro=input('when was he born? \n')
    #yes bro yes sis
if input('Do you have a sister? please answer yes or no. \n')== 'Yes':
       print('Okay.')
sister=input('When was she born? \n')
print('Your mother was born on',Mom,', your father was born on', Dad, ', your brother was born on', Bro,'and your sister was born on',sister,'.\n')
if input('Do you have a sister? please answer yes or no. \n')== 'No' :
   print('Your mother was born on',Mom,', your father was born on', Dad, 'and your brother was born on', Bro,'.\n')

    # No bro
if input('Do you have a brother? please answer yes or no. \n')== 'No':
 print('okay.')
    #No bro yes sis
if input('Do you have a sister? please answer yes or no. \n')== 'Yes':
    sister=input('When was she born? \n')
print('Your mother was born on',Mom,', your father was born on', Dad, 'and your sister was born on', sister,'.')
if input('Do you have a sister? please answer yes or no. \n')== 'No' :
   print('Your mother was born on',Mom,', your father was born on', Dad,'.\n')
