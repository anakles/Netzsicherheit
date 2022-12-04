set -e

mkdir ca
cd ca
# rm -f ca.key ca.crt chuck.key chuck.csr chuck.crt

# Cobbled together following hints from:
# https://web.archive.org/web/20200927204126/https://www.dalesandro.net/create-self-signed-smime-certificates/
#
# https://tools.ietf.org/html/rfc3850
# https://security.stackexchange.com/questions/30066/which-extensions-to-use-for-a-s-mime-certificate/30069#30069

# Generate CA key (without passphrase, use -aes256 for pw protection).
openssl genrsa -out ca.key 4096

openssl req -new -x509 -days 7300 -key ca.key -out ca.crt -subj "/C=DE/ST=NRW/L=Bochum/O=RUB/OU=NDS/CN=Bruce Schneier/emailAddress=bruce.schneier@rub.de"

# Email?

# Look at content.
openssl x509 -inform pem -in ca.crt -text -noout

openssl genrsa -out chuck.key 4096
openssl req -new -key chuck.key -out chuck.csr -subj "/C=DE/ST=NRW/L=Bochum/O=RUB/OU=NDS/CN=Chuck Norris/emailAddress=chuck.norris@rub.de"
openssl x509 -req -days 7300 -in chuck.csr -CA ca.crt -CAkey ca.key -set_serial 1 -out chuck.crt -addtrust emailProtection -addreject clientAuth -addreject serverAuth -trustout -extfile ../smime.cnf -extensions smime

openssl x509 -inform pem -in chuck.crt -text -noout

openssl pkcs12 -export -in chuck.crt -inkey chuck.key -out chuck.p12
