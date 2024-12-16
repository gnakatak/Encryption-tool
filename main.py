import tkinter as tk
from tkinter import messagebox
from encrypter import encrypter, numbers, imprime_cifra, zerar as zerar_encrypter
from decrypter import decrypter, number, imprime_cifra, zerar as zerar_decrypter

def main():
    def centralizar_janela():
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()

        largura_janela = 500
        altura_janela = 350

        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2

        janela.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

    def mostrar_menu_principal():
        limpar_janela()

        # Título
        tk.Label(janela, text="Bem-vindo ao Programa de Cifra e Decifra!", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Adicionando os botões no grid, com as opções de 'sticky' para centralizar
        tk.Button(janela, text="Cifrar", command=mostrar_menu_cifrar, width=20).grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        tk.Button(janela, text="Decifrar", command=mostrar_menu_decifrar, width=20).grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        tk.Button(janela, text="Explicação da Cifra", command=mostrar_explicacao, width=20).grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        tk.Button(janela, text="Sair", command=janela.quit, width=20).grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Expansão automática para os botões
        janela.grid_rowconfigure(1, weight=1)
        janela.grid_rowconfigure(2, weight=1)
        janela.grid_columnconfigure(0, weight=1)
        janela.grid_columnconfigure(1, weight=1)

    def mostrar_explicacao():
        limpar_janela()

        try:
            # Abrindo o arquivo .md com codificação UTF-8
            with open("explicacao.md", "r", encoding="utf-8") as file:
                explicacao = file.read()
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo de explicação não encontrado!")
            return
        except UnicodeDecodeError:
            messagebox.showerror("Erro", "Erro ao ler o arquivo. Certifique-se de que ele esteja codificado em UTF-8.")
            return

        tk.Label(janela, text="Explicação da Cifra", font=("Arial", 16)).pack(pady=10)

        # Usando o widget Text para exibir o conteúdo do arquivo
        campo_explicacao = tk.Text(janela, height=15, width=60)
        campo_explicacao.insert(tk.END, explicacao)
        campo_explicacao.config(state=tk.DISABLED)  # Desabilita a edição do texto
        campo_explicacao.pack(pady=10)

        frame_botoes = tk.Frame(janela)
        frame_botoes.pack(pady=5)

        tk.Button(frame_botoes, text="Voltar", command=mostrar_menu_principal, width=20).pack(side="left", padx=5)

    def mostrar_menu_cifrar():
        limpar_janela()

        def realizar_cifra():
            texto = entrada.get()
            if escolha_cifra.get() == '1':
                resposta = encrypter(texto, 1)
            elif escolha_cifra.get() == '2':
                resposta = encrypter(texto, 2)
            else:
                messagebox.showerror("Erro", "Selecione um tipo de cifra!")
                return
            zerar_encrypter()
            mostrar_resultado(texto,''.join(resposta))

        tk.Label(janela, text="Escolha o tipo de cifra:").pack()

        escolha_cifra = tk.StringVar()
        escolha_cifra.set('1')  # Define a opção padrão
        tk.Radiobutton(janela, text="Simples", variable=escolha_cifra, value='1').pack(anchor="w")
        tk.Radiobutton(janela, text="Complexa", variable=escolha_cifra, value='2').pack(anchor="w")

        tk.Label(janela, text="Digite o texto:").pack()
        entrada = tk.Entry(janela, width=40)
        entrada.pack()

        frame_botoes = tk.Frame(janela)
        frame_botoes.pack(pady=5)

        tk.Button(frame_botoes, text="Cifrar", command=realizar_cifra, width=20).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Voltar", command=mostrar_menu_principal, width=20).pack(side="left", padx=5)

    def mostrar_menu_decifrar():
        limpar_janela()

        def realizar_decifra():
            texto = entrada.get()
            if escolha_decifra.get() == '1':
                resposta = decrypter(texto, 1)
            elif escolha_decifra.get() == '2':
                resposta = decrypter(texto, 2)
            else:
                messagebox.showerror("Erro", "Selecione um tipo de decifra!")
                return
            zerar_decrypter()
            mostrar_resultado(texto,''.join(resposta))

        tk.Label(janela, text="Escolha o tipo de decifra:").pack()

        escolha_decifra = tk.StringVar()
        escolha_decifra.set('1')  # Define a opção padrão
        tk.Radiobutton(janela, text="Simples", variable=escolha_decifra, value='1').pack(anchor="w")
        tk.Radiobutton(janela, text="Complexa", variable=escolha_decifra, value='2').pack(anchor="w")

        tk.Label(janela, text="Digite o texto:").pack()
        entrada = tk.Entry(janela, width=40)
        entrada.pack()

        frame_botoes = tk.Frame(janela)
        frame_botoes.pack(pady=5)

        tk.Button(frame_botoes, text="Decifrar", command=realizar_decifra, width=20).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Voltar", command=mostrar_menu_principal, width=20).pack(side="left", padx=5)

    def mostrar_resultado(original, resultado):
        limpar_janela()

        tk.Label(janela, text=original, font=("Arial", 14)).pack(pady=10)

        campo_resultado = tk.Text(janela, height=4, width=50)
        campo_resultado.insert(tk.END, resultado)
        campo_resultado.config(state=tk.DISABLED)
        campo_resultado.pack(pady=10)

        frame_botoes = tk.Frame(janela)
        frame_botoes.pack(pady=5)

        tk.Button(frame_botoes, text="Voltar ao Início", command=mostrar_menu_principal, width=20).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Copiar para Área de Transferência", command=lambda: copiar_texto(campo_resultado), width=20).pack(side="left", padx=5)

    def copiar_texto(campo):
        janela.clipboard_clear()
        janela.clipboard_append(campo.get("1.0", tk.END))
        messagebox.showinfo("Sucesso", "Texto copiado para a área de transferência!")

    def limpar_janela():
        for widget in janela.winfo_children():
            widget.destroy()

    janela = tk.Tk()
    janela.title("Programa de Cifra e Decifra")

    centralizar_janela()

    mostrar_menu_principal()

    janela.mainloop()

if __name__ == "__main__":
    main()