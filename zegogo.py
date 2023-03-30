import PySimpleGUI as sg
import sqlite3

con = sqlite3.connect('dados.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS cadastro(email,login,senha)')

identifi = None

def janela_login():
    sg.theme('DarkGrey9')
    layout_esquerda=[
        [sg.Image(filename='imagens/img2.png')]
    ]
    layout_direita = [
        [sg.Text('Login:', pad=(90,0))],
        [sg.InputText('',size=(30,0), key='loginp')],
        [sg.Text('Senha:', pad=(90,0))],
        [sg.InputText('',size=(30,0), password_char='*',key='senhap')],
        [sg.Button('Entrar',image_filename='imagens/circulo_azul.png',button_color=('#36383e') ,border_width=0, mouseover_colors='#36383e', pad=(45,0))],
        [sg.Button('Esqueci a senha',button_color=('black', '#36383e'),border_width=0,mouseover_colors="#36383e", pad=(60,0))],
        [sg.Button('Cadastra-se',button_color=('black', '#36383e'),border_width=0,mouseover_colors="#36383e" ,pad=(74,0))],
    ] 
    
    layout = [
        [sg.Column(layout_esquerda), sg.VSeparator(pad=((10,10),(10,10))), sg.Column(layout_direita)]
    ]
    return sg.Window('Login', layout, finalize=True)

def painel_admin():
    sg.theme('Reddit')
    layout=[
        [sg.Button('Voltar')],
        [sg.Text('EMAIL:')],
        [sg.Input(key='emailadmin')],
        [sg.Text('LOGIN:')],
        [sg.Input(key='loginadmin')],
        [sg.Text('SENHA:')],
        [sg.Input(key='senhaadmin')],
        [sg.Button('Inserir'), sg.Button('Editar'), sg.Button('Atualizar'), sg.Button('Excluir')],
        [sg.Table(values=dados, headings=['Email', 'Login', 'Senha'], key= 'tabela', size=(300,220), col_widths=[30, 30, 30], auto_size_columns=False, justification='c')],
        
    ]
    
    return sg.Window('Painel Admin', layout,size=(800,600),finalize=True)


def janela_cadastro():
    sg.theme('DarkGrey9')
    layout=[
        [sg.Button('Voltar',button_color=('#63748c'), font=('Calibri', 10, 'bold'))],
        [sg.Text('E-mail:', pad=(110,5))],
        [sg.InputText('', pad=(25,0), key='emailcadastro')],
        [sg.Text('Seu login:', pad=(105,0))],
        [sg.InputText('',size=(20,0), pad=(65,0), key='logincadastro')],
        [sg.Text('Sua senha:',pad=(105,0))],
        [sg.InputText('',password_char='*',size=(20,0), pad=(65,0), key='senhacadastro')],
        [sg.Button('Enviar',pad=(70,5), image_filename='circulo_azul.png',button_color=('#36383e') ,border_width=0, mouseover_colors='#36383e')],
        [sg.Button('Cancelar',button_color=('#36383e'), pad=(105,0))],
    ]
    return sg.Window('Tela de Cadastro', layout,size=(300,250),finalize=True)

def janela_esquecisenha():
    sg.theme('DarkGrey9')
    
    layout = [
        [sg.Button('Voltar',button_color=('#63748c'), font=('Calibri', 10, 'bold'))],
        [sg.Text('Informe seu email:',pad=(130,0))],[sg.InputText('',size=(80,0),pad=(0,8), key='emailrecuperacao')],
        [sg.Button('Enviar', pad=(0,0), font=('Calibri', 12, 'bold')), sg.Button('Cancelar', pad=(10,0),font=('Calibri', 12, 'bold'))],
    ]
    return sg.Window('Recuperação de conta', layout, size=(400,150), finalize=True)

def editar_janela():
    sg.theme('DarkGrey9')

    layout = [
        [sg.Button('Voltar', button_color= ('#63748c'), font=('Calibri', 10, 'bold'))],
        [sg.Text('EMAIL:')],
        [sg.Input(key='emaileditar')],
        [sg.Text('LOGIN:')],
        [sg.Input(key='logineditar')],
        [sg.Text('SENHA:')],
        [sg.Input(key='senhaeditar')],
        [sg.Button('Salvar', key=('-salvar_editado-'))]
        
    ]
    return sg.Window('Editar', layout, size=(400,250), finalize=True)

def atualizar_cadastro():
    cur.execute("SELECT email,login,senha FROM cadastro")
    dados_cadastro = cur.fetchall()
    janela4['tabela'].update(values=dados_cadastro)

def get_cadastro():
    cur.execute('SELECT email, login, senha FROM cadastro')
    return list(cur.fetchall())

"""
def operacao_banco(operacao, dados_):
    if operacao == 'salvar':
        pass
    if operacao == 'deltar':
        pass
    if operacao == 'edit':
        pass

dados_ = ['email','login', 'senha']
operacao = 'salvar'
operacao_banco('salvar', dados_)
"""


janela1, janela2, janela3, janela4, janela5 = janela_login(),None,None,None,None
dados_cadastro = {}
data = get_cadastro()
while True:
    window,event,values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED or event == 'Cancelar':
        break

    if window == janela2 and event == sg.WIN_CLOSED or event == 'Cancelar':
        break

    if window == janela3 and event == sg.WIN_CLOSED or event == 'Cancelar':
        break

    if window == janela4 and event == sg.WIN_CLOSED or event == 'Cancelar':
        break

    if window == janela5 and event == sg.WIN_CLOSED or event == 'Cancelar':
        janela5.hide

    if window == janela1 and event == 'Entrar':
        user = values['loginp']
        password = values['senhap']
        cur.execute('SELECT * FROM cadastro WHERE login = ? AND senha = ?', (user,password))
        resultado = cur.fetchone()
        cur.execute("SELECT email,login, senha FROM cadastro")
        dados = cur.fetchall()
        if user == 'admin' and password == 'adminti':
            sg.popup(f'Bem vindo ao Zé Gogo, {values["loginp"]}!')
            janela4 = painel_admin()
            janela1.hide()
            #break
        elif resultado:
            sg.popup(f'Bem vindo ao Zé Gogo, {user}!')
            #break
        else:
            sg.popup('Login ou senha incorretos')


    if window == janela1 and event == 'Cadastra-se':
        janela2 = janela_cadastro()
        janela1.hide()
    
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    
    if window == janela2 and event == 'Enviar':
        email = values['emailcadastro']
        login = values['logincadastro']
        senha = values['senhacadastro']
        cur.execute('SELECT * FROM cadastro WHERE email = ? OR login = ?', (email,login))
        resultado = cur.fetchone()
        if resultado:
            sg.popup('E-mail ou login já cadastrados.')
        else:
            cur.execute('INSERT INTO cadastro VALUES(?,?,?)', (email,login,senha))
            con.commit()
            sg.popup(f'Verique seu e-mail e confirme sua conta: {values["emailcadastro"]}')
            cur.execute('SELECT * FROM cadastro')
            data = cur.fetchall()
            dados_cadastro['login'] = login
            dados_cadastro['senha'] = senha
            janela2.close()
            janela1.un_hide()
    
    if window == janela1 and event == 'Esqueci a senha':
        janela1.hide()
        janela3 = janela_esquecisenha()
    
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()
    
    if window == janela3 and event == 'Enviar':
        cur.execute('SELECT * FROM cadastro WHERE email = ?', (values['emailrecuperacao'],))
        resultado = cur.fetchone()
        if resultado:
            sg.popup('E-mail encontrado! Verifique sua caixa de entrada.')
        else:
            sg.popup('E-mail não encontrado.') 

    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela1.un_hide()
    
    if window == janela5 and event == 'Voltar':
        janela5.hide()
    
    if window == janela4 and event == 'Inserir':
        emailp = values['emailadmin']
        loginp = values['loginadmin']
        senhap = values['senhaadmin']
        cur.execute('SELECT * FROM cadastro WHERE email = ? OR login = ?', (emailp,loginp))
        resultado = cur.fetchone()
        if resultado:
            sg.popup('E-mail ou login já cadastrados.')
        else:
            cur.execute ("INSERT INTO cadastro (email,login,senha) VALUES (?,?,?)", (emailp,loginp,senhap))
            confirm = sg.popup_yes_no('Deseja inserir esse registro?')
            if confirm == 'Yes':
                sg.popup('Inserido com sucesso!')
                cur.execute('SELECT * FROM cadastro')
                data = cur.fetchall()
                con.commit()
                atualizar_cadastro()
                window.Element('emailadmin').update('')
                window.Element('loginadmin').update('')
                window.Element('senhaadmin').update('')

    if window == janela4 and event == 'Atualizar':
        atualizar_cadastro()

    elif window == janela4 and event == 'Excluir':
        # Recupera os índices dos registros selecionados na tabela
        indexes = window['tabela'].SelectedRows
        if len(indexes) == 0:
            sg.popup('Selecione um registro para excluir.')
        else:
            # Pede confirmação do usuário
            confirm = sg.popup_yes_no('Tem certeza que deseja excluir o(s) registro(s) selecionado(s)?')
            if confirm == 'Yes':
                # Exclui os registros selecionados
                for index in indexes:
                    if index in indexes:
                        emaildelete = data[index][0]
                        cur.execute('DELETE FROM cadastro WHERE email = ?', (emaildelete,))
                        con.commit()
                        cur.execute('SELECT * FROM cadastro')
                        data = cur.fetchall()
                    sg.popup('Registro(s) excluído(s) com sucesso!')
                    atualizar_cadastro()

    if window == janela4 and event == 'Editar':
        indexes = window['tabela'].SelectedRows
        if len(indexes) == 0:
            sg.popup('Selecione um registro para alterar!')
        else:
            janela5 = editar_janela()
            data = window['tabela'].get()[indexes[0]]
            identifi = data[1]
            janela5['emaileditar'].update(data[0])
            janela5['logineditar'].update(data[1])
            janela5['senhaeditar'].update(data[2])
    
    if window == janela5 and event == '-salvar_editado-':
        emaile = values['emaileditar']
        logine = values['logineditar']
        senhae = values['senhaeditar']
        cur.execute(f"UPDATE cadastro SET email='{emaile}', login='{logine}', senha='{senhae}' WHERE login='{identifi}'")
        con.commit()
        sg.popup('Dados editados com sucesso!')
        janela5.close()
        atualizar_cadastro()
    
             
    
                



        

