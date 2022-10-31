var chart = LightweightCharts.createChart(document.getElementById('chart'), {
	width: 1000,
  	height: 500,
	layout: {
		backgroundColor: '#000000',
		textColor: 'rgba(255, 255, 255, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	priceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
		timeVisible: true,
		secondsVisible: false,
	},
});

	var candleSeries = chart.addCandlestickSeries({
		upColor: 'rgb(38,166,154)',
		downColor: 'rgb(255,82,82)',
		wickUpColor: 'rgb(38,166,154)',
		wickDownColor: 'rgb(255,82,82)',
		borderVisible: false,
	});

	var uniqueCandlesticks = []
	var markers = []

	// fetch('http://localhost:5000/history')

	// .then((r) => r.json())
	// .then((response) => {
	// 	candleSeries.setData(response);

	// 	for (let candlestick_entry in response) {
	// 		uniqueCandlesticks.push(response[candlestick_entry].time)
	// 		if((uniqueCandlesticks.length ) % 2) {
	// 			markers.push({ time: response[candlestick_entry].time, position: 'aboveBar', color: '#f68410', shape: 'circle', text: 'D' });
	// 	}
	// 	//candleSeries.setMarkers(markers);
	// 	}
	// })

var binanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_1m");

binanceSocket.onmessage = function (event) {	
	var message = JSON.parse(event.data);
	var candlestick = message.k;
	console.log(candlestick)

	candleSeries.update({
		time: candlestick.t /1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close: candlestick.c
	})
	var datesForMarkers = [candleSeries.length];
	console.log('hello')

	if(!(uniqueCandlesticks.includes(candlestick.t))) {
		uniqueCandlesticks.push(candlestick.t)
		if((uniqueCandlesticks.length ) % 2) {
			markers.push({ time: candlestick.t /1000, position: 'aboveBar', color: '#f68410', shape: 'circle', text: 'D' });
		}
		candleSeries.setMarkers(markers);
	}
}

