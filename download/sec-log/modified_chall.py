#! /usr/bin/env python
import SocketServer,threading

# n = 25504352309535290475248970674346405639150033303276037621954645287836414954584485104061261800020387562499019659311665606506084209652278825297538342995446093360707480284955051977871508969158833725741319229528482243960926606982225623875037437446029764584076579733157399563314682454896733000474399703682370015847387660034753890964070709371374885394037462378877025773834640334396506494513394772275132449199231593014288079343099475952658539203870198753180108893634430428519877349292223234156296946657199158953622932685066947832834071847602426570899103186305452954512045960946081356967938725965154991111592790767330692701669
n = 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385618630224045260938256521594051014100163503337502422415671183189322191205776067978479547419392319431496088564871089271483778027246774457788805555615297270366146466252347288451288375751247197329959735437170802389801569971064368598028871180778637354490929426176883740658057736936793507039520194977558948892181985349
e = 65537

# f = open('secret.txt')
d = 5898098930664372161128074829076419356987227246173412034550117668776758168912199871424259976551040907261253269612384183151031692738438163285141971568645313554265009447949817877739660272707182642620010763579532663749617952106205271883847985815379304438693059890385678999923376035502428981136685143444486798943804807487192707178720184667695716115902505383790053375341061279601961200801530380606467051543801013900820743379533587829273087413517724910508213960585521910897933698207234596052346902824759366233883262120445044914724165895445391554046940565650539341737412923841880733053015593783624333240884617673534472113613
# phin = 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385618270685418288475074975733012856295216779742106633954356636329159875740424456976553282002437674616424046324643329528697062709667236828955560569920435991417897710716560438720317823146807994837771496531004898219790032294763003913103108232952416272836455099475862371485461257042301630080087585306846289643733710380
flag = 'fakeflag{7hi5_1s_4_c!uMmy_fLa9}'#f.readline().strip()

# Translate a number to a string (byte array), for example 5678 = 0x162e = \x16\x2e
def num2str(n):
    d = ('%x' % n)
    if len(d) % 2 == 1:
        d = '0' + d
    return d.decode('hex')
# Translate byte array back to number \x16\x2e = 0x162e = 5678
def str2num(s):
    return int(s.encode('hex'),16)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            self.request.sendall("\nWelcome to the secure login server, make your choice from the following options:\n1. Register yourself as a user.\n2. Collect flag\n3. Sign a message\n4. Exit\nChoice: ")
            inp = self.request.recv(1024).strip()
            if inp == '1':
                self.request.sendall("Pick a username: ")
                uname = self.request.recv(1024).strip()
                self.request.sendall("Enter your full name: ")
                full = self.request.recv(1024).strip()
                ticket = 'ticket:user|%s|%s' % (uname,full)
                ticket = pow(str2num(ticket),d,n)
                ticket = num2str(ticket)
                self.request.sendall("Your ticket:\n")
                self.request.sendall(ticket.encode('hex') + "\n")
            elif inp == '2':
                self.request.sendall("Enter your ticket: ")
                ticket = self.request.recv(1024).strip()
                try:
                    ticket = int(ticket,16)
                except:
                    ticket = 0
                ticket = pow(ticket,e,n)
                ticket = num2str(ticket)
                if ticket.startswith('ticket:'):
                    if ticket.startswith('ticket:admin|root|'):
                        self.request.sendall("Here you go!\n")
                        self.request.sendall(flag + "\n")
                        break
                    else:
                        self.request.sendall("Sorry that function is only available to admin user root\n")
                else:
                    self.request.sendall("That doesn't seem to be a valid ticket\n")
            elif inp == '3':
                self.request.sendall("Enter your message, hex encoded (i.e. 4142 for AB): ")
                msg = self.request.recv(1024).strip()
                try:
                    msg = msg.decode('hex')
                except:
                    self.request.sendall("That's not a valid message\n!")
                    continue
                msg = '\xff' + msg # Add some padding at the start so users can't use this to sign a ticket
                if str2num(msg) >= n:
                    self.request.sendall("That's not a valid message\n!")
                    continue
                signed = pow(str2num(msg),d,n)
                signed = num2str(signed)
                self.request.sendall("Your signature:\n")
                self.request.sendall(signed.encode('hex') + "\n")
            elif inp == '4':
                self.request.sendall("Bye!\n")
                break
            else:
                self.request.sendall(inp.encode('hex')+'\n')
                print(inp.encode('hex'), len(inp))
                self.request.sendall("Invalid choice!\n")

SocketServer.TCPServer.allow_reuse_address = True
server = ThreadedTCPServer(("0.0.0.0", 12345), MyTCPHandler)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()
server.serve_forever()
