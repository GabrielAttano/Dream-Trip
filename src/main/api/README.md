# DreamTripAPI

API responsável por fazer o scrapping do preço das passagens e autenticação do usuário.

# Rotas

## Get

/user/{user_id} - Rota para receber os dados do usuário. Recebe o user_id do usuário.

/packages/destinations - Rota para receber as destinações válidas.

/packages/{package_id} - Rota para receber os dados de um pacote. Recebe o package_id do pacote.

## Post

/user/create - Rota para criação de usuário. Recebe um body com email, username e password desejado.

/packages/create - Rota para criação de um pacote. Recebe um body com start_date (Data no formato ISO de qual deverá ser o primeiro dia das viagens), stay_time, destinations (Lista com as siglas dos destinos), start_destination e o user_id de quem criou o pacote.