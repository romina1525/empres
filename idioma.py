class Idioma:
    def __init__(self, name, origem, bandera):
        self._name = name
        self._origem = origem
        self._bandera = bandera
    def __str__(self):
        return f'{self._name} | {self._bandera} | {self._origem}'
    
 
idioma_espanhol = Idioma('espanhol', '🇪🇸', '''🏴󠁧󠁢󠁷󠁬󠁳󠁿''')
idioma_portugues = Idioma('Portugues', '🇧🇷', '''🏴󠁧󠁢󠁷󠁬󠁳󠁿''')
idioma_ingles = Idioma('ingles', '🇺🇸', '''🏴󠁧󠁢󠁷󠁬󠁳󠁿''')
idioma_frances = Idioma('frances', '🇫🇷', '''🏴󠁧󠁢󠁷󠁬󠁳󠁿''')
idioma_aleman = Idioma('aleman', '🇩🇪', '''🏴󠁧󠁢󠁷󠁬󠁳󠁿''')

idiomas =[idioma_espanhol, idioma_portugues, idioma_ingles, idioma_frances, idioma_aleman]
 
print(idioma_espanhol)
print(idioma_portugues)
print(idioma_ingles)
print(idioma_frances)
print(idioma_aleman)


 
 
 
 