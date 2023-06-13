import PySimpleGUI as sg
import BMI

# set the black theme
sg.theme('DarkPurple4')

# define the layout
layout = [
    [sg.Text('BMI Calculator', font=('Helvetica', 20,'bold'), size=(30, 1), justification='center')], 
    # [sg.Column([[sg.Text('BMI Calculator', font=('Helvetica', 20,'bold'), justification='center')]], element_justification='c')],
    [sg.Text('Chiều cao (cm) :', font=('Helvetica', 10)), sg.InputText(key='height')],
    [sg.Text('Cân nặng  (kg)  :', font=('Helvetica', 10)), sg.InputText(key='weight')],
    [sg.Button('Tính BMI', size=(11,1), button_color=('white','#730080'), font=('Helvetica', 11), pad=((8,0),(5,10)), border_width=2, focus=True), 
     sg.Button('Thoát', size=(6,1), button_color=('white','#730080'), font=('Helvetica', 11), pad=((0,8),(5,10)), border_width=2, focus=True)],
    [sg.Text('Chỉ số BMI : ', font=('Helvetica', 10)), sg.Text('0', font=('Helvetica', 10), size=(5,1), key='BMI',text_color='red')],
    [sg.Text('Tình trạng   : ', font=('Helvetica', 10)), sg.Text('', font=('Helvetica', 10), key='category', text_color='red')],
   [sg.Column([[sg.Text('@phamhaithanh', font=('Helvetica', 8))]], element_justification='right', pad=((400, 0), 0))]
   ]

# create the window
window = sg.Window('BMI Calculator', layout)

# main event loop
while True:
    event, values = window.read()

    # exit the program if the user closes the window
    if event == sg.WIN_CLOSED or event == 'Thoát':
        break

    # calculate the BMI and show the results
    try:
        if event == 'Tính BMI':
            height = float(values['height'])
            weight = float(values['weight'])
            bmi = BMI.bodymassindex(height, weight)
            window['BMI'].update(str(bmi))
            if bmi < 18.5:
                window['category'].update('Bạn đang thiếu cân')
            elif 18.5 <= bmi <= 24.9:
                window['category'].update('Cân nặng của bạn bình thường')
            elif 25.0 <= bmi <= 29.9:
                window['category'].update('Bạn đang thừa cân')
            elif bmi >= 30.0:
                window['category'].update('Bạn đang bị béo phì')
    except ValueError:
        sg.popup("Vui lòng nhập chỉ số của bạn!",font=("Helvetica",10))

# close the window
window.close()