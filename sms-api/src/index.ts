const express = require('express');

const app = express();
const port = 3000;

app.listen(port, () => {
    console.log(`SMS API listening on port ${port}`);
});

var counter = 0;

app.get('/whatsapp', (req: any, res: any) => {
    const phoneNumber = req.query.number;
    console.log("SMS code requested for number " + phoneNumber);

    ++ counter;
    if (counter % 10 == 0) {
        // every 10 requests succeed, code is received.
        res.send("123456");
    } else {
        // code not yet received, respond with 404
        res.status(404).end();
    }
});
