function predictAdmission() {
    let data = {
        gre: parseFloat(document.getElementById("gre").value),
        toefl: parseFloat(document.getElementById("toefl").value),
        university: parseFloat(document.getElementById("university").value),
        sop: parseFloat(document.getElementById("sop").value),
        lor: parseFloat(document.getElementById("lor").value),
        cgpa: parseFloat(document.getElementById("cgpa").value),
        research: parseInt(document.getElementById("research").value)
    };

    fetch("https://university-admission-frontend.onrender.com", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("result").innerText = `Prediction Result: ${result.admission_chance}%`;
    })
    .catch(error => console.error("Error:", error));
}
