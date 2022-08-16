"""
Descrição rápida e simples.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi finibus sodales faucibus. Phasellus finibus nisi non
venenatis ultrices. Aenean ipsum libero, commodo sed libero nec, luctus vehicula mauris. Nulla convallis condimentum
dolor vel ullamcorper. Praesent iaculis, ex sit amet gravida cursus, ligula felis lobortis odio, ac sagittis purus nibh
it amet quam. Curabitur sodales congue libero vitae tempor. Curabitur nec pulvinar odio, eu scelerisque erat.

Suspendisse potenti. Quisque mattis accumsan nunc sed pellentesque. Aenean nec facilisis purus. Praesent sit amet
sagittis quam. Cras sollicitudin cursus feugiat. Praesent ultricies augue ac accumsan scelerisque. Nullam vitae ornare
mauris. Aliquam erat volutpat. Nulla diam nunc, feugiat nec scelerisque consequat, ullamcorper et odio. Vestibulum in
odio semper, rutrum arcu at, faucibus nisl. Praesent ornare pharetra ligula ut rutrum. In et condimentum ante, et
commodo augue. Ut placerat non lectus pellentesque faucibus. Morbi auctor, leo nec ornare pulvinar, velit turpis
iaculis nisl, id ultrices enim eros a ligula. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per
inceptos himenaeos.

"""

class MinhaClasse:
    """Documentação normal
    Conforme qualquer outra documentação que você tenha usado anteriormente
    """
    atributo = 1
    atributo2 = 'Valor'

    def __init__(self, texto):
        """Inicializa os dados

        :param texto: o texto da classe
        :type texto: str
        """
        self.texto = texto
        self.exibe_texto(texto)

    @staticmethod
    def exibe_texto(texto):
        """Método que exibe um texto de até 100 caracteres na tela

        :param texto: Um texto de 100 até caracteres
        :type texto: str

        :return: O texto de até 100 caracteres
        :rtype: str

        :raises ValueError: Se o texto tiver mais que 100 caracteres
        :raises TypeError: Se o texto não for uma string
        """

        if not isinstance(texto, str):
            raise TypeError('O texto precisa ser uma string.')

        if len(texto) > 100:
            raise ValueError('O texto precisa ter até caracteres')

        return texto

