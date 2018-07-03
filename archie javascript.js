const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log('I am ready!');
});

client.on('message', message => {
  if (message.content === 'ping') {
    message.reply('pong');
  }
});

//client.login(process.env."NDYyMjcyMDcyMjM2NzkzODU2.Dh2ULg.1q_9bL0XLirQ8GVb6sa1Y8vgwe0");
