from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Mentestech - Plataforma de Cursos'

@main.route('/pix')
def pix():
    return 'Página de teste PIX'

@main.route('/mercadopago')
def mercado_pago():
    return 'Página de teste MercadoPago'

@main.route('/paypal')
def paypal():
    return 'Página de teste PayPal'
