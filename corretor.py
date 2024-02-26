import requests

class CorretorOrtografico:
    def __init__(self):
        self.api_base_url = "https://languagetool.org/api/v2"

    def corrigir(self, texto):
        url = f"{self.api_base_url}/check"
        payload = {"text": texto, "language": "pt-BR"}
        response = requests.post(url, data=payload)

        if response.status_code == 200:
            correcoes = response.json().get("matches", [])
            texto_corrigido = texto

            for correcao in reversed(correcoes):
                if "replacements" in correcao:
                    sugestao = correcao["replacements"][0]["value"] # pegar a mais aproximada (mas pode ser configurada para exibir a lista inteira)
                    texto_corrigido = (
                        texto_corrigido[:correcao["offset"]]
                        + sugestao
                        + texto_corrigido[correcao["offset"] + correcao["length"]:]
                    )

            return texto_corrigido

        else:
            return texto

# Exemplo de uso
corretor = CorretorOrtografico()

texto_digitado = input("Digite um texto: ")
corrigido = corretor.corrigir(texto_digitado)

print(f"Texto corrigido: {corrigido}")
