const data = {
  labels: [],
  datasets: [
    {
      label: 'Temperature',
      backgroundColor: '#ff0000',
      borderColor: '#ff0000',
      tension: 0.2,
      pointRadius: 0,
      data: [],
    },
    /*{
      label: 'Station 1',
      backgroundColor: '#00ff00',
      borderColor: '#00ff00',
      tension: 0.2,
      pointRadius: 0,
      data: [],
    }*/
  ]
};

const config = {
  type: 'line',
  data: data,
  options: {
    scales: {
      y: {
        max: 90,
        min: 50
      }
    }
  }
};

const chart = new Chart(document.getElementsByTagName('canvas')[0], config);

const fetchData = () => {
  let stationID = document.getElementById('station').selectedIndex;
  let timeValue;
  let currentTime = Math.floor(Date.now() / 1000);
  switch (document.getElementById('time').selectedIndex) {
    case 0:
      timeValue = currentTime - 3600;
      break;
    case 1:
      timeValue = currentTime - 43200;
      break;
    case 2:
      timeValue = currentTime - 86400;
      break;
    case 3:
      timeValue = currentTime - 604800;
  }
  let apiCall = `http://127.0.0.1:5000/api/data?station=${stationID}&time=${timeValue}`;
  fetch(apiCall, {
    headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
    }
  })
  .then(res => res.json())
  .then(data => {
    chart.data.labels = [];
    chart.data.datasets[0].data = [];
    data.forEach(dataPoint => {
      chart.data.labels.push(convertTime(dataPoint.time));
      chart.data.datasets[0].data.push(dataPoint.temp);
    })
    chart.update();
  });
  let ymin = document.getElementById('ymin').value;
  let ymax = document.getElementById('ymax').value;
  let tension = document.getElementById('tension').value;
  if (ymax != '' && ymin != '') {
    chart.options.scales = {
      y: {
        min: parseInt(ymin),
        max: parseInt(ymax)
      }
    }
  }
  if (tension != '') {
    chart.data.datasets[0].tension = tension;
  }
  chart.update();
}

const convertTime = UNIX_timestamp => {
  var a = new Date(UNIX_timestamp * 1000);
  var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var year = a.getFullYear();
  var month = months[a.getMonth()];
  var date = a.getDate();
  var hour = a.getHours();
  var min = a.getMinutes();
  var sec = a.getSeconds();
  var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
  return time;
}