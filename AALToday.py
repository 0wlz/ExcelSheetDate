import os, openpyxl, datetime, time

os.chdir('C:\\Users\\taket\\OneDrive\\Documents\\Python projects') # Opens the directory that contains the workbook

wb = openpyxl.load_workbook('AAL Records.xlsx') # Loads the workbook

today = (datetime.datetime.now().strftime("%d.%m.%y")) # Creates variable with today's date

wb.create_sheet(index=0, title=today) #Creates a sheet at the first position and titles it with today's date

sheet = wb[today]#Assigns the variable sheet with today's workbook

sheet['A2'] = 'ARB1' #Assigns the cells with premade IDs for tanks
sheet['A3'] = 'ARB2'
sheet['A4'] = 'TL1'
sheet['A5'] = 'TL2'
sheet['A6'] = 'TL3'
sheet['A7'] = 'TL4'
sheet['A8'] = 'TL5'
sheet['A9'] = 'ML1'
sheet['A10'] = 'ML2'
sheet['A11'] = 'ML3'
sheet['A12'] = 'ML4'
sheet['A13'] = 'BL1'
sheet['A14'] = 'BL2'
sheet['A15'] = 'BL3'
sheet['A16'] = 'ARB3'
sheet['A17'] = 'RA1'
sheet['A18'] = 'RA2'
sheet['A19'] = 'RA3'
sheet['A20'] = 'RA4'
sheet['A21'] = 'RA5'
sheet['A22'] = 'BE1'
sheet['A23'] = 'TE1'
sheet['A24'] = 'ME1'
sheet['A25'] = 'BE2'
sheet['A26'] = 'TR1'
sheet['A27'] = 'TR2'
sheet['A28'] = 'TR3'
sheet['A29'] = 'TR4'
sheet['A30'] = 'TR5'
sheet['A31'] = 'TR6'
sheet['A32'] = 'MR1'
sheet['A33'] = 'MR2'
sheet['A34'] = 'BR1'
sheet['A35'] = 'BR2'



sheet['B1'] = 'Species'  #Assigns cells for titles
sheet['C1'] = 'Basking Temp'
sheet['D1'] = 'Ambient Temp'
sheet['E1'] = 'UVI Reading'

wb.save('AAL Records.xlsx')

