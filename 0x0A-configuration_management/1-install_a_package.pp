#A puppet script that installs version flask v2.1.0 on a node
package { 'flask' :
  ensure   => '2.1.0',
  provider => 'pip3',
}
