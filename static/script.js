async function calcular() {
    const valor = document.getElementById("valor").value;
    const desconto = document.getElementById("desconto").value;
    const vip = document.getElementById("vip").checked;

    const response = await fetch("/calcular", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            valor: valor,
            desconto: desconto,
            vip: vip
        })
    });

    const data = await response.json();

    document.getElementById("resultado").innerText =
        "Cashback: R$ " + data.cashback;
}