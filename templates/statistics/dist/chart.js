// function initBarChart() {
//     var a = document.getElementById("barChart");
//     new Chart(a, {
//         type: "bar",
//         data: {
//             labels: ["January", "February", "March", "April", "May", "June", "July"],
//             datasets: [{
//                 label: "Electronics",
//                 backgroundColor: "#f56954",
//                 data: [65, 59, 80, 81, 56, 55, 40]
//             }, {
//                 label: "Fashion",
//                 backgroundColor: "#00a65a",
//                 data: [28, 48, 40, 19, 86, 27, 90]
//             }, {
//                 label: "Foods",
//                 backgroundColor: "#00c0ef",
//                 data: [70, 60, 65, 50, 60, 70, 80]
//             }]
//         },
//         options: {
//             scaleBeginAtZero: !0,
//             scaleShowGridLines: !0,
//             scaleGridLineColor: "rgba(0,0,0,.05)",
//             scaleGridLineWidth: 1,
//             scaleShowHorizontalLines: !0,
//             scaleShowVerticalLines: !0,
//             barShowStroke: !0,
//             barStrokeWidth: 2,
//             barValueSpacing: 5,
//             barDatasetSpacing: 1,
//             responsive: !0,
//             maintainAspectRatio: !0,
//             legend: {
//                 display: !0,
//                 position: "right",
//                 labels: {
//                     boxWidth: 15,
//                     defaultFontColor: "#343a40",
//                     defaultFontSize: 11
//                 }
//             }
//         }
//     })
// }
// $(document).ready(function() {
//     initBarChart()
// });