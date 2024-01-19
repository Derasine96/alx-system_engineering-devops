#Connect to a sever without password

sshd_config { 'PasswordAuthentication':
  value  => 'no',
}

file { '~/.ssh/school':
  ensure   => 'present',
  username => 'ubuntu',
  require  => sshd_config['PasswordAuthentication'],
}
