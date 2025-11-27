import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter


def conectar():
    return sqlite3.connect('clientes.db')


def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS clientes(
              
              nome TEXT,
              email TEXT,
              telefone TEXT,
              endereco TEXT
    ) ''')
    conn.commit()
    conn.close()


def inserir_cliente():
    nome = nome_entry.get()
    email = email_entry.get()
    telefone = telefone_entry.get()
    endereco = endereco_entry.get()

    if  nome and email and telefone and endereco:
        conn = conectar()
        c = conn.cursor()
        try:
            c.execute("INSERT INTO clientes VALUES (?,?,?,?)",
                      ( nome, email, telefone, endereco))
            conn.commit()
            conn.close()
            messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO!')
            mostrar_cliente()
            limpar()
        except sqlite3.IntegrityError:
            messagebox.showerror('', 'CPF JÁ CADASTRADO!')
    else:
        messagebox.showwarning('', 'INSIRA TODOS OS DADOS')


def mostrar_cliente():
    for row in tree.get_children():
        tree.delete(row)
        
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM clientes')
    clientes = c.fetchall()
    for cli in clientes:
        tree.insert("", "end", values=(cli[0], cli[1], cli[2], cli[3], cli[4]))
    conn.close()


def atualizar():
    selecao = tree.selection()
    if selecao:
        dado_edit = tree.item(selecao)['values'][0]
        novo_nome = nome_entry.get()
        novo_email = email_entry.get()
        novo_telefone = telefone_entry.get()
        novo_endereco = endereco_entry.get()

        if dado_edit and novo_nome and novo_email and novo_telefone and novo_endereco:
            conn = conectar()
            c = conn.cursor()
            c.execute("""UPDATE clientes 
                         SET cpf=?, nome=?, email=?, telefone=?, endereco=?
                         WHERE cpf=?""",
                      (dado_edit, novo_nome, novo_email, novo_telefone, novo_endereco))
            conn.commit()
            conn.close()
            messagebox.showinfo('', 'DADOS ATUALIZADOS COM SUCESSO!')
            mostrar_cliente()
            limpar()
        else:
            messagebox.showwarning('', 'PREENCHA TODOS OS CAMPOS')
    else:
        messagebox.showerror('', 'SELECIONE UM CLIENTE')


def delete_cliente():
    selecao = tree.selection()
    if selecao:
        user_del = tree.item(selecao)['values'][0]
        conn =  conectar()
        c = conn.cursor()     
        c.execute("DELETE FROM usuarios WHERE cpf = ?", (user_del,))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADO DELETADO COM SUCESSO')
        mostrar_cliente()
    else:
        messagebox.showerror('', 'ERRO AO DELETAR O DADO') 

def limpar():
    nome_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)
    endereco_entry.delete(0, tk.END)


def carregar_dados(event):
    selecao = tree.selection()
    if selecao:
        dados = tree.item(selecao)['values']
        limpar()
        nome_entry.insert(0, dados[1])
        email_entry.insert(0, dados[2])
        telefone_entry.insert(0, dados[3])
        endereco_entry.insert(0, dados[4])


janela =  customtkinter.CTk()
janela.configure(fg_color='pink')
janela.title('CADASTRO DE CLIENTES')
janela.geometry('800x640')

tk.Label(janela, text='CADASTRO ', font=('arial', 15)).grid(row=0, column=0, pady=10, padx=10)

fr0 =  customtkinter.CTkFrame(janela )
fr0.grid(columnspan=3)



tk.Label(fr0, text='Nome', font=('arial', 15)).grid(row=2, column=0, pady=10, padx=10)
nome_entry = tk.Entry(fr0, font=('arial', 15))
nome_entry.grid(row=2, column=1, pady=10, padx=10)

tk.Label(fr0, text='E-mail', font=('arial', 15)).grid(row=3, column=0, pady=10, padx=10)
email_entry = tk.Entry(fr0, font=('arial', 15))
email_entry.grid(row=3, column=1, pady=10, padx=10)

tk.Label(fr0, text='Telefone', font=('arial', 15)).grid(row=4, column=0, pady=10, padx=10)
telefone_entry = tk.Entry(fr0, font=('arial', 15))
telefone_entry.grid(row=4, column=1, pady=10, padx=10)

tk.Label(fr0, text='Endereço', font=('arial', 15)).grid(row=5, column=0, pady=10, padx=10)
endereco_entry = tk.Entry(fr0, font=('arial', 15))
endereco_entry.grid(row=5, column=1, pady=10, padx=10)

fr =  customtkinter.CTkFrame(janela)
fr.grid(columnspan=3)

btn_salvar =  customtkinter.CTkButton(fr, text= 'SALVAR', font=('arial', 15), command=inserir_cliente, fg_color='black')
btn_salvar.grid(row=6, column=0, padx=10, pady=10)

btn_atualizar =  customtkinter.CTkButton(fr, text= 'ATUALIZAR', font=('arial', 15), command=atualizar, fg_color='black')
btn_atualizar.grid(row=6, column=1, padx=10, pady=10)

btn_delete =  customtkinter.CTkButton(fr, text= 'DELETAR', font=('arial', 15), command= delete_cliente, fg_color='black')
btn_delete.grid(row=6, column=2, padx=10, pady=10)

btn_limpar =  customtkinter.CTkButton(fr, text= 'LIMPAR', font=('arial', 15), command=limpar, fg_color='black')
btn_limpar.grid(row=6, column=3, padx=10, pady=10)

fr2 = customtkinter.CTkFrame(janela)
fr2.grid(columnspan=3)

colunas = ('NOME', 'E-MAIL', 'TELEFONE', 'ENDEREÇO')
tree =  ttk.Treeview(fr2, columns=colunas, show='headings', height=20)
tree.grid(row=7, column=0, padx=10, sticky='nsew')

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, anchor= tk.CENTER)

tree.bind("<ButtonRelease-1>", carregar_dados)


criar_tabela()
mostrar_cliente()
janela.mainloop()