livros = [
    {
        'Título': 'Harry Potter e a Pedra Filosofal',
        'Autor': 'J.K. Rowling',
        'Ano Publicação': 1997,
        'Gênero': 'Fantasia',
        'Preço': 29.99
    },
    {
        'Título': '1984',
        'Autor': 'George Orwell',
        'Ano Publicação': 1949,
        'Gênero': 'Ficção',
        'Preço': 19.99
    },
    {
        'Título': 'O Senhor dos Anéis',
        'Autor': 'J.R.R. Tolkien',
        'Ano Publicação': 1954,
        'Gênero': 'Fantasia',
        'Preço': 24.99
    },
    {
        'Título': 'Orgulho e Preconceito',
        'Autor': 'Jane Austen',
        'Ano Publicação': 1813,
        'Gênero': 'Romance',
        'Preço': 14.99
    },
    {
        'Título': 'Dom Quixote',
        'Autor': 'Miguel de Cervantes',
        'Ano Publicação': 1605,
        'Gênero': 'Clássico',
        'Preço': 12.99
    },
    {
        'Título': 'O Pequeno Príncipe',
        'Autor': 'Antoine de Saint-Exupéry',
        'Ano Publicação': 1943,
        'Gênero': 'Infantil',
        'Preço': 9.99
    },
    {
        'Título': 'A Revolução dos Bichos',
        'Autor': 'George Orwell',
        'Ano Publicação': 1945,
        'Gênero': 'Ficção',
        'Preço': 17.99
    },
    {
        'Título': 'Cem Anos de Solidão',
        'Autor': 'Gabriel García Márquez',
        'Ano Publicação': 1967,
        'Gênero': 'Realismo',
        'Preço': 21.99
    },
    {
        'Título': 'Percy Jackson e o Ladrão de Raios',
        'Autor': 'Rick Riordan',
        'Ano Publicação': 2005,
        'Gênero': 'Fantasia',
        'Preço': 16.99
    },
    {
        'Título': 'A Culpa é das Estrelas',
        'Autor': 'John Green',
        'Ano Publicação': 2012,
        'Gênero': 'Romance',
        'Preço': 18.99
    },
    {
        'Título': 'O Alquimista',
        'Autor': 'Paulo Coelho',
        'Ano Publicação': 1988,
        'Gênero': 'Autoajuda',
        'Preço': 15.99
    },
    {
        'Título': 'O Código Da Vinci',
        'Autor': 'Dan Brown',
        'Ano Publicação': 2003,
        'Gênero': 'Suspense',
        'Preço': 22.99
    },
    {
        'Título': 'As Crônicas de Nárnia',
        'Autor': 'C.S. Lewis',
        'Ano Publicação': 1950,
        'Gênero': 'Fantasia',
        'Preço': 20.99
    }
]

# Nome do arquivo
nome_arquivo = 'livros.txt'

# Abrir o arquivo em modo de escrita
with open(nome_arquivo, 'w') as arquivo:
    # Escrever as informações dos livros no arquivo
    for livro in livros:
        linha = f"{livro['Título']} | {livro['Autor']} | {livro['Ano Publicação']} | {livro['Gênero']} | {livro['Preço']}\n"
        arquivo.write(linha)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
