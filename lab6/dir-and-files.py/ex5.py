# Файлға мәлімет жазатын функция
def writesome(list_of_elements):
    # 'sometext.txt' файлын ашу ('+a' - append режимінде)
    with open("sometext.txt", 'a') as f:  
        text = "\n"  # Жаңа жолдан бастау үшін ('\n')
        
        # Тізімдегі әр элементті жолға қосу
        for i in list_of_elements:
            text += str(i) + ' '  # Әр элементті жолға бос орынмен бірге қосу
        
        f.write(text)  # Файлға жазу
       

# Функцияны тестілеу
writesome([12345, 56789, 90987654, "dfghjkl", "efrgf", 34, 34])
