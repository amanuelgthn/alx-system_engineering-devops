# Install flask from pip3
# version must be 2.1.0
package {'flask':
    ensure   => present,
    provides => pip3,
    version  => '2.1.0',
    }