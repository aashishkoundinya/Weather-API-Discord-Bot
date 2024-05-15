const { Client } = require('discord.js');

const client = new Client();

const status = {
  presence: 'online',
  activity: {
    name: 'custom status',
  },
};

client.on('ready', () => {
  client.user.setPresence(status);
});

client.login('--Insert Bot Token Here--');