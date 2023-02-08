

import tkinter as tk
import sqlite3

# Criação da janela principal
root = tk.Tk()
root.title("Estoque de Produtos")
root.geometry("400x300")

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# Criação da tabela de produtos, se ela ainda não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        codigo TEXT NOT NULL,
        nome TEXT NOT NULL,
        descricao TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        valor REAL NOT NULL
);
""")
conn.commit()

# Função para inserir um produto no banco de dados
def inserir_produto():
    codigo = codigo_entry.get()
    nome = nome_entry.get()
    descricao = descricao_entry.get()
    quantidade = quantidade_entry.get()
    valor = valor_entry.get()

    cursor.execute("""
    INSERT INTO produtos (codigo, nome, descricao, quantidade, valor)
    VALUES (?,?,?,?,?)
    """, (codigo, nome, descricao, quantidade, valor))
    conn.commit()

    codigo_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    descricao_entry.delete(0, tk.END)
    quantidade_entry.delete(0, tk.END)
    valor_entry.delete(0, tk.END)

    listar_produtos()

# Função para atualizar um produto no banco de dados
def atualizar_produto():
    id = id_entry.get()
    codigo = codigo_entry.get()
    nome = nome_entry.get()
    descricao = descricao_entry.get()
    quantidade = quantidade_entry.get()
    valor = valor_entry.get()

    cursor.execute("""
    UPDATE produtos
    SET codigo = ?, nome = ?, descricao = ?, quantidade = ?, valor = ?
    WHERE id = ?
    """, (codigo, nome, descricao, quantidade, valor, id))
    conn.commit()

    id_entry.delete(0, tk.END)
    codigo_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    descricao_entry.delete(0, tk.END)
    quantidade_entry.delete(0, tk.END)
    valor_entry.delete(0, tk.END)
    listar_produtos()

#Função para deletar um produto no banco de dados
def deletar_produto():
    id = id_entry.get()
    cursor.execute("""
        DELETE FROM produtos WHERE id = ?
        """, (id,))
    conn.commit()

    id_entry.delete(0, tk.END)

    listar_produtos()

#Função para listar os produtos na tela
def listar_produtos():
    listbox.delete(0, tk.END)
    cursor.execute("""
    SELECT * FROM produtos;
    """)
    produtos = cursor.fetchall()
    for produto in produtos:
        listbox.insert(tk.END, produto)

#Label e Entry para inserir o código do produto
codigo_label = tk.Label(root, text="Código:")
codigo_label.pack()
codigo_entry = tk.Entry(root)
codigo_entry.pack()

#Label e Entry para inserir o nome do produto
nome_label = tk.Label(root, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

#Label e Entry para inserir a descrição do produto
descricao_label = tk.Label(root, text="Descrição:")
descricao_label.pack()
descricao_entry = tk.Entry(root)
descricao_entry.pack()

#Label e Entry para inserir a quantidade do produto
quantidade_label = tk.Label(root, text="Quantidade:")
quantidade_label.pack()
quantidade_entry = tk.Entry(root)
quantidade_entry.pack()

#Label e Entry para inserir o valor do produto
valor_label = tk.Label(root, text="Valor:")
valor_label.pack()
valor_entry = tk.Entry(root)
valor_entry.pack()

#Label e Entry para inserir o ID do produto a ser atualizado ou deletado
id_label = tk.Label(root, text="ID:")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

#Botão para inserir um produto
inserir_button = tk.Button(root, text="Inserir", command=inserir_produto)
inserir_button.pack()

#Botão para atualizar um produto
atualizar_button = tk.Button(root, text="Atualizar", command=atualizar_produto)
atualizar_button.pack()

#Botão para deletar um produto
deletar_button = tk.Button(root, text="Deletar", command=deletar_produto)
deletar_button.pack()

#Listbox para exibir os produtos cadastrados
listbox = tk.Listbox(root)
listbox.pack()

#Inicializa a lista de produtos na tela
listar_produtos()

root.mainloop()
