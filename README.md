# Custom components for Home Assistant

A number of custom components I have developed for Home Assistant.

## Skånetrafiken Jojo sensor

Reads the balance of a Jojo card from Skånetrafiken website.

**Directory:** `skanetrafiken_jojo`

**Usage:**
```
sensor:
  - platform: skanetrafiken_jojo
    card_number: 1234567890
    card_cvc: 12CD
```
By default the balance will be polled every one hour.
This can be changed by the `scan_interval` configuration key.