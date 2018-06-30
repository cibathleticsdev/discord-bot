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

client.login(process.env."NDYyMjcyMDcyMjM2NzkzODU2.DhhSCQ.UK_3JEF59C87Ju36Z6dwbFvie9U");
