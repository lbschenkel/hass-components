# Custom components for Home Assistant

A number of custom components I have developed for Home Assistant.

## Skånetrafiken Jojo sensor

Reads the balance of a Jojo card from Skånetrafiken website.

**Component:** `sensor/skanetrafiken_jojo.py`

**Usage:**
```
sensor:
  - platform: skanetrafiken_jojo
    card_number: 1234567890
    card_cvc: 12CD
```
By default the balance will be polled every one hour.
This can be changed by the `scan_interval` configuration key.

## Broadlink RM switch

Patched version of [official component](https://www.home-assistant.io/components/switch.broadlink/)
that (in addition to base64) supports packets to be described in
Pronto hex format. When described in this format, packets are
automatically converted to Broadlink format by this component before
they are sent to the device.

This allows codes from IR databases such as [irdb.tk](http://irdb.dk)
to be used verbatim.

**Component:** `switch/broadlink.py`

**Usage:**
```
sensor:
  - platform: broadlink
    host: 1.2.3.4
    mac: '01:23:45:67:89:0A'
    switches:
      tv_panasonic:
          command_on: >-
            0000 0070 0000 0032 0080 0040 0010 0010 0010 0030 0010 0010
            0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010
            0010 0010 0010 0010 0010 0010 0010 0010 0010 0030 0010 0010
            0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010
            0010 0010 0010 0010 0010 0030 0010 0010 0010 0010 0010 0010
            0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010
            0010 0030 0010 0030 0010 0030 0010 0030 0010 0030 0010 0010
            0010 0010 0010 0010 0010 0030 0010 0030 0010 0030 0010 0030
            0010 0030 0010 0010 0010 0030 0010 0ACD
          command_off: >-
            0000 0070 0000 0032 0080 0040 0010 0010 0010 0030 0010 0010
            0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010
            0010 0010 0010 0010 0010 0010 0010 0010 0010 0030 0010 0010
            0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010
            0010 0010 0010 0010 0010 0030 0010 0010 0010 0010 0010 0010
            0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0010 0030
            0010 0030 0010 0030 0010 0030 0010 0030 0010 0030 0010 0010
            0010 0010 0010 0030 0010 0030 0010 0030 0010 0030 0010 0030
            0010 0030 0010 0010 0010 0030 0010 0ACD
```
