$(document).ready(function () {
    // database bar
    $.ajax({
        type: "GET",
        url: "/compounds",
        data: {disease: $("#selectedDisease").val()},
        contentType: 'application/json',
        dataType: "json",
        success: function (data) {
            var source = data.data;
            var dbChart = echarts.init($('#chart1'))
            var options = {
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'shadow'
                    }
                },
                legend: {
                    data: ['The number of compounds']
                },
                xAxis: {
                    name: 'Database',
                    type: 'category',
                    data: ['chEMBL', 'BindingDB', 'DrugBank', 'GtopDB', 'DGiDB']
                },
                yAxis: {
                    name: 'The number of compounds',
                    type: 'value'
                },
                series: [{
                    type: 'bar',
                    data: [{
                        value: source[0],
                        itemStyle: {
                            color: "#EE0606"
                        }
                    },{
                        value: source[1],
                        itemStyle: {
                            color: "#EE4806"
                        }
                    },{
                        value: source[2],
                        itemStyle: {
                            color: "#F5D707"
                        }
                    },{
                        value: source[3],
                        itemStyle: {
                            color: "#6AF507"
                        }
                    },{
                        value: source[4],
                        itemStyle: {
                            color: "#0D83DE"
                        }
                    }]
                }]
            }
            dbChart.setOption(options)
        }
    })

})