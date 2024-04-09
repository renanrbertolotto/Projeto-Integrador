create table produtos(
    idProduto int primary key,
    nome varchar2(255),
    descricao varchar2(255),
    custoProduto decimal (10,2),
    custofixo decimal(10,2),
    comissao decimal (10,2),
    imposto decimal (10,2),
    margemLucro decimal (10,2)
);