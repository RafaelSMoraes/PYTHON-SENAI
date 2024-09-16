#Escreva um programa que peça ao usuário uma senha
# e verifique se ela está correta (a senha correta é "python123").

senha = input('Digite a senha: ').strip()

if senha == 'python123':
    print('Senha correta')
else:
    print('Senha Incorreta')