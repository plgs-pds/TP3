# Documentação TP3

Abra o terminal (ou prompt de comando) e execute:
git clone github.com/ usuario / nome-do-repositorio .git

Navegue até o diretório do projeto:
cd nome-do-repositorio

Instale as Dependências:
Com o ambiente virtual ativado, instale as dependências necessárias:
pip install -r requirements.txt

Verifique o Suporte ao datetime:
Se você encontrar problemas com o reconhecimento do módulo datetime, certifique-se de que ele esteja sendo importado corretamente no seu script:
from datetime import datetime
Não é necessário instalar o datetime manualmente, pois ele faz parte da biblioteca padrão do Python.

## Executando o Servidor Flask

No terminal, estando no diretório do projeto, execute:
python server.py
- Isso iniciará o servidor Flask localmente, geralmente em http://127.0.0.1:5000/.

## Executando o Cliente

Em outro terminal ou prompt de comando, execute o cliente.
python client.py
O cliente irá se comunicar com o servidor através das requisições HTTP.

## Solução de Problemas
Problema: Módulo datetime não reconhecido.
Solução: Verifique se o Python 3.x está instalado corretamente e se o código de importação (from datetime import datetime) está correto.

Problema: Flask não instalado.
Solução: Execute pip install Flask para instalar o Flask manualmente.

## Considerações Finais
O Flask foi escolhido por sua simplicidade e flexibilidade, que o tornam ideal para prototipagem rápida e projetos de pequeno a médio porte. Comparado a frameworks maiores como Django, Flask permite mais controle sobre as decisões de arquitetura do projeto.

Desafios Enfrentados:
Gerenciamento de Dependências: Foi necessário garantir que todas as dependências fossem instaladas corretamente, o que pode ser difícil em diferentes ambientes de desenvolvimento.
Suporte a IPv6: A implementação do suporte a IPv6 foi um dos desafios, exigindo configuração adicional para garantir que o servidor e o cliente pudessem se comunicar corretamente.
