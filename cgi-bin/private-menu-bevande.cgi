#!\Perl64\bin\perl

#use utf8;
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Encode qw(decode encode);

use My::Base;
use My::PrintMenu;
use My::Operation;

my $q = new CGI;
my $session = CGI::Session->load() or die $!;

checkSession($session);

my %path = (   add_bevanda => 'add-bevanda.cgi',
               mod_bevanda => 'mod-bevanda.cgi',
               del_bevanda => 'private-menu-bevande.cgi',
);

printStartHtml('Menù bevande - Area Amministratore', "Menù bevande", "bevande");

my $message = checkDelete($q, "bevande/listaBevande/bevanda");

#print $q->a({-href => 'private-menu.cgi'}, 'Torna alle categorie menù');

if ($message ne '') {
   print $message;
}

printMenuBevande(1, \%path);

printEndHtml();

exit 0;
