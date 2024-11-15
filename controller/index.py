from flask import Flask, Blueprint, render_template, request
from models.dados import itens
import math

index = Blueprint('index', __name__)

@index.route('/')
def home():
    tamanho_pagina = 10
    total_paginas = math.ceil(len(itens) / tamanho_pagina)
    pagina = request.args.get('pagina', 1, type=int)

    inicio = (pagina - 1) * tamanho_pagina
    fim = inicio + tamanho_pagina
    itens_ = itens[inicio:fim]


    return render_template('index.html', itens=itens_, total_paginas=total_paginas, pagina=pagina)
