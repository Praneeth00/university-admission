function predictAdmission() {
    let gre = parseFloat(document.getElementById("gre").value);
    let toefl = parseFloat(document.getElementById("toefl").value);
    let university = parseFloat(document.getElementById("university").value);
    let sop = parseFloat(document.getElementById("sop").value);
    let lor = parseFloat(document.getElementById("lor").value);
    let cgpa = parseFloat(document.getElementById("cgpa").value);
    let research = parseInt(document.getElementById("research").value);

    if (isNaN(gre) || isNaN(toefl) || isNaN(university) || isNaN(sop) || isNaN(lor) || isNaN(cgpa)) {
        alert("Please fill in all fields correctly.");
        return;
    }

    let prediction = (0.3 * (gre / 340) + 0.2 * (toefl / 120) + 0.1 * (university / 5) +
                      0.1 * (sop / 5) + 0.1 * (lor / 5) + 0.2 * (cgpa / 10) + 0.05 * research) * 100;

    document.getElementById("result").innerText = `Prediction Result: ${prediction.toFixed(2)}% chance of admission`;
}
