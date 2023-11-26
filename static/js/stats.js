Highcharts.chart('container',  {
  colors: ['#10487F', '#406D99', '#668AAD', '#85A1BD', '#C1CFDD'],
  chart: {
    type: 'pie'
  },
  title: {
    text: 'Estadisticas'
  },
  subtitle: {
    text:
    'Estas son las estadisticas de los hinchas'
  },
  plotOptions: {
    pie: {
      allowPointSelect: true,
      cursor: 'pointer',
      dataLabels: {
        enabled: true,
        format: '{point.name}: {point.percentage:.1f}%'
      },
      showInLegend: true
    }
  },
  series: [
    {
      name: 'Hinchas',
      colorByPoint: true,
      data: [
        
      ]
    }
  ]
});
Highcharts.chart('container2',  {
  colors: ['#10487F', '#406D99', '#668AAD', '#85A1BD', '#C1CFDD'],
  chart: {
    type: 'pie'
  },
  title: {
    text: 'Estadisticas'
  },
  subtitle: {
    text:
    'Estas son las estadisticas de los artesanos'

  },
  plotOptions: {
    pie: {
      allowPointSelect: true,
      cursor: 'pointer',
      dataLabels: {
        enabled: true,
        format: '{point.name}: {point.percentage:.1f}%'
      },
      showInLegend: true
    }
  },
  series: [
    {
      name: 'Artesanos',
      colorByPoint: true,
      data: []
    }
  ]
});
fetch("http://localhost:3006/get-stats-data")
  .then((response) => response.json())
  .then((data) => {
    const parsedData = data.data.map((item) => {
      return {
        name: item.name,
        y: item.data,
      };
    });
    const parsedData2 = data.data2.map((item) => {
      return {
        name: item.name,
        y: item.data,
      };
    });
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container"
    );
    const chart2 = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container2"
    );
    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });
    chart2.update({
      series: [
        {
          data: parsedData2,
        },
      ],
    });
  })
  .catch((error) => console.error("Error:", error));
