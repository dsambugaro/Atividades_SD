**Questão 1**) Faça um servidor para processar as seguintes mensagens dos clientes. O servidor deve suportar mensagens
de múltiplos clientes. Use o TCP. As mensagens de solicitação estão no formato String UTF:
* TIME: Retorna a hora do sistema como uma String UTF no formato HH:MM:SS
* DATE: Retorna a data do sistema como uma String UTF no formato DD/MM/AAAA
* FILES: Retorna os arquivos da pasta definida por padrao (p. ex. /home/user/shared)
> Formato: retorna um inteiro indicando o número de arquivos (int) e envia individualmente o nome de um arquivo como uma String UTF.
* DOWN nome-arquivo: Faz o download do arquivo nome-arquivo
> Formato: retorna um inteiro 0 se nome não existe ou retorna o tamanho do arquivo (int) em bytes. Recebe byte a byte e grava em um diretório padrão
* EXIT: Finaliza a conexão

---

Necessário python 3.8.X

Necessário criar o diretório ```$HOME/server``` para o server e o diretório ```$HOME/client``` para o cliente.

Execução:
```bash
$ ./main.py [-h] [--port PORT] {server,client} [host]
```
- host padrão: localhost
- porta padrão: 5000