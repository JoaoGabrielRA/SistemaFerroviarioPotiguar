from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db import connection

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cadastrado(request):
    return render(request,'cadastrado.html')

def login(request):
    erroMsg = ''
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        with connection.cursor() as cursor:
            # Primeira consulta para obter 'valor', 'cpf' e 'idviagem'
            cursor.execute("SELECT nome FROM app_ferrovia_usuarios WHERE cpf=%s AND senha=%s", [cpf,senha])
            response = cursor.fetchone()        

            if response:
                nome = response[0]
                return render(request,'validacao.html',{"nome":nome})
        erroMsg = "Usuário não encontrado!"
    return render(request, 'login.html', {"erroMsg": erroMsg})

def validacao(request):
    erroMsg = ''
    if request.method == 'POST':
        
        # Obtenha os dados do formulário
        bilhete = request.POST.get('nBilhete')
 
        with connection.cursor() as cursor:
            # Primeira consulta para obter 'valor', 'cpf' e 'idviagem'
            cursor.execute("SELECT cpf_passageiro_id, id_viagem_id FROM app_ferrovia_passagems WHERE id=%s", [bilhete])
            response = cursor.fetchone()
        if response:
            # Descompacte os resultados da primeira consulta
            cpf_passageiro_id, id_viagem_id = response
            dados = {
                'idPassagem': bilhete,
                'cpf': cpf_passageiro_id,
                'idviagem': id_viagem_id,
            }

            with connection.cursor() as cursor:
                # Segunda consulta para obter 'nome' do usuário
                cursor.execute("SELECT nome FROM app_ferrovia_usuarios WHERE cpf=%s", [dados['cpf']])
                response2 = cursor.fetchone()

            # Verifique se há um resultado na segunda consulta
            if response2:
                nome = response2[0]

            # with connection.cursor() as cursor:
            #     # Segunda consulta para obter 'nome' do usuário
            #     cursor.execute("""SELECT
            #         u.nome,
            #         FROM
            #         app_ferrovia_usuarios u
            #         JOIN
            #         app_ferrovia_viagem v ON u.cpf = v.usuario_id
            #         WHERE
            #         u.cpf = %s
            #         AND v.id = %s""", [dados['cpf'], dados['idviagem']])
            # testeJoin = cursor.fetchone()

            # Verifique se há um resultado na segunda consulta
            if response2:
                nome = response2[0]
                
            with connection.cursor() as cursor:
                # Segunda consulta para obter 'nome' do usuário
                cursor.execute("SELECT data, origem, destino FROM app_ferrovia_viagem WHERE id=%s", [dados['idviagem']])
                response3 = cursor.fetchone()

            # Verifique se há um resultado na segunda consulta
            if response3:
                data, origem, destino = response3
                dadosViagem = {
                    'dataViagem': data,
                    'origem': origem,
                    'destino': destino,
                }

            return render(request, 'validacao.html', {"dados": dados, "nomeUsuario": nome,"dadosViagem": dadosViagem})
        else:
            erroMsg = "Bilhete não encontrado!"
    return render(request, 'validacao.html',{"erroMsg": erroMsg})


def validaBlilhete(request):
    context = {}
    return render(request, 'validacao.html', context)

# def cadastroUsuario(request):
#     #if(resquest.method == 'POST'):
#     context = {}
#     return render(request, 'cadastro.html', context)

def cadastroUsuario(request):
    if request.method == 'POST':
        # Obtenha os dados do formulário
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')


        # Execute a inserção no banco de dados usando SQL puro
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO app_ferrovia_usuarios (cpf, nome, email, senha) VALUES (%s, %s, %s, %s)",
                           [cpf, nome, email, senha])


        # Redirecione para a página de sucesso ou faça algo mais
        return redirect('cadastrado')

    # Se o método não for POST, renderize o formulário
    return render(request, 'cadastro.html')