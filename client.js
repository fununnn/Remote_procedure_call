const net = require('net');

const request = {
    method: 'floor',
    params: [parseFloat('4.5')],
    id: 1
};

const client = new net.Socket();
const HOST = '127.0.0.1';
const PORT = 65432;

client.connect(PORT, HOST, () => {
    console.log('Connected to server');
    // serverへJSONファイルを送信
    client.write(JSON.stringify(request));
});

client.on('data', (data) => {
    // レスポンスをサーバーから受信
    const response = JSON.parse(data);

    if (response.error) {
        console.error('Error', response.error);
    } else {
        console.log('Result', response.result);
    }
    client.end();
});

client.on('close', () => {
    console.log('Connection closed');
});
