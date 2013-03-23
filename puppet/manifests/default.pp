Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/", "/usr/share/red5" ] }

file { '/etc/motd':
	content => "Python Dev Box"
}

exec { 'apt-get update':
	command => 'apt-get update',
}

$devPackages = ["vim", "apache2", "libapache2-mod-wsgi", "subversion"]
package { $devPackages:
	ensure => "installed",
	require => Exec['apt-get update'],
}

file {'/etc/apache2/conf.d/python-wsgi-vhost':
	notify  => Service["apache2"],
	ensure  => file,
	require => Package['apache2'],
	content => template('sitebase/apache-python-wsgi-vhost.erb'),
}

