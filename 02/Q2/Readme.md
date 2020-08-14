
**Questão 2**) Fazer um sistema de upload de arquivos via UDP. Um servidor UDP deverá receber as partes dos arquivos
(1024 bytes), verificar ao final a integridade via um checksum (MD5) e armazenar o arquivo em uma pasta padrão.
Sugestões: o servidor pode receber o nome e tamanho do arquivo como o primeiro pacote e o checksum como o último.
Testar o servidor com arquivos textos e binários (ex: imagens, pdf) de tamanhos arbitrários (ex: 100 bytes, 4KiB,
4MiB). O protocolo para a comunicação deve ser criado e especificado textualmente ou graficamente.

Opcionais:
- a) gerar log no servidor com o horário de início e término da transferência, nome do arquivo, tamanho do arquivo,
origem do arquivo.
- b) fazer interface gráfica no cliente para selecionar localmente o arquivo.
- c) fazer barra de estado para mostrar o percentual transferido e o restante.
- d) suportar transferências simultâneas.

---

Necessário python 3.8.X

Necessário criar o diretório ```$HOME/server``` para o server.

Execução:
```bash
$ ./main.py [-h] [--port PORT] {server,client} [host]
```
- host padrão: localhost
- porta padrão: 5000
  
---
 ### Protocolo

*Cabeçalho:*
- 1 byte: Tamanho do nome do arquivo
- 1 a 255 bytes: Nome do arquivo
- 4 bytes: Tamanho do arquivo em bytes

*Envio do arquivo:*
> Repete-se até terminar o envio do arquivo
- 1 byte: número do pedaço (*chunk*)
- 1 a 1024 bytes: pedaço (*chunk*) do arquivo
  
*MD5*
- 1 byte: Tamanho do MD5
- 1 a 255 bytes: MD5