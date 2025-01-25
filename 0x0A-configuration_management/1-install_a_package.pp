# A puppet script that installs version 2.1.0 of flask on a node
package { 'flask' :
  ensure   => '2.1.0',
  provider => 'pip3',
}
