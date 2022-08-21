class valida_horario_saudacao:
    def valida_horario_e_saudacao():
        horario = input('Digite um horário (0-23): ')

        if horario.isdigit():#valida se é um num ou se é uma str
            horario = int(horario) #cascate convertendo str em inteiro 

            if horario < 0 or horario > 23:# validando se o num esta entre 0 e 23hrs
                print("Horário deve estar entre 0 e 23")
            else:
                if horario <= 11:
                    print('Boa dia!')
                elif horario <= 17:
                    print('Boa tarde!')
                else:
                    print('Boa noite!')
        else:
            print("Por favor, digite um horário entre 0 e 23.")# caso seja um str pede ao usuario para digitar novamente