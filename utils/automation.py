# Importação das Bibliotecas
import pandas as pd
import pyautogui

# Encontra a janela de Cadastro de Produtos
cadastro_de_produtos = pyautogui.getWindowsWithTitle('Cadastro de Produtos')[0]

# Se a janela estiver minimizada, será maximizada
if cadastro_de_produtos.isMinimized:
    cadastro_de_produtos.restore()

# Foca na janela de Cadastro de Produtos
cadastro_de_produtos.activate()

# Importação da base de dados
tabela = pd.read_csv('produtos.csv')

# Informando um tempo de pausa para cada comando da automação
pyautogui.PAUSE = 0.4

# Laço para preenchimento dos campos
for linha in tabela.index:
    # Campo de inserção de Código do Produto
    pyautogui.press('tab')
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)

    # Campo de inserção de Marca do Produto
    pyautogui.press('tab')
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)

    # Campo de inserção de Tipo do Produto
    pyautogui.press('tab')
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)

    # Campo de inserção de Categoria do Produto
    pyautogui.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)

    # Campo de inserção de Preço Unitário do Produto
    pyautogui.press('tab')
    preco_unit = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unit)

    pyautogui.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)

    # Campo de inserção de Observação do Produto (Opcional)
    pyautogui.press('tab')
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(obs)

    # Apertar no botão de Cadastrar Produto
    pyautogui.press('tab')
    pyautogui.press('space')
