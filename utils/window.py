def window():
    import tkinter as tk

    def cadastrar_produto():
        # Alterar o texto informacional
        texto = 'Produto cadastrado com sucesso!'
        texto_informacional['text'] = texto.upper()

        # Limpar os campos de texto
        campo_codigo.delete(0, tk.END)
        campo_marca.delete(0, tk.END)
        campo_tipo.delete(0, tk.END)
        campo_categoria.delete(0, tk.END)
        campo_preco_unit.delete(0, tk.END)
        campo_custo.delete(0, tk.END)
        campo_obs.delete(0, tk.END)

    # Criar a Janela
    janela = tk.Tk()
    # Alterar o Título da Janela
    janela.title('Cadastro de Produtos')

    # Campo de código do Produto
    tk.Label(janela, text='Código:').grid(row=0,
                                          column=0,
                                          sticky='w',
                                          padx=(10, 0))
    campo_codigo = tk.Entry(janela, width=30)
    campo_codigo.grid(row=0, column=1, padx=10, pady=10)

    # Campo de Marca do Produto
    tk.Label(janela, text='Marca:').grid(row=1,
                                         column=0,
                                         sticky='w',
                                         padx=(10, 0))
    campo_marca = tk.Entry(janela, width=30)
    campo_marca.grid(row=1, column=1, padx=10, pady=10)

    # Campo de Tipo do Produto
    tk.Label(janela, text='Tipo:').grid(row=2,
                                        column=0,
                                        sticky='w',
                                        padx=(10, 0))
    campo_tipo = tk.Entry(janela, width=30)
    campo_tipo.grid(row=2, column=1, padx=10, pady=10)

    # Campo de Categoria do Produto
    tk.Label(janela, text='Categoria:').grid(row=3,
                                             column=0,
                                             sticky='w',
                                             padx=(10, 0))
    campo_categoria = tk.Entry(janela, width=30)
    campo_categoria.grid(row=3, column=1, padx=10, pady=10)

    # Campo de Preço Unitário do Produto
    tk.Label(janela, text='Preço Unitário:').grid(row=4,
                                                  column=0,
                                                  sticky='w',
                                                  padx=(10, 0))
    campo_preco_unit = tk.Entry(janela, width=30)
    campo_preco_unit.grid(row=4, column=1, padx=10, pady=10)

    # Campo de Custo do Produto
    tk.Label(janela, text='Custo:').grid(row=5,
                                         column=0,
                                         sticky='w',
                                         padx=(10, 0))
    campo_custo = tk.Entry(janela, width=30)
    campo_custo.grid(row=5, column=1, padx=10, pady=10)

    # Campo de Observação do Produto (Opcional)
    tk.Label(janela, text='Observação:').grid(row=6,
                                              column=0,
                                              sticky='w',
                                              padx=(10, 0))
    campo_obs = tk.Entry(janela, width=30)
    campo_obs.grid(row=6, column=1, padx=10, pady=10)

    # Botão de cadastrar o Produto
    tk.Button(janela,
              text='Cadastrar Produto',
              command=cadastrar_produto,
              bg='#103778',
              fg='white').grid(row=7,
                               columnspan=2,
                               pady=10)

    # Texto para confirmar que o Produto foi cadastrado com sucesso
    texto_informacional = tk.Label(janela, text='')
    texto_informacional.grid(row=8, columnspan=2, pady=15)

    janela.mainloop()
