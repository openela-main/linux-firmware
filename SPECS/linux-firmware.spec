%global debug_package %{nil}
%global firmware_release 140

%global _firmwarepath	/usr/lib/firmware
%define _binaries_in_noarch_packages_terminate_build 0

Name:		linux-firmware
Version:	20230814
Release:	%{firmware_release}%{?dist}
Summary:	Firmware files used by the Linux kernel
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
URL:		http://www.kernel.org/
BuildArch:	noarch

Source0:	https://www.kernel.org/pub/linux/kernel/firmware/%{name}-%{version}.tar.xz
Patch1:		0001-copy-firmware.sh-be-verbose.patch

BuildRequires:	git-core
BuildRequires:	make
Requires:	linux-firmware-whence
Provides:	kernel-firmware = %{version}
Obsoletes:	kernel-firmware < %{version}
Conflicts:	microcode_ctl < 2.1-0

%description
This package includes firmware files required for some devices to
operate.

%package whence
Summary:	WHENCE License file
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
%description whence
This package contains the WHENCE license file which documents the vendor license details.

%package -n iwl100-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 100 Series Adapters
License:	Redistributable, no modification permitted
Version:	39.31.5.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl100-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl100 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl105-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 105 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl105-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl105 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl135-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 135 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl135-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl135 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl1000-firmware
Summary:	Firmware for Intel® PRO/Wireless 1000 B/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	39.31.5.1
Epoch:		1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl1000-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl1000 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl2000-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 2000 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl2000-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl2000 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl2030-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 2030 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl2030-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl2030 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl3160-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 3160 Series Adapters
License:	Redistributable, no modification permitted
Epoch:		1
Version:	25.30.13.0
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl3160-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl3945-firmware
Summary:	Firmware for Intel® PRO/Wireless 3945 A/B/G network adaptors
License:	Redistributable, no modification permitted
Version:	15.32.2.9
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl3945-firmware
This package contains the firmware required by the iwl3945 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl4965-firmware
Summary:	Firmware for Intel® PRO/Wireless 4965 A/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	228.61.2.24
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl4965-firmware
This package contains the firmware required by the iwl4965 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl5000-firmware
Summary:	Firmware for Intel® PRO/Wireless 5000 A/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	8.83.5.1_1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl5000-firmware
This package contains the firmware required by the iwl5000 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl5150-firmware
Summary:	Firmware for Intel® PRO/Wireless 5150 A/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	8.24.2.2
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl5150-firmware
This package contains the firmware required by the iwl5150 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6000 AGN Adapter
License:	Redistributable, no modification permitted
Version:	9.221.4.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl6000-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000g2a-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6005 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl6000g2a-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000g2b-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6030 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl6000g2b-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6050-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6050 Series Adapters
License:	Redistributable, no modification permitted
Version:	41.28.5.1
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl6050-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl7260-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 726x/8000/9000/AX200/AX201 Series Adapters
License:	Redistributable, no modification permitted
Epoch:		1
Version:	25.30.13.0
Release:	%{firmware_release}%{?dist}
Requires:	linux-firmware-whence
%description -n iwl7260-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n libertas-usb8388-firmware
Summary:	Firmware for Marvell Libertas USB 8388 Network Adapter
License:	Redistributable, no modification permitted
Epoch:		2 
Requires:	linux-firmware-whence
%description -n libertas-usb8388-firmware
Firmware for Marvell Libertas USB 8388 Network Adapter

%package -n libertas-usb8388-olpc-firmware
Summary:	OLPC firmware for Marvell Libertas USB 8388 Network Adapter
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n libertas-usb8388-olpc-firmware
Firmware for Marvell Libertas USB 8388 Network Adapter with OLPC mesh network
support.

%package -n libertas-sd8686-firmware
Summary:	Firmware for Marvell Libertas SD 8686 Network Adapter
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n libertas-sd8686-firmware
Firmware for Marvell Libertas SD 8686 Network Adapter

%package -n libertas-sd8787-firmware
Summary:	Firmware for Marvell Libertas SD 8787 Network Adapter
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n libertas-sd8787-firmware
Firmware for Marvell Libertas SD 8787 Network Adapter

%package -n liquidio-firmware
Summary:	Firmware for Cavium LiquidIO Intelligent Server Adapter
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n liquidio-firmware
Firmware for Cavium LiquidIO Intelligent Server Adapter

%package -n netronome-firmware
Summary:	Firmware for Netronome Smart NICs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n netronome-firmware
Firmware for Netronome Smart NICs

%prep
%autosetup -S git -p1

%build

%install
mkdir -p %{buildroot}/%{_firmwarepath}
mkdir -p %{buildroot}/%{_firmwarepath}/updates

%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9
make DESTDIR=%{buildroot}/ FIRMWAREDIR=%{_firmwarepath} install-xz
%else
make DESTDIR=%{buildroot}/ FIRMWAREDIR=%{_firmwarepath} install
%endif

#Cleanup files we don't want to ship
pushd %{buildroot}/%{_firmwarepath}
# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
rm -rf ess korg sb16 yamaha

# Remove source files we don't need to install
rm -rf carl9170fw
rm -rf cis/{src,Makefile}
rm -f atusb/ChangeLog
rm -f av7110/{Boot.S,Makefile}
rm -f dsp56k/{bootstrap.asm,concat-bootstrap.pl,Makefile}
rm -f iscis/{*.c,*.h,README,Makefile}
rm -f keyspan_pda/{keyspan_pda.S,xircom_pgs.S,Makefile}
rm -f usbdux/*dux */*.asm

# No need to install old firmware versions where we also provide newer versions
# which are preferred and support the same (or more) hardware
rm -f libertas/sd8686_v8*
rm -f libertas/usb8388_v5.bin*

# Remove firmware for Creative CA0132 HD as it's in alsa-firmware
rm -f ctefx.bin* ctspeq.bin*

# Remove superfluous infra files
rm -f check_whence.py configure Makefile README

# Remove executable bits from random firmware
find . -type f -executable -exec chmod -x {} \;
popd

# Create file list but exclude firmwares that we place in subpackages
FILEDIR=`pwd`
pushd %{buildroot}/%{_firmwarepath}
find . \! -type d > $FILEDIR/linux-firmware.files
find . -type d | sed -e '/^.$/d' > $FILEDIR/linux-firmware.dirs
popd
sed -i -e 's:^./::' linux-firmware.{files,dirs}
sed -i -e '/^iwlwifi/d' \
	-i -e '/^libertas\/sd8686/d' \
	-i -e '/^libertas\/usb8388/d' \
	-i -e '/^mrvl\/sd8787/d' \
	-i -e '/^liquidio/d' \
	-i -e '/^netronome/d' \
	linux-firmware.files
sed -i -e 's!^!/usr/lib/firmware/!' linux-firmware.{files,dirs}
sed -i -e 's/^/"/;s/$/"/' linux-firmware.files
sed -e 's/^/%%dir /' linux-firmware.dirs >> linux-firmware.files


%files -f linux-firmware.files
%dir %{_firmwarepath}
%license LICENCE.* LICENSE.* GPL*

%files whence
%license WHENCE

%files -n iwl100-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-100-5.ucode*

%files -n iwl105-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-105-*.ucode*

%files -n iwl135-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-135-*.ucode*

%files -n iwl1000-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-1000-*.ucode*

%files -n iwl2000-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-2000-*.ucode*

%files -n iwl2030-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-2030-*.ucode*

%files -n iwl3160-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-3160-*.ucode*
%{_firmwarepath}/iwlwifi-3168-*.ucode*

%files -n iwl3945-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-3945-*.ucode*

%files -n iwl4965-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-4965-*.ucode*

%files -n iwl5000-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-5000-*.ucode*

%files -n iwl5150-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-5150-*.ucode*

%files -n iwl6000-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-6000-*.ucode*

%files -n iwl6000g2a-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-6000g2a-*.ucode*

%files -n iwl6000g2b-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-6000g2b-*.ucode*

%files -n iwl6050-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-6050-*.ucode*

%files -n iwl7260-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-7260-*.ucode*
%{_firmwarepath}/iwlwifi-7265-*.ucode*
%{_firmwarepath}/iwlwifi-7265D-*.ucode*
%{_firmwarepath}/iwlwifi-8000C-*.ucode*
%{_firmwarepath}/iwlwifi-8265-*.ucode*
%{_firmwarepath}/iwlwifi-9000-*.ucode*
%{_firmwarepath}/iwlwifi-9260-*.ucode*
%{_firmwarepath}/iwlwifi-cc-a0-*.ucode*
%{_firmwarepath}/iwlwifi-Qu*.ucode*
%{_firmwarepath}/iwlwifi-ty-a0-gf-a0*.ucode*
%{_firmwarepath}/iwlwifi-ty-a0-gf-a0.pnvm*
%{_firmwarepath}/iwlwifi-so-a0-*.ucode*
%{_firmwarepath}/iwlwifi-so-a0-*.pnvm*

%files -n libertas-usb8388-firmware
%license LICENCE.Marvell
%dir %{_firmwarepath}/libertas
%{_firmwarepath}/libertas/usb8388_v9.bin*

%files -n libertas-usb8388-olpc-firmware
%license LICENCE.Marvell
%dir %{_firmwarepath}/libertas
%{_firmwarepath}/libertas/usb8388_olpc.bin*

%files -n libertas-sd8686-firmware
%license LICENCE.Marvell
%dir %{_firmwarepath}/libertas
%{_firmwarepath}/libertas/sd8686*

%files -n libertas-sd8787-firmware
%license LICENCE.Marvell
%dir %{_firmwarepath}/mrvl
%{_firmwarepath}/mrvl/sd8787*

%files -n liquidio-firmware
%license LICENCE.cavium_liquidio
%dir %{_firmwarepath}/liquidio
%{_firmwarepath}/liquidio/*

%files -n netronome-firmware
%license LICENCE.Netronome
%dir %{_firmwarepath}/netronome
%{_firmwarepath}/netronome/*

%changelog
* Fri Sep 1 2023 Jan Stancek <jstancek@redhat.com> - 20230814-140
- NAVI 31 failing to boot (rhbz 2235321)
- Revert "amdgpu: partially revert firmware for GC 11.0.0 and GC 11.0.2"

* Mon Aug 14 2023 Jan Stancek <jstancek@redhat.com> - 20230814-139
- CVE-2023-20569 linux-firmware: hw amd: Return Address Predictor velunerability leading to information disclosure (rhbz 2230418)
- [AMDCLIENT 9.3 Bug] Linux FW update to fix multi monitor behind TBT3 dock & random flickers (rhbz 2227845)
- amdgpu: partially revert firmware for GC 11.0.0 and GC 11.0.2
- linux-firmware: Update AMD cpu microcode
- Merge branch 'for-upstream' of http://git.chelsio.net/pub/git/linux-firmware
- rtl_bt: Add firmware v2 file for RTL8852C
- Revert "rtl_bt: Update RTL8852C BT USB firmware to 0x040D_7225"
- amdgpu: DMCUB updates for various AMDGPU asics
- cxgb4: Update firmware to revision 1.27.4.0
- Merge branch 'rb3-update' of https://github.com/lumag/linux-firmware
- Merge https://github.com/pkshih/linux-firmware
- Mellanox: Add new mlxsw_spectrum firmware xx.2012.1012
- linux-firmware: Add URL for latest FW binaries for NXP BT chipsets
- rtw89: 8851b: update firmware to v0.29.41.1
- qcom: sdm845: add RB3 sensors DSP firmware
- amdgpu: Update DMCUB for DCN314 & Yellow Carp
- Merge branch 'dmc-adlp_2.20-mtl_2.13' of git://anongit.freedesktop.org/drm/drm-firmware
- Merge branch 'for-upstream' of https://github.com/CirrusLogic/linux-firmware
- ice: add LAG-supporting DDP package
- i915: Update MTL DMC to v2.13
- i915: Update ADLP DMC to v2.20
- cirrus: Add CS35L41 firmware for Dell Oasis Models

* Wed Jul 26 2023 Jan Stancek <jstancek@redhat.com> - 20230726-138
- Navi32 dGPU firmware (rhbz 2047486)
- CVE-2023-20593 linux-firmware: hw: amd: Cross-Process Information Leak (rhbz 2227156)
- Update to upstream 20230726 release.
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- copy-firmware: Fix linking directories when using compression
- copy-firmware: Fix test: unexpected operator
- qcom: sc8280xp: LENOVO: remove directory sym link
- qcom: sc8280xp: LENOVO: Remove execute bits
- amdgpu: update VCN 4.0.0 firmware
- amdgpu: add initial SMU 13.0.10 firmware
- amdgpu: add initial SDMA 6.0.3 firmware
- amdgpu: add initial PSP 13.0.10 firmware
- amdgpu: add initial GC 11.0.3 firmware
- linux-firmware: Update AMD fam17h cpu microcode
- linux-firmware: Update AMD cpu microcode
- amdgpu: update green sardine VCN firmware
- amdgpu: update renoir VCN firmware
- amdgpu: update raven VCN firmware
- amdgpu: update raven2 VCN firmware
- amdgpu: update Picasso VCN firmware
- amdgpu: update DMCUB to v0.0.175.0 for various AMDGPU ASICs
- Updated NXP SR150 UWB firmware
- wfx: update to firmware 3.16.1
- mediatek: Update mt8195 SCP firmware to support 10bit mode
- i915: update DG2 GuC to v70.8.0
- i915: update to GuC 70.8.0 and HuC 8.5.1 for MTL
- cirrus: Add CS35L41 firmware for ASUS ROG 2023 Models
- Partially revert "amdgpu: DMCUB updates for DCN 3.1.4 and 3.1.5"
- linux-firmware: update firmware for mediatek bluetooth chip (MT7922)
- linux-firmware: update firmware for MT7922 WiFi device
- linux-firmware: Update firmware file for Intel Bluetooth AX203
- linux-firmware: Update firmware file for Intel Bluetooth AX203
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX210
- linux-firmware: Update firmware file for Intel Bluetooth AX200
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- Fix qcom ASoC tglp WHENCE entry
- check_whence: Check link targets are valid
- iwlwifi: add new FWs from core80-39 release
- iwlwifi: update cc/Qu/QuZ firmwares for core80-39 release
- qcom: Add Audio firmware for SC8280XP X13s

* Mon Jul 3 2023 Jan Stancek <jstancek@redhat.com> - 20230625-137
- Fix PSR-SU issues with kernel 6.2 or later (rhbz 2218668)
- Update to upstream 20230625 release.
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- Makefile, copy-firmware: support xz/zstd compressed firmware
- copy-firmware: silence the last shellcheck warnings
- copy-firmware: drop obsolete backticks, quote
- copy-firmware: tweak sed invocation
- copy-firmware: quote deskdir and dirname
- check_whence: error if symlinks are in-tree
- check_whence: error if File: is actually a link
- check_whence: strip quotation marks
- linux-firmware: wilc1000: update WILC1000 firmware to v16.0
- ice: update ice DDP wireless_edge package to 1.3.10.0
- amdgpu: DMCUB updates for DCN 3.1.4 and 3.1.5
- amdgpu: update DMCUB to v0.0.172.0 for various AMDGPU ASICs
- fix broken cirrus firmware symlinks
- qcom: Update the microcode files for Adreno a630 GPUs.
- qcom: sdm845: rename the modem firmware
- qcom: sdm845: update remoteproc firmware
- rtl_bt: Update RTL8852A BT USB firmware to 0xDAC7_480D
- rtl_bt: Update RTL8852C BT USB firmware to 0x040D_7225
- amdgpu: DMCUB updates for various AMDGPU asics
- linux-firmware: update firmware for MT7922 WiFi device
- linux-firmware: update firmware for MT7921 WiFi device
- linux-firmware: update firmware for mediatek bluetooth chip (MT7922)
- linux-firmware: update firmware for mediatek bluetooth chip (MT7921)
- i915: Add HuC v8.5.0 for MTL
- mediatek: Update mt8195 SCP firmware to support hevc
- qcom: apq8016: add Dragonboard 410c WiFi and modem firmware
- cirrus: Add firmware for new Asus ROG Laptops
- brcm: Add symlinks from Pine64 devices to AW-CM256SM.txt
- amdgpu: Update GC 11.0.1 and 11.0.4
- rtw89: 8851b: add firmware v0.29.41.0
- ice: update ice DDP comms package to 1.3.40.0
- cxgb4: Update firmware to revision 1.27.3.0

* Wed Jun 28 2023 Jan Stancek <jstancek@redhat.com> - 20230525-136
- fix broken symlink /usr/lib/firmware/qcom/LENOVO/21BX.xz (rhbz 2214391)

* Thu May 25 2023 Jan Stancek <jstancek@redhat.com> - 20230525-135
- Update to upstream 20230525 release (rhbz 2178579).
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- amdgpu: update yellow carp firmware for amd.5.5 release
- amdgpu: update navi14 firmware for amd.5.5 release
- amdgpu: update navi12 firmware for amd.5.5 release
- amdgpu: update vega20 firmware for amd.5.5 release
- amdgpu: update vega12 firmware for amd.5.5 release
- amdgpu: update navi10 firmware for amd.5.5 release
- amdgpu: update vega10 firmware for amd.5.5 release
- amdgpu: update PSP 13.0.11 firmware for amd.5.5 release
- amdgpu: update GC 11.0.4 firmware for amd.5.5 release
- amdgpu: update SDMA 6.0.1 firmware for amd.5.5 release
- amdgpu: update PSP 13.0.4 firmware for amd.5.5 release
- amdgpu: update GC 11.0.1 firmware for amd.5.5 release
- amdgpu: update 13.0.8 firmware for amd.5.5 release
- amdgpu: update GC 10.3.7 firmware for amd.5.5 release
- amdgpu: update vangogh firmware for amd.5.5 release
- amdgpu: update VCN 4.0.4 firmware for amd.5.5 release
- amdgpu: update SMU 13.0.7 firmware for amd.5.5 release
- amdgpu: update PSP 13.0.7 firmware for amd.5.5 release
- amdgpu: update GC 11.0.2 firmware for amd.5.5 release
- amdgpu: update renoir firmware for amd.5.5 release
- amdgpu: update VCN 4.0.0 firmware for amd.5.5 release
- amdgpu: update SMU 13.0.0 firmware for amd.5.5 release
- amdgpu: update PSP 13.0.0 firmware for amd.5.5 release
- amdgpu: update GC 11.0.0 firmware for amd.5.5 release
- amdgpu: update green sardine firmware for amd.5.5 release
- amdgpu: update beige goby firmware for amd.5.5 release
- amdgpu: update dimgrey cavefish firmware for amd.5.5 release
- amdgpu: update arcturus firmware for amd.5.5 release
- amdgpu: update vcn 3.1.2 firmware for amd.5.5 release
- amdgpu: update psp 13.0.5 firmware for amd.5.5 release
- amdgpu: update GC 10.3.6 firmware for amd.5.5 release
- amdgpu: update navy flounder firmware for amd.5.5 release
- amdgpu: update sienna cichlid firmware for amd.5.5 release
- amdgpu: update aldebaran firmware for amd.5.5 release
- amdgpu: DMCUB updates for various AMDGPU asics
- ice: update ice DDP comms package to 1.3.40.0
- rtlwifi: Add firmware v6.0 for RTL8192FU
- rtlwifi: Update firmware for RTL8188EU to v28.0
- cirrus: Add firmware and tuning files for HP G10 series laptops
- linux-firmware: update firmware for mediatek bluetooth chip (MT7922)
- WHENCE: comment out duplicate MediaTek firmware
- i915: Add GuC v70.6.6 for MTL
- amdgpu: update DCN 3.1.6 DMCUB firmware
- rtl_bt: Update RTL8852B BT USB firmware to 0xDBC6_B20F
- rtl_bt: Update RTL8761B BT USB firmware to 0xDFC6_D922
- rtl_bt: Update RTL8761B BT UART firmware to 0x9DC6_D922
- Group all Conexant V4L devices together
- rtl_nic: update firmware of USB devices
- linux-firmware: Update firmware file for Intel Bluetooth AX200
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX203
- linux-firmware: Update firmware file for Intel Bluetooth AX203
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX210
- linux-firmware: update firmware for MT7981
- qca: Update firmware files for BT chip WCN6750
- mt76xx: Move the old Mediatek WiFi firmware to mediatek
- rtl_bt: Add firmware and config files for RTL8851B
- linux-firmware: Update AMD cpu microcode
- linux-firmware: add firmware for MT7981
- linux-firmware: update firmware for MT7921 WiFi device
- linux-firmware: update firmware for mediatek bluetooth chip (MT7921)
- linux-firmware: update qat firmware
- linux-firmware: Add firmware for Cirrus CS35L41 on Lenovo Laptops
- linux-firmware: update firmware for MT7916
- rtw89: 8852b: update format-1 fw to v0.29.29.1
- rtw89: 8852c: update fw to v0.27.56.13
- ath11k: WCN6855 hw2.0: update board-2.bin
- ath11k: WCN6750 hw1.0: update to WLAN.MSL.1.0.1-01160-QCAMSLSWPLZ-1
- ath11k: QCN9074 hw1.0: update to WLAN.HK.2.7.0.1-01744-QCAHKSWPL_SILICONZ-1
- ath11k: IPQ8074 hw2.0: update to WLAN.HK.2.7.0.1-01744-QCAHKSWPL_SILICONZ-1
- ath11k: IPQ8074 hw2.0: update board-2.bin
- ath11k: IPQ6018 hw1.0: update to WLAN.HK.2.7.0.1-01744-QCAHKSWPL_SILICONZ-1
- ath11k: IPQ6018 hw1.0: update board-2.bin
- ath10k: QCA99X0 hw2.0: update board-2.bin
- ath10k: QCA9984 hw1.0: update board-2.bin
- ath10k: QCA9888 hw2.0: update board-2.bin
- ath10k: QCA6174 hw3.0: update board-2.bin
- ath10k: QCA4019 hw1.0: update board-2.bin

* Thu Apr 6 2023 Jan Stancek <jstancek@redhat.com> - 20230404-134
- Update to upstream 20230404 release (rhbz 2183603).
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- nvidia: update Tu10x and Tu11x signed firmware to support newer Turing HW
- linux-firmware: update firmware for MT7922 WiFi device
- linux-firmware: update firmware for mediatek bluetooth chip (MT7922)
- linux-firmware: Amphion: Update vpu firmware
- iwlwifi: add new FWs from core78-32 release
- iwlwifi: update 9000-family firmwares to core78-32
- amdgpu: Update SDMA 6.0.1 firmware
- amdgpu: Add PSP 13.0.11 firmware
- amdgpu: Update PSP 13.0.4 firmware
- amdgpu: Update GC 11.0.1 firmware
- amdgpu: Update DCN 3.1.4 firmware
- amdgpu: Add GC 11.0.4 firmware
- rtw88: 8822c: Update normal firmware to v9.9.15
- linux-firmware: Update firmware file for Intel Bluetooth AX101
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth AX203
- linux-firmware: Update firmware file for Intel Bluetooth AX203
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX210
- linux-firmware: add firmware files for NXP BT chipsets
- rtw89: 8852b: update format-1 fw to v0.29.29.0
- rtw89: 8852b: add format-1 fw v0.29.26.0
- rtw89: 8852b: rollback firmware to v0.27.32.1
- i915: Update MTL DMC to v2.12
- i915: Update ADLP DMC to v2.19
- mediatek: Update mt8192/mt8195 SCP firmware to support MM21 and MT21
- iwlwifi: update core69 and core72 firmwares for So device

* Mon Mar 13 2023 Herton R. Krzesinski <herton@redhat.com> - 20230310-133
- Removed notices and check about the liquidio/lio_23xx_vsw.bin file: starting
  with 20230310 release of linux-firmware, it was removed upstream as well.
- Update to upstream 20230310 release (rhbz 2029566).
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- qat: update licence text
- rtl_bt: Update RTL8822C BT USB firmware to 0x0CC6_D2E3
- rtl_bt: Update RTL8822C BT UART firmware to 0x05C6_D2E3
- WHENCE: remove duplicate File entries
- WHENCE: remove trailing white space
- linux-firmware: add fw for qat_4xxx
- Fix symlinks for Intel firmware
- linux-firmware: update firmware for mediatek bluetooth chip (MT7921)
- linux-firmware: update firmware for MT7921 WiFi device
- iwlwifi: update core69 and core72 firmwares for Ty device
- rtlwifi: Add firmware v16.0 for RTL8710BU aka RTL8188GU
- brcm: Add nvram for the Lenovo Yoga Book X90F / X90L convertible
- brcm: Fix Xiaomi Inc Mipad2 nvram/.txt file macaddr
- brcm: Add nvram for the Advantech MICA-071 tablet
- rtl_bt: Update RTL8852C BT USB firmware to 0xD7B8_FABF
- rtl_bt: Add firmware and config files for RTL8821CS
- rtw89: 8852b: update fw to v0.29.29.0
- rtw89: 8852b: update fw to v0.29.26.0
- liquidio: remove lio_23xx_vsw.bin
- intel: avs: Add AudioDSP base firmware for CNL-based platforms
- intel: avs: Add AudioDSP base firmware for APL-based platforms
- intel: avs: Add AudioDSP base firmware for SKL-based platforms
- ath11k: WCN6855 hw2.0: update to WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.23
- ath11k: WCN6855 hw2.0: update board-2.bin
- ath11k: WCN6750 hw1.0: update board-2.bin
- ath11k: IPQ5018 hw1.0: add to WLAN.HK.2.6.0.1-00861-QCAHKSWPL_SILICONZ-1
- ath11k: IPQ5018 hw1.0: add board-2.bin
- ath10k: QCA6174 hw3.0: update firmware-sdio-6.bin to version WLAN.RMH.4.4.1-00174
- ath10k: WCN3990 hw1.0: update board-2.bin
- cnm: update chips&media wave521c firmware.
- amdgpu: Update GC 11.0.1 firmware
- intel: catpt: Add AudioDSP base firmware for BDW platforms

* Thu Feb 16 2023 Herton R. Krzesinski <herton@redhat.com> - 20230210-132
- Update ath10k/ath11k firmware (rhbz 2169013):
  ath11k: WCN6855 hw2.0: update to WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.23
  ath11k: WCN6855 hw2.0: update board-2.bin
  ath11k: WCN6750 hw1.0: update board-2.bin
  ath11k: IPQ5018 hw1.0: add to WLAN.HK.2.6.0.1-00861-QCAHKSWPL_SILICONZ-1
  ath11k: IPQ5018 hw1.0: add board-2.bin
  ath10k: QCA6174 hw3.0: update firmware-sdio-6.bin to version WLAN.RMH.4.4.1-00174
  ath10k: WCN3990 hw1.0: update board-2.bin
- Ship new firmware files using patch/git apply instead of as rpm sources.

* Tue Feb 14 2023 Herton R. Krzesinski <herton@redhat.com> - 20230210-131
- Update amdgpu/gc_11_0_1_rlc.bin file from the following linux-firmware commit:
  commit c0a0bc2 - amdgpu: Update GC 11.0.1 firmware (rhbz 2047462).

* Mon Feb 13 2023 Herton R. Krzesinski <herton@redhat.com> - 20230210-130
- Update to upstream 20230210 release (rhbz 2047488).
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- linux-firmware: Update AMD cpu microcode
- brcm: revert firmware files for Cypress devices
- brcm: restore previous firmware file for BCM4329 device
- rtw88: 8822c: Update normal firmware to v9.9.14
- i915: Add DMC v2.11 for MTL
- linux-firmware: Add firmware for Cirrus CS35L41 on UM3402 ASUS Laptop
- linux-firmware: Add missing tuning files for HP Laptops using Cirrus Amps
- i915: Add DMC v2.18 for ADLP
- amdgpu: Add VCN 4.0.2 firmware
- amdgpu: Add PSP 13.0.4 firmware
- amdgpu: Add SDMA 6.0.1 fimware
- amdgpu: Add GC 11.0.1 firmware
- amdgpu: Add DCN 3.1.4 firmware
- iwlwifi: remove old intermediate 5.15+ firmwares
- iwlwifi: remove 5.10 and 5.15 intermediate old firmwares
- iwlwifi: remove 5.4 and 5.10 intermediate old firmwares
- iwlwifi: remove 4.19 and 5.4 intermediate old firmwares
- iwlwifi: remove old unsupported older than 4.14 LTS
- linux-firmware: update firmware for MT7921 WiFi device
- linux-firmware: update firmware for mediatek bluetooth chip (MT7921)
- amdgpu: update vangogh firmware
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX210
- linux-firmware: Update firmware file for Intel Bluetooth AX200
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth 9260
- brcm: add configuration files for CyberTan WC121
- qcom: add firmware files for Adreno A200
- rtw89: 8852c: update fw to v0.27.56.10
- QCA: Add Bluetooth firmware for QCA2066
- amdgpu: add VCN4.0.4 firmware from amd-5.4
- amdgpu: add SMU13.0.7 firmware from amd-5.4
- amdgpu: add SDMA6.0.2 firmware from amd-5.4
- amdgpu: add PSP13.0.7 firmware from amd-5.4
- amdgpu: add GC11.0.2 firmware from amd-5.4
- amdgpu: add DCN3.2.1 firmware from amd-5.4
- amdgpu: update VCN4.0.0 firmware from amd-5.4
- amdgpu: update SMU13.0.0 firmware from amd-5.4
- amdgpu: update SDMA6.0.0 firmware from amd-5.4
- amdgpu: update PSP13.0.0 firmware from amd-5.4
- amdgpu: update GC11.0.0 firmware from amd-5.4
- iwlwifi: add new FWs from core76-35 release
- iwlwifi: update cc/Qu/QuZ firmwares for core76-35 release
- iwlwifi: add new FWs from core75-47 release
- iwlwifi: update 9000-family firmwares to core75-47
- amdgpu: update renoir DMCUB firmware
- amdgpu: Update renoir PSP firmware
- amdgpu: update copyright date for LICENSE.amdgpu
- linux-firmware: update firmware for MT7921 WiFi device
- linux-firmware: update firmware for MT7922 WiFi device
- linux-firmware: update firmware for mediatek bluetooth chip (MT7922)
- cxgb4: Update firmware to revision 1.27.1.0
- qca: Update firmware files for BT chip WCN6750
- rtw89: 8852c: update fw to v0.27.56.9
- rtw89: 8852c: update fw to v0.27.56.8

* Thu Dec 15 2022 Herton R. Krzesinski <herton@redhat.com> - 20221214-129
- Update to upstream 20221012 release (rhbz 2153045, 2047484).
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- amdgpu: updated navi10 firmware for amd-5.4
- amdgpu: updated yellow carp firmware for amd-5.4
- amdgpu: updated raven2 firmware for amd-5.4
- amdgpu: updated raven firmware for amd-5.4
- amdgpu: updated PSP 13.0.8 firmware for amd-5.4
- amdgpu: updated GC 10.3.7 RLC firmware for amd-5.4
- amdgpu: updated vega20 firmware for amd-5.4
- amdgpu: updated PSP 13.0.5 firmware for amd-5.4
- amdgpu: add VCN 4.0.0 firmware for amd-5.4
- amdgpu: add SMU 13.0.0 firmware for amd-5.4
- amdgpu: Add SDMA 6.0.0 firmware for amd-5.4
- amdgpu: add PSP 13.0.0 firmware for amd-5.4
- amdgpu: add GC 11.0.0 firmware for amd-5.4
- amdgpu: add DCN 3.2.0 firmware for amd-5.4
- amdgpu: updated vega10 firmware for amd-5.4
- amdgpu: updated beige goby firmware for amd-5.4
- amdgpu: updated dimgrey cavefish firmware for amd-5.4
- amdgpu: updated vangogh firmware for amd-5.4
- amdgpu: updated picasso firmware for amd-5.4
- amdgpu: updated navy flounder firmware for amd-5.4
- amdgpu: updated green sardine firmware for amd-5.4
- amdgpu: updated sienna cichlid firmware for amd-5.4
- amdgpu: updated arcture firmware for amd-5.4
- amdgpu: updated navi14 firmware for amd-5.4
- amdgpu: updated renoir firmware for amd-5.4
- amdgpu: updated navi12 firmware for amd-5.4
- amdgpu: updated aldebaran firmware for amd-5.4
- sr150 : Add NXP SR150 UWB firmware
- brcm: add/update firmware files for brcmfmac driver
- rtl_bt: Update RTL8821C BT(USB I/F) FW to 0x75b8_f098
- amdgpu: update sdma_5.2.7 firmware
- QCA: Add Bluetooth firmware for WCN785x This adds required Bluetooth firmware
  files for QCA WCN785x. The image version is 2.0.0-00515.
- linux-firmware: update firmware for MT7916
- linux-firmware: update firmware for MT7915
- i915: Add DMC v2.08 for DG2
- amdgpu: update green sardine DMCUB firmware
- i915: Add DMC v2.10 for MTL
- linux-firmware: update firmware for MT7986
- linux-firmware: update firmware for mediatek bluetooth chip (MT7921)
- linux-firmware: update firmware for MT7921 WiFi device
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX210
- linux-firmware: Update firmware file for Intel Bluetooth AX200
- amdgpu: update DMCUB firmware for DCN 3.1.6
- rtl_bt: Update RTL8822C BT UART firmware to 0xFFB8_ABD6
- rtl_bt: Update RTL8822C BT USB firmware to 0xFFB8_ABD3
- WHENCE: mrvl: prestera: Add WHENCE entries for newly updated 4.1 FW images
- mrvl: prestera: Update Marvell Prestera Switchdev FW to v4.1
- iwlwifi: add new FWs from core74_pv-60 release
- qcom: drop split a530_zap firmware file
- qcom/vpu-1.0: drop split firmware in favour of the mbn file
- qcom/venus-4.2: drop split firmware in favour of the mbn file
- qcom/venus-4.2: replace split firmware with the mbn file
- qcom/venus-1.8: replace split firmware with the mbn file
- linux-firmware: Add firmware for Cirrus CS35L41 on new ASUS Laptop
- iwlwifi: add new PNVM binaries from core74-44 release
- iwlwifi: add new FWs from core69-81 release
- qcom: update venus firmware files for VPU-2.0
- qcom: remove split SC7280 venus firmware images
- qcom: update venus firmware file for v5.4
- qcom: replace split SC7180 venus firmware images with symlink
- rtw89: 8852b: update fw to v0.27.32.1
- rtlwifi: update firmware for rtl8192eu to v35.7
- rtlwifi: Add firmware v4.0 for RTL8188FU
- i915: Add HuC 7.10.3 for DG2
- cnm: update chips&media wave521c firmware.
- brcm: add symlink for Pi Zero 2 W NVRAM file
- linux-firmware: Add firmware for Cirrus CS35L41 on ASUS Laptops
- linux-firmware: Add firmware for Cirrus CS35L41 on Lenovo Laptops
- linux-firmware: Add firmware for Cirrus CS35L41 on HP Laptops
- rtw89: 8852b: add initial fw v0.27.32.0
- iwlwifi: add new FWs from core72-129 release
- iwlwifi: update 9000-family firmwares to core72-129

* Wed Oct 26 2022 Frantisek Hrbata <fhrbata@redhat.com> - 20221012-128
- Update to upstream 20221012 release (rhbz 2121447).
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- rtl_bt: Update RTL8852C BT USB firmware to 0xD5B8_A40A
- amdgpu: update GC 10.3.6 RLC firmware
- amdgpu: update GC 10.3.7 RLC firmware
- amdgpu: update Yellow Carp RLC firmware
- amdgpu: update Beige Goby RLC firmware
- amdgpu: update Dimgrey Cavefish RLC firmware
- amdgpu: update Navy Flounder RLC firmware
- amdgpu: update Sienna Cichlid RLC firmware
- mediatek: Update mt8195 SOF firmware to v0.4.1
- qcom: add squashed version of a530 zap shader
- rtw89: 8852c: update fw to v0.27.56.1
- rtw89: 8852c: update fw to v0.27.56.0
- mediatek: Update mt8186 SCP firmware
- linux-firmware: Update AMD cpu microcode
- mediatek: mt8195: Update scp.img to v2.0.11956
- mediatek: Add new mt8195 SOF firmware
- mediatek: Update mt8186 SOF firmware to v0.2.1
- linux-firmware: update firmware for mediatek bluetooth chip (MT7922)
- rtl_bt: Update RTL8852A BT USB firmware to 0xD9B8_8207
- linux-firmware: update firmware for mediatek bluetooth chip (MT7921)
- linux-firmware: update firmware for MT7922 WiFi device
- linux-firmware: update firmware for MT7921 WiFi device
- cxgb4: Update firmware to revision 1.27.0.0
- i915: Add versionless HuC files for current platforms
- i915: Add GuC v70.5.1 for DG1, DG2, TGL and ADL-P
- qca: Update firmware files for BT chip WCN3991.
- Removing crnv32
- amdgpu: update yellow carp DMCUB firmware
- amdgpu: add firmware for VCN 3.1.2 IP block
- amdgpu: add firmware for SDMA 5.2.6 IP block
- amdgpu: add firmware for PSP 13.0.5 IP block
- amdgpu: add firmware for GC 10.3.6 IP block
- amdgpu: add firmware for DCN 3.1.5 IP block
- qcom: rename Lenovo ThinkPad X13s firmware paths
- rtw89: 8852c: update fw to v0.27.42.0
- rtw89: 8852c: update fw to v0.27.36.0
- Mellanox: Add new mlxsw_spectrum firmware xx.2010.3146
- amdgpu: update beige goby VCN firmware
- amdgpu: update dimgrey cavefish VCN firmware
- amdgpu: update navy flounder VCN firmware
- amdgpu: update sienna cichlid VCN firmware
- rtl_bt: Update RTL8852C BT USB firmware to 0xDFB8_5A33
- mediatek: reference the LICENCE file for MediaTek firmwares
- mediatek: Add new mt8186 SOF firmware
- ice: Update package to 1.3.30.0
- QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00438
- brcm: Add nvram for Lenovo Yoga Tablet 2 830F/L and 1050F/L tablets
- brcm: Add nvram for the Xiaomi Mi Pad 2 tablet
- brcm: Add nvram for the Asus TF103C tablet
- Add amd-ucode README file
- qca: Update firmware files for BT chip WCN6750.      This commit will update required firmware files for WCN6750.
- amdgpu: Update Yellow Carp VCN firmware
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX210
- linux-firmware: Update firmware file for Intel Bluetooth AX200
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- Mellanox: Add new mlxsw_spectrum firmware xx.2010.3020
- qcom: Add firmware for Lenovo ThinkPad X13s
- linux-firmware: Add firmware for Cirrus CS35L41
- i915: Add GuC v70.4.1 for DG2
- i915: Add DMC v2.07 for DG2
- amdgpu partially revert "amdgpu: update beige goby to release 22.20"
- mediatek: Update mt8183/mt8192/mt8195 SCP firmware
- amdgpu: update renoir to release 22.20
- amdgpu: update beige goby to release 22.20
- amdgpu: update yellow carp to release 22.20
- amdgpu: update dimgrey cavefish to release 22.20
- amdgpu: update vega20 to release 22.20
- amdgpu: update vega12 to release 22.20
- amdgpu: update raven to release 22.20
- amdgpu: update navy flounder to release 22.20
- amdgpu: update vega10 to release 22.20
- amdgpu: update sienna cichlid to release 22.20
- amdgpu: update navi14 to release 22.20
- amdgpu: update green sardine to release 22.20
- amdgpu: update vangogh to release 22.20
- amdgpu: update navi12 to release 22.20
- amdgpu: update navi10 to release 22.20
- amdgpu: update picasso to release 22.20
- amdgpu: update aldebaran to release 22.20
- amdgpu: update psp 13.0.8 TA firmware
- WHENCE: Fix the dangling symlinks fix
- amdgpu: update DMCUB firmware for DCN 3.1.6
- WHENCE: Correct dangling symlinks

* Mon Jul 11 2022 Patrick Talbert <ptalbert@redhat.com> - 20220708-127
- Update compressed firmware support patch for upstream changes
- Update to upstream 20220708 release (rhbz 2040281, 2045911, 2105392).
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- Correct WHENCE entry for wfx firmware
- bnx2: Drop unsupported Broadcom NetXtremeII firmware
- bnx2: drop unsupported firmwares
- bnx2: sort firmware names in filesystem order
- Remove old Broadcom Everest (bnx2x) v4/5 firmware
- drop Token Ring network firmwares
- Drop TDA7706 radio firmware
- Drop Intel WiMax firmware
- Drop Computone IntelliPort Plus serial firmware
- Drop ATM Ambassador devices firmware
- brocade: drop old unsupported firmware revs
- amdgpu: update yellow carp DMCUB firmware
- linux-firmware: update firmware for MT7622 WiFi device
- linux-firmware: update firmware for MT7922 WiFi device
- linux-firmware: update firmware for mediatek bluetooth chip (MT7922)
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX210
- linux-firmware: Update firmware file for Intel Bluetooth AX200
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- mediatek: Add SCP firmware for MT8186
- rtw88: 8822c: Update normal firmware to v9.9.13
- rtw88: 8822c: Update normal firmware to v9.9.12
- amdgpu: update Yellow Carp VCN firmware
- linux-firmware: update firmware for MT7921 WiFi device
- linux-firmware: update firmware for mediatek bluetooth chip (MT7921)
- qed: update 8.59.1.0 firmware
- Link some devices that ship with the AW-CM256SM
- Add initial AzureWave AW-CM256SM NVRAM file
- Remove the Pine64 Quartz copy of the RPi NVRAM
- qca: Update firmware files for BT chip WCN6750.
- QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00409
- WHENCE: add symlinks for StarFive based boards
- linux-firmware: wilc1000: update WILC1000 firmware to v15.6
- brcm: Add NVRAM file 43455 based Wifi/BT module as used on the Quartz64 Model B from Pine64. This file is based on the existing "brcm/brcmfmac43455-sdio.raspberrypi,4-model-b.txt" NVRAM file.
- iwlwifi: add new FWs from core70-87 release
- iwlwifi: update 9000-family firmwares to core70-87
- rtl_bt: Update RTL8852A BT USB firmware to 0xDFB8_0634
- Makefile: replace mkdir by install
- iwlwifi: remove old unsupported 3160/7260/7265/8000/8265 firmware
- ath11k: WCN6855 hw2.0: update to WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.9
- WHENCE: ath11k: move regdb.bin before board-2.bin
- ath10k: QCA9984 hw1.0: update firmware-5.bin to 10.4-3.9.0.2-00157
- ath10k: QCA9888 hw2.0: update board-2.bin
- ath10k: QCA9888 hw2.0: update firmware-5.bin to 10.4-3.9.0.2-00157
- ath10k: QCA4019 hw1.0: update board-2.bin
- ath10k: WCN3990 hw1.0: add board-2.bin
- amdgpu: update beige goby firmware for 22.10
- amdgpu: update renoir firmware for 22.10
- amdgpu: update dimgrey cavefish firmware for 22.10
- amdgpu: update vega20 firmware for 22.10
- amdgpu: update yellow carp firmware for 22.10
- amdgpu: update vega12 firmware for 22.10
- amdgpu: update navy flounder firmware for 22.10
- amdgpu: update vega10 firmware for 22.10
- amdgpu: update raven2 firmware for 22.10
- amdgpu: update raven firmware for 22.10
- amdgpu: update sienna cichlid firmware for 22.10
- amdgpu: update green sardine firmware for 22.10
- amdgpu: update PCO firmware for 22.10
- amdgpu: update vangogh firmware for 22.10
- amdgpu: update navi14 firmware for 22.10
- amdgpu: update navi12 firmware for 22.10
- amdgpu: update navi10 firmware for 22.10
- amdgpu: update aldebaran firmware for 22.10
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX210
- linux-firmware: Update firmware file for Intel Bluetooth AX200
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- mediatek: Update mt8192 SCP firmware

* Wed May 11 2022 Patrick Talbert <ptalbert@redhat.com> - 20220509-126
- Update to upstream 20220509 release (rhbz 2081548, 2081550, 2068137).
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- mediatek: Update mt8183 SCP firmware
- ice: Update package to 1.3.28.0
- i915: Add DMC v2.06 for DG2
- rtl_bt: Update RTL8852A BT USB firmware to 0xDBB7_C1D9
- amdgpu: update psp_13_0_8 firmware
- amdgpu: update gc_10_3_7_rlc firmware
- amdgpu: update dcn_3_1_6_dmcub firmware
- ath11k: QCA6390 hw2.0: update to WLAN.HST.1.0.1-05266-QCAHSTSWPLZ_V2_TO_X86-1
- qcom: add firmware files for Adreno a420 & related generations
- qcom: add firmware files for Adreno a330
- qcom: add firmware files for Adreno a220
- i915: Add GuC v70.1.2 for DG2
- rtw89: 8852c: add new firmware v0.27.20.0 for RTL8852C
- Mellanox: Add lc_ini_bundle for xx.2010.1006
- Mellanox: xx.2010.1502: Distribute non-xz-compressed lc_ini_bundle
- ath10k: QCA9984 hw1.0: update board-2.bin
- ath10k: QCA9984 hw1.0: update firmware-5.bin to 10.4-3.9.0.2-00156
- ath10k: QCA9888 hw2.0: update board-2.bin
- ath10k: QCA9888 hw2.0: update firmware-5.bin to 10.4-3.9.0.2-00156
- ath10k: QCA6174 hw3.0: update board-2.bin
- ath10k: QCA6174 hw3.0: update firmware-6.bin to WLAN.RM.4.4.1-00288-QCARMSWPZ-1
- ath10k: QCA4019 hw1.0: update board-2.bin
- ath10k: QCA99X0 hw2.0: add board-2.bin
- ath11k: WCN6855 hw2.0: update to WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.7
- ath11k: WCN6750 hw1.0: add to WLAN.MSL.1.0.1-00887-QCAMSLSWPLZ-1
- ath11k: WCN6750 hw1.0: add board-2.bin
- ath11k: QCN9074 hw1.0: add to WLAN.HK.2.5.0.1-01208-QCAHKSWPL_SILICONZ-1
- ath11k: QCN9074 hw1.0: add board-2.bin
- ath11k: QCA6390 hw2.0: update board-2.bin
- ath11k: IPQ8074 hw2.0: update to WLAN.HK.2.5.0.1-01208-QCAHKSWPL_SILICONZ-1
- ath11k: IPQ8074 hw2.0: update board-2.bin
- ath11k: IPQ6018 hw1.0: update to WLAN.HK.2.5.0.1-01208-QCAHKSWPL_SILICONZ-1
- ath11k: IPQ6018 hw1.0: update board-2.bin
- Mellanox: Add new mlxsw_spectrum firmware xx.2010.1502
- amdgpu: update yellow carp DMCUB firmware
- linux-firmware: update firmware for mediatek bluetooth chip (MT7922)
- linux-firmware: update firmware for MT7922 WiFi device
- mediatek: Add mt8195 SCP firmware
- qcom: apq8096: add modem firmware
- qcom: apq8096: add aDSP firmware
- rtl_bt: Add firmware and config files for RTL8852C
- mediatek: Add mt8192 SCP firmware
- linux-firmware: Update AMD cpu microcode
- nvidia: add GA102/GA103/GA104/GA106/GA107 signed firmware
- brcm: rename Rock960 NVRAM to AP6356S and link devices to it
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX210
- linux-firmware: Update firmware file for Intel Bluetooth AX200
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth 9260
- amdgpu: update green sardine VCN firmware
- amdgpu: update renoir VCN firmware
- amdgpu: update navi14 VCN firmware
- amdgpu: update navi12 VCN firmware
- amdgpu: update navi10 VCN firmware
- linux-firmware: update firmware for MT7921 WiFi device
- linux-firmware: update firmware for mediatek bluetooth chip (MT7921)
- i915: Add GuC v70.1.1 for all platforms
- rtw88: 8821c: Update normal firmware to v24.11.00
- ice: Add wireless edge file for Intel E800 series driver
- ice: update ice DDP comms package to 1.3.31.0
- amdgpu: update PSP 13.0.8 firmware
- amdgpu: update GC 10.3.7 firmware
- rtl_bt: Add firmware and config files for RTL8852B
- iwlwifi: add new FWs from core68-60 release
- ath11k: add links for WCN6855 hw2.1
- ath11k: WCN6855 hw2.0: add WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3
- ath11k: WCN6855 hw2.0: add board-2.bin and regdb.bin
- ath10k/ath11k: mark notice.txt as "File:"
- linux-firmware: add firmware for MT7986
- amdgpu: add firmware for SDMA 5.2.7 IP block
- amdgpu: add firmware for PSP 13.0.8 IP block
- amdgpu: add firmware for DCN 3.1.6 IP block
- amdgpu: add firmware for GC 10.3.7 IP block
- rtw89: 8852a: update fw to v0.13.36.0
- iwlwifi: update 9000-family firmwares to core68-60
- amdgpu: update raven2 VCN firmware
- amdgpu: update raven VCN firmware
- amdgpu: update picasso VCN firmware
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9462
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX211
- linux-firmware: Update firmware file for Intel Bluetooth AX210
- linux-firmware: Update firmware file for Intel Bluetooth AX200
- linux-firmware: Update firmware file for Intel Bluetooth AX201
- linux-firmware: Update firmware file for Intel Bluetooth 9560
- linux-firmware: Update firmware file for Intel Bluetooth 9260
- linux-firmware: Update AMD SEV firmware
- rtw89: 8852a: update fw to v0.13.35.0
- Mellanox: Add new mlxsw_spectrum firmware xx.2010.1406
- wfx: update to firmware 3.14
- wfx: add antenna configuration files
- wfx: rename silabs/ into wfx/
- linux-firmware: update firmware for mediatek bluetooth chip(MT7921)
- linux-firmware: Update firmware patch for Intel Bluetooth 8260
- linux-firmware: Update firmware file for Intel Bluetooth 8265
- linux-firmware: Intel BT 7265: Fix Security Issues
- rtl_bt: Update RTL8852A BT USB firmware to 0xDFB7_6D7A
- rtl_bt: Update RTL8822C BT USB firmware to 0x19B7_6D7D
- rtl_bt: Update RTL8822C BT UART firmware to 0x15B7_6D7D
- amdgpu: Update yellow carp firmware from 21.50
- amdgpu: Update vega20 firmware from 21.50
- amdgpu: Update vega12 firmware from 21.50
- amdgpu: Update vega10 firmware from 21.50
- amdgpu: Update vangogh firmware from 21.50
- amdgpu: Update renoir firmware from 21.50
- amdgpu: Update raven2 firmware from 21.50
- amdgpu: Update raven firmware from 21.50
- amdgpu: Update picasso firmware from 21.50
- amdgpu: Update beige goby firmware from 21.50
- amdgpu: Update dimgrey cavefish firmware from 21.50
- amdgpu: Update navy flounder firmware from 21.50
- amdgpu: Update sienna cichlid firmware from 21.50
- amdgpu: Update navi14 firmware from 21.50
- amdgpu: Update navi12 firmware from 21.50
- amdgpu: Update navi10 firmware from 21.50
- amdgpu: Update cyan skillfish2 firmware from 21.50
- amdgpu: Update green sardine firmware from 21.50
- amdgpu: Update arcturus firmware from 21.50
- amdgpu: Add aldebaran firmware from 21.50
- LICENSE.amdgpu: update copyright date
- linux-firmware: Update AMD cpu microcode
- linux-firmware: update firmware for MT7921 WiFi device

* Thu Feb 10 2022 Herton R. Krzesinski <herton@redhat.com> - 20220209-125
- Update to upstream 20220209 release (rhbz 1967151, 2031174). Changes
  since the last update are noted on items below, copied from the git
  changelog of upstream linux-firmware repository
- Amphion: Add VPU firmwares for NXP i.MX8Q SoCs
- i915: Add DMC firmware v2.16 for ADL-P
- mediatek: Update MT8173 VPU firmware to v1.1.7
- Update firmware file for Intel Bluetooth 9260
- Update firmware file for Intel Bluetooth 9462
- Update firmware file for Intel Bluetooth 9560
- Update firmware file for Intel Bluetooth AX201
- Update firmware file for Intel Bluetooth AX211
- Update firmware file for Intel Bluetooth AX210
- Update firmware file for Intel Bluetooth AX200
- update firmware for mediatek bluetooth chip (MT7921)
- update firmware for MT7921 WiFi device
- Mellanox: Add new mlxsw_spectrum firmware xx.2010.1232
- add marvell CPT firmware images
- update firmware for MT7915
- iwlwifi: add new FWs from core63-136 release
- iwlwifi: add new FWs from core66-88 release
- iwlwifi: update 9000-family firmwares to core66-88
- add firmware for MT7916
- Update firmware file for Intel Bluetooth 9462
- WHENCE: add missing symlink for NanoPi R1
- amdgpu: update yellow carp dmcub firmware
- QCA: Add Bluetooth nvm file for WCN685x
- QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00324
- QCA: Update Bluetooth WCN685x 2.0 firmware to 2.0.0-00609
- cxgb4: Update firmware to revision 1.26.6.0
- cnm: add chips&media wave521c firmware
- rtw88: 8822c: Update normal firmware to v9.9.11
- i915: Add GuC v69.0.3 for all platforms
- rtw89: 8852a: update fw to v0.13.33.0

* Thu Jan 13 2022 Herton R. Krzesinski <herton@redhat.com> - 20211216-124
- Update to upstream 20211216 release (rhbz 2035777). Changes since the
  last update are noted on items below, copied from the git changelog
  of upstream linux-firmware repository
- amdgpu: update green sardine PSP firmware
- bnx2x: Add FW 7.13.21.0
- wilc1000: update WILC1000 firmware to v15.4.1
- rtl_bt: Update RTL8761B BT UART firmware to 0x0CA9_8A6B
- rtl_bt: Update RTL8761B BT USB firmware to 0x09A9_8A6B
- cxgb4: Update firmware to revision 1.26.4.0
- i915: Add DMC firmware v2.14 for ADL-P
- Update firmware file for Intel Bluetooth 9462
- Update firmware file for Intel Bluetooth AX211
- Update firmware file for Intel Bluetooth AX210
- Update firmware file for Intel Bluetooth 9560
- Update firmware file for Intel Bluetooth 9260
- Update firmware file for Intel Bluetooth AX200
- Update firmware file for Intel Bluetooth AX201
- amdgpu: update yellow carp dmcub firmware
- amdgpu: update vangogh DMCUB firmware
- QCA: Add Bluetooth default nvm file for WCN685x
- Update ath10k/QCA6174/hw3.0/board-2.bin
- mrvl: prestera: Update Marvell Prestera Switchdev v4.0
- QCA: Add Bluetooth firmware for WCN685x
- Update AMD cpu microcode
- amdgpu: update raven2 firmware from 21.40
- amdgpu: update navi14 firmware from 21.40
- amdgpu: update raven firmware from 21.40
- amdgpu: update navi12 firmware from 21.40
- amdgpu: update navi10 firmware from 21.40
- amdgpu: update vega20 firmware from 21.40
- amdgpu: update vega12 firmware from 21.40
- amdgpu: update vega10 firmware from 21.40
- amdgpu: update picasso firmware from 21.40
- amdgpu: update vangogh firmware from 21.40
- amdgpu: update beige goby firmware from 21.40
- amdgpu: add cyan skillfish firmware from 21.40
- amdgpu: update dimgrey cavefish firmware from 21.40
- amdgpu: update green sardine firmware from 21.40
- amdgpu: update navy flounder firmware from 21.40
- amdgpu: update renoir firmware from 21.40
- amdgpu: update arcturus firmware from 21.40
- amdgpu: update sienna cichlid firmware from 21.40
- rtl_bt: Update RTL8852A BT USB firmware to 0xDBA9_6937
- iwlwifi: add new FWs from core64-96 release
- iwlwifi: update 9000-family firmwares to core64-96
- amdgpu: update VCN firmware for green sardine
- update firmware for mediatek bluetooth chip (MT7921)

* Fri Nov 12 2021 Herton R. Krzesinski <herton@redhat.com> - 20211027-123
- Update to upstream 20211027 release (rhbz 1986659). Changes since the
  last update are noted on items below, copied from the git changelog
  of upstream linux-firmware repository
- Update AMD cpu microcode
- QCA: Update Bluetooth firmware for WCN685x
- bnx2x: Add FW 7.13.20.0
- Mellanox: Add new mlxsw_spectrum firmware xx.2010.1006
- Update NXP Management Complex firmware to version 10.28.1
- Update firmware for MT7921 WiFi device
- rtw89: 8852a: update fw to v0.13.30.0
- Update firmware file for Intel Bluetooth 9462
- Update firmware file for Intel Bluetooth 9560
- Update firmware file for Intel Bluetooth AX201
- Update firmware file for Intel Bluetooth AX211
- Update firmware file for Intel Bluetooth AX210
- Update firmware file for Intel Bluetooth 9260
- Update firmware file for Intel Bluetooth AX200
- brcm: Add 43455 based AP6255 NVRAM for the ACEPC T8 Mini PC
- amdgpu: update VCN firmware for dimgrey cavefish
- amdgpu: update VCN firmware for navy flounder
- amdgpu: update VCN firmware for sienna cichlid
- amdgpu: update VCN firmware for vangogh
- amdgpu: update VCN firmware for renoir
- amdgpu: update VCN firmware for picasso
- amdgpu: update VCN firmware for raven2
- amdgpu: update VCN firmware for raven
- amdgpu: Add initial firmware for Beige Goby
- cxgb4: Update firmware to revision 1.26.2.0
- Update frimware for mediatek bluetooth chip (MT7921)
- i915: Update ADLP DMC v2.12

* Tue Sep 28 2021 Herton R. Krzesinski <herton@redhat.com> - 20210919-122
- Update to upstream 20210919 release (rhbz 1979806). Changes since the
  last update are noted on items below, copied from the git changelog
  of upstream linux-firmware repository
- qed: Add firmware 8.59.1.0
- Update firmware file for Intel Bluetooth AX211/AX210/AX200/AX201
- Update firmware file for Intel Bluetooth 9560/9260/8265
- iwlwifi: add FWs for new So device types with multiple RF modules
- amdgpu: add initial firmware for Yellow Carp
- Add firmware for mediatek bluetooth chip (MT7922)
- Update AMD SEV firmware
- Update firmware for mediatek bluetooth chip (MT7921)
- Update RTL8852A BT USB firmware to 0xD9A9_1D69
- Update RTL8822C BT UART firmware to 0x05A9_1A4A
- Update RTL8822C BT USB firmware to 0x09A9_1A4A
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.3326
- Update firmware of RTL8153C
- ice: update package file to 1.3.26.0
- amdgpu: revert back to older raven2/raven/picasso sdma firmware
- amdgpu: add initial vangogh support
- amdgpu: update vega20/vega12/vega10/renoir/raven2/raven firmware from 21.30
- amdgpu: update polaris12/picasso/dimgrey cavefish/flounder firmware from 21.30
- amdgpu: update sienna cichlid/navi14/navi12/navi10 firmware from 21.30
- amdgpu: update green sardine/arcturus firmware from 21.30
- QCA: Updated firmware files for WCN3991
- i915: Add v2.03 DMC for RKL
- i915: Add v2.12 DMC for TGL
- qca: Add firmware files for BT chip WCN6750
- iwlwifi: add ty firmware from Core63-43

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 20210716-121.1
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Aug 05 2021 Herton R. Krzesinski <herton@redhat.com> - 20210716-121
- Update to upstream 20210716 release (rhbz 1984973, rhbz 1876310).
  What changed in this release is noted on items below, copied from Fedora's
  linux-firmware changelog done by Peter Robinson
- update NXP 8897/8997 firmware images
- rtlwifi: de-dupe rtl8723b/rtl8192e SDIO/USB WiFi firmware
- Mediatek: update WiFi/bluetooth chip (MT7921)
- Mediatek: update MT7915 firmware to 20201105
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.2946
- cxgb4: Update firmware to revision 1.26.0.0
- firmware/i915/guc: Add HuC v7.9.3 for TGL & DG1
- firmware/i915/guc: Add GuC v62.0.3 for ADL-P
- firmware/i915/guc: Add GuC v62.0.0 for all platforms
- nvidia: fix symlinks for tu104/tu106 acr unload firmware
- iwlwifi: new/updated 8000/9000/other from core60-51 release
- Update firmware file for Intel Bluetooth AX210/201/200
- rtw88: 8822c: Update normal firmware to v9.9.10
- rtl_bt: Update RTL8852A BT(UART I/F) FW to 0xD9A8_A0CD
- rtl_bt: Update RTL8822C BT(UART I/F) FW to 0x05A8_C6B4
- rtl_bt: Update RTL8822C BT(USB I/F) FW to 0x09A8_A0CB
- rtl_bt: Add rtl8761b/rtl8761bu firmware
- QCA: Update Bluetooth firmware for QCA6174/QCA6390
- QCA: Add Bluetooth firmware for WCN685x
- amdgpu: update 21.20 vcn firmware for green sardine, renoir, navi10/12/14
- amdgpu: add initial dimgrey cavefish firmware from 21.20
- amdgpu: updated 21.20 firmware for: Picasso, green sardine, arcturus
  vega10/12/20, navi10/12/14, raven1/2, renoir, navy flounder
- cypress: update firmware: cyw54591/cyw43570 pcie
- cypress: update firmware: cyw4373/cyw4356/cyw4354/cyw43455/cyw43430/cyw43340/cyw43012 sdio
- nvidia: Update Tegra194 XUSB firmware to v60.09
- nvidia: Update Tegra186 XUSB firmware to v55.18
- nvidia: Update Tegra210 XUSB firmware to v50.26
- nvidia: Add VIC firmware for Tegra194
- update firmware for cadence mhdp8546
- i915: Add ADL-P DMC Support
- qcom: add gpu firmwares for sc7280
- qcom: Add venus firmware files for VPU-2.0
- qcom: update venus firmware files for v5.4
- qcom: sm8250: update remoteproc firmware
- qcom: update a650 firmware files
- QCA: Update Bluetooth firmware for QCA6174
- WHENCE: link to similar config file for rtl8821a support
- rtw89: 8852a: update fw to v0.13.8.0
- rtw88: 8822c: Update normal firmware to v9.9.9
- rtl_bt: Update RTL8852A BT USB firmware to 0xD9A8_7893
- rtl_bt: Add rtl8723bs_config-OBDA0623.bin symlink
- rtl_bt: Update RTL8822C BT(UART I/F) FW to 0x59A_76A3
- rtl_nic: add new firmware for RTL8153 and RTL8156 series
- Intel: Update firmware for Intel Bluetooth AX210/201/200, 9560, 9260, 8265
- Intel BT 7265: Fix Security Issues
- mrvl: prestera: Add Marvell Prestera Switchdev firmware 3.0 version
- amdgpu: update GPU firmwares from 21.10
- amdgpu: add initial support for arcturus, navy flounder
- amdgpu: add new polaris 12 MC firmware
- amdgpu: update navi10/14 smc firmware
- cxgb4: Update firmware to revision 1.25.4.0
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.2438
- nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.14.A.6
- brcm: add missing symlink for Pi Zero W NVRAM file
- brcm: Add a link to enable khadas VIM2's WiFi
- brcm: Link CM4's WiFi firmware with DMI machine name.
- brcm: Add nvram for the Chuwi Hi8 (CWI509) tablet
- brcm: Add nvram for the Predia Basic tablet

* Thu May 27 2021 Herton R. Krzesinski <herton@redhat.com> - 20210315-120
- Remove liquidio/lio_23xx_vsw.bin due GPL violation (rhbz 1959913)

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 20210315-119.1
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Mar 15 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210315-119
- Update to upstream 20210315 release
- Update to Intel Bluetooth AX200/201 firmware
- rtw88: 8822c: Update normal firmware to v9.9.6
- rtw89: 8852a: add firmware v0.9.12.2
- iwlwifi: updates for 9000-family/7265D/core59-66 (cc, Qu, QuZ, ty)
- amdgpu: add initial firmware for green sardine
- Silabs new WF200 firmware
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.2406
- Added Mediatek bluetooth chip (MT7921)

* Mon Mar 08 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210208-118
- Fix for Raspberry Pi 4 WiFi

* Mon Feb  8 2021 Peter Robinson <pbrobinson@fedoraproject.org> 20210208-117
- Update to upstream 20210208 release
- rtl_bt: Updates for RTL8822C, RTL8821C, added RTL8852A
- Link Cypress brcmfmac firmwares to old brcm location
- brcm NVRAM updates for Raspberry Pi, added 96boards Rock960
- QCom SM8250 (SD865) firmware for Compute, Audio DSPs, Adreno a650, venus VPU-1.0
- i915: Added firmware for DG1, ADL-S
- Uodated bluetooth firmware for Intel Bluetooth AX200/201/210
- rtw88: RTL8821C: Update firmware to v24.8
- New MT7921 firmware
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.2304

* Sat Dec 19 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 20201218-116
- Update to upstream 20201218 release
- AMD gpu: Updates for vega10/12/20, renoir, navi10/12/14, raven1/2
- AMD gpuL add sienna cichlid
- Update AMD SEV firmware
- Add Mellanox mlxsw_spectrum xx.2008.2018 firmware
- i915: Add GuC firmware v49.0.1
- Intel bluetooth updates for AX200/201/210, 9560, 9260
- Add Lontium LT9611UXC DSI to HDMI bridge firmware
- Update QCA WCN3991 firmware
- Update mediatek MT8173 VPU firmware to v1.1.6

* Thu Nov 19 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 20201118-115
- Update to upstream 20201118 release
- rtw88: RTL8822C: Update firmware to v9.9.4
- amdgpu: update picasso/raven/raven2 VCN firmware
- rtl_bt: Update RTL8822C BT(USB I/F) FW to 0x099A_281A
- QCA: Update Bluetooth firmware for QCA6390
- qcom : updated venus firmware files for v5.4
- QCA : Fixed BT SSR due to command timeout / IO fatal error
- ath11k: Updated firmware for QCA6390/IPQ8074/IPQ6018
- ath10l: Updated firmware for QCA9984/QCA9888/QCA6174

* Thu Nov 19 2020 Dave Airlie <airlied@redhat.com> - 20201022-114
- Update AMDGPU fw for 6800

* Fri Oct 23 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 20201022-113
- Update to upstream 20201022 release
- All symlinks created using WHENCE links option
- Update Marvell Switchdev firmware with ABI changes
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.1312
- Cadence MHDP8546 DP bridge
- Intel Bluetooth updates for: 7265(D1)
- iwlwifi: update 3168, 7265D, 8000C, 8265, core56-54 firmwares
- QCA WCN3991 updates
- TI VPDMA 1b8.bin firmware
- amdgpu: navi10/12/14/picasso/raven/renoir/vega10/12/20 update to 20.40
- ice: add comms for Intel E800 series driver, firmware to 1.3.16.0
- qcom : updated venus firmware
- i915: Add DG1 DMC v2.02
- mediatek: VPU: separate venc service
- ath10k: add SDIO firmware for QCA9377 WiFi
- rtl_bt: Update RTL8821C BT FW to 0xAA6C_A99E
- cypress: add Cypress firmware and clm_blob files for:
  43012, 43340, 43362, 4339, 43430, 43455, 4354, 4356, 43570, 4373, 54591

* Fri Sep 18 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 20200918-112
- amdgpu firmware for 20.30: navi10/12
- wl18xx: update firmware file 8.9.0.0.83
- mt7615: update firmware to 20200814
- qcom: Add updated a5xx and a6xx microcode
- mediatek: update MT7915 firmware to 20200819
- Intel Bluetooth updates 9260/9560/AX201/AX200
- AMD SEV firmware update
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.1310

* Mon Aug 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 20200817-111
- Update to upstream 20200817 release
- Link Raspberry Pi 3A+ WiFi NVRAM to the 3B+ NVRAM
- Update RTL8822C BT UART firmware to 0x0599_8A4F
- i915: Add DMC FW 2.02 for RKL, 2.08 for TGL, HuC FW v7.5.0 for TGL
- amdgpu: update vega20/12/10, renoir, raven/2, picasso, navi10/14 firmware for 20.30
- update NXP SDSD-8997 firmware image
- Mellanox: Add new mlxsw_spectrum firmware xx.2008.1036

* Tue Jul 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200721-110
- Update to upstream 20200721 release
- Bluetooth updates for Intel AX200/AX201/9560/9260, QCom QCA6390
- rtl_nic updated RTL8125B
- WiFi: WCN3991, MT7663, wilc1000 FW v15.4
- amdgpu: add UVD firmware for SI asics

* Fri Jun 19 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200619-109
- Update to upstream 20200619 release
- Bluetooth updates: Intel 9260/9560/AX200/AX201
- mlxsw_spectrum firmware xx.2007.1168
- rtl_nic firmware for RTL8125B
- rtw88: RTL8822C firmware v9.9
- cxgb4 firmware 1.24.17.0
- mrvl: firmware for Prestera ASIC devices

* Tue May 19 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200519-108
- Update to upstream 20200519 release
- Bluetooth updates: Intel 9260/9560/AX200/AX201, new QCA9377
- wifi: rtw88: support RTL8723DE, update RTL8821C
- wifi: intel: update 8265/7265D/3168/8000C/9000/9260cc/Qu

* Tue Apr 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200421-107
- Update to upstream 20200421 release
- amdgpu: Update vega20/12/10, renoir, raven, raven2, picasso, navi10/14 for 20.10
- Bluetooth updates for Intel AX201/AX200, RTL8822C, QCA6390
- Add firmware for MT7663 Wifi/BT combo and mt8183 SCP devices
- cxgb4: Update firmware to 1.24.14.0, T6 config update

* Mon Mar 16 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200316-106
- Update to upstream 20200316 release
- Bluetooth firmware updates: Intel, QCom, RTL8822C
- Agilio SmartNIC flower firmware to rev AOTC-2.12.A.13
- amdgpu: Update to raven2, renoir, navi10, vega10, vega12, vega20
- Intel i915: HuC, DMC firmware updates
- nvidia: add TU116/117 signed firmware
- amlogic: video decoder firmware updates
- rtl_nic: update firmware for RTL8153A

* Wed Jan 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> 20200122-105
- Update to upstream 20200122 release
- Intel bluetooth updates: AX200/AX201/9560
- nvidia: TU102/TU104/TU106 signed firmware
- AMD: update navi10/14, radeon, vega10/12/20, picasso, raven firmware
- qed, mediatek, Mellanox updates
- QCom SDM845 WLAN firmware
- ath10k: updates for WCN3990, QCA9984, QCA988X, QCA9888, QCA9887, QCA6174
- Update AMD cpu microcode for processor family 17h

* Mon Dec 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20191215-104
- Update to upstream 20191215 release
- qcom: Add SDM845 firmwares for modem, Audio DSP, Compute DSP
- Realtek firmwares for RTL8153, RTL8822CU, RTL8168fp/RTL8117, rtw88
- Storage firmwares for mlxsw, cxgb4, QL4xxxx, bnx2x
- amdgpu: raven/navi14/navi10 , i915
- NXP Management Complex: LS108x, LS208x, LX2160.
- Raspberry Pi 4 WiFi NVRAM

* Tue Oct 22 2019 Josh Boyer <jwboyer@fedoraproject.org> 20191022-103
- Rework to use upstream install

* Mon Sep 23 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190923-102
- Update Intel WiFi and Bluetooth firmwares
- Mellanox new mlxsw_spectrum firmware 13.2000.1886
- Some new Broadcom NVRAM for new devices
- Firmware rtl8125a-3 for Realtek's 2.5Gbps chip RTL8125
- Updated nvidia tegra firmwares
- Updated i915, QCom Adreno a630, amdgpu Navi10 firmware

* Thu Aug 15 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190815-101
- Updates for various ath10k and rtw88 Wireless firmwares
- Update NXP Layerscape Management Complex firmware
- update Agilio SmartNIC flower firmware
- cxgb4 firmware update

* Tue Aug  6 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190717-100
- Pull in upstream intel iwliwfi firmware updates WiFi/BT firmware issues (RHBZ 1733369)

* Wed Jul 17 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190717-99
- Update to upstream 20190717 release
- New/updated Intel iwlwifi/bluetooth firmware for various generations
- New RS9116 chipset firmware for rsi
- Updated Intel i915 / AMD gpu firmware

* Mon Jul 15 2019 Dave Airlie <airlied@redhat.com> - 20190618-98
- Add some navi firmware (not upstream yet, soon)

* Wed Jun 19 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190618-97
- Update to upstream 20190618 release
- Updated mhdp8546 DP, nvidia, AMD firmware
- New/updated wireless for Redpine 9113, Intel 9260/9560/22161 Bluetooth
- i.MX SDMA and CNN55XX crypto firmware update

* Tue May 14 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190514-96
- Update to upstream 20190514 release

* Tue Apr 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190416-95
- Update to upstream 20190416 release

* Wed Mar 13 2019 Josh Boyer <jwboyer@fedoraproject.org> 20190312-94
- Update to upstream 20190312 release
- amgpug, rtl, AMD SEV, and other various updates

* Thu Feb 14 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190213-93.git710963fe
- ath10k updates for QCA6174/QCA9888/QCA988X/QCA9984
- Marvell updates for SD8977/SD8897-B0/PCIe-USB8997
- amdgpu: add firmware for vega20 from 18.50
- nvidia: add TU10x typec controller firmware
- bnx2x: Add FW 7.13.11.0

* Thu Feb  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190118-92.gita8b75cac
- Split out LiquidIO and Netronome firmware to their own package
- Ship just one copy of WHENCE

* Tue Jan 22 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190118-91.gita8b75cac
- Latest Intel 9000 series WiFi/Bluetooth firmware
- Marvell WiFi (USB8801), cxgb4, amdgpu updates
- Raspberrp Pi 3-series NMRAM updates

* Wed Dec 19 2018 Justin M. Forbes <jforbes@fedoraproject.org> - 20181219-89.git0f22c852
- Latest upstream snapshot

* Fri Oct 12 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20181008-88.gitc6b6265d
- update BT firmwares for QCA ROME, TI CC2560(A), mt7668u
- Update WiFi firmware for Marvell SD8997, iwlwifi 7000, 8000 and 9000 series, Realtek rtw88
- nvidia: add GV100 signed firmware
- Agilio SmartNIC firmwares
- Raspberry Pi 3/3B+ WiFi fixes

* Mon Oct  1 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180913-87.git44d4fca9
- Latest upstream snapshot
- Minor spec cleanups

* Wed Aug 15 2018 Josh Boyer <jwboyer@fedoraproject.org> - 20180815-86.gitf1b95fe5
- Latest upstream snapshot

* Fri May 25 2018 Josh Boyer <jwboyer@fedoraproject.org> - 20180525-85.git7518922b
- Latest upstream snapshot

* Mon May 07 2018 Josh Boyer <jwboyer@fedoraproject.org> - 20180507-84.git8fc2d4e5
- Latest upstream snapshot

* Mon Apr 02 2018 Josh Boyer <jwboyer@fedoraproject.org> - 20180402-83.git8c1e439c
- Latest upstream snapshot

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20171215-82.git2451bb22.1
- Escape macros in %%changelog

* Fri Jan 05 2018 Josh Boyer <jwboyer@fedoraproject.org> 20171215-92.git2451bb22
- Add amd-ucode for fam17h

* Fri Dec 15 2017 Josh Boyer <jwboyer@fedoraproject.org> 20171215-81.git2451bb22
- Updated skl DMC, cnl audio, netronome SmartNIC, amdgpu vega10 and raven,
  intel bluetooth, brcm CYW4373, and liquidio vswitch firmwares

* Sun Nov 26 2017 Josh Boyer <jwboyer@fedoraproject.org> 20171126-80.git17e62881
- Updated bcm 4339 4354 4356 4358 firmware, new bcm 43430
- Fixes CVE-2016-0801 CVE-2017-0561 CVE-2017-9417

* Thu Nov 23 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20171123-79.git90436ce
- Updated Intel GPU, amdgpu, iwlwifi, mvebu wifi, liquidio, QCom a530 & Venus, mlxsw, qed
- Add iwlwifi 9000 series

* Wed Oct 11 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20171009-78.gitbf04291
- Updated cxgb4, QCom gpu, Intel OPA IB, amdgpu, rtlwifi
- Ship the license in %%license for all sub packages
- Modernise spec

* Mon Sep 18 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170828-77.gitb78acc9
- Add patches to fix ath10k regression (rhbz 1492161)

* Mon Aug 28 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170828-76.gitb78acc9
- Update to latest upstream snapshot
- ath10k, iwlwifi, kabylake, liquidio, amdgpu, and cavium crypot updates

* Thu Jun 22 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170622-75.gita3a26af2
- Update to latest upstream snapshot
- imx, qcom, and tegra ARM related updates

* Mon Jun 05 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170605-74.git37857004
- Update to latest upstream snapshot

* Wed Apr 19 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170419-73.gitb1413458
- Update to the latest upstream snapshot
- New nvidia, netronome, and marvell firmware
- Updated intel audio firmware

* Mon Mar 13 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170313-72.git695f2d6d
- Update to the latest upstream snapshot
- New nvidia, AMD, and i915 GPU firmware
- Updated iwlwifi and intel bluetooth firmware

* Mon Feb 13 2017 Josh Boyer <jwboyer@fedoraproject.org> - 20170213-71.git6d3bc888
- Update to the latest upstream snapshot

* Wed Feb 01 2017 Stephen Gallagher <sgallagh@redhat.com> - 20161205-70.git91ddce49
- Add missing %%license macro

* Mon Dec 05 2016 Josh Boyer <jwboyer@fedoraproject.org> 20161205-69.git91ddce49
- Update to the latest upstream snapshot
- New intel bluetooth and rtlwifi firmware

* Fri Sep 23 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160923-68.git42ad5367
- Update to the latest upstream snapshot
- ath10k, amdgpu, mediatek, brcm, marvell updates
 
* Tue Aug 16 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160816-67.git7c3dfc0b
- Update to the latest upstream snapshot (rhbz 1367203)
- Intel audio, rockchip, amdgpu, iwlwifi, nvidia pascal updates

* Thu Jun 09 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160609-66.gita4bbc811
- Update to the latest upstream snapshot
- Intel bluetooth, radeon smc, Intel braswell/broxton audio, cxgb4 updates

* Thu May 26 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160526-65.git80d463be
- Update to the latest upstream snapshot
- amdgpu, Skylake audio, and rt2xxx wifi firmware updates

* Thu May 05 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160505-64.git8afadbe5
- Update to the latest upstream snapshot
- AMD, intel, and QCA6xxx updates (rhbz 1294263)

* Mon Mar 21 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160321-63.git5f8ca0c
- Update to latest upstream snapshot
- New Skylake GuC and audio firmware, AMD ucode updates

* Wed Mar 16 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160316-62.gitdeb1d836
- Update to latest upstream snapshot
- New firmware for iwlwifi 3168, 7265D, 8000C, and 8265 devices

* Thu Feb 04 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160204-61.git91d5dd13
- Update to latest upstream snashot
- rtlwifi, iwlwifi, intel bluetooth, skylake audio updates

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151214-60.gitbbe4917c.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Josh Boyer <jwboyer@fedoraproject.org> 20151214-60.gitbbe4917c
- Update to latest upstream snapshot
- Includes firmware for mt7601u (rhbz 1264631)

* Mon Nov 30 2015 Josh Boyer <jwboyer@fedoraproject.org> 20151130-59.gita109a8ff
- Update to latest upstream snapshot
- Includes -16 ucode for iwlwifi, skylake dmc and audio updates, brcm updates
  bnx2x, and others

* Fri Oct 30 2015 Josh Boyer <jwboyer@fedoraproject.org> 20151030-58.git66d3d8d7
- Update to latest upstream snapshot
- Includes ath10k and mwlwifi firmware updates (rhbz 1276360)

* Mon Oct 12 2015 Josh Boyer <jwboyer@fedoraproject.org> 20151012-57.gitd82d3c1e
- Update to latest upstream snapshot
- Includes skylake and intel bluetooth firmware updates

* Fri Sep 04 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150904-56.git6ebf5d57
- Update to latest upstream git snapshot
- Includes amdgpu firmware and skylake updates

* Thu Sep 03 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150903-55.git38358cfc
- Add firmware from Alex Deucher for amdgpu driver (rhbz 1259542)

* Thu Sep 03 2015 Josh Boyer <jwboyer@fedoraproject.org>
- Update to latest upstream git snapshot
- Updates for nvidia, bnx2x, and atmel devices

* Wed Jul 15 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150715-54.git69640304
- Update to latest upstream git snapshot
- New iwlwifi firmware for 726x/316x/8000 devices
- New firmware for i915 skylake and radeon devices
- Various other updates

* Tue Jun 23 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150521-53.git3161bfa4
- Don't obsolete ivtv-firmware any longer (rhbz 1232773)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150521-52.git3161bfa4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150521-52.git3161bfa4
- Update to latest upstream git snapshot
- Updated iwlwifi 316x/726x firmware
- Add cx18-firmware Obsoletes from David Ward (rhbz 1222164)

* Wed May 06 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150415-51.gitec89525b
- Obsoletes ivtv-firmware (rbhz 1211055)

* Fri May 01 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150415-50.gitec89525b
- Add v4l-cx25840.fw back now that ivtv-firmware is retired (rhbz 1211055)

* Tue Apr 14 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150415-49.gitec89525b
- Fix conflict with ivtv-firmware (rhbz 1203385)

* Fri Apr 10 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150415-47.gitec89525b
- Update to the latest upstream git snapshot

* Thu Mar 19 2015 Josh Boyer <jwboyer@fedoraproject.org>
- Ship the cx18x firmware files (rhbz 1203385)

* Mon Mar 16 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150316-46.git020e534e
- Update to latest upstream git snapshot

* Fri Feb 13 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150213-45.git17657c35
- Update to latest upstream git snapshot
- Firmware for Surface Pro 3 WLAN/Bluetooth (rhbz 1185804)

* Thu Jan 15 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150115-44.git78535e88.fc22
- Update to latest upstream git snapshot
- Adjust iwl{3160,7260} version numbers (rhbz 1167695)

* Tue Oct 14 2014 Josh Boyer <jwboyer@fedoraproject.org> 20141013-43.git0e5f6377.fc22
- Fix 3160/7260 version numbers (rhbz 1110522)

* Mon Oct 13 2014 Josh Boyer <jwboyer@fedoraproject.org> 20141013-42.git0e5f6377.fc22
- Update to latest upstream git snapshot

* Fri Sep 12 2014 Josh Boyer <jwboyer@fedoraproject.org> 20140912-41.git365e80cce.fc22
- Update to the latest upstream git snapshot

* Thu Aug 28 2014 Josh Boyer <jwboyer@fedoraproject.org>
- Update to latest upstream git snapshot for new radeon firmware (rhbz 1130738)
- Fix versioning after mass rebuild and for iwl5000-firmware (rhbz 1130979)

* Fri Aug 08 2014 Kyle McMartin <kyle@fedoraproject.org> 20140808-39.gitce64fa89.1
- Update from upstream linux-firmware.
- Nuke unapplied radeon patches.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140605-38.gita4f3bc03.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Josh Boyer <jwboyer@fedoraproject.org> - 20140605-38.gita4f3bc03
- Updates for Intel 3160/7260/7265 firmware (1087717)
- Add firmware for rtl8723be (rhbz 1091753)
- Updates for radeon CIK, SI/CI, and Mullins/Beema GPUs (rhbz 1094153)
- Various other firmware updates

* Mon Mar 17 2014 Josh Boyer <jwboyer@fedoraproject.org>
- Updates for Intel 3160/7260 and BCM43362 (rhbz 1071590)

* Tue Mar 04 2014 Josh Boyer <jwboyer@fedoraproject.org>
- Fixup Intel wireless package descriptions and Source0 (rhbz 1070600)

* Fri Jan 31 2014 Josh Boyer <jwboyer@fedoraproject.org> - 20140131-35.gitd7f8a7c8
- Update to new snapshot
- Updates for Intel 3160/7260, radeon HAWAII GPUs, and some rtlwifi chips
- Fixes bugs 815579 1046935

* Tue Oct 01 2013 Kyle McMartin <kyle@fedoraproject.org> - 20131001-32.gitb8ac7c7e
- Update to a new git snapshot, drop radeon patches.

* Mon Sep 16 2013 Josh Boyer <jwboyer@fedoraproject.org> - 20130724-31.git31f6b30
- Obsolete ql2x00-firmware packages again (rhbz 864959)

* Sat Jul 27 2013 Josh Boyer <jwboyer@redhat.com> - 20130724-30.git31f6b30
- Add AMD ucode back in now that microcode_ctl doesn't provide it

* Fri Jul 26 2013 Dave Airlie <airlied@redhat.com> 20130724-29.git31f6b30
- add radeon firmware which are lost on the way upstream (#988268)

* Thu Jul 25 2013 Josh Boyer <jwboyer@redhat.com> - 20130724-28.git31f6b30
- Temporarily remove AMD microcode (rhbz 988263)
- Remove Creative CA0132 HD-audio files as they're in alsa-firmware

* Wed Jul 24 2013 Josh Boyer <jwboyer@redhat.com> - 20130724-27.git31f6b30
- Update to latest upstream
- New rtl, iwl, and amd firmware

* Fri Jun 07 2013 Josh Boyer <jwboyer@redhat.com> - 20130607-26.git2892af0
- Update to latest upstream release
- New radeon, bluetooth, rtl, and wl1xxx firmware

* Mon May 20 2013 Kyle McMartin <kyle@redhat.com> - 20130418-25.gitb584174
- Use a common version number for both the iwl*-firmware packages and
  linux-firmware itself.
- Don't reference old kernel-firmware package in %%description

* Mon May 20 2013 Kyle McMartin <kyle@redhat.com> - 20130418-0.3.gitb584174
- Bump iwl* version numbers as well...

* Mon May 20 2013 Kyle McMartin <kyle@redhat.com> - 20130418-0.2.gitb584174
- UsrMove: move firmware to /usr/lib/firmware
- Remove duplicate /usr/lib/firmware/updates entry (already in linux-firmware.dirs)
- Simplify sed by using '!' instead of '/' as regexp delimiter
- Fix date error (commited on Mon Feb 04, so change that entry)

* Thu Apr 18 2013 Josh Boyer <jwboyer@redhat.com> - 20130418-0.1.gitb584174
- Update to latest upstream git tree

* Tue Mar 19 2013 Josh Boyer <jwboyer@redhat.com>
- Own the firmware directories (rhbz 919249)

* Thu Feb 21 2013 Josh Boyer <jwboyer@redhat.com> - 20130201-0.4.git65a5163
- Obsolete netxen-firmware.  Again.  (rhbz 913680)

* Mon Feb 04 2013 Josh Boyer <jwboyer@redhat.com> - 20130201-0.3.git65a5163
- Obsolete ql2[45]00-firmware packages (rhbz 906898)
 
* Fri Feb 01 2013 Josh Boyer <jwboyer@redhat.com> 
- Update to latest upstream release
- Provide firmware for carl9170 (rhbz 866051)

* Wed Jan 23 2013 Ville Skyttä <ville.skytta@iki.fi> - 20121218-0.2.gitbda53ca
- Own subdirs created in /lib/firmware (rhbz 902005)

* Wed Jan 23 2013 Josh Boyer <jwboyer@redhat.com>
- Correctly obsolete the libertas-usb8388-firmware packages (rhbz 902265)

* Tue Dec 18 2012 Josh Boyer <jwboyer@redhat.com>
- Update to latest upstream.  Adds brcm firmware updates

* Wed Oct 10 2012 Josh Boyer <jwboyer@redhat.com>
- Consolidate rt61pci-firmware and rt73usb-firmware packages (rhbz 864959)
- Consolidate netxen-firmware and ql2[123]xx-firmware packages (rhbz 864959)

* Tue Sep 25 2012 Josh Boyer <jwboyer@redhat.com>
- Update to latest upstream.  Adds marvell wifi updates (rhbz 858388)

* Tue Sep 18 2012 Josh Boyer <jwboyer@redhat.com>
- Add patch to create libertas subpackages from Daniel Drake (rhbz 853198)

* Fri Sep 07 2012 Josh Boyer <jwboyer@redhat.com> 20120720-0.2.git7560108
- Add epoch to iwl1000 subpackage to preserve upgrade patch (rhbz 855426)

* Fri Jul 20 2012 Josh Boyer <jwboyer@redhat.com> 20120720-0.1.git7560108
- Update to latest upstream.  Adds more realtek firmware and bcm4334

* Tue Jul 17 2012 Josh Boyer <jwboyer@redhat.com> 20120717-0.1.gitf1f86bb
- Update to latest upstream.  Adds updated realtek firmware

* Thu Jun 07 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.5.git375e954
- Bump release to get around koji

* Thu Jun 07 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.4.git375e954
- Drop udev requires.  Systemd now provides udev

* Tue Jun 05 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.3.git375e954
- Fix location of BuildRequires so git is inclued in the buildroot
- Create iwlXXXX-firmware subpackages (rhbz 828050)

* Thu May 10 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.1.git375e954
- Update to latest upstream.  Adds new bnx2x and radeon firmware

* Wed Apr 18 2012 Josh Boyer <jwboyer@redhat.com> 20120418-0.1.git85fbcaa
- Update to latest upstream.  Adds new rtl and ath firmware

* Wed Mar 21 2012 Dave Airlie <airlied@redhat.com> 20120206-0.3.git06c8f81
- use git to apply the radeon firmware

* Wed Mar 21 2012 Dave Airlie <airlied@redhat.com> 20120206-0.2.git06c8f81
- add radeon southern islands/trinity firmware

* Tue Feb 07 2012 Josh Boyer <jwboyer@redhat.com> 20120206-0.1.git06c8f81
- Update to latest upstream git snapshot.  Fixes rhbz 786937

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110731-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 04 2011 Tom Callaway <spot@fedoraproject.org> 20110731-2
- resolve conflict with netxen-firmware

* Wed Aug 03 2011 David Woodhouse <dwmw2@infradead.org> 20110731-1
- Latest firmware release with v1.3 ath9k firmware (#727702)

* Sun Jun 05 2011 Peter Lemenkov <lemenkov@gmail.com> 20110601-2
- Remove duplicated licensing files from /lib/firmware

* Wed Jun 01 2011 Dave Airlie <airlied@redhat.com> 20110601-1
- Latest firmware release with AMD llano support.

* Thu Mar 10 2011 Dave Airlie <airlied@redhat.com> 20110304-1
- update to latest upstream for radeon ni/cayman, drop nouveau fw we don't use it anymore

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 David Woodhouse <dwmw2@infradead.org> 20110125-1
- Update to linux-firmware-20110125 (new bnx2 firmware)

* Fri Jan 07 2011 Dave Airlie <airlied@redhat.com> 20101221-1
- rebase to upstream release + add new radeon NI firmwares.

* Thu Aug 12 2010 Hicham HAOUARI <hicham.haouari@gmail.com> 20100806-4
- Really obsolete ueagle-atm4-firmware

* Thu Aug 12 2010 Hicham HAOUARI <hicham.haouari@gmail.com> 20100806-3
- Obsolete ueagle-atm4-firmware

* Fri Aug 06 2010 David Woodhouse <dwmw2@infradead.org> 20100806-2
- Remove duplicate radeon firmwares; they're upstream now

* Fri Aug 06 2010 David Woodhouse <dwmw2@infradead.org> 20100806-1
- Update to linux-firmware-20100806 (more legacy firmwares from kernel source)

* Fri Apr 09 2010 Dave Airlie <airlied@redhat.com> 20100106-4
- Add further radeon firmwares

* Wed Feb 10 2010 Dave Airlie <airlied@redhat.com> 20100106-3
- add radeon RLC firmware - submitted upstream to dwmw2 already.

* Tue Feb 09 2010 Ben Skeggs <bskeggs@redhat.com> 20090106-2
- Add firmware needed for nouveau to operate correctly (this is Fedora
  only - do not upstream yet - we just moved it here from Fedora kernel)

* Wed Jan 06 2010 David Woodhouse <David.Woodhouse@intel.com> 20090106-1
- Update

* Fri Aug 21 2009 David Woodhouse <David.Woodhouse@intel.com> 20090821-1
- Update, fix typos, remove some files which conflict with other packages.

* Thu Mar 19 2009 David Woodhouse <David.Woodhouse@intel.com> 20090319-1
- First standalone kernel-firmware package.
