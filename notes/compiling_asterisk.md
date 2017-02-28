# Compiling Asterisk

A set of notes around what commands are required to spin up a basic Asterisk
instance with just the modules that are required for our demo VNF.

## System setup
```
yum update -y
yum install ntp -y
ntpdate pool.ntp.org
systemctl enable ntpd.service
systemctl start ntpd.service
yum install epel-release vim-enhanced -y
```

* Disable SElinux in `/etc/selinux/config
* `systemctl reboot`

## Asterisk dependency install
```
yum install gcc gcc-c++ cpp ncurses-devel libxml2-devel sqlite-devel \
  openssl-devel newt-devel kernel-devel libuuid-devel net-snmp-devel bzip2 \
  jansson-devel pjproject-devel libsrtp-devel gsm-devel speex-devel
```

## Asterisk menuselect building
```
mkdir ~/src
cd ~/src
git clone https://github.com/asterisk/asterisk.git
cd asterisk
git checkout 14.3.0
git checkout -b 14.3.0
./configure --libdir=/usr/lib64
make menuselect.makeopts
```

## Configure modules to build

Small script to make building menuselect.makeopts a bit easier

```
#!/usr/bin/env bash
enable_mods=""
for arg; do
  enable_mods="${enable_mods} --enable $arg"
done

menuselect/menuselect --disable-all $enable_mods --enable-category MENUSELECT_BRIDGES --enable LOADABLE_MODULES menuselect.makeopts
```

Configure menuselect

```
./buildmenu.sh app_stasis res_stasis cdr_syslog chan_bridge_media chan_rtp chan_pjsip codec_a_mu codec_ulaw pbx_config res_pjproject res_sorcery_astdb res_sorcery_config res_sorcery_memory res_sorcery_memory_cache res_rtp_asterisk res_ari res_ari_applications res_ari_asterisk res_ari_bridges res_ari_channels res_ari_device_states res_ari_endpoints res_ari_events res_ari_mailboxes res_ari_model res_ari_playbacks res_ari_recordings res_ari_sounds res_pjsip res_pjsip_acl res_pjsip_authenticator_digest res_pjsip_caller_id res_pjsip_config_wizard res_pjsip_dialog_info_body_generator res_pjsip_diversion res_pjsip_dlg_options res_pjsip_dtmf_info res_pjsip_empty_info res_pjsip_endpoint_identifier_anonymous res_pjsip_endpoint_identifier_ip res_pjsip_endpoint_identifier_user res_pjsip_exten_state res_pjsip_header_funcs res_pjsip_logger res_pjsip_messaging res_pjsip_mwi res_pjsip_mwi_body_generator res_pjsip_nat res_pjsip_notify res_pjsip_one_touch_record_info res_pjsip_outbound_authenticator_digest res_pjsip_outbound_publish res_pjsip_outbound_registration res_pjsip_path res_pjsip_pidf_body_generator res_pjsip_publish_asterisk res_pjsip_pubsub res_pjsip_refer res_pjsip_registrar res_pjsip_registrar_expire res_pjsip_rfc3326 res_pjsip_sdp_rtp res_pjsip_send_to_voicemail res_pjsip_session res_pjsip_sips_contact res_pjsip_t38 res_pjsip_transport_management res_pjsip_transport_websocket res_pjsip_xpidf_body_generator res_stasis res_stasis_answer res_stasis_device_state res_stasis_mailbox res_stasis_playback res_stasis_recording res_stasis_snoop res_stasis_test res_statsd res_timing_timerfd
```
