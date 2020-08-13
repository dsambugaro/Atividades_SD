
**Questão 2**) Faça uma aplicação com um servidor que gerencia um conjunto de arquivos remotos entre múltiplos usuários. O servidor deve responder aos seguintes comandos:
- ADDFILE (1): adiciona um arquivo novo.
- DELETE (2): remove um arquivo existente.
- GETFILESLIST (3): retorna uma lista com o nome dos arquivos.
- GETFILE (4): faz download de um arquivo.

> O servidor deve registrar as ações em logs.

As solicitações possuem o seguinte cabeçalho em comum:
- 1 byte: requisição (1) – Message Type (0x01)
- 1 byte: código do comando – Command Identifier (0x01 a 0x04)
- 1 byte: tamanho do nome do arquivo – Filename Size
- variável [0-255]: nome do arquivo em bytes – Filename

As respostas possuem o seguinte cabeçalho em comum:
- 1 byte: resposta (2) – Message Type (0x02)
- 1 byte: código do comando – Command Identifier (0x01 a 0x04)
- 1 byte: status code (1-SUCCESS, 2-ERROR) – Status Code


para o **ADDFILE**, adicionam-se os campos na solicitação:
4 bytes: tamanho do arquivo (big endian order) em bytes.
variável[1 a 232]: bytes do arquivo.


para o **GETFILESLIST**, adicionam-se os campos na resposta:
2 bytes: número de arquivos (big endian order)
Repete-se até terminar os nomes:
1 byte: tamanho do nome (1-255)
variável [1 a 255]: nome do arquivo


para o **GETFILE**. adicionam-se os campos na resposta:
4 bytes: tamanho do arquivo (big endian order) em bytes
variável [1 a 232]: bytes do arquivo.
* Ao fazer download do arquivo, grave em uma pasta padrão.
* Para enviar e receber arquivo façam envio e recebimento byte a byte

---

Necessário python 3.8.X

Necessário criar o diretório ```$HOME/server``` para o server e o diretório ```$HOME/client``` para o cliente.

Execução:
```bash
$ ./main.py [-h] [--port PORT] {server,client} [host]
```
- host padrão: localhost
- porta padrão: 5000