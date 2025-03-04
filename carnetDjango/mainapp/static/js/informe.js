document.addEventListener("DOMContentLoaded", function () {
    let dataElement = document.getElementById("graficoData");

    if (dataElement) {
        let rawData = document.getElementById("graficoData").textContent;
        

        try {
            let data = JSON.parse(rawData);
            console.log("Datos parseados correctamente:", data);

            let total = Object.values(data).reduce((a, b) => a + b, 0);
            let porcentajes = Object.values(data).map(value => ((value / total) * 100).toFixed(2));
            let etiquetas = Object.keys(data).map((label, index) => `${label} (${porcentajes[index]}%)`);

            let ctx = document.getElementById('graficoTorta').getContext('2d');
            new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: etiquetas,
                    datasets: [{
                        data: Object.values(data),
                        backgroundColor: ['#002b46', '#39A900'],
                    }]
                }
            });

        } catch (error) {
            console.error("⚠ Error al parsear JSON:", error);
        }
    }

    document.getElementById("downloadExcel").addEventListener("click", function() {
        window.location.href = "/descargar-excel/";
    });
});
