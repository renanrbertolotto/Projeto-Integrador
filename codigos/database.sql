create table PIprodutos(
    idProduto int primary key,
    nome varchar2(255),
    descricao varchar2(255),
    custoProduto decimal (10,2),
    custofixo decimal(2,2),
    comissao decimal (2,2),
    imposto decimal (2,2),
    margemLucro decimal (2,2)
);