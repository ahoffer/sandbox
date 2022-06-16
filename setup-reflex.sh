#!/bin/bash
set -e
BACKUP_HOSTNAME=node2
BIND_USER=cn=unix_ldap,ou=Service_Accounts,ou=VIP-C,dc=vipc,dc=local
BIND_USER_PASSWORD='ENC(ATGfjyajrr++M1Wcg7/x+ES2yR4cixXQisKGokfGouykmIN9FXJY6WwD)'
BROKER_PASSWORD='ENC(ATGfjyYJe11N0JinBGALVIw2JiFmddpyoGAamxRIGwkwbVlH66+BCV4EJ0NWG88NoFSqpc0=)'
BROKER_USER=reflex_internal_user
CLASSIFICATION=U
CLUSTER_AUTH='ENC(-4db652271cf8b661)'
DO_LDAP=no
EXPORT_METRICS=true
EXTERNAL_BACKUP=node2
EXTERNAL_LIVE=node1
EXTERNAL_SOLR=yes
HYDRA_DISC_HOST=hydra
HYDRA_DISC_PORT=
HYDRA_DISC_PROTOCOL=
HYDRA_DISC_URL=
HYDRA_HOST=hydra
HYDRA_PASS=
HYDRA_PORT=
HYDRA_PROTOCOL=
HYDRA_SECRET=
HYDRA_URL=
HYDRA_USER=
IP_LIST=reflex1,reflex2
KEYSTORE_PASSWORD=changeit
LDAP_HOSTS=ldap
LDAP_LOGIN_ATTRS=cn
LDAP_PORT=636
LIVE_HOSTNAME=node1
RELEASABILITY=FOUO
SITE_ID=BLK_MESA
SSL_ENABLED=yes
TRUSTSTORE_PASSWORD=changeit
APP_HOME=/opt/reflex
CONFIG_PATH=${APP_HOME}/bin/configure-cluster-cli
MODE=live
source ${CONFIG_PATH}/config-main.sh
echo "Sourcing ${CONFIG_PATH}/config-main.sh"
if [ $MODE == "live" ]; then
  setupReflexInstance $MODE
elif [ $MODE == "backup" ]; then
  setupReflexInstance $MODE --externalHttpsPort="18993"
elif [ $MODE == "replay" ]; then
  setupReflexInstance $MODE --externalHttpsPort="28993"
elif [ $MODE == "all" ]; then
  setupReflexInstance $MODE
else
  echo "Invalid MODE argument. MODE must be set to 'live', 'backup', or 'replay'."
  exit 1
fi

chown -R reflex:reflex /opt/reflex
exec runuser -u reflex ${APP_HOME}/bin/reflex server
sleep 2
