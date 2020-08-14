**Questão 1**) Fazer um chat P2P que possibite os clientes trocarem mensagens entre si. As mensagens possuem o formato:
- tamanho apelido (tam_apl) [1 byte]- apelido [tam_apl bytes]
- tamanho mensagem (tam_msg) [1 byte]
- mensagem [tam_msg bytes]

Opcionais:
- a) fazer um servidor TCP para acessar e incluir o apelido e endereço da lista de pessoas ativas na conversação.
- b) ao fechar a conexão com o servidor TCP, deve-se remover o apelido e endereço da lista.
- c) a cada  2s  os  clientes  podem  verificar  se há  modificações  na lista  do servidor  ou, o servidor pode  enviar  umanotificação de atualização sempre que ocorrer uma mudança de estado.
- d) fazer um mecanismo de emotions usando ícones .

---

Necessário python 3.8.X

Execução:
```bash
$ ./main.py [-h] port nickname peer_ip peer_port
```
- port           Your UDP port
- nickname       Your nickname on chat
- peer_ip        Peer IP
- peer_port      Peer UDP port

> -h for help