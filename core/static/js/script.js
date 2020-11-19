        // Line
        var ctx = document.getElementById("myChart").getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ["Rubi", "Diamante", "Esmeralda", "Turquesa", "Coral", "Safira", "Jade"],
                datasets: [{
                    label: '# Ocorrências',
                    data: [12, 19, 3, 5, 2, 3, 1],
                    backgroundColor: [
                        'rgba(168, 3, 79, 0.2)',
                        'rgba(163, 158, 140, 0.2)',
                        'rgba(0, 170, 158, 0.2)',
                        'rgba(0, 130, 155, 0.2)',
                        'rgba(245, 95, 26, 0.2)',
                        'rgba(28, 20, 107, 0.2)',
                        'rgba(0, 176, 82, 0.2)'
                    ],
                    borderColor: [
                        '#a8034f',
                        '#a39e8c',
                        '#00aa9e',
                        '#00829b',
                        '#f55f1a',
                        '#1c146b',
                        '#00b052'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });


        //line
        var ctxL = document.getElementById("lineChart").getContext('2d');
        var myLineChart = new Chart(ctxL, {
            type: 'line',
            data: {
                labels: ["January", "February", "March", "April", "May", "June", "July"],
                datasets: [{
                        label: "Rubi",
                        backgroundColor: [
                            'rgba(168, 3, 79, 0.2)',
                        ],
                        borderColor: [
                            'rgba(168, 3, 79, 0.7)',
                        ],
                        borderWidth: 2,
                        data: [65, 59, 80, 81, 56, 55, 40]
                    },
                    {
                        label: "Turquesa",
                        backgroundColor: [
                            'rgba(0, 130, 155, 0.2)',
                        ],
                        borderColor: [
                            'rgba(0, 130, 155, 0.7)',
                        ],
                        data: [28, 48, 40, 19, 86, 27, 90]
                    },
                    {
                        label: "Safira",
                        backgroundColor: [
                            'rgba(28, 20, 107, 0.2)',
                        ],
                        borderColor: [
                            'rgba(28, 20, 107, 0.7)',
                        ],
                        data: [30, 31, 28, 34, 40, 52, 60]
                    },
                ]
            },
            options: {
                responsive: true
            }
        });


        //radar
        var ctxR = document.getElementById("radarChart").getContext('2d');
        var myRadarChart = new Chart(ctxR, {
            type: 'radar',
            data: {
                labels: ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"],
                datasets: [{
                    label: "My First dataset",
                    data: [65, 59, 90, 81, 56, 55, 40],
                    backgroundColor: [
                        'rgba(105, 0, 132, .2)',
                    ],
                    borderColor: [
                        'rgba(200, 99, 132, .7)',
                    ],
                    borderWidth: 2
                }, {
                    label: "My Second dataset",
                    data: [28, 48, 40, 19, 96, 27, 100],
                    backgroundColor: [
                        'rgba(0, 250, 220, .2)',
                    ],
                    borderColor: [
                        'rgba(0, 213, 132, .7)',
                    ],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true
            }
        });

        //doughnut
        var ctxD = document.getElementById("doughnutChart").getContext('2d');
        var myLineChart = new Chart(ctxD, {
            type: 'doughnut',
            data: {
                labels: ["Progressive Transferse Cracking", "Lateral Wear", "Abnormal Vertical Wear", "Corrosion", "Isolated Wheel Burn"],
                datasets: [{
                    data: [19, 12, 5, 3, 3],
                    backgroundColor: ['rgba(163, 158, 140, 0.3)', 'rgba(168, 3, 79, 0.2)', 'rgba(0, 130, 155, 0.2)', 'rgba(0, 170, 158, 0.2)', 'rgba(28, 20, 107, 0.2)','#1c146b','rgba(28, 20, 107, 0.2)'],
                    hoverBackgroundColor: ["#a39e8c", "#a8034f", "#00829b", "#00aa9e", "#1c146b"]
                }]
            },
            options: {
                responsive: true
            }
        });
 new WOW().init();


        // Initialize maps
        google.maps.event.addDomListener(window, 'load', regular_map);

        new Chart(document.getElementById("horizontalBar"), {
            "type": "horizontalBar",
            "data": {
                "labels": ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Grey"],
                "datasets": [{
                    "label": "My First Dataset",
                    "data": [22, 33, 55, 12, 86, 23, 14],
                    "fill": false,
                    "backgroundColor": ["rgba(255, 99, 132, 0.2)", "rgba(255, 159, 64, 0.2)",
                        "rgba(255, 205, 86, 0.2)", "rgba(75, 192, 192, 0.2)",
                        "rgba(54, 162, 235, 0.2)",
                        "rgba(153, 102, 255, 0.2)", "rgba(201, 203, 207, 0.2)"
                    ],
                    "borderColor": ["rgb(255, 99, 132)", "rgb(255, 159, 64)", "rgb(255, 205, 86)",
                        "rgb(75, 192, 192)", "rgb(54, 162, 235)", "rgb(153, 102, 255)",
                        "rgb(201, 203, 207)"
                    ],
                    "borderWidth": 1
                }]
            },
            "options": {
                "scales": {
                    "xAxes": [{
                        "ticks": {
                            "beginAtZero": true
                        }
                    }]
                }
            }
        });