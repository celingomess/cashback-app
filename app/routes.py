from flask import Blueprint, render_template, request, redirect
from .database import conectar
from .service import calcular_cashback

main = Blueprint("main", __name__)

@main.route("/")
def index():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM compras ORDER BY id DESC")
    compras = cursor.fetchall()

    return render_template("index.html", compras=compras)


@main.route("/calcular", methods=["POST"])
def calcular():

    nome = request.form["nome"]
    valor = float(request.form["valor"])

    cashback = calcular_cashback(valor)

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO compras (nome, valor_compra, cashback)
    VALUES (%s,%s,%s)
    """

    cursor.execute(sql, (nome, valor, cashback))
    conexao.commit()

    return redirect("/")