#!/usr/local/bin/perl
#
# postfix-module by Guillaume Cottenceau <gc@mandrakesoft.com>,
# for webmin by Jamie Cameron
#
# Copyright (c) 2000 by Mandrakesoft
#
# Permission to use, copy, modify, and distribute this software and its
# documentation under the terms of the GNU General Public License is hereby 
# granted. No representations are made about the suitability of this software 
# for any purpose. It is provided "as is" without express or implied warranty.
# See the GNU General Public License for more details.
#
# 
# Manages virtuals for Postfix
#
# << Here are all options seen in Postfix sample-virtual.cf >>


require './postfix-lib.pl';

$access{'header'} || &error($text{'header_ecannot'});
&ui_print_header(undef, $text{'header_title'}, "", "header");

# Start of header checks for
print &ui_form_start("save_opts_header.cgi");
print &ui_table_start($text{'header_title'}, "width=100%", 2);

$none = $text{'opts_none'};
&option_mapfield("header_checks", 60, $none);

print &ui_table_end();
print &ui_form_end([ [ undef, $text{'opts_save'} ] ]);

# Header map contents
print &ui_hr();
if (&get_current_value("header_checks") eq "")
{
    print $text{'no_map'},"<p>\n";
}
else
{
    &generate_map_edit("header_checks", $text{'map_click'}." ".
		       &hlink($text{'help_map_format'}, "header"), 1,
		       $text{'header_name'}, $text{'header_value'});
}

&ui_print_footer("", $text{'index_return'});

