$(document).ready(function () {
    // database bar
    // $('#my-card-widget').CardWidget('toggle')
    var dbChart = echarts.init(document.getElementById("chart1"), null, {renderer: 'svg'})

    function getCompounds() {
        $.ajax({
            type: "GET",
            url: "/data/compounds",
            data: {disease: $("#selectedDisease").val()},
            contentType: 'application/json',
            dataType: "json",
            success: function (data) {
                var source = data.data;

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
                        }, {
                            value: source[1],
                            itemStyle: {
                                color: "#EE4806"
                            }
                        }, {
                            value: source[2],
                            itemStyle: {
                                color: "#F5D707"
                            }
                        }, {
                            value: source[3],
                            itemStyle: {
                                color: "#6AF507"
                            }
                        }, {
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
    }

    getCompounds();
    $("#selectedDisease").change(getCompounds);

    $("#detail").bootstrapTable({
        method: 'get',
        toolbar: '#toolbar',
        striped: true,
        cache: false,
        pagination: true,
        sortable: false,
        sortOrder: 'asc',
        pageNumber: 1,
        pageSize: 10,
        pageList: [10, 25, 50, 100],
        url: '/data/detail',
        queryParamsType: '',
        sidePagination: 'server',
        columns: [{
            field: 'disease_id',
            title: 'disease_id',
            align: 'center'
        }, {
            field: 'disease_name',
            title: 'disease_name',
            align: 'center'
        }, {
            field: 'drug_inchikey',
            title: 'drug_inchikey',
            align: 'center'
        }, {
            field: 'drug_name',
            title: 'drug_name',
            align: 'center'
        }, {
            field: 'com_inchikey',
            title: 'com_inchikey',
            align: 'center'
        }, {
            field: 'tar_over_rate',
            title: 'tar_over_rate',
            align: 'center'
        }, {
            field: 'tc',
            title: 'tc',
            align: 'center'
        }, {
            field: 'target_overlap_rate',
            title: 'target_overlap_rate',
            align: 'center'
        }]
    })

})