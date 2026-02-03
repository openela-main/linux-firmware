%global debug_package %{nil}

%global _firmwarepath	/usr/lib/firmware
%define _binaries_in_noarch_packages_terminate_build 0

Name:		linux-firmware
Version:	20260107
Release:	19.2%{?dist}
Summary:	Firmware files used by the Linux kernel
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
URL:		http://www.kernel.org/
BuildArch:	noarch

Source0:	https://www.kernel.org/pub/linux/kernel/firmware/%{name}-%{version}.tar.xz

BuildRequires:	git-core
BuildRequires:	make
BuildRequires:	python3
# Not required but de-dupes FW so reduces size
# Disabled for now: we use 'make COPYOPTS="--ignore-duplicates" install'
#BuildRequires:	rdfind

Requires:	linux-firmware-whence
Provides:	kernel-firmware = %{version}
Obsoletes:	kernel-firmware < %{version}
Conflicts:	microcode_ctl < 2.1-0

Recommends:	amd-gpu-firmware
Recommends:	intel-gpu-firmware
Recommends:	nvidia-gpu-firmware
%if 0%{?fedora} && 0%{?fedora} < 40
Requires:	amd-ucode-firmware
Requires:	cirrus-audio-firmware
Requires:	intel-audio-firmware
Requires:	nxpwireless-firmware
Requires:	tiwilink-firmware
%else
Recommends:	amd-ucode-firmware
Recommends:	cirrus-audio-firmware
Recommends:	intel-audio-firmware
Recommends:	nxpwireless-firmware
Recommends:	tiwilink-firmware
%endif
%if 0%{?fedora} && 0%{?fedora} < 39
Requires:	atheros-firmware
Requires:	brcmfmac-firmware
Requires:	mt7xxx-firmware
Requires:	realtek-firmware
%else
Recommends:	atheros-firmware
Recommends:	brcmfmac-firmware
Recommends:	mt7xxx-firmware
Recommends:	realtek-firmware
%endif

%description
This package includes firmware files required for some devices to
operate.

%package whence
Summary:	WHENCE License file
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
%description whence
This package contains the WHENCE license file which documents the vendor license details.

# GPU firmwares
%package -n amd-gpu-firmware
Summary:	Firmware for AMD GPUs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n amd-gpu-firmware
Firmware for AMD amdgpu and radeon GPUs.

%package -n intel-gpu-firmware
Summary:	Firmware for Intel GPUs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n intel-gpu-firmware
Firmware for Intel GPUs including GuC (Graphics Microcontroller), HuC (HEVC/H.265
Microcontroller) and DMC (Display Microcontroller) firmware for Skylake and later
platforms.

%package -n nvidia-gpu-firmware
Summary:	Firmware for NVIDIA GPUs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
# Older linux-firmware packages contained /usr/lib/firmware/nvidia/ad10*
# directories, but now nvidia-gpu-firmware has them as symlinks.
# Require update of linux-firmware to avoid file conflict.
Requires:	((linux-firmware >= 20250521-16) if linux-firmware)
%description -n nvidia-gpu-firmware
Firmware for NVIDIA GPUs.

# Microcode updates
%package -n amd-ucode-firmware
Summary:	Microcode updates for AMD CPUs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n amd-ucode-firmware
Microcode updates for AMD CPUs, ARM SEV amd TEE.

# WiFi/Bluetooth firmwares
%package -n atheros-firmware
Summary:	Firmware for Qualcomm Atheros WiFi/Bluetooth adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n atheros-firmware
Firmware for Qualcomm Atheros ath6k/ath9k/ath10k/ath11k WiFi adapters.

%package -n brcmfmac-firmware
Summary:	Firmware for Broadcom/Cypress brcmfmac WiFi/Bluetooth adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n brcmfmac-firmware
Firmware for Broadcom/Cypress brcmfmac WiFi/Bluetooth adapters.

%package -n iwlegacy-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 3945(A)BG and 4965AGN adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
Obsoletes:	iwl3945-firmware < %{version}-%{release}
Obsoletes:	iwl4965-firmware < %{version}-%{release}
Provides:	iwl3945-firmware = %{version}-%{release}
Provides:	iwl4965-firmware = %{version}-%{release}
%description -n iwlegacy-firmware
This package contains the firmware required by the iwlegacy driver
for Linux. This includes the 3945(A)BG and 4965AGN WiFi NICs. Usage
of the firmware is subject to the terms and conditions contained
inside the provided LICENSE file. Please read it carefully.

%package -n iwlwifi-dvm-firmware
Summary:	DVM Firmware for Intel(R) Wireless WiFi adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
Obsoletes:	iwl100-firmware < %{version}-%{release}
Obsoletes:	iwl105-firmware < %{version}-%{release}
Obsoletes:	iwl135-firmware < %{version}-%{release}
Obsoletes:	iwl1000-firmware < 1:%{version}-%{release}
Obsoletes:	iwl2000-firmware < %{version}-%{release}
Obsoletes:	iwl2030-firmware < %{version}-%{release}
Obsoletes:	iwl5000-firmware < %{version}-%{release}
Obsoletes:	iwl5150-firmware < %{version}-%{release}
Obsoletes:	iwl6000-firmware < %{version}-%{release}
Obsoletes:	iwl6000g2a-firmware < %{version}-%{release}
Obsoletes:	iwl6000g2b-firmware < %{version}-%{release}
Obsoletes:	iwl6050-firmware < %{version}-%{release}
Provides:	iwl100-firmware = %{version}-%{release}
Provides:	iwl105-firmware = %{version}-%{release}
Provides:	iwl135-firmware = %{version}-%{release}
Provides:	iwl1000-firmware = 1:%{version}-%{release}
Provides:	iwl2000-firmware = %{version}-%{release}
Provides:	iwl2030-firmware = %{version}-%{release}
Provides:	iwl5000-firmware = %{version}-%{release}
Provides:	iwl5150-firmware = %{version}-%{release}
Provides:	iwl6000-firmware = %{version}-%{release}
Provides:	iwl6000g2a-firmware = %{version}-%{release}
Provides:	iwl6000g2b-firmware = %{version}-%{release}
Provides:	iwl6050-firmware = %{version}-%{release}
%description -n iwlwifi-dvm-firmware
This package contains the firmware required by the iwlwifi driver
for Linux built with DVM firmware support (CONFIG_IWLDVM=y/m). Usage of
the firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n iwlwifi-mvm-firmware
Summary:	MVM Firmware for Intel(R) Wireless WiFi adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
Obsoletes:	iwl3160-firmware < 1:%{version}-%{release}
Obsoletes:	iwl7260-firmware < 1:%{version}-%{release}
Obsoletes:	iwlax2xx-firmware < %{version}-%{release}
Provides:	iwl3160-firmware = 1:%{version}-%{release}
Provides:	iwl7260-firmware = 1:%{version}-%{release}
Provides:	iwlax2xx-firmware = %{version}-%{release}
%description -n iwlwifi-mvm-firmware
This package contains the firmware required by the iwlwifi driver
for Linux built with MVM firmware support (CONFIG_IWLMVM=y/m).  Usage of
the firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n libertas-firmware
Summary:	Firmware for Marvell Libertas SD/USB WiFi Network Adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
Obsoletes:      libertas-sd8686-firmware < %{version}-%{release}
Obsoletes:      libertas-sd8787-firmware < %{version}-%{release}
Obsoletes:      libertas-usb8388-firmware < 2:%{version}-%{release}
Obsoletes:      libertas-usb8388-olpc-firmware < %{version}-%{release}
Provides:       libertas-sd8686-firmware < %{version}-%{release}
Provides:       libertas-sd8787-firmware < %{version}-%{release}
Provides:       libertas-usb8388-firmware < 2:%{version}-%{release}
Provides:       libertas-usb8388-olpc-firmware < %{version}-%{release}
%description -n libertas-firmware
Firmware for the Marvell Libertas series of WiFi Network Adapters
Including the SD 8686/8787 and USB 8388/8388.

%package -n mt7xxx-firmware
Summary:	Firmware for Mediatek 7600/7900 series WiFi/Bluetooth adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n mt7xxx-firmware
Firmware for Mediatek 7600/7900 series WiFi/Bluetooth adapters

%package -n nxpwireless-firmware
Summary:	Firmware for NXP WiFi/Bluetooth/UWB adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n nxpwireless-firmware
Firmware for NXP WiFi/Bluetooth/UWB adapters.

%package -n realtek-firmware
Summary:	Firmware for Realtek WiFi/Bluetooth adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n realtek-firmware
Firmware for Realtek WiFi/Bluetooth adapters

%package -n tiwilink-firmware
Summary:	Firmware for Texas Instruments WiFi/Bluetooth adapters
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n tiwilink-firmware
Firmware for Texas Instruments WiFi/Bluetooth adapters

# SMART NIC and network switch firmwares
%package -n liquidio-firmware
Summary:	Firmware for Cavium LiquidIO Intelligent Server Adapter
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n liquidio-firmware
Firmware for Cavium LiquidIO Intelligent Server Adapter

%package -n mlxsw_spectrum-firmware
Summary:	Firmware for Mellanox Spectrum 1/2/3 Switches
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n mlxsw_spectrum-firmware
Firmware for Mellanox Spectrumi series 1/2/3 ethernet switches.

%package -n mrvlprestera-firmware
Summary:	Firmware for Marvell Prestera Switchdev/ASIC devices
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n mrvlprestera-firmware
Firmware for Marvell Prestera Switchdev/ASIC devices

%package -n netronome-firmware
Summary:	Firmware for Netronome Smart NICs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n netronome-firmware
Firmware for Netronome Smart NICs

# Silicon Vendor specific
%package -n qcom-firmware
Summary:	Firmware for Qualcomm SoCs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
Requires:	atheros-firmware = %{version}-%{release}
%description -n qcom-firmware
Firmware for various compoents in Qualcomm SoCs including Adreno
GPUs, Venus video encode/decode, Audio DSP, Compute DSP, WWAN
modem, Sensor DSPs.

# Vision and ISP hardware
%package -n intel-vsc-firmware
Summary:	Firmware files for Intel Visual Sensing Controller (IVSC)
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n intel-vsc-firmware
Firmware files for Intel Visual Sensing Controller (IVSC) for
Tiger Lake, Alder Lake and Raptor Lake SoCs.

# Sound codec hardware
%package -n cirrus-audio-firmware
Summary:	Firmware for Cirrus audio amplifiers and codecs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n cirrus-audio-firmware
Firmware for Cirrus audio amplifiers and codecs

%package -n intel-audio-firmware
Summary:	Firmware for Intel audio DSP amplifiers and codecs
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n intel-audio-firmware
Firmware for Intel audio DSP amplifiers and codecs

# Random other hardware
%package -n dvb-firmware
Summary:	Firmware for various DVB broadcast receivers
License:	Redistributable, no modification permitted
Requires:	linux-firmware-whence
%description -n dvb-firmware
Firmware for various DVB broadcast receivers. These include the
Siano DTV devices, devices based on Conexant chipsets (cx18,
cx23885, cx23840, cx231xx), Xceive xc4000/xc5000, DiBcom dib0700,
Terratec H5 DRX-K, ITEtech IT9135 Ax and Bx, and av7110.

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

pushd %{buildroot}/%{_firmwarepath}

# Move amd-ucode readme to docs directory due to dracut issue (RHEL-15387)
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}/amd-ucode
%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9
mv -f amd-ucode/README.xz %{buildroot}/%{_defaultdocdir}/%{name}/amd-ucode
%else
mv -f amd-ucode/README %{buildroot}/%{_defaultdocdir}/%{name}/amd-ucode
%endif
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

# Remove obsolete and password-protected vgxe firmware (see bug 2108051 and RHEL-32145)
rm -rf vxge

# Remove superfluous infra files
rm -rf check_whence.py configure Makefile README.md Dockerfile \
	contrib build_packages.py

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
sed \
	-i -e '/^amdgpu/d' \
	-i -e '/^amd/d' \
	-i -e '/^amdtee/d' \
	-i -e '/^amd-ucode/d' \
	-i -e '/^ar3k/d' \
	-i -e '/^ath6k/d' \
	-i -e '/^ath9k_htc/d' \
	-i -e '/^ath10k/d' \
	-i -e '/^ath11k/d' \
	-i -e '/^ath12k/d' \
	-i -e '/^as102_data/d' \
	-i -e '/^av7110/d' \
	-i -e '/^brcm/d' \
	-i -e '/^cirrus/d' \
	-i -e '/^cmmb/d' \
	-i -e '/^cypress/d' \
	-i -e '/^dvb/d' \
	-i -e '/^i915/d' \
	-i -e '/^intel\/avs/d' \
	-i -e '/^intel\/catpt/d' \
	-i -e '/^intel\/IntcSST2.bin/d' \
	-i -e '/^intel\/dsp_fw/d' \
	-i -e '/^intel\/fw_sst/d' \
	-i -e '/^intel\/ipu/d' \
	-i -e '/^intel\/ipu3/d' \
	-i -e '/^intel\/irci_irci/d' \
	-i -e '/^intel\/vsc/d' \
	-i -e '/^isdbt/d' \
	-i -e '/^iwlwifi/d' \
	-i -e '/^intel\/iwlwifi\/iwlwifi/d' \
	-i -e '/^nvidia\/a/d' \
	-i -e '/^nvidia\/g/d' \
	-i -e '/^nvidia\/tu/d' \
	-i -e '/^lgs8g75/d' \
	-i -e '/^libertas/d' \
	-i -e '/^liquidio/d' \
	-i -e '/^mellanox/d' \
	-i -e '/^mediatek\/mt76/d' \
	-i -e '/^mediatek\/mt79/d' \
	-i -e '/^mediatek\/BT/d' \
	-i -e '/^mediatek\/WIFI/d' \
	-i -e '/^mt7601u.bin/d' \
	-i -e '/^mt7650.bin/d' \
	-i -e '/^mt7662.bin/d' \
	-i -e '/^mt7662_rom_patch.bin/d' \
	-i -e '/^mrvl\/prestera/d' \
	-i -e '/^mrvl\/sd8787/d' \
	-i -e '/^netronome/d' \
	-i -e '/^nxp/d' \
	-i -e '/^qca/d' \
	-i -e '/^qcom/d' \
	-i -e '/^a300_pfp.fw/d' \
	-i -e '/^a300_pm4.fw/d' \
	-i -e '/^radeon/d' \
	-i -e '/^rtl_bt/d' \
	-i -e '/^rtlwifi/d' \
	-i -e '/^rtw88/d' \
	-i -e '/^rtw89/d' \
	-i -e '/^sms1xxx/d' \
	-i -e '/^tdmb/d' \
	-i -e '/^ti-connectivity/d' \
	-i -e '/^v4l-cx2/d' \
	linux-firmware.{files,dirs}
sed -i -e 's!^!/usr/lib/firmware/!' linux-firmware.{files,dirs}
sed -i -e 's/^/"/;s/$/"/' linux-firmware.files
sed -e 's/^/%%dir /' linux-firmware.dirs >> linux-firmware.files

%files -f linux-firmware.files
%dir %{_firmwarepath}
%doc %{_defaultdocdir}/%{name}
%license LICENCE.* LICENSE.* GPL*

%files whence
%license WHENCE

# GPU firmwares
%files -n amd-gpu-firmware
%license LICENSE.radeon LICENSE.amdgpu
%{_firmwarepath}/amdgpu/
%{_firmwarepath}/amdnpu/
%{_firmwarepath}/radeon/

%files -n intel-gpu-firmware
%license LICENSE.i915
%{_firmwarepath}/i915/

%files -n nvidia-gpu-firmware
%license LICENCE.nvidia
%dir %{_firmwarepath}/nvidia
%{_firmwarepath}/nvidia/a*
%{_firmwarepath}/nvidia/g*
%{_firmwarepath}/nvidia/tu*

# Microcode updates
%files -n amd-ucode-firmware
%license LICENSE.amd-ucode
%{_firmwarepath}/amd/
%{_firmwarepath}/amdtee/
%{_firmwarepath}/amd-ucode/

# WiFi/Bluetooth firmwares
%files -n atheros-firmware
%license LICENCE.atheros_firmware
%license LICENSE.QualcommAtheros_ar3k
%license LICENSE.QualcommAtheros_ath10k
%license LICENCE.open-ath9k-htc-firmware
%license qca/NOTICE.txt
%{_firmwarepath}/ar3k/
%{_firmwarepath}/ath6k/
%{_firmwarepath}/ath9k_htc/
%{_firmwarepath}/ath10k/
%{_firmwarepath}/ath11k/
%{_firmwarepath}/ath12k/
%{_firmwarepath}/qca/

%files -n brcmfmac-firmware
%license LICENCE.broadcom_bcm43xx
%license LICENCE.cypress
%{_firmwarepath}/brcm/
%{_firmwarepath}/cypress/

%files -n iwlegacy-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-3945-*.ucode*
%{_firmwarepath}/iwlwifi-4965-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-3945-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-4965-*.ucode*

%files -n iwlwifi-dvm-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-100-*.ucode*
%{_firmwarepath}/iwlwifi-105-*.ucode*
%{_firmwarepath}/iwlwifi-135-*.ucode*
%{_firmwarepath}/iwlwifi-1000-*.ucode*
%{_firmwarepath}/iwlwifi-2000-*.ucode*
%{_firmwarepath}/iwlwifi-2030-*.ucode*
%{_firmwarepath}/iwlwifi-5000-*.ucode*
%{_firmwarepath}/iwlwifi-5150-*.ucode*
%{_firmwarepath}/iwlwifi-6000-*.ucode*
%{_firmwarepath}/iwlwifi-6000g2a-*.ucode*
%{_firmwarepath}/iwlwifi-6000g2b-*.ucode*
%{_firmwarepath}/iwlwifi-6050-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-100-5.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-105-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-135-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-1000-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-2000-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-2030-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-5000-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-5150-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-6000-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-6000g2a-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-6000g2b-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-6050-*.ucode*

%files -n iwlwifi-mvm-firmware
%license LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-3160-*.ucode*
%{_firmwarepath}/iwlwifi-3168-*.ucode*
%{_firmwarepath}/iwlwifi-7260-*.ucode*
%{_firmwarepath}/iwlwifi-7265-*.ucode*
%{_firmwarepath}/iwlwifi-7265D-*.ucode*
%{_firmwarepath}/iwlwifi-8000C-*.ucode*
%{_firmwarepath}/iwlwifi-8265-*.ucode*
%{_firmwarepath}/iwlwifi-9000-*.ucode*
%{_firmwarepath}/iwlwifi-9260-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-3160-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-3168-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-7260-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-7265-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-7265D-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-8000C-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-8265-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-9000-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-9260-*.ucode*
%{_firmwarepath}/iwlwifi-cc-a0-*.ucode*
%{_firmwarepath}/iwlwifi-gl-c0*
%{_firmwarepath}/iwlwifi-ma-b0*
%{_firmwarepath}/iwlwifi-Qu*.ucode*
%{_firmwarepath}/iwlwifi-ty-a0*
%{_firmwarepath}/iwlwifi-so-a0*
%{_firmwarepath}/iwlwifi-bz-b0*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-cc-a0-*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-gl-c0*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-ma-b0*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-Qu*.ucode*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-ty-a0*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-so-a0*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-bz-b0*
%{_firmwarepath}/iwlwifi-sc-a0-*
%{_firmwarepath}/intel/iwlwifi/iwlwifi-sc-a0-*

%files -n libertas-firmware
%license LICENCE.Marvell LICENCE.OLPC
%dir %{_firmwarepath}/libertas
%dir %{_firmwarepath}/mrvl
%{_firmwarepath}/libertas/*
%{_firmwarepath}/mrvl/sd8787*

%files -n mt7xxx-firmware
%license LICENCE.mediatek
%license LICENCE.ralink_a_mediatek_company_firmware
%dir %{_firmwarepath}/mediatek
%{_firmwarepath}/mediatek/mt76*
%{_firmwarepath}/mediatek/mt79*
%{_firmwarepath}/mediatek/BT*
%{_firmwarepath}/mediatek/WIFI*
%{_firmwarepath}/mt7601u.bin*
%{_firmwarepath}/mt7650.bin*
%{_firmwarepath}/mt7662.bin*
%{_firmwarepath}/mt7662_rom_patch.bin*
# ^^^ compat symlink mt7601u.bin -> mediatek/mt7601u.bin
# ^^^ compat symlink mt7650.bin -> mediatek/mt7650.bin
# ^^^ compat symlink mt7662.bin -> mediatek/mt7662.bin
# ^^^ compat symlink mt7662_rom_patch.bin -> mediatek/mt7662_rom_patch.bin

%files -n nxpwireless-firmware
%license LICENSE.nxp
%dir %{_firmwarepath}/nxp
%{_firmwarepath}/nxp/*

%files -n realtek-firmware
%license LICENCE.rtlwifi_firmware.txt
%{_firmwarepath}/rtl_bt/
%{_firmwarepath}/rtlwifi/
%{_firmwarepath}/rtw88/
%{_firmwarepath}/rtw89/

%files -n tiwilink-firmware
%license LICENCE.ti-connectivity
%dir %{_firmwarepath}/ti-connectivity/
%{_firmwarepath}/ti-connectivity/*

# SMART NIC and network switch firmwares
%files -n liquidio-firmware
%license LICENCE.cavium_liquidio
%dir %{_firmwarepath}/liquidio
%{_firmwarepath}/liquidio/*

%files -n mrvlprestera-firmware
%license LICENCE.Marvell
%dir %{_firmwarepath}/mrvl/prestera
%{_firmwarepath}/mrvl/prestera/*

%files -n mlxsw_spectrum-firmware
%dir %{_firmwarepath}/mellanox/
%{_firmwarepath}/mellanox/*

%files -n netronome-firmware
%license LICENCE.Netronome
%dir %{_firmwarepath}/netronome
%{_firmwarepath}/netronome/*

# Silicon Vendor specific
%files -n qcom-firmware
%license LICENSE.qcom LICENSE.qcom_yamato qcom/NOTICE.txt
%dir %{_firmwarepath}/qcom
%{_firmwarepath}/qcom/*
%{_firmwarepath}/a300_pfp.fw*
%{_firmwarepath}/a300_pm4.fw*
# ^^^ these two are compat symlinks to qcom/* files

# Vision and ISP hardware
%files -n intel-vsc-firmware
%license LICENSE.ivsc
%dir %{_firmwarepath}/intel/ipu/
%dir %{_firmwarepath}/intel/vsc/
%{_firmwarepath}/intel/ipu3-fw.bin*
%{_firmwarepath}/intel/irci_irci_ecr-master_20161208_0213_20170112_1500.bin*
# ^^^ this is a compat symlink to the ipu/irci_irci... file
%{_firmwarepath}/intel/ipu/*
%{_firmwarepath}/intel/vsc/*

# Sound codec hardware
%files -n cirrus-audio-firmware
%license LICENSE.cirrus
%dir %{_firmwarepath}/cirrus
%{_firmwarepath}/cirrus/*

%files -n intel-audio-firmware
%license LICENCE.adsp_sst LICENCE.IntcSST2
%dir %{_firmwarepath}/intel/
%dir %{_firmwarepath}/intel/avs/
%dir %{_firmwarepath}/intel/catpt/
%{_firmwarepath}/intel/avs/*
%{_firmwarepath}/intel/catpt/*
%{_firmwarepath}/intel/IntcSST2.bin*
# ^^^ this is a compat symlink to catpt/bdw/dsp_basefw.bin
%{_firmwarepath}/intel/dsp_fw*
%{_firmwarepath}/intel/fw_sst*

# Random other hardware
%files -n dvb-firmware
%license LICENSE.dib0700 LICENCE.it913x LICENCE.siano
%license LICENCE.xc4000 LICENCE.xc5000 LICENCE.xc5000c
%dir %{_firmwarepath}/av7110/
%{_firmwarepath}/av7110/*
%{_firmwarepath}/as102_data*
%{_firmwarepath}/cmmb*
%{_firmwarepath}/dvb*
%{_firmwarepath}/isdbt*
%{_firmwarepath}/lgs8g75*
%{_firmwarepath}/sms1xxx*
%{_firmwarepath}/tdmb*
%{_firmwarepath}/v4l-cx2*

# workaround for directory->symlink changes
%pretrans -n nvidia-gpu-firmware -p <lua>
path = "/usr/lib/firmware/nvidia/ad103"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end
path = "/usr/lib/firmware/nvidia/ad104"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end
path = "/usr/lib/firmware/nvidia/ad106"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end
path = "/usr/lib/firmware/nvidia/ad107"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

%changelog
* Wed Jan 07 2026 Denys Vlasenko <dvlasenk@redhat.com> - 20260107-19.2
- Update linux-firmware to latest upstream (RHEL-140094)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- qcom: Update aic100 firmware files
- qca: Update Bluetooth WCN6750 1.1.3-00100 firmware to 1.1.3-00105
- firmware: Revert kernel_boot.elf due to license compliance issue
- linux-firmware: add firmware for an8811hb 2.5G ethernet phy
- i915: Xe3LPD_3002 DMC v2.28
- i915: Xe3LPD DMC v2.33
- intel_vpu: Add firmware for 50xx NPUs and update older ones
- linux-firmware: Update AMD SEV firmware
- amdgpu: DMCUB updates for various ASICs
- qcom: venus-5.4: fix ELF segment alignment to 4 bytes
- mediatek MT7925: update bluetooth firmware to 20251210093205
- linux-firmware: update firmware for MT7925 WiFi device
- rcar_gen4_pcie: add firmware for Renesas R-Car Gen4 PCIe controller
- qcom: Update CDSP firmware for qcm6490 platform
- rtl_bt: Update RTL8852BT/RTL8852BE-VT BT USB FW to 0x488C_DB55
- linux-firmware: Add firmware file for Intel Scorpius core
- rtw89: 8852b: update fw to v0.29.29.15
- cirrus: cs35l41: Update firmware and tuning for various HP laptops
- cirrus: cs35l41: Add support for new HP Clipper laptop
- qcom: drop compatibility a640_zap.mdt symlink
- qcom: add version for a530v3_gpmu.fw2
- xe: Update GUC to v70.55.3 for BMG, PTL
- iwlwifi: add Bz/Sc FW for core101-82 release
- iwlwifi: Add Sc/Gf firmware for core101-82 release
- iwlwifi: update ty/So/Ma firmwares for core101-82 release
- iwlwifi: update cc/Qu/QuZ firmwares for core101-82 release
- amdgpu: DMCUB updates for various ASICs
- qcom: Add firmwares for sm8150 GPU
- qcom: Add firmwares for sm8450 GPU
- qcom: Add firmwares for sm8550 GPU
- qcom: Add firmwares for sm8650 GPU
- qcom: Add firmwares for sm8750 GPU
- Makefile: add licence header
- ath10k: WCN3990 hw1.0: update board-2.bin
- ath10k: QCA9888 hw2.0: update board-2.bin
- ath10k: QCA4019 hw1.0: update board-2.bin
- cirrus: cs35l41: Add support for new HP laptops
- Revert "amdgpu: update GC 11.5.0 firmware"
- linux-firmware: Update amd-ucode copyright information
- linux-firmware: Update AMD cpu microcode
- linux-firmware: Update firmware file for Intel Scorpius core
- linux-firmware: Update firmware file for Intel BlazarIGfP core
- linux-firmware: Update firmware file for Intel BlazarI core
- linux-firmware: Update firmware file for Intel BlazarU-HrPGfP core
- linux-firmware: Update firmware file for Intel BlazarU core
- ath11k: QCA6698AQ hw2.1: update to WLAN.HSP.1.1-04866-QCAHSPSWPL_V1_V2_SILICONZ_IOE-1
- ath11k: QCA2066 hw2.1: update board-2.bin
- qcom: update ADSP firmware for x1e80100 platform, change the license
- qcom: reorder ADSP, CDSP firmware entries for qcs8300 in WHENCE
- Reapply "amdgpu: update SMU 14.0.3 firmware"
- Revert "amdgpu: update SMU 14.0.3 firmware"
- Revert "amdgpu: update GC 10.3.6 firmware"
- Revert "amdgpu: update GC 11.5.1 firmware"
- linux-firmware: update firmware for MT7925 WiFi device
- mediatek MT7925: update bluetooth firmware to 20251124093155
- intel_vpu: Update NPU firmware
- WHENCE: fix version string for video firmware
- qcom: vpu: update video firmware binary for SM8250
- xe: Update GUC to v70.54.0 for BMG, PTL
- Revert "amdgpu: update GC 11.0.1 firmware"
- QCA: Add Bluetooth firmware for WCN685x uart interface
- qcom: Add ADSP firmware for qcs6490-thundercomm-rubikpi3
- qcom: venus-5.4: update firmware binary for v5.4
- qcom: venus-5.4: remove unused firmware file
- iwlwifi: add Sc/Wh FW for core98-181 release
- amdgpu: DMCUB updates for various ASICs
- rtl_bt: Update RTL8852B BT USB FW to 0x42D3_4E04
- ASoC: tas2781: Add more symbol links on SPI devices
- amdgpu: update vega20 firmware
- amdgpu: update vega12 firmware
- amdgpu: update vega10 firmware
- amdgpu: update vangogh firmware
- amdgpu: update renoir firmware
- amdgpu: update yellow carp firmware
- amdgpu: update VCN 3.1.2 firmware
- amdgpu: update PSP 13.0.5 firmware
- amdgpu: update GC 10.3.6 firmware
- amdgpu: update VCN 5.0.0 firmware
- amdgpu: update SMU 14.0.3 firmware
- amdgpu: update PSP 14.0.3 firmware
- amdgpu: update GC 12.0.1 firmware
- amdgpu: update SMU 14.0.2 firmware
- amdgpu: update PSP 14.0.2 firmware
- amdgpu: update GC 12.0.0 firmware
- amdgpu: update VCN 4.0.4 firmware
- amdgpu: update smu 13.0.7 firmware
- amdgpu: update PSP 13.0.7 firmware
- amdgpu: update GC 11.0.2 firmware
- amdgpu: update SMU 13.0.10 firmware
- amdgpu: update SDMA 6.0.3 firmware
- amdgpu: update PSP 13.0.10 firmware
- amdgpu: update GC 11.0.3 firmware
- amdgpu: update smu 13.0.0 kicker firmware
- amdgpu: update PSP 13.0.0 kicker firmware
- amdgpu: update VCN 4.0.0 firmware
- amdgpu: update SMU 13.0.0 firmware
- amdgpu: update PSP 13.0.0 firmware
- amdgpu: update GC 11.0.0 firmware
- amdgpu: update navy flounder firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: update navi14 firmware
- amdgpu: update navi12 firmware
- amdgpu: update navi10 firmware
- amdgpu: update VCN 5.0.1 firmware
- amdgpu: update PSP 13.0.12 firmware
- amdgpu: update GC 9.5.0 firmware
- amdgpu: update PSP 13.0.14 firmware
- amdgpu: update GC 9.4.4 firmware
- amdgpu: update PSP 14.0.5 firmware
- amdgpu: update GC 11.5.3 firmware
- amdgpu: update PSP 14.0.4 firmware
- amdgpu: update GC 11.5.2 firmware
- amdgpu: update green sardine firmware
- amdgpu: update VCN 4.0.3 firmware
- amdgpu: update SDMA 4.4.2 firmware
- amdgpu: update PSP 13.0.6 firmware
- amdgpu: update GC 9.4.3 firmware
- amdgpu: update VCN 4.0.6 firmware
- amdgpu: update PSP 14.0.1 firmware
- amdgpu: update GC 11.5.1 firmware
- amdgpu: update PSP 13.0.11 firmware
- amdgpu: update GC 11.0.4 firmware
- amdgpu: update VCN 4.0.5 firmware
- amdgpu: update PSP 14.0.0 firmware
- amdgpu: update GC 11.5.0 firmware
- amdgpu: update VCN 4.0.2 firmware
- amdgpu: update PSP 13.0.4 firmware
- amdgpu: update GC 11.0.1 firmware
- amdgpu: update beige goby firmware
- amdgpu: update dimgrey cavefish firmware
- amdgpu: update aldebaran firmware
- amdgpu: add vce1 firmware
- mediatek MT7922: update bluetooth firmware to 20251118163447
- linux-firmware: update firmware for MT7922 WiFi device
- qcom: update ADSP, CDSP firmware for kaanapali platform, change the license
- qcom: add ADSP, CDSP firmware for sm8750 platform
- rtl_nic: add firmware rtl9151a-1
- qcom: Update aic100 firmware files
- mt76: add firmware for MT7990
- mt76: update firmware for MT7992
- mt76: update firmware for MT7996
- cirrus: cs35l57: Add firmware for a few Dell products
- cirrus: cs42l45: Add firmware for Cirrus Logic CS42L45 SDCA codec
- qcom: Add sdx35 Foxconn vendor firmware image file
- linux-firmware: Update AMD cpu microcode
Resolves: RHEL-140094

* Tue Nov 11 2025 Denys Vlasenko <dvlasenk@redhat.com> - 20251111-19.1
- Update linux-firmware to latest upstream (RHEL-128447)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- rtl_bt: Update RTL8922A BT USB firmware to 0x41C0_C905
- linux-firmware: add firmware for mt7987 internal 2.5G ethernet phy
- rtw88: 8822b: Update firmware to v30.20.0
- rtl_nic: add firmware rtl8125k-1
- ASoC: tas2781: Update dsp firmware for HP and ASUS projects
- ASoC: tas2781: Update dsp firmware for HP and ASUS projects
- amdgpu: DMCUB updates for various ASICs
- amdgpu: DMCUB updates for various ASICs
- qcom: add SOCCP firmware for kaanapali platform
- xe: Update GUC to v70.53.0 for BMG, LNL, PTL
- i915: Update GUC to v70.53.0 for DG2, MTL
- rtw89: 8851b: update fw to v0.29.41.5
- rtw89: 8852b: update fw to v0.29.128.0 with format suffix -2
- rtw89: 8852b: update fw to v0.29.29.14
- Revert "rtw89: 8852b: update fw to v0.29.128.0"
- rtw89: 8852bt: update fw to v0.29.127.0 with format suffix -1
- rtw89: 8852bt: update fw to v0.29.122.1
- Revert "rtw89: 8852bt: update fw to v0.29.127.0"
- linux-firmware: Update firmware file for Intel BlazarU core
- linux-firmware: Update firmware file for Intel BlazarI core
- linux-firmware: Create audio folder in ti folder, and move all the audio firmwares into it
- amdgpu: DMCUB updates for various ASICs
- linux-firmware: Update WHENCE for microcode_amd_fam19h.bin
- linux-firmware: Update AMD cpu microcode
- linux-firmware: update firmware for MT7925 WiFi device
- mediatek MT7925: update bluetooth firmware to 20251015213201
- rtl_bt: Add firmware and config files for RTL8761CUV
- linux-firmware: Update AMD cpu microcode
- qcom: add ADSP firmware for kaanapali platform
- amdgpu: DMCUB updates for various ASICs
- linux-firmware: Renaming the file to cover a wide range of HP Lunar Lake system.
- mediatek MT7920: update bluetooth firmware to 20251020151255
- linux-firmware: update firmware for MT7922 WiFi device
- linux-firmware: update firmware for MT7920 WiFi device
- amd-ucode: Fix minimum revisions in README
- cirrus: cs35l41: Rename various Asus Laptop firmware files to not have Speaker ID
- mediatek MT7922: update bluetooth firmware to 20251020143443
- Revert "linux-firmware: update firmware for MT7922 WiFi device"
- QCA: Update Bluetooth WCN6856 firmware 2.1.0-00653 to 2.1.0-00659
- iwlwifi: add Bz/Fm and gl FW for core98-161 release
- iwlwifi: update Bz/Hr and Bz/Gf firmwares for core98-161 release
- iwlwifi: update ty/So/Ma firmwares for core98-161 release
- iwlwifi: update cc/Qu/QuZ firmwares for core98-161 release
- intel: qat: Fix missing link
- amdgpu: DMCUB updates for various ASICs
- nvidia: add generic bootloader for GSP-enabled systems
- linux-firmware: qcom: sync audioreach firmwares from v1.0.0 build
- qcom: vpu: rename firmware binaries
- Intel IPU7: Update product signed firmware binary
- i915: Xe2LPD DMC v2.29
- i915: Xe3LPD DMC v2.32
- i915: Xe3LPD_3002 DMC v2.27
- WHENCE: nvidia: rearrange GSP-RM firmware lines
- linux-firmware: Add ISH firmware file for Intel Pather Lake platform
- linux-firmware: Update firmware file for Intel Magnetar core
- linux-firmware: Update firmware file for Intel BlazarU core
- linux-firmware: Update firmware file for Intel BlazarI core
- qcom: add CDSP firmware for kaanapali platform
- qcom: add version for A650 GMU firmware
- qca: Update Bluetooth WCN6750 1.1.3-00091 firmware to 1.1.3-00100
- qcom: Add firmwares for Kaanapali GPU
- qcom: Update A623 GMU fw
- qcom: Fix QCS615 chipset's GPU secure fw
- qcom: Update DSP firmware for sa8775p platform
- amdgpu: DMCUB updates for various ASICs
- WHENCE: remove link for Kaanapali video firmware
- intel_vpu: Update NPU firmware
- linux-firmware: Add Dell ISH firmware for Intel Lunar Lake systems
- Update VCN for Navi1x, Green Sardine and Renoir
- WHENCE: extract multitech license text
- WHENCE: extract ueagle license
- WHENCE: use LICENCE.sensoray for s2255drv
- WHENCE: rename LICENCE.go7007-s2250 to LICENCE.sensoray
- WHENCE: clean up emi62 and yam license statements
- qcom: vpu: update video firmware binary for SM8550
- rtl_bt: Update RTL8852BT/RTL8852BE-VT BT USB FW to 0x3BAC_ADBA
- qcom: vpu: add video firmware for Kaanapali
- qcom: Update DSP firmware for qcs8300 platform.
- qcom: Add Audio topology for HAMOA-EVK
- intel/ish:Add ISH firmware file for Intel Lunar Lake platform
- mediatek: update firmware version info for MT7986/81/16
- linux-firmware: ql2500_fw: update ISP25xx Firmware
- qcom: Update aic100 firmware files
- qcom: Add audio topology and ADSP firmware for qcs6490-radxa-dragon-q6a
- amdgpu: DMCUB updates for various ASICs
- mediatek: mtk_wed: drop links for mt7988
- Revert "amdgpu: update gc 10.3.6 firmware"
- qcom: Update DSP firmware for qcs8300 platform.
- powervr: update firmware for Imagination Technologies BXS-4-64 GPU
- qcom: Update DSP firmware for sa8775p platform.
- amdgpu: DMCUB updates for various ASICs
- ath12k: WCN7850 hw2.0: update board-2.bin
- qcom: move LEMANS EVK firmware to correct location
- amdgpu: update PSP 14.0.3 kicker firmware
- amdgpu: update vega20 firmware
- amdgpu: update vega12 firmware
- amdgpu: update vega10 firmware
- amdgpu: update vangogh firmware
- amdgpu: update VCN 4.0.6 firmware
- amdgpu: update PSP 14.0.1 firmware
- amdgpu: update GC 11.5.1 firmware
- amdgpu: update VCN 4.0.5 firmware
- amdgpu: update VPE 6.1.0 firmware
- amdgpu: update PSP 14.0.0 firmware
- amdgpu: update GC 11.5.0 firmware
- amdgpu: update renoir firmware
- amdgpu: update yellow carp firmware
- amdgpu: update VCN 3.1.2 firmware
- amdgpu: update PSP 13.0.5 firmware
- amdgpu: update GC 10.3.6 firmware
- amdgpu: update PSP 13.0.11 firmware
- amdgpu: update GC 11.0.4 firmware
- amdgpu: update VCN 4.0.2 firmware
- amdgpu: update PSP 13.0.4 firmware
- amdgpu: update GC 11.0.1 firmware
- amdgpu: update VCN 5.0.0 firmware
- amdgpu: update PSP 14.0.3 firmware
- amdgpu: update GC 12.0.1 firmware
- amdgpu: update SMU 14.0.2 firmware
- amdgpu: update PSP 14.0.2 firmware
- amdgpu: update GC 12.0.0 firmware
- amdgpu: update VCN 4.0.4 firmware
- amdgpu: update PSP 13.0.7 firmware
- amdgpu: update GC 11.0.2 firmware
- amdgpu: update SMU 13.0.10 firmware
- amdgpu: update PSP 13.0.10 firmware
- amdgpu: update GC 11.0.3 firmware
- amdgpu: update SMU 13.0.0 kicker firmware
- amdgpu: update PSP 13.0.0 kicker firmware
- amdgpu: update VCN 4.0.0 firmware
- amdgpu: update SDMA 6.0.0 firmware
- amdgpu: update SMU 13.0.0 firmware
- amdgpu: update PSP 13.0.0 firmware
- amdgpu: update GC 11.0.0 firmware
- amdgpu: update beige goby firmware
- amdgpu: update dimgrey cavefish firmware
- amdgpu: update navy flounder firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: update navi14 firmware
- amdgpu: update navi12 firmware
- amdgpu: update navi10 firmware
- amdgpu: update VCN 5.0.1 firmware
- amdgpu: update PSP 13.0.12 firmware
- amdgpu: update GC 9.5.0 firmware
- amdgpu: update PSP 13.0.14 firmware
- amdgpu: update GC 9.4.4 firmware
- amdgpu: update SDMA 6.1.3 firmware
- amdgpu: update PSP 14.0.5 firmware
- amdgpu: update GC 11.5.3 firmware
- amdgpu: update VPE 6.1.3 firmware
- amdgpu: update PSP 14.0.4 firmware
- amdgpu: update GC 11.5.2 firmware
- amdgpu: update green sardine firmware
- amdgpu: update VCN 4.0.3 firmware
- amdgpu: update PSP 13.0.6 firmware
- amdgpu: update GC 9.4.3 firmware
- linux-firmware: update firmware for en8811h 2.5G ethernet phy
- amdgpu: DMCUB updates for various ASICs
- intel/ish: Add firmware for LENOVO THINKPAD X1 2-in-1 Gen 10
- mediatek MT7922: update bluetooth firmware to 20250903123504
- linux-firmware: update firmware for MT7922 WiFi device
- qcom: move Monaco EVK topology from qcs8275 to qcs8300 subdir
- qcom: Add Audio topology for MONACO-EVK
- qcom: add CDSP firmware for qcs615 platform
- qcom: Add Audio topology for LEMANS-EVK
- ath12k: WCN7850 hw2.0@ncm865: add to WLAN.IOE_HMT.1.1-00018-QCAHMTSWPL_V1.0_V2.0_SILICONZ-1
- linux-firmware: update firmware for MT7925 WiFi device
- mediatek MT7925:update bluetooth firmware to 20250825220109 Update binary firmware for MT7925 BT devices.
- qcom: vpu: update firmware binaries to fix encoder drain handling
- intel_vpu: Update NPU firmware
- Revert "cs35l56: Rename firmware for Thinkbook 16P Gen6 (17AA3921) without multiple speakers"
- cs35l56: Rename firmware for Thinkbook 16P Gen6 (17AA3921) without multiple speakers
- xe: Update GUC to v70.49.4 for BMG, LNL, PTL
- i915: Update GUC to v70.49.4 for ADL-P, DG1, DG2, MTL, TGL
- qcom: add ADSP firmware for qcs615 platform
- rtl_bt: Update RTL8822C BT USB firmware to 0x2B66_D962
- iwlwifi: add Bz-HR FW for core90-93 release
- Fix link entry for qat_895xcc.bin
- Move QAT firmware to intel/ subdirectory
- Move all iwlwifi top level files to intel/ directory
- Revert "intel/ish: Add firmware for LENOVO THINKPAD X1 2-in-1 Gen 10"
- ath11k: Support WCN6855 hw2.1 with NFA firmware variant
- amdgpu: Update ISP FW for isp v4.1.1
- Update README.md to clarify S-o-b requirements
- firmware: qcom: Reorder VPU firmware entries in WHENCE
- intel_vpu: Update NPU firmware
- amdgpu: DMCUB updates for various ASICs
- intel/ish: Add firmware for LENOVO THINKPAD X1 2-in-1 Gen 10
- cirrus: cs35l41: Move entries to correct driver section in WHENCE
- cirrus: cs35l56: Update firmware for Cirrus Amps for some Lenovo laptops
- ath11k: WCN6855 hw2.0@nfa765: add to WLAN.HSP.1.1-04685-QCAHSPSWPL_V1_V2_SILICONZ_IOE-1
- cirrus: cs35l56: Add firmware for Cirrus Amps for some Lenovo laptops
- qcom: Add firmware binary for SM8650.
- Link rtl8723b_config.bin to rtl8723bs
- rtw89: 8922a: update fw to v0.35.80.3
- rtw89: 8852c: update fw to v0.27.129.4
- rtw89: 8852c: update fw to v0.27.129.3
- qcom: add CDSP firmware for x1e80100 platform
- iwlwifi: add Bz/gl FW for core97-84 release
- iwlwifi: update ty/So/Ma firmwares for core97-84 release
- iwlwifi: update cc/Qu/QuZ firmwares for core97-84 release
- amdgpu: DMCUB updates for various ASICs
- realtek: rt1321: Add patch firmware of MCU
- mediatek: Add MT8189 SCP firmware
Resolves: RHEL-128447

* Tue Aug 12 2025 Denys Vlasenko <dvlasenk@redhat.com> - 20250812-19
- Update linux-firmware to latest upstream (RHEL-108921)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- amdgpu: DMCUB updates for various ASICs
- panthor: Add firmware for more Mali GPUs
- amdgpu: update renoir firmware
- amdgpu: add SMU 14.0.3 kicker firmware
- amdgpu: add PSP 14.0.3 firmware
- amdgpu: add GC 12.0.1 kicker firmware
- amdgpu: update navy flounder firmware
- amdgpu: update SDMA 6.1.2 firmware
- amdgpu: update PSP 14.0.4 firmware
- amdgpu: update GC 11.5.2 firmware
- amdgpu: update yellow carp firmware
- amdgpu: update VCN 5.0.0 firmware
- amdgpu: update SDMA 7.0.1 firmware
- amdgpu: update PSP 14.0.3 firmware
- amdgpu: update GC 12.0.1 firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: update vega20 firmware
- amdgpu: update SDMA 7.0.0 firmware
- amdgpu: update PSP 14.0.2 firmware
- amdgpu: update GC 12.0.0 firmware
- amdgpu: update vega12 firmware
- amdgpu: update vega10 firmware
- amdgpu: update VCN 3.1.2 firmware
- amdgpu: update PSP 13.0.5 firmware
- amdgpu: update GC 10.3.6 firmware
- amdgpu: update VCN 4.0.4 firmware
- amdgpu: update SDMA 6.0.2 firmware
- amdgpu: update PSP 13.0.7 firmware
- amdgpu: update GC 11.0.2 firmware
- amdgpu: update navi14 firmware
- amdgpu: update SDMA 6.0.3 firmware
- amdgpu: update PSP 13.0.10 firmware
- amdgpu: update GC 11.0.3 firmware
- amdgpu: update navi12 firmware
- amdgpu: update vangogh firmware
- amdgpu: update navi10 firmware
- amdgpu: update PSP 13.0.0 kicker firmware
- amdgpu: update VCN 5.0.1 firmware
- amdgpu: update PSP 13.0.12 firmware
- amdgpu: update GC 9.5.0 firmware
- amdgpu: update VCN 4.0.0 firmware
- amdgpu: update SDMA 6.0.0 firmware
- amdgpu: update GC 11.0.0 firmware
- amdgpu: update PSP 13.0.14 firmware
- amdgpu: update PSP 13.0.6 firmware
- amdgpu: update GC 9.4.3 firmware
- amdgpu: update vpe 6.1.1 firmware
- amdgpu: update VCN 4.0.6 firmware
- amdgpu: update SDMA 6.1.1 firmware
- amdgpu: update PSP 14.0.1 firmware
- amdgpu: update GC 11.5.1 firmware
- amdgpu: update PSP 13.0.11 firmware
- amdgpu: update GC 11.0.4 firmware
- amdgpu: update beige goby firmware
- amdgpu: update PSP 13.0.8 firmware
- amdgpu: update GC 10.3.7 firmware
- amdgpu: update VCN 4.0.5 firmware
- amdgpu: update PSP 14.0.0 firmware
- amdgpu: update GC 11.5.0 firmware
- amdgpu: update VCN 4.0.2 firmware
- amdgpu: update SDMA 6.0.1 firmware
- amdgpu: update PSP 13.0.4 firmware
- amdgpu: update GC 11.0.1 firmware
- amdgpu: update dimgrey_cavefish firmware
- amdgpu: update aldebaran firmware
- qca: Update Bluetooth WCN6750 1.1.3-00069 firmware to 1.1.3-00091
- qcom: Add QDSP firmware file for Qualcomm QDU100 device.
- ath12k: WCN7850 hw2.0: update to WLAN.HMT.1.1.c5-00302-QCAHMTSWPL_V1.0_V2.0_SILICONZ-1.115823.3
- ath12k: QCN9274 hw2.0: update to WLAN.WBE.1.5-01651-QCAHKSWPL_SILICONZ-1
- ath11k: WCN6855 hw2.0: update board-2.bin
- ath11k: QCA6698AQ hw2.1: update to WLAN.HSP.1.1-04650-QCAHSPSWPL_V1_V2_SILICONZ_IOE-2
- ath11k: QCA2066 hw2.1: update to WLAN.HSP.1.1-03926.13-QCAHSPSWPL_V2_SILICONZ_CE-2.52297.9
- ath11k: QCA2066 hw2.1: update board-2.bin
- qcom: Update xbl_config firmware file.
- amdgpu: Update GCN 4.0.5 microcode
- amdgpu: Update SDMA 6.1.0 microcode
- amdgpu: Update GC 11.5.0 microcode
- qcom: Add QDU100 firmware image files required for booting.
- linux-firmware: Add firmware for airoha-npu driver
- linux-firmware: update firmware for MT7925 WiFi device
- mediatek MT7925: update bluetooth firmware to 20250721233113
- qcom: Update DSP firmware for qcm6490 platform
- qcom: update Venus firmware file for v6.0
- i915: Xe3LPD DMC v2.29
- linux-firmware: Update AMD cpu microcode
- qcom: Add QCS6490 symlink for QUPv3 firmware
- qcom: Add firmware binary for SM8750.
- amdgpu: update dmcub fw for dcn314
- cirrus: cs35l41: Add Firmware for various ASUS commercial Laptops using CS35L41 HDA
- cirrus: cs35l41: Update Firmware for Dell Oasis
- cirrus: cs35l56: Add firmware for Cirrus CS35L56 for various Dell laptops
- qcom: Add Audio topology for QCS6490 RB3Gen2
- intel_vpu: Update NPU firmware
- amdgpu: update dmcub fw for various DCN version
- WHENCE: extract more license statements
- WHENCE: clarify io_ti origin
- amdgpu: Update GC 11.5.1 microcode
- rtw89: 8852b: update fw to v0.29.128.0
- rtw89: 8852bt: update fw to v0.29.127.0
- rtw89: 8922a: add regd fw element with version R72-R6
- rtw89: 8852c: add regd fw element with version R72-R57
- rtw89: 8922a: update BB parameter V49
- qcom: Update gpu firmwares of QCS615 chipset
- linux-firmware: Update firmware file for Intel Solar core
- linux-firmware: Update firmware file for Intel BlazarU core
- linux-firmware: Update firmware file for Intel BlazarI core
Resolves: RHEL-108921

* Tue Jul 08 2025 Denys Vlasenko <dvlasenk@redhat.com> - 20250708-18
- nvidia-gpu-firmware was missing firmware/nvidia/ad10{3,4,6,7} directories (RHEL-95393)
- Resume after suspend-to-ram did not restore screen on some AMD GPUs (RHEL-100947)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- xe: Add fan_control v203.0.0.0 for BMG
- amdgpu: Add DCN 3.6
- amdgpu: Add PSP 14.0.5
- amdgpu: Add SDMA 6.1.3
- amdgpu: Add GC 11.5.3
- mediatek MT7921: update bluetooth firmware to 20250625154126
- qcom/adreno: document firmware revisions
- qcom/adreno: move A610 and A702 ZAP files to Adreno driver section
- qcom: Add sdx61 Foxconn vendor firmware image file
- Revert "linux-firmware: Update firmware file for Intel Pulsar core"
- qcom/adreno: sort entries in WHENCE
- xe: First HuC release for Pantherlake
- xe: First GuC release for Pantherlake
- linux-firmware: update firmware for MT7921 WiFi device
- rtw89: 8922a: update fw to v0.35.80.0
- rtw89: 8852c: update fw to v0.27.129.1
- rtw89: 8852c: update fw to v0.27.128.0
- WHENCE: extract license texts
- WHENCE: expand the advansys license statement
- WHENCE: some older AMD drivers are MIT licensed
- qcom: update firmware binary for SM8550
- amdgpu: DMCUB updates for DCN401
- qcom: venus-5.4: add the firmware binary for qcs615
- Revert "qcom: Add sdx61 Foxconn vendor firmware image file"
- amdgpu: update dmcub fw for dcn401
- qcom: Add sdx61 Foxconn vendor firmware image file
- brcm: Fix symlinks for Khadas VIM SDIO wifi config
- amdgpu: update renoir firmware
- amdgpu: update vcn 5.0.0 firmware
- amdgpu: update smu 14.0.3 firmware
- amdgpu: update sdma 7.0.1 firmware
- amdgpu: update psp 14.0.3 firmware
- amdgpu: update gc 12.0.1 firmware
- amdgpu: update navy flounder firmware
- amdgpu: update psp 14.0.4 firmware
- amdgpu: update gc 11.5.2 firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: add raven2 ip discovery firmware
- amdgpu: update smu 14.0.2 firmware
- amdgpu: update sdma 7.0.0 firmware
- amdgpu: update psp 14.0.2 firmware
- amdgpu: update gc 12.0.0 firmware
- amdgpu: update vcn 4.0.6 firmware
- amdgpu: update psp 14.0.1 firmware
- amdgpu: update gc 11.5.1 firmware
- amdgpu: update psp 13.0.11 firmware
- amdgpu: update gc 11.0.4 firmware
- amdgpu: add picasso ip discovery firmware
- amdgpu: add raven ip discovery firmware
- amdgpu: update vega20 firmware
- amdgpu: update vega12 firmware
- amdgpu: update smu 13.0.7 firmware
- amdgpu: update vcn 4.0.4 firmware
- amdgpu: update psp 13.0.7 firmware
- amdgpu: update gc 11.0.2 firmware
- amdgpu: update navi14 firmware
- amdgpu: update vega10 firmware
- amdgpu: update gc 10.3.6 firmware
- amdgpu: update smu 13.0.10 firmware
- amdgpu: update psp 13.0.10 firmware
- amdgpu: update gc 11.0.3 firmware
- amdgpu: update navi12 firmware
- amdgpu: update vangogh firmware
- amdgpu: update navi10 firmware
- amdgpu: add smu 13.0.0 kicker firmware
- amdgpu: add psp 13.0.0 kicker firmware
- amdgpu: add gc 11.0.0 kicker firmware
- amdgpu: add vcn 5.0.1 firmware
- amdgpu: add sdma 4.4.4 firmware
- amdgpu: add psp 13.0.12 firmware
- amdgpu: add gc 9.5.0 firmware
- amdgpu: add arcturus IP discovery firmware
- amdgpu: update vcn 4.0.0 firmware
- amdgpu: update smu 13.0.0 firmware
- amdgpu: update psp 13.0.0 firmware
- amdgpu: update gc 11.0.0 firmware
- amdgpu: update psp 13.0.14 firmware
- amdgpu: update gc 9.4.4 firmware
- amdgpu: update psp 13.0.6 firmware
- amdgpu: update gc 9.4.3 firmware
- amdgpu: update beige_goby firmware
- amdgpu: update vcn 4.0.5 firmware
- amdgpu: update gc 11.5.0 firmware
- amdgpu: update vcn 4.0.2 firmware
- amdgpu: update gc 11.0.1 firmware
- amdgpu: update dimgrey_cavefish firmware
- amdgpu: update aldebaran firmware
- WHENCE: fix subtly incorrect licensing
- amdgpu: update dmcub fw for dcn32 and dcn401
- mediatek: Update mt8186 SCP firmware
- amdgpu: Update DMCUB fw for DCN401 & DCN315
- WHENCE: unify Driver statements
- qcom: add gpu firmwares for X1P42100 chipset
- QCA: Update WCN785x btusb firmware to 2.0.0-00799-5
- rtl_nic: update firmware of RTL8153A
- qcom: sc8280xp: Updated power FW for X13s
- linux-firmware: update firmware for MT7986
- linux-firmware: update firmware for MT7981
- linux-firmware: update firmware for MT7916
- cirrus: cs35l41: Add Firmware for ASUS NUC using CS35L41
- Revert "iwlwifi: add Bz/gl FW for core96-76 release"
- amdgpu: DMCUB updates for various ASICs
- mediatek MT7922: update bluetooth firmware to 20250523103438
- mediatek MT7921: update bluetooth firmware to 20250523111333
- linux-firmware: update firmware for MT7922 WiFi device
- linux-firmware: update firmware for MT7921 WiFi device
Resolves: RHEL-95393, RHEL-100947

* Wed Jun 04 2025 Denys Vlasenko <dvlasenk@redhat.com> - 20250604-17
- 1.3.41.0 DDP firmware does not support QS silicon E825C nics (RHEL-92555)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- xe: Update GUC to v70.45.2 for BMG, LNL
- i915: Update GUC to v70.45.2 for DG2
- xe: Update LNL GSC to v104.0.5.1429
- amdgpu: DMCUB updates for various ASICs
- qcom: add QUPv3 firmware for QCS8300 platform
- Intel IPU7: Add firmware binary files
- ice: update wireless_edge package to 1.3.23.0
- ice: update comms package to 1.3.55.0
- ice: update package to 1.3.43.0
- linux-firmware: Update firmware file for Intel Pulsar core
- linux-firmware: Update firmware file for Intel BlazarI core
- linux-firmware: Update firmware file for Intel Quasar core
- linux-firmware: Update firmware file for Intel Solar core
- linux-firmware: Update firmware file for Intel Magnetar core
- linux-firmware: Update firmware file for Intel BlazarU core
- iwlwifi: add Bz/gl FW for core96-76 release
- iwlwifi: update ty/So/Ma firmwares for core96-76 release
- iwlwifi: update cc/Qu/QuZ firmwares for core96-76 release
- iwlwifi: update firmwares for 8000 series
- iwlwifi: update 7265D firmware
- mediatek MT7925: update bluetooth firmware to 20250526153203
- linux-firmware: update firmware for MT7925 WiFi device
- qcom: sc8280xp: FW blob updates for X13s
- brcm: Add symlinks for Khadas VIM SDIO wifi config to AW-CM256SM.txt
- ath12k: WCN7850 hw2.0: update to WLAN.HMT.1.1.c5-00284.1-QCAHMTSWPL_V1.0_V2.0_SILICONZ-3
- cirrus: cs35l41: Fix firmware links for several ASUS laptops
Resolves: RHEL-92555

* Wed May 21 2025 Denys Vlasenko <dvlasenk@redhat.com> - 20250521-16
- accel: NPU: Update linux-firmware to include firmware for device (RHEL-85120)
- Add amdnpu linux firmware folder (RHEL-77950)
- Introduce new PMF TA (RHEL-86837)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- cirrus: cs35l41: Add Firmware for various HP Agusta Laptops using CS35L41 HDA
- Adjust QUPv3 driver name
- cnm: Add Chips&Media wave633c firmware for NXP i.MX9
- qcom: add QUPv3 firmware for QCM6490 platform
- mediatek: Add mt8196 VCP firmware
- cirrus: cs35l41: Add Firmware for various ACER Laptops using CS35L41 HDA
- nvidia: add GSP-RM version 570.144 firmware images
- amdgpu: DMCUB updates for various ASICs
- powervr: add firmware for Imagination Technologies BXS-4-64 GPU
- rtl_bt: Update RTL8822C BT USB and UART firmware to 0x7C20
- brcmfmac: Add a couple of NanoPi devices
- rtl_nic: add firmware rtl8127a-1
- cnm: update chips&media wave521c firmware.
- intel_vpu: Update NPU firmware
- intel: avs: Update topology file for Digital Microphone Array
- amdgpu: updates for dcn 3.20 and dcn 4.01 firmware to 0.1.10.0
- linux-firmware: Amphion: Update vpu firmware
- amd_pmf: Update AMD PMF TA Firmware to v3.1
- amdgpu: update dcn 4.01 firmware to 0.1.8.0
- qcom: Add link for SM8350 GPU firmware
- cirrus: cs35l56: Add firmware for Cirrus Amps for some Lenovo laptops
- cirrus: cs35l56: Add firmware for Cirrus Amps for some ASUS laptops
- cirrus: cs35l56: Update firmware for Cirrus Amps for some Lenovo laptops
- cirrus: cs35l56: Update firmware for Cirrus Amps for some Dell laptops
- linux-firmware: update firmware for MT7925 WiFi device
- mediatek MT7925: update bluetooth firmware to 20250425073330
- rtw89: 8852c: add tables for dynamic antenna TXPWR
- rtw89: 8922a: update fw to v0.35.71.0
- brcm: Add NVRAM file for Radxa Rock Pi X mini PC
- i915: Update Xe3LPD DMC to v2.23
- rtl_bt: Update RTL8852B BT USB FW to 0x098B_154B
- ath11k: WCN6855 hw2.0: update board-2.bin
- ath11k: IPQ5018 hw1.0: update to WLAN.HK.2.6.0.1-01300-QCAHKSWPL_SILICONZ-1
- ath12k: WCN7850 hw2.0: update to WLAN.HMT.1.1.c5-00284-QCAHMTSWPL_V1.0_V2.0_SILICONZ-3
- ath12k: QCN9274 hw2.0: update board-2.bin
- qcom: vpu: update video firmware binary for SA8775p
- iwlwifi: add Bz/gl FW for core95-82 release
- iwlwifi: update ty/So/Ma firmwares for core95-82 release
- iwlwifi: update cc/Qu/QuZ firmwares for core95-82 release
- iwlwifi: add Bz-hr FW for core93-123 release
- qcom: add QUPv3 firmware for QCS9100 platform
- ASoC: tas2781: Swap channel for SPI projects.
- bmi260: Add BMI260 IMU initial configuration data file
- rtl_bt: Update RTL8852BT/RTL8852BE-VT BT USB FW to 0x1881_BA06
- rtw89: 8922a: update element RF TXPWR to R40
- rtw89: 8852c: update element RF TXPWR to R78
- rtw89: 8852c: add fw v0.27.125.0 with format version 2
- Revert "rtw89: 8852c: update fw to v0.27.125.0"
- qcom: vpu: add video firmware binary for qcm6490
- contrib: process_linux_firmware: set user agent
- amdgpu: update vcn 4.0.5 firmware
- amdgpu: update psp 14.0.0 firmware
- amdgpu: update vcn 4.0.2 firmware
- amdgpu: update psp 13.0.4 firmware
- amdgpu: update gc 11.0.1 firmware
- amdgpu: update navy flounder firmware
- amdgpu: update psp 14.0.4 firmware
- amdgpu: update gc 11.5.2 firmware
- amdgpu: update vcn 5.0.0 firmware
- amdgpu: update smu 14.0.3 firmware
- amdgpu: update psp 14.0.3 firmware
- amdgpu: update gc 12.0.1 firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: update yellow carp firmware
- amdgpu: update smu 14.0.2 firmware
- amdgpu: update psp 14.0.2 firmware
- amdgpu: update gc 12.0.0 firmware
- amdgpu: update vega20 firmware
- amdgpu: update navi14 firmware
- amdgpu: update vega12 firmware
- amdgpu: update vcn 4.0.4 firmware
- amdgpu: update smu 13.0.7 firmware
- amdgpu: update psp 13.0.7 firmware
- amdgpu: update gc 11.0.2 firmware
- amdgpu: update vega10 firmware
- amdgpu: update psp 13.0.5 firmware
- amdgpu: update navi12 firmware
- amdgpu: update psp 13.0.10 firmware
- amdgpu: update gc 11.0.3 firmware
- amdgpu: update navi10 firmware
- amdgpu: update vangogh firmware
- amdgpu: update picasso firmware
- amdgpu: update vcn 4.0.0 firmware
- amdgpu: update psp 13.0.0 firmware
- amdgpu: update gc 11.0.0 firmware
- amdgpu: update psp 13.0.14 firmware
- amdgpu: update gc 9.4.4 firmware
- amdgpu: update arcturus firmware
- amdgpu: update psp 13.0.6 firmware
- amdgpu: update gc 9.4.3 firmware
- amdgpu: update beige goby firmware
- amdgpu: update psp 13.0.8 firmware
- amdgpu: update psp 14.0.1 firmware
- amdgpu: update gc 11.5.1 firmware
- amdgpu: update psp 13.0.11 firmware
- amdgpu: update gc 11.0.4 firmware
- amdgpu: update dimgrey cavefish firmware
- amdgpu: update aldebaran firmware
- amdgpu: update dcn 4.01 frmware to 0.1.6.0
- intel: ish: Update license file for ISH
- intel: avs: Update topology file for I2S Analog Devices 4567
- intel: avs: Update topology file for I2S Realtek 5663
- intel: avs: Update topology file for I2S Realtek 5640
- intel: avs: Update topology file for I2S Realtek 5514
- intel: avs: Update topology file for I2S Realtek 298
- intel: avs: Update topology file for I2S Realtek 286
- intel: avs: Update topology file for I2S Realtek 274
- intel: avs: Update topology file for I2S Nuvoton 8825
- intel: avs: Update topology file for I2S Maxim 98927
- intel: avs: Update topology file for I2S Maxim 98373
- intel: avs: Update topology file for I2S Maxim 98357a
- intel: avs: Update topology file for HDAudio codecs
- intel: avs: Update topology file for HDMI codecs
- intel: avs: Update topology file for Digital Microphone Array
- intel: avs: Update topology file for I2S Dialog 7219
- xe: Update GUC to v70.44.1 for BMG and LNL
- i915: Update GUC to v70.44.1 for i915 platforms
- qcom:x1e80100: Iris Support for Lenovo T14s G6 Qualcomm platform
- qcom:x1e80100: Support for Lenovo Yoga Slim 7 Snapdragon platform
- Mellanox: Add new mlxsw_spectrum firmware xx.2014.4012
- linux-firmware: add firmware for Aeonsemi AS21x1x 1G/2.5G/5G/10G Ethernet Phy
- QCA: Add 8 bluetooth nvm files for WCN785x btusb
- QCA: Update WCN785x btusb firmware to 2.0.0-00790-3
- qcom: update firmware binary for SM8250
- mediatek: Add new mt8195 SOF firmware
- mediatek: Add new mt8188 SOF firmware
- rtl_bt: Update RTL8852BT/RTL8852BE-VT BT USB FW to 0x17E9_16ED
- Revert "rtl_bt: Update RTL8852BT/RTL8852BE-VT BT USB FW to 0x0471_70A6"
- intel_vpu: Update NPU firmware
- cirrus: cs35l56: Correct filenames of SSID 103c8e1b and 103c8e1c
- rtl_bt: Update RTL8852BT/RTL8852BE-VT BT USB FW to 0x0471_70A6
- amdgpu: update dcn 3.5 and dcn 3.5.1 firmware to 9.0.27.0
- amdgpu: update dcn 3.1.4 firmware to 8.0.78.0
- amdgpu: update dcn 4.01 firmware to 0.1.3.0
- amdgpu: update dcn 3.5 firmware to 0.1.0.0
- cirrus: cs35l41: Add Firmware for various HP Laptops using CS35L41 HDA
- cirrus: Add cs35l56 firmware symlinks for Asus UM5606KA
- qcom: Add DSP firmware for QCS8300 platform
- mediatek: Add MT8188 SCP firmware
- copy-firmware: fail gracefully if moreutils parallel is installed
- copy-firmware: make script smarter about bad parameters
- copy-firmware: add usage help text
- linux-firmware: Update firmware file for Intel BlazarI core
- qcom: Add Audio firmware for Lenovo Slim 7x
- qcom: Add Audio firmware for Lenovo T14s
- amdgpu: DMCUB updates for various ASICs
Resolves: RHEL-85120, RHEL-77950, RHEL-86837

* Fri Mar 14 2025 Denys Vlasenko <dvlasenk@redhat.com> - 20250314-15
- accel: ivpu: Update firmware for NPU (RHEL-38586)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- rtw88: Add firmware v33.6.0 for RTL8814AE/RTL8814AU
- rtw89: 8922a: update fw to v0.35.64.0
- rtw89: 8922a: update fw to v0.35.63.0
- rtw89: 8852c: update fw to v0.27.125.0
- iwlwifi: add Bz/gl FW for core94-91 release
- iwlwifi: update ty/So/Ma firmwares for core94-91 release
- iwlwifi: update cc/Qu/QuZ firmwares for core94-91 release
- amdgpu: update psp 14.0.0 firmware
- amdgpu: update gc 11.5.0 firmware
- amdgpu: update vcn 4.0.2 firmware
- amdgpu: update psp 13.0.4 firmware
- amdgpu: update gc 11.0.1 firmware
- amdgpu: update navy flounder firmware
- amdgpu: update gc 11.5.2 firmware
- amdgpu: update vcn 5.0.0 firmware
- amdgpu: update smu 14.0.3 firmware
- amdgpu: update sdma 7.0.1 firmware
- amdgpu: update gc 14.0.3 firmware
- amdgpu: update gc 12.0.1 firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: update yellow carp firmware
- amdgpu: update smu 14.0.2 firmware
- amdgpu: update psp 14.0.2 firmware
- amdgpu: update gc 12.0.0 firmware
- amdgpu: update vega20 firmware
- amdgpu: update navi14 firmware
- amdgpu: update vega12 firmware
- amdgpu: update vcn 4.0.4 firmware
- amdgpu: update psp 13.0.7 firmware
- amdgpu: update gc 11.0.2 firmware
- amdgpu: update vega10 firmware
- amdgpu: update vcn 3.1.2 firmware
- amdgpu: update gc 10.3.6 firmware
- amdgpu: update navi10 firmware
- amdgpu: update navi12 firmware
- amdgpu: update psp 13.0.10 firmware
- amdgpu: update gc 11.0.3 firmware
- amdgpu: update vangogh firmware
- amdgpu: update picasso firmware
- amdgpu: update vcn 4.0.0 firmware
- amdgpu: update psp 13.0.0 firmware
- amdgpu: update gc 11.0.0 firmware
- amdgpu: update psp 13.0.14 firmware
- amdgpu: update gc 9.4.4 firmware
- amdgpu: update psp 13.0.6 firmware
- amdgpu: update gc 9.4.3 firmware
- amdgpu: update beige goby firmware
- amdgpu: update gc 10.3.7 firmware
- amdgpu: update psp 14.0.1 firmware
- amdgpu: update gc 11.5.1 firmware
- amdgpu: update gc 11.0.4 firmware
- amdgpu: update dimgrey cavefish firmware
- amdgpu: update aldebaran firmware
- qcom: Update gpu firmwares for qcs8300 chipset
- linux-firmware: add firmware for qat_420xx devices
- amdgpu: DMCUB updates for various ASICs
- i915: Update Xe3LPD DMC to v2.20
- linux-firmware: update firmware for MT7925 WiFi device
- mediatek MT7925: update bluetooth firmware to 20250305133215
- mediatek MT7920: update bluetooth firmware to 20250210151502
- linux-firmware: Update firmware file for Intel BlazarU core
- linux-firmware: Update firmware file for Intel BlazarI core
- intel_vpu: Add firmware for 37xx and 40xx NPUs
- QCA: Add Bluetooth firmwares for QCA2066 with USB transport
- QCA: Add two bluetooth firmware nvm files for QCA2066
- QCA: Update Bluetooth QCA2066 firmware to 2.1.0-00653
- QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00653
- cirrus: cs35l41: Add firmware and tuning for ASUS Consumer laptops
- cirrus: cs35l41: Add Firmware for various ASUS Commercial laptops
- ASoC: tas2781: Update dsp firmware for Gemtree project
- xe: Update GUC to v70.40.2 for BMG, LNL
- amdgpu: DMCUB updates for various ASICs
- amdgpu: DCUB update for DCN401 and DCN315
- cirrus: cs35l41: Add firmware and tunings for CS35L41 driver for Steam Deck
- ath11k: QCN9074 hw1.0: update to WLAN.HK.2.9.0.1-02175-QCAHKSWPL_SILICONZ-2
- ath11k: QCA6698AQ hw2.1: update to WLAN.HSP.1.1-04604-QCAHSPSWPL_V1_V2_SILICONZ_IOE-1
- ath11k: QCA6698AQ hw2.1: update board-2.bin
- rtw89: 8852bt: update fw to v0.29.122.0 and BB parameter to 07
- linux-firmware: Update AMD SEV firmware
- linux-firmware: update firmware for MT7920 WiFi device
- qca: update WCN3988 firmware
- amdgpu: Update ISP FW for isp v4.1.1
- qcom: add firmware for Adreno A225
- cirrus: cs35l56: Add and update firmware for Cirrus CS35L56 for two HP laptops
- cirrus: cs35l56: Add firmware for Cirrus Amps for some ASUS laptops
- cirrus: cs35l56: Add and update firmware for Cirrus CS35L56 for various Lenovo laptops
- cirrus: cs35l56: Update firmware for Cirrus Amps for some Dell laptops
- linux-firmware: update firmware for en8811h 2.5G ethernet phy
- i915: Update Xe3LPD DMC to v2.17
- ASoC: tas2781: Change regbin firmwares for single device
Resolves: RHEL-38586

* Tue Feb 25 2025 Denys Vlasenko <dvlasenk@redhat.com> - 20250212-14
- accel: ivpu: Update firmware for NPU (RHEL-38586)
Resolves: RHEL-38586

* Wed Feb 12 2025 Denys Vlasenko <dvlasenk@redhat.com> - 20250212-13
- Missing firmware for the enablement of TI AMP TAS2781 SPI driver (RHEL-78328)
- MI325 GPU firmware (RHEL-78328)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- i915: Update Xe2LPD DMC to v2.28
- ASoC: tas2781: Add regbin firmware by index for single device
- WHENCE: qca: add missing version information
- WHENCE: split generic QCA section into USB and serial sections
- rtl_bt: Update RTL8852B BT USB FW to 0x0474_842D
- iwlwifi: add Bz/gl FW for core93-123 release
- iwlwifi: update ty/So/Ma firmwares for core93-123 release
- iwlwifi: update cc/Qu/QuZ firmwares for core93-82 release
- ASoC: tas2781: Add dsp firmware for new projects
- amdgpu: DMCUB update for DCN401
- ath12k: WCN7850 hw2.0: update board-2.bin
- ath12k: QCN9274 hw2.0: update to WLAN.WBE.1.4.1-00199-QCAHKSWPL_SILICONZ-1
- ath12k: QCN9274 hw2.0: update board-2.bin
- ath11k: WCN6750 hw1.0: update board-2.bin
- ath11k: QCN9074 hw1.0: update to WLAN.HK.2.9.0.1-02146-QCAHKSWPL_SILICONZ-1
- ath11k: QCA6698AQ hw2.1: add to WLAN.HSP.1.1-04479-QCAHSPSWPL_V1_V2_SILICONZ_IOE-1
- ath11k: QCA6698AQ hw2.1: add board-2.bin
- ath11k: QCA6390 hw2.0: update board-2.bin
- ath11k: QCA2066 hw2.1: update to WLAN.HSP.1.1-03926.13-QCAHSPSWPL_V2_SILICONZ_CE-2.52297.6
- ath11k: QCA2066 hw2.1: update board-2.bin
- ath11k: IPQ8074 hw2.0: update to WLAN.HK.2.9.0.1-02146-QCAHKSWPL_SILICONZ-1
- ath11k: IPQ6018 hw1.0: update to WLAN.HK.2.7.0.1-02409-QCAHKSWPL_SILICONZ-1
- copy-firmware: Fix 'No such file or directory' error.
- ath11k: add device-specific firmware for QCM6490 boards
- qca: add more WCN3950 1.3 NVM files
- qca: add firmware for WCN3950 chips
- qca: move QCA6390 firmware to separate section
- qca: restore licence information for WCN399x firmware
- amdgpu: DMCUB updates for various ASICs
- amdgpu: DMCUB updates forvarious AMDGPU ASICs
- Merge https://github.com/quicjathot/bt_msl_fw_1.1.3_00069 into wcn6750
- qca: Update Bluetooth WCN6750 1.1.0-00476 firmware to 1.1.3-00069
- qcom:x1e80100: Support for Lenovo T14s G6 Qualcomm platform
- qcom:x1e80100: Support for Lenovo T14s G6 Qualcomm platform
- linux-firmware: Update FW files for MRVL SD8997 chips
- i915: Update Xe2LPD DMC to v2.27
- Merge https://github.com/vivesahu-qcom/bt_hsp_fw650 into wcn6856
- qca: Update Bluetooth WCN6856 firmware 2.1.0-00642 to 2.1.0-00650
- rtl_bt: Update RTL8852B BT USB FW to 0x049B_5037
- amdgpu: Update ISP FW for isp v4.1.1
- trivial: contrib: wrap the process in try/except to catch server issues
- trivial: contrib: use python-magic to detect encoding of emails
- Merge https://github.com/che-jiang/qca_btfw into qca
- QCA: Add Bluetooth firmware for QCA6698
- amdgpu: revert DMCUB 3.1.4 firmware
- amlogic: update firmware for w265s2
Resolves: RHEL-78328, RHEL-78328

* Tue Jan 21 2025 Denys Vlasenko <dvlasenk@redhat.com> - 20250121-12
- Update linux-firmware to latest upstream (RHEL-75551)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- mediatek MT7925: update bluetooth firmware to 20250113153307
- linux-firmware: update firmware for MT7925 WiFi device
- amdgpu: update psp 13.0.10 firmware
- amdgpu: update gc 11.0.3 firmware
- amdgpu: update psp 13.0.8 firmware
- amdgpu: update psp 13.0.5 firmware
- amdgpu: update vcn 4.0.0 firmware
- amdgpu: update psp 13.0.0 firmware
- amdgpu: update gc 11.0.0 firmware
- amdgpu: update beige goby firmware
- amdgpu: update dimgrey cavefish firmware
- amdgpu: update navy flounder firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: update navi14 firmware
- amdgpu: update smu 14.0.3 firmware
- amdgpu: update psp 14.0.3 firmware
- amdgpu: update gc 12.0.1 firmware
- amdgpu: update navi12 firmware
- amdgpu: update smu 14.0.2 firmware
- amdgpu: update psp 14.0.2 firmware
- amdgpu: update gc 12.0.0 firmware
- amdgpu: update gc 9.4.3 firmware
- amdgpu: update navi10 firmware
- amdgpu: update vcn 4.0.4 firmware
- amdgpu: update psp 13.0.7 firmware
- amdgpu: update gc 11.0.2 firmware
- amdgpu: update yellow carp firmware
- qcom: correct licence information for SA8775P binaries
- qcom: update SLPI firmware for RB5 board
- amdgpu: DMCUB updates for various AMDGPU ASICs
- qcom: add DSP firmware for SA8775p platform
- qcom: correct venus firmware versions
- qcom: add missing version information
- linux-firmware: Update firmware (v10) for mt7988 internal
- iwlwifi: add Bz FW for core90-93 release
- linux-firmware: wilc3000: add firmware for WILC3000 WiFi device
- rtw89: 8852b: update fw to v0.29.29.8
- rtw89: 8852c: update fw to v0.27.122.0
- rtw89: 8922a: update fw to v0.35.54.0
- rtw89: 8922a: update fw to v0.35.52.1 and stuffs
- rtw89: 8852bt: update fw to v0.29.110.0
- rtw89: 8852b: update fw to v0.29.29.7
- amdgpu: DMCUB updates for various AMDGPU ASICs
- amdgpu: update sdma 6.0.3 firmware
- amdgpu: update psp 13.0.10 firmware
- amdgpu: update gc 11.0.3 firmware
- amdgpu: update sdma 4.4.5 firmware
- amdgpu: update psp 13.0.14 firmware
- amdgpu: update gc 9.4.4 firmware
- amdgpu: update psp 13.0.5 firmware
- amdgpu: update vega20 firmware
- amdgpu: update vega12 firmware
- amdgpu: update vega10 firmware
- amdgpu: update vcn 4.0.0 firmware
- amdgpu: update psp 13.0.0 firmware
- amdgpu: update gc 11.0.0 firmware
- amdgpu: update picasso firmware
- amdgpu: update beige goby firmware
- amdgpu: update vangogh firmware
- amdgpu: update dimgrey cavefish firmware
- amdgpu: update navy flounder firmware
- amdgpu: update psp 13.0.11 firmware
- amdgpu: update gc 11.0.4 firmware
- amdgpu: update vcn 4.0.2 firmware
- amdgpu: update psp 13.0.4 firmware
- amdgpu: update gc 11.0.1 firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: update vcn 4.0.6 firmware
- amdgpu: update psp 14.0.1 firmware
- amdgpu: update vcn 4.0.5 firmware
- amdgpu: update gc 11.5.0 firmware
- amdgpu: update vcn 5.0.0 firmware
- amdgpu: update smu 14.0.3 firmware
- amdgpu: update psp 14.0.3 firmware
- amdgpu: update gc 12.0.1 firmware
- amdgpu: update navi14 firmware
- amdgpu: update arcturus firmware
- amdgpu: update renoir firmware
- amdgpu: update smu 14.0.2 firmware
- amdgpu: update psp 14.0.2 firmware
- amdgpu: update gc 12.0.0 firmware
- amdgpu: update navi12 firmware
- amdgpu: update vcn 4.0.3 firmware
- amdgpu: update sdma 4.4.2 firmware
- amdgpu: update psp 13.0.6 firmware
- amdgpu: update gc 9.4.3 firmware
- amdgpu: update yellow carp firmware
- amdgpu: update vcn 4.0.4 firmware
- amdgpu: update psp 13.0.7 firmware
- amdgpu: update gc 11.0.2 firmware
- amdgpu: update navi10 firmware
- amdgpu: update aldebaran firmware
- cirrus: cs35l56: Correct some links to address the correct amp instance
- linux-firmware: Update firmware file for Intel Bluetooth Magnetar core
- linux-firmware: Update firmware file for Intel BlazarU core
- linux-firmware: Update firmware file for Intel Bluetooth Solar core
- cirrus: cs35l41: Add Firmware for Ayaneo system 1f660105
- Fix has_gnu_parallel function
- rtl_bt: Add separate config for RLT8723CS Bluetooth part
- amdgpu: revert VCN 3.1.2 firmware
- amdgpu: revert yellow carp VCN firmware
- amdgpu: revert sienna cichlid VCN firmware
- amdgpu: revert navy flounder VCN firmware
- amdgpu: revert dimgrey cavefish VCN firmware
- WHENCE: Link the Raspberry Pi CM5 and 500 to the 4B
- copy-firmware.sh: Fix typo in error message.
- Add support to install files/symlinks in parallel.
- Makefile: Remove obsolete/broken reference.
- check_whence.py: Use a more portable shebang.
- rtl_bt: Update RTL8852B BT USB FW to 0x04BE_1F5E
- cnm: update chips&media wave521c firmware.
- WHENCE: Add "Info:" tag to text that's clearly not part of the license
- rtl_nic: add firmware rtl8125bp-2
- qcom: venus-5.4: update firmware binary for sc7180 and qcs615
- cirrus: cs35l56: Correct filenames of SSID 17aa3832
- cirrus: cs35l56: Add and update firmware for various Cirrus CS35L54 and CS35L56 laptops
- cirrus: cs35l56: Correct SSID order for 103c8d01 103c8d08 10431f43
- rtl_nic: add firmware rtl8125d-2
- Merge https://github.com/zijun-hu/qca_btfw into qca-bt
Resolves: RHEL-75551

* Tue Dec 10 2024 Denys Vlasenko <dvlasenk@redhat.com> - 20241210-11
- [AMDCLIENT 10.0 Feature] amdgpu linux-firmware for the 2025 H mobile platform (RHEL-61604)
- [AMDCLIENT 10.0 Feature] linux-firmware for a 2025 mobile platform (RHEL-61477)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- linux-firmware: Update firmware file for Intel BlazarU core
- amdgpu: update dmcub 0.0.246.0 firmware
- Add top level license file.
- amdgpu: update raven firmware
- amdgpu: update gc 11.0.3 firmware
- amdgpu: update psp 13.0.14 firmware
- amdgpu: update vcn 3.1.2 firmware
- amdgpu: update vpe 6.1.3 firmware
- amdgpu: update psp 14.0.4 firmware
- amdgpu: update gc 11.5.2 firmware
- amdgpu: update vcn 4.0.0 firmware
- amdgpu: update gc 11.0.0 firmware
- amdgpu: update picasso firmware
- amdgpu: update beige goby firmware
- amdgpu: update vangogh firmware
- amdgpu: update dimgrey cavefish firmware
- amdgpu: update navy flounder firmware
- amdgpu: update gc 11.0.4 firmware
- amdgpu: update green sardine firmware
- amdgpu: update vcn 4.0.2 firmware
- amdgpu: update gc 11.0.1 firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: update vcn 4.0.6 firmware
- amdgpu: update gc 11.5.1 firmware
- amdgpu: update vcn 4.0.5 firmware
- amdgpu: update psp 14.0.0 firmware
- amdgpu: add vcn 5.0.0 firmware
- amdgpu: add smu 14.0.3 firmware
- amdgpu: add sdma 7.0.1 firmware
- amdgpu: add psp 14.0.3 firmware
- amdgpu: add gc 12.0.1 firmware
- amdgpu: update navi14 firmware
- amdgpu: update renoir firmware
- amdgpu: add smu 14.0.2 firmware
- amdgpu: add sdma 7.0.0 firmware
- amdgpu: add psp 14.0.2 firmware
- amdgpu: add gc 12.0.0 firmware
- amdgpu: update navi12 firmware
- amdgpu: update psp 13.0.6 firmware
- amdgpu: update yellow carp firmware
- amdgpu: update vcn 4.0.4 firmware
- amdgpu: update gc 11.0.2 firmware
- amdgpu: update navi10 firmware
- amdgpu: update aldebaran firmware
- upstream amdnpu firmware
- i915: Update Xe2LPD DMC to v2.24
- cirrus: cs35l56: Add firmware for Cirrus CS35L56 for various Dell laptops
- iwlwifi: add Bz-gf FW for core89-91 release
- amdgpu: update smu 13.0.10 firmware
- amdgpu: update sdma 6.0.3 firmware
- amdgpu: update psp 13.0.10 firmware
- amdgpu: update gc 11.0.3 firmware
- amdgpu: add smu 13.0.14 firmware
- amdgpu: add sdma 4.4.5 firmware
- amdgpu: add psp 13.0.14 firmware
- amdgpu: add gc 9.4.4 firmware
- amdgpu: update vcn 3.1.2 firmware
- amdgpu: update psp 13.0.5 firmware
- amdgpu: update psp 13.0.8 firmware
- amdgpu: update vega20 firmware
- amdgpu: update vega12 firmware
- amdgpu: update psp 14.0.4 firmware
- amdgpu: update gc 11.5.2 firmware
- amdgpu: update vega10 firmware
- amdgpu: update vcn 4.0.0 firmware
- amdgpu: update smu 13.0.0 firmware
- amdgpu: update psp 13.0.0 firmware
- amdgpu: update gc 11.0.0 firmware
- amdgpu: update beige goby firmware
- amdgpu: update vangogh firmware
- amdgpu: update dimgrey cavefish firmware
- amdgpu: update navy flounder firmware
- amdgpu: update psp 13.0.11 firmware
- amdgpu: update gc 11.0.4 firmware
- amdgpu: update vcn 4.0.2 firmware
- amdgpu: update psp 13.0.4 firmware
- amdgpu: update gc 11.0.1 firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: update vpe 6.1.1 firmware
- amdgpu: update vcn 4.0.6 firmware
- amdgpu: update psp 14.0.1 firmware
- amdgpu: update gc 11.5.1 firmware
- amdgpu: update vcn 4.0.5 firmware
- amdgpu: update psp 14.0.0 firmware
- amdgpu: update gc 11.5.0 firmware
- amdgpu: update navi14 firmware
- amdgpu: update arcturus firmware
- amdgpu: update renoir firmware
- amdgpu: update navi12 firmware
- amdgpu: update sdma 4.4.2 firmware
- amdgpu: update psp 13.0.6 firmware
- amdgpu: update gc 9.4.3 firmware
- amdgpu: update vcn 4.0.4 firmware
- amdgpu: update psp 13.0.7 firmware
- amdgpu: update gc 11.0.2 firmware
- amdgpu: update navi10 firmware
- amdgpu: update aldebaran firmware
- ice: update ice DDP wireless_edge package to 1.3.20.0
- ice: update ice DDP comms package to 1.3.52.0
- ice: update ice DDP package to ice-1.3.41.0
- amdgpu: update DMCUB to v9.0.10.0 for DCN314
- amdgpu: update DMCUB to v9.0.10.0 for DCN351
- linux-firmware: Update AMD cpu microcode
- xe: Update GUC to v70.36.0 for BMG, LNL
- i915: Update GUC to v70.36.0 for ADL-P, DG1, DG2, MTL, TGL
- iwlwifi: add Bz-gf FW for core91-69 release
- Merge https://github.com/zijun-hu/qca_btfw into qca
- qcom: venus-5.4: add venus firmware file for qcs615
- qcom: update venus firmware file for SC7280
- QCA: Add 22 bluetooth firmware nvm files for QCA2066
- mediatek MT7922: update bluetooth firmware to 20241106163512
- mediatek MT7921: update bluetooth firmware to 20241106151414
- linux-firmware: update firmware for MT7922 WiFi device
- linux-firmware: update firmware for MT7921 WiFi device
- qcom: Add QDU100 firmware image files.
- qcom: Update aic100 firmware files
- dedup-firmware.sh: fix infinite loop for --verbose
Resolves: RHEL-61604, RHEL-61477

* Mon Nov 11 2024 Denys Vlasenko <dvlasenk@redhat.com> - 20241111-10
- Update linux-firmware to latest upstream (RHEL-65206)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- rtl_bt: Update RTL8852BT/RTL8852BE-VT BT USB FW to 0x04D7_63F7
- cnm: update chips&media wave521c firmware.
- mediatek MT7920: update bluetooth firmware to 20241104091246
- linux-firmware: update firmware for MT7920 WiFi device
- copy-firmware.sh: Run check_whence.py only if in a git repo
- cirrus: cs35l56: Add firmware for Cirrus CS35L56 for various Dell laptops
- amdgpu: update DMCUB to v9.0.10.0 for DCN351
- rtw89: 8852a: update fw to v0.13.36.2
- rtw88: Add firmware v52.14.0 for RTL8812AU
- i915: Update Xe2LPD DMC to v2.23
- linux-firmware: update firmware for mediatek bluetooth chip (MT7925)
- linux-firmware: update firmware for MT7925 WiFi device
- WHENCE: Add sof-tolg for mt8195
- linux-firmware: Update firmware file for Intel BlazarI core
- qcom: Add link for QCS6490 GPU firmware
- qcom: update gpu firmwares for qcs615 chipset
- cirrus: cs35l56: Update firmware for Cirrus Amps for some HP laptops
- ath11k: move WCN6750 firmware to the device-specific subdir
Resolves: RHEL-65206

* Tue Oct 29 2024 Troy Dawson <tdawson@redhat.com> - 20241029-9
- Bump release for October 2024 mass rebuild:
Resolves: RHEL-64018

* Tue Oct 29 2024 Denys Vlasenko <dvlasenk@redhat.com> - 20241029-8
- Update linux-firmware to latest upstream (RHEL-65206)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- xe: Update LNL GSC to v104.0.0.1263
- i915: Update MTL/ARL GSC to v102.1.15.1926
- amdgpu: DMCUB updates for various AMDGPU ASICs
- i915: Add Xe3LPD DMC
- cnm: update chips&media wave521c firmware.
- linux-firmware: Add firmware for Cirrus CS35L41
- linux-firmware: Update firmware file for Intel BlazarU core
- Makefile: error out of 'install' if COPYOPTS is set
- check_whence.py: skip some validation if git ls-files fails
- qcom: Add Audio firmware for X1E80100 CRD/QCPs
- amdgpu: DMCUB updates forvarious AMDGPU ASICs
- brcm: replace NVRAM for Jetson TX1
- rtlwifi: Update firmware for RTL8192FU to v7.3
- make: separate installation and de-duplication targets
- check_whence.py: check the permissions
- Remove execute bit from firmware files
- configure: remove unused file
- rtl_nic: add firmware rtl8125d-1
- iwlwifi: add gl/Bz FW for core91-69 release
- iwlwifi: update ty/So/Ma firmwares for core91-69 release
- iwlwifi: update cc/Qu/QuZ firmwares for core91-69 release
- Merge https://github.com/zijun-hu/qca_btfw into wcn785x
- cirrus: cs35l56: Add firmware for Cirrus CS35L56 for a Lenovo Laptop
- cirrus: cs35l56: Add firmware for Cirrus CS35L56 for some ASUS laptops
- cirrus: cs35l56: Add firmware for Cirrus Amps for some HP laptops
- linux-firmware: update firmware for en8811h 2.5G ethernet phy
- mtk_wed: add firmware for mt7988 Wireless Ethernet Dispatcher
- ath12k: WCN7850 hw2.0: update board-2.bin
- ath12k: QCN9274 hw2.0: add to WLAN.WBE.1.3.1-00162-QCAHKSWPL_SILICONZ-1
- ath12k: QCN9274 hw2.0: add board-2.bin
- copy-firmware.sh: rename variables in symlink hanlding
- copy-firmware.sh: remove no longer reachable test -L
- copy-firmware.sh: remove no longer reachable test -f
- copy-firmware.sh: call ./check_whence.py before parsing the file
- copy-firmware.sh: warn if the destination folder is not empty
- copy-firmware.sh: add err() helper
- copy-firmware.sh: fix indentation
- copy-firmware.sh: reset and consistently handle destdir
- Revert "copy-firmware: Support additional compressor options"
- copy-firmware.sh: flesh out and fix dedup-firmware.sh
- Style update yaml files
- editorconfig: add initial config file
- check_whence.py: annotate replacement strings as raw
- check_whence.py: LC_ALL=C sort -u the filelist
- check_whence.py: ban link-to-a-link
- check_whence.py: use consistent naming
- Add a link from TAS2XXX1EB3.bin -> ti/tas2781/TAS2XXX1EB30.bin
- tas2781: Upload dsp firmware for ASUS laptop 1EB30 & 1EB31
- rtlwifi: Add firmware v39.0 for RTL8192DU
- Revert "ath12k: WCN7850 hw2.0: update board-2.bin"
- QCA: Add Bluetooth firmwares for WCN785x with UART transport
- amdgpu: DMCUB DCN35 update
- brcm: Add BCM4354 NVRAM for Jetson TX1
- brcm: Link FriendlyElec NanoPi M4 to AP6356S nvram
- linux-firmware: add firmware for MediaTek Bluetooth chip (MT7920)
- linux-firmware: add firmware for MT7920
- amdgpu: update raven firmware
- amdgpu: update SMU 13.0.10 firmware
- amdgpu: update PSP 13.0.10 firmware
- amdgpu: update GC 11.0.3 firmware
- amdgpu: update VCN 3.1.2 firmware
- amdgpu: update PSP 13.0.5 firmware
- amdgpu: update PSP 13.0.8 firmware
- amdgpu: update vega12 firmware
- amdgpu: update PSP 14.0.4 firmware
- amdgpu: update GC 11.5.2 firmware
- amdgpu: update vega10 firmware
- amdgpu: update VCN 4.0.0 firmware
- amdgpu: update PSP 13.0.0 firmware
- amdgpu: update GC 11.0.0 firmware
- amdgpu: update picasso firmware
- amdgpu: update beige goby firmware
- amdgpu: update vangogh firmware
- amdgpu: update dimgrey cavefish firmware
- amdgpu: update navy flounder firmware
- amdgpu: update green sardine firmware
- amdgpu: update VCN 4.0.2 firmware
- amdgpu: update PSP 13.0.4 firmware
- amdgpu: update GC 11.0.1 firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: update VCN 4.0.6 firmware
- amdgpu: update PSP 14.0.1 firmware
- amdgpu: update GC 11.5.1 firmware
- amdgpu: update VCN 4.0.5 firmware
- amdgpu: update PSP 14.0.0 firmware
- amdgpu: update GC 11.5.0 firmware
- amdgpu: update navi14 firmware
- amdgpu: update renoir firmware
- amdgpu: update navi12 firmware
- amdgpu: update SMU 13.0.6 firmware
- amdgpu: update SDMA 4.4.2 firmware
- amdgpu: update PSP 13.0.6 firmware
- amdgpu: update GC 9.4.3 firmware
- amdgpu: update yellow carp firmware
- amdgpu: update VCN 4.0.4 firmware
- amdgpu: update PSP 13.0.7 firmware
- amdgpu: update GC 11.0.2 firmware
- amdgpu: update navi10 firmware
- amdgpu: update aldebaran firmware
- qcom: update gpu firmwares for qcm6490 chipset
- mt76: mt7996: add firmware files for mt7992 chipset
- mt76: mt7996: add firmware files for mt7996 chipset variants
- qcom: add gpu firmwares for sa8775p chipset
- amdgpu: update DMCUB to v0.0.233.0 DCN351
- rtw89: 8922a: add fw format-2 v0.35.42.1
- copy-firmware: Handle links to uncompressed files
- WHENCE: Fix battmgr.jsn entry type
- amdgpu: Add VPE 6.1.3 microcode
- amdgpu: add SDMA 6.1.2 microcode
- amdgpu: Add support for PSP 14.0.4
- amdgpu: add GC 11.5.2 microcode
- qcom: qcm6490: add ADSP and CDSP firmware
- linux-firmware: Update firmware file for Intel Bluetooth Magnetor core
- linux-firmware: Update firmware file for Intel BlazarU core
- linux-firmware: Update firmware file for Intel Bluetooth Solar core
- rtl_bt: Update RTL8852B BT USB FW to 0x0447_9301
Resolves: RHEL-65206

* Tue Sep 17 2024 Denys Vlasenko <dvlasenk@redhat.com> - 20240910-7
- linux-firmware broken links (RHEL-45213)
Resolves: RHEL-45213

* Tue Sep 10 2024 Denys Vlasenko <dvlasenk@redhat.com> - 20240910-6
- linux-firmware broken links (RHEL-45213)
- AMD SEV: IOMMU improperly handles certain special address leading to a loss of guest integrity (RHEL-54251)
- AMD SEV: Incomplete system memory cleanup in SEV firmware corrupt guest private memory (RHEL-54236)
- SMM Lock Bypass (RHEL-55299)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- realtek: rt1320: Add patch firmware of MCU
- i915: Update MTL DMC v2.23
- cirrus: cs35l56: Add firmware for Cirrus CS35L54 for some HP laptops
- amdgpu: Revert sienna cichlid dmcub firmware update
- Merge tag 'iwlwifi-fw-2024-09-03' of http://git.kernel.org/pub/scm/linux/kernel/git/iwlwifi/linux-firmware into iwlwifi-20240903
- iwlwifi: add Bz FW for core89-58 release
- rtl_nic: add firmware rtl8126a-3
- linux-firmware: update firmware for MT7921 WiFi device
- linux-firmware: update firmware for mediatek bluetooth chip (MT7921)
- amdgpu: update DMCUB to v0.0.232.0 for DCN314 and DCN351
- qcom: vpu: restore compatibility with kernels before 6.6
- amdgpu: DMCUB updates forvarious AMDGPU ASICs
- rtw89: 8922a: add fw format-1 v0.35.41.0
- linux-firmware: update firmware for MT7925 WiFi device
- linux-firmware: update firmware for mediatek bluetooth chip (MT7925)
- rtl_bt: Add firmware and config files for RTL8922A
- rtl_bt: Add firmware file for the the RTL8723CS Bluetooth part
- rtl_bt: de-dupe identical config.bin files
- rename rtl8723bs_config-OBDA8723.bin -> rtl_bt/rtl8723bs_config.bin
- linux-firmware: Update AMD SEV firmware
- linux-firmware: update firmware for MT7996
- Revert "i915: Update MTL DMC v2.22"
- Merge tag 'amd-2024-08-12' of https://gitlab.freedesktop.org/drm/firmware into amd-2024-08-12
- ath12k: WCN7850 hw2.0: update board-2.bin
- ath11k: WCN6855 hw2.0: update to WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.41
- ath11k: WCN6855 hw2.0: update board-2.bin
- ath11k: QCA2066 hw2.1: add to WLAN.HSP.1.1-03926.13-QCAHSPSWPL_V2_SILICONZ_CE-2.52297.3
- ath11k: QCA2066 hw2.1: add board-2.bin
- ath11k: IPQ5018 hw1.0: update to WLAN.HK.2.6.0.1-01291-QCAHKSWPL_SILICONZ-1
- qcom: vpu: add video firmware for sa8775p
- amdgpu: DMCUB updates for various AMDGPU ASICs
- qcom: update path for video firmware for vpu-1/2/3.0
- Merge https://github.com/zijun-hu/qca_btfw into qca_btfw
- Merge tag 'rtw-fw-2024-08-08' of https://github.com/pkshih/linux-firmware into rtw89
- QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00642
- rtw89: 8852c: add fw format-1 v0.27.97.0
- rtw89: 8852bt: add firmware 0.29.91.0
- amdgpu: Update ISP FW for isp v4.1.1
- Merge tag 'intel-2024-08-02' of https://gitlab.freedesktop.org/drm/firmware into intel-20240805
- Merge https://github.com/zijun-hu/qca_btfw into list-20240802
- mediatek: Update mt8195 SOF firmware
- Merge tag 'amd-2024-08-02' of https://gitlab.freedesktop.org/drm/firmware into amd-20240802
- amdgpu: DMCUB updates for DCN314
- xe: First GuC release v70.29.2 for BMG
- xe: Add GuC v70.29.2 for LNL
- i915: Add GuC v70.29.2 for ADL-P, DG1, DG2, MTL, and TGL
- i915: Update MTL DMC v2.22
- i915: update MTL GSC to v102.0.10.1878
- xe: Add BMG HuC 8.2.10
- xe: Add GSC 104.0.0.1161 for LNL
- xe: Add LNL HuC 9.4.13
- i915: update DG2 HuC to v7.10.16
- amdgpu: Update ISP FW for isp v4.1.1
- amdgpu: Update ISP FW for isp v4.1.1
- amdgpu: add new ISP 4.1.1 firmware
- QCA: Update Bluetooth QCA2066 firmware to 2.1.0-00641
- amdgpu: update DMCUB to v0.0.227.0 for DCN35 and DCN351
- Merge tag 'iwlwifi-fw-2024-07-25' of ssh://gitolite.kernel.org/pub/scm/linux/kernel/git/iwlwifi/linux-firmware into iwlfifi-fw-2024-07
- Revert "iwlwifi: update ty/So/Ma firmwares for core89-58 release"
- linux-firmware: update firmware for MT7922 WiFi device
- linux-firmware: update firmware for MT7921 WiFi device
- linux-firmware: update firmware for mediatek bluetooth chip (MT7922)
- linux-firmware: update firmware for mediatek bluetooth chip (MT7921)
- iwlwifi: add gl FW for core89-58 release
- iwlwifi: update ty/So/Ma firmwares for core89-58 release
- iwlwifi: update cc/Qu/QuZ firmwares for core89-58 release
- mediatek: Update mt8195 SOF firmware and sof-tplg
- ASoC: tas2781: fix the license issue for tas781 firmware
- rtl_bt: Update RTL8852B BT USB FW to 0x048F_4008
- .gitignore: Ignore intermediate files
- i915: Update Xe2LPD DMC to v2.21
- qcom: move signed x1e80100 signed firmware to the SoC subdir
- qcom: add video firmware file for vpu-3.0
- amdgpu: update DMCUB to v0.0.225.0 for Various AMDGPU Asics
- qcom: add gpu firmwares for x1e80100 chipset
- linux-firmware: add firmware for qat_402xx devices
- amdgpu: update raven firmware
- amdgpu: update SMU 13.0.10 firmware
- amdgpu: update SDMA 6.0.3 firmware
- amdgpu: update PSP 13.0.10 firmware
- amdgpu: update GC 11.0.3 firmware
- amdgpu: update vega20 firmware
- amdgpu: update PSP 13.0.5 firmware
- amdgpu: update PSP 13.0.8 firmware
- amdgpu: update vega12 firmware
- amdgpu: update vega10 firmware
- amdgpu: update VCN 4.0.0 firmware
- amdgpu: update SDMA 6.0.0 firmware
- amdgpu: update PSP 13.0.0 firmware
- amdgpu: update GC 11.0.0 firmware
- amdgpu: update picasso firmware
- amdgpu: update beige goby firmware
- amdgpu: update vangogh firmware
- amdgpu: update dimgrey cavefish firmware
- amdgpu: update navy flounder firmware
- amdgpu: update PSP 13.0.11 firmware
- amdgpu: update GC 11.0.4 firmware
- amdgpu: update green sardine firmware
- amdgpu: update VCN 4.0.2 firmware
- amdgpu: update SDMA 6.0.1 firmware
- amdgpu: update PSP 13.0.4 firmware
- amdgpu: update GC 11.0.1 firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: update VPE 6.1.1 firmware
- amdgpu: update VCN 4.0.6 firmware
- amdgpu: update SDMA 6.1.1 firmware
- amdgpu: update PSP 14.0.1 firmware
- amdgpu: update GC 11.5.1 firmware
- amdgpu: update VCN 4.0.5 firmware
- amdgpu: update SDMA 6.1.0 firmware
- amdgpu: update PSP 14.0.0 firmware
- amdgpu: update GC 11.5.0 firmware
- amdgpu: update navi14 firmware
- amdgpu: update renoir firmware
- amdgpu: update navi12 firmware
- amdgpu: update PSP 13.0.6 firmware
- amdgpu: update GC 9.4.3 firmware
- amdgpu: update yellow carp firmware
- amdgpu: update VCN 4.0.4 firmware
- amdgpu: update SMU 13.0.7 firmware
- amdgpu: update SDMA 6.0.2 firmware
- amdgpu: update PSP 13.0.7 firmware
- amdgpu: update GC 11.0.2 firmware
- amdgpu: update navi10 firmware
- amdgpu: update raven2 firmware
- amdgpu: update aldebaran firmware
- linux-firmware: Update AMD cpu microcode
- intel: avs: Add topology file for I2S Analog Devices 4567
- intel: avs: Add topology file for I2S Nuvoton 8825
- intel: avs: Add topology file for I2S Maxim 98927
- intel: avs: Add topology file for I2S Maxim 98373
- intel: avs: Add topology file for I2S Maxim 98357a
- intel: avs: Add topology file for I2S Dialog 7219
- intel: avs: Add topology file for I2S Realtek 5663
- intel: avs: Add topology file for I2S Realtek 5640
- intel: avs: Add topology file for I2S Realtek 5514
- intel: avs: Add topology file for I2S Realtek 298
- intel: avs: Add topology file for I2S Realtek 286
- intel: avs: Add topology file for I2S Realtek 274
- intel: avs: Add topology file for Digital Microphone Array
- intel: avs: Add topology file for HDMI codecs
- intel: avs: Add topology file for HDAudio codecs
- Add a copy of Apache-2.0
- intel: avs: Update AudioDSP base firmware for APL-based platforms
- linux-firmware: Add ISH firmware file for Intel Lunar Lake platform
- amdgpu: update DMCUB to v0.0.224.0 for Various AMDGPU Asics
- cirrus: cs35l41: Update various firmware for ASUS laptops using CS35L41
- amdgpu: Update ISP FW for isp v4.1.1
Resolves: RHEL-45213, RHEL-54251, RHEL-54236, RHEL-55299

* Mon Jun 24 2024 Troy Dawson <tdawson@redhat.com> - 20240624-5
- Bump release for June 2024 mass rebuild

* Mon Jun 24 2024 Denys Vlasenko <dvlasenk@redhat.com> - 20240624-4
- linux-firmware ships encrypted zip files (named *.ncf) [rhel-10.0.beta] (RHEL-32183)
  Changes since the last update are noted on items below, copied from
  the git changelog of upstream linux-firmware repository.
- linux-firmware: mediatek: Update MT8173 VPU firmware to v1.2.0
- qcom: Add AIC100 firmware files
- amlogic: Update bluetooth firmware binary
- linux-firmware: Update firmware file for Intel BlazarU core
- linux-firmware: Update firmware file for Intel Bluetooth Magnetor core
- linux-firmware: Update firmware file for Intel Bluetooth Solar core
- linux-firmware: Update firmware file for Intel Bluetooth Pulsar core
- rtl_bt: Update RTL8822C BT UART firmware to 0xB5D6_6DCB
- rtl_bt: Update RTL8822C BT USB firmware to 0xAED6_6DCB
- amdgpu: update DMCUB to v0.0.222.0 for DCN314
- iwlwifi: add ty/So/Ma firmwares for core88-87 release
- iwlwifi: update cc/Qu/QuZ firmwares for core88-87 release
- linux-firmware: add new cc33xx firmware for cc33xx chips
- cirrus: cs35l56: Update firmware for Cirrus CS35L56 for ASUS UM5606 laptop
- cirrus: cs35l56: Update firmware for Cirrus CS35L56 for various ASUS laptops
- Merge https://github.com/zijun-hu/qca_btfw into qca
- linux-firmware: Add firmware for Lenovo Thinkbooks
- amdgpu: update yellow carp firmware
- amdgpu: update VCN 4.0.4 firmware
- amdgpu: update SDMA 6.0.2 firmware
- amdgpu: update PSP 13.0.7 firmware
- amdgpu: update GC 11.0.2 firmware
- amdgpu: update navi10 firmware
- amdgpu: update raven2 firmware
- amdgpu: update raven firmware
- amdgpu: update SMU 13.0.10 firmware
- amdgpu: update SDMA 6.0.3 firmware
- amdgpu: update PSP 13.0.10 firmware
- amdgpu: update GC 11.0.3 firmware
- amdgpu: update VCN 3.1.2 firmware
- amdgpu: update PSP 13.0.5 firmware
- amdgpu: update psp 13.0.8 firmware
- amdgpu: update vega20 firmware
- amdgpu: update vega12 firmware
- amdgpu: update vega10 firmware
- amdgpu: update VCN 4.0.0 firmware
- amdgpu: update smu 13.0.0 firmware
- amdgpu: update SDMA 6.0.0 firmware
- amdgpu: update PSP 13.0.0 firmware
- amdgpu: update GC 11.0.0 firmware
- amdgpu: update picasso firmware
- amdgpu: update beige goby firmware
- amdgpu: update vangogh firmware
- amdgpu: update dimgrey cavefish firmware
- amdgpu: update green sardine firmware
- amdgpu: update navy flounder firmware
- amdgpu: update PSP 13.0.11 firmware
- amdgpu: update GC 11.0.4 firmware
- amdgpu: update VCN 4.0.2 firmware
- amdgpu: update SDMA 6.0.1 firmware
- amdgpu: update PSP 13.0.4 firmware
- amdgpu: update GC 11.0.1 firmware
- amdgpu: update sienna cichlid firmware
- amdgpu: update VCN 4.0.5 firmware
- amdgpu: update PSP 14.0.0 firmware
- amdgpu: update GC 11.5.0 firmware
- amdgpu: update navi14 firmware
- amdgpu: update SMU 13.0.6 firmware
- amdgpu: update PSP 13.0.6 firmware
- amdgpu: update GC 9.4.3 firmware
- amdgpu: update renoir firmware
- amdgpu: update navi12 firmware
- amdgpu: update aldebaran firmware
- amdgpu: add support for PSP 14.0.1
- amdgpu: add support for VPE 6.1.1
- amdgpu: add support for VCN 4.0.6
- amdgpu: add support for SDMA 6.1.1
- amdgpu: add support for GC 11.5.1
- amdgpu: Add support for DCN 3.5.1
- QCA: Update Bluetooth QCA2066 firmware to 2.1.0-00639
- cnm: update chips&media wave521c firmware.
- linux-firmware: Add ordinary firmware for RTL8821AU device
- amdgpu: add new ISP 4.1.1 firmware
- amdgpu: DMCUB updates for various AMDGPU ASICs
- linux-firmware: Amphion: Update vpu firmware
- linux-firmware: Update firmware file for Intel BlazarU core
- linux-firmware: Update firmware file for Intel Bluetooth Magnetor core
- linux-firmware: Update firmware file for Intel Bluetooth Solar core
- linux-firmware: Update firmware file for Intel Bluetooth Solar core
- i915: Add BMG DMC v2.06
- linux-firmware: Add CS35L41 HDA Firmware for Asus HN7306
- linux-firmware: Update firmware tuning for HP Consumer Laptop
- amdgpu: DMCUB updates for various AMDGPU ASICs
- rtl_bt: Update RTL8822C BT UART firmware to 0x0FD6_407B
- rtl_bt: Update RTL8822C BT USB firmware to 0x0ED6_407B
- cirrus: cs35l56: Add firmware for Cirrus CS35L56 for various ASUS laptops
- linux-firmware: Add firmware and tuning for Lenovo Y770S
- amdgpu: DMCUB updates for various AMDGPU ASICs
- linux-firmware: Add firmware for Cirrus CS35L56 for various HP laptops
- i915: Update Xe2LPD DMC to v2.20
- linux-firmware: Remove Calibration Firmware and Tuning for CS35L41
- linux-firmware: Add firmware for Lenovo Thinkbook 13X
- ASoC: tas2781: Add dsp firmware for Thinkpad ICE-1 laptop
- amdgpu: add DMCUB 3.5 firmware
- amdgpu: add VPE 6.1.0 firmware
- amdgpu: add VCN 4.0.5 firmware
- amdgpu: add UMSCH 4.0.0 firmware
- amdgpu: add SDMA 6.1.0 firmware
- amdgpu: add PSP 14.0.0  firmware
- amdgpu: add GC 11.5.0 firmware
- amdgpu: update license date
- Montage: update firmware for Mont-TSSE
Resolves: RHEL-32183

* Thu Mar 28 2024 Jan Stancek <jstancek@redhat.com> - 20240328-3
- Update to upstream 20240328

* Thu Jan 18 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 20240115-2
- Update some firmware filters

* Mon Jan 15 2024 Peter Robinson <pbrobinson@fedoraproject.org>
- Update to upstream 20240115
- Split out Intel/Cirrus audio firmware, ISP firmware, NXP/TI WiFi Firmware
- Intel Bluetooth: Update firmware file for AX101/AX203/AX210/AX211
- Cirrus: Add CS35L41 firmware for Legion Slim 7 Gen 8 laptops
- Cirrus: Add firmware for CS35L41 for various Dell laptops
- update firmware for qat_4xxx devices
- update firmware for w1u_uart
- Cirrus: Add firmware file for cs42l43
- amdgpu: DMCUB updates for DCN312/DCN314
- amlogic/bluetooth: add firmware bin of W1 serial soc(w1u_uart)
- Add firmware for Mediatek WiFi/bluetooth chip (MT7925)
- ASoC: tas2781/tas2563: Add dsp firmware for laptops or other mobile devices
- rtl_bt: Add firmware and config files for RTL8852BT/RTL8852BE-VT
- ath11k: Updates for WCN6855/WCN6750/IPQ8074
- ath10k: Updates to WCN3990/QCA9888/QCA4019/QCA6174
- ath12k: add new driver and firmware for WCN7850
- iwlwifi: update gl FW for core80-165 release
- intel: vsc: Add firmware for Visual Sensing Controller
- Cirrus: Add CS35L41 firmware and tunings for ASUS Zenbook 2022/2023 Models
- QCA: Add bluetooth firmware nvm files for QCA2066
- QCA: Update Bluetooth QCA2066 firmware to 2.1.0-00629
- amdgpu: DMCUB updates for various AMDGPU ASICs
- qcom: Add Audio firmware for SM8550/SM8650 QRD

* Wed Dec 13 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20231211-1
- Update to upstream 20231211 release
- wfx: update to firmware 3.17
- wfx: fix broken firmware
- Update AMD cpu microcode
- cxgb4: Update firmware to revision 1.27.5.0
- add firmware for en8811h 2.5G ethernet phy
- s5p-mfc: Add MFC v12 Firmware
- Add a COPYOPTS variable
- rtl_bt: Update RTL8852A BT USB firmware to 0xDFC8_145F
- ice: update ice DDP wireless_edge package to 1.3.13.0
- Update firmware for MT7921/MT7922 Bluetooth device
- Update firmware for MT7921/MT7922 WiFi device
- amdgpu: update DMCUB firmware to 0.0.194.0 for DCN321 and DCN32
- qcom: update qcm2290/qrb4210 firmware
- qcom: update qcm2290/qrb4210 WiFi firmware file
- qcom: update Venus firmware file for v6.0
- powervr: add firmware for Imagination Technologies AXE-1-16M GPU
- ice: update ice DDP comms package to 1.3.45.0
- ice: update ice DDP package to 1.3.35.0
- mediatek: Remove an unused packed library
- mediatek: Sync shared memory structure changes
- Intel Bluetooth: Update firmware file for Intel Bluetooth BE200
- amdgpu: update DMCUB firmware to 0.0.193.0 for DCN31 and DCN314
- i915: Update MTL DMC to v2.19
- iwlwifi: fix for the new FWs from core83-55 release
- iwlwifi: add new FWs from core83-55 release
- iwlwifi: update cc/Qu/QuZ firmwares for core83-55 release
- Add firmware for Cirrus CS35L41 for HP G11 Laptops/2024 ASUS Zenbook Laptops
- add firmware for mt7988 internal 2.5G ethernet phy
- Update firmware for Magnetor Intel Bluetooth AX101/AX203/AX211
- Update firmware for SolarF Intel Bluetooth AX101/AX203/AX211
- Update firmware for Solar Intel Bluetooth AX101/AX203/AX210/AX211

* Tue Nov 14 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20231111-1
- Update to upstream 20231111 release
- Move AMD SEV and TEE firmware to amd-ucode package
- amdgpu: DMCUB updates for various AMDGPU ASICs
- nvidia: add GSP-RM version 535.113.01 firmware images
- Update firmware file for Intel Bluetooth AX101/AX203/AX210/AX211/BE200
- amdgpu: DMCUB updates for various AMDGPU ASICs
- qca: add bluetooth firmware for WCN3988
- ixp4xx: Add the IXP4xx firmware
- rtw89: 8852b: update fw to v0.29.29.5
- rtw89: 8851b: update fw to v0.29.41.3

* Mon Oct 30 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20231030-1
- Update to upstream 20231030 release
- Update firmware file for Intel Bluetooth AX203/AX210/AX211/
- Update firmware file for Intel Bluetooth Magnetor AX101/AX201/AX211
- rtl_nic: update firmware of RTL8156B
- Update AMD cpu microcode
- amdgpu: update SMU 13.0.0 firmware
- add Amlogic bluetooth firmware
- i915: Add GuC v70.13.1 for DG2, TGL, ADL-P and MTL
- iwlwifi: add a missing FW from core80-39 release
- WHENCE: add symlink for BananaPi M64
- i915: Update MTL DMC to v2.17
- amdgpu: update various firmware from 5.7 branch
- iwlwifi: add FWs for new GL and MA device types with multiple RF modules
- amd_pmf: Add initial PMF TA for Smart PC Solution Builder
- Update FW files for MRVL PCIE 8997 chipsets
- rtl_bt: Update RTL8851B BT USB firmware to 0x048A_D230
- iwlwifi: add new FWs from core81-65 release
- iwlwifi: update cc/Qu/QuZ firmwares for core81-65 release

* Tue Oct 17 2023 Michel Lind <salimma@fedoraproject.org> - 20230919-4
- Create amd-ucode-firmware subpackage

* Mon Oct 16 2023 Michel Lind <salimma@fedoraproject.org> - 20230919-3
- Re-add recommended firmware accidentally dropped in -2

* Mon Oct 02 2023 Neal Gompa <ngompa@fedoraproject.org> - 20230919-2
- Flip conditional to make weak-installing firmware the default

* Tue Sep 19 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230919-1
- Update to upstream 20230919 release
- amd-ucode: Add note on fam19h warnings
- i915: update MTL HuC to version 8.5.4
- amdgpu: update DMCUB to 0.0.183.0 for various AMDGPU ASICs
- qcom: add link to sc8280xp audioreach firmware
- qcom: sm8250: add RB5 sensors DSP firmware
- qcom: Update vpu-1.0 firmware
- qcom: sm8250: update DSP firmware
- qcom: add firmware for the onboard WiFi on qcm2290 / qrb4210
- qcom: add venus firmware files for v6.0
- qcom: add firmware for QRB4210 platforms
- qcom: add firmware for QCM2290 platforms
- qcom: add GPU firmware for QCM2290 / QRB2210
- ath10k/WCN3990: move wlanmdsp to qcom/sdm845
- QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00605
- Fix carl9170fw shell scripts for shellcheck errors
- i915: Update MTL DMC to v2.16
- Update firmware file for Intel Bluetooth AX200/AX201/AX203/AX210/AX211
- Update firmware for qat_4xxx devices
- Update AMD SEV firmware
- rtw89: 8852b: update fw to v0.29.29.3
- rtw89: 8851b: update fw to v0.29.41.2
- i915: add GSC 102.0.0.1655 for MTL
- cirrus: Add CS35L41 firmware for HP G11 models
- Update AMD cpu microcode
- rtl_bt: Add firmware v2 file for RTL8852C
- Revert "rtl_bt: Update RTL8852C BT USB firmware to 0x040D_7225"
- cxgb4: Update firmware to revision 1.27.4.0

* Thu Aug 10 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230804-153
- Update AMD cpu microcode

* Sun Aug 06 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230804-152
- Update to upstream 20230804 release
- Split out QCom Arm IP firmware
- Merge Marvell libertas WiFi firmware
- Mellanox: Add new mlxsw_spectrum firmware xx.2012.1012
- Add URL for latest FW binaries for NXP BT chipsets
- rtw89: 8851b: update firmware to v0.29.41.1
- qcom: sdm845: add RB3 sensors DSP firmware
- amdgpu: Update DMCUB for DCN314 & Yellow Carp
- ice: add LAG-supporting DDP package
- i915: Update MTL DMC to v2.13
- i915: Update ADLP DMC to v2.20
- cirrus: Add CS35L41 firmware for Dell Oasis Models
- copy-firmware: Fix linking directories when using compression
- copy-firmware: Fix test: unexpected operator
- qcom: sc8280xp: LENOVO: remove directory sym link
- qcom: sc8280xp: LENOVO: Remove execute bits
- amdgpu: update VCN 4.0.0 firmware
- amdgpu: add initial SMU 13.0.10 firmware
- amdgpu: add initial SDMA 6.0.3 firmware
- amdgpu: add initial PSP 13.0.10 firmware
- amdgpu: add initial GC 11.0.3 firmware
- Update AMD fam17h cpu microcode
- Update AMD cpu microcode
- amdgpu: update various generation VCN firmware
- amdgpu: update DMCUB to v0.0.175.0 for various AMDGPU ASICs
- Updated NXP SR150 UWB firmware
- wfx: update to firmware 3.16.1
- mediatek: Update mt8195 SCP firmware to support 10bit mode
- i915: update DG2 GuC to v70.8.0
- i915: update to GuC 70.8.0 and HuC 8.5.1 for MTL
- cirrus: Add CS35L41 firmware for ASUS ROG 2023 Models
- Partially revert "amdgpu: DMCUB updates for DCN 3.1.4 and 3.1.5"
- Update firmware for MT7922 WiFi/Bluetooth device
- Update firmware file for Intel Bluetooth AX200/201/203/210/211
- Fix qcom ASoC tglp WHENCE entry
- check_whence: Check link targets are valid
- iwlwifi: add new FWs from core80-39 release
- iwlwifi: update cc/Qu/QuZ firmwares for core80-39 release
- qcom: Add Audio firmware for SC8280XP X13s

* Sun Jul 02 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230625-151
- Update to upstream 20230625 release
- Move to upstreamed compression support
- Minor spec cleanups
- wilc1000: update WILC1000 firmware to v16.0
- ice: update ice DDP wireless_edge package to 1.3.10.0
- amdgpu: DMCUB updates for DCN 3.1.4 and 3.1.5
- amdgpu: update DMCUB to v0.0.172.0 for various AMDGPU ASICs
- qcom: Update the microcode files for Adreno a630 GPUs.
- qcom: sdm845: rename the modem firmware
- qcom: sdm845: update remoteproc firmware
- rtl_bt: Update RTL8852A BT USB firmware to 0xDAC7_480D
- rtl_bt: Update RTL8852C BT USB firmware to 0x040D_7225
- update firmware for MT7921/MT7922 WiFi device
- update firmware for mediatek MT7921/MT7922 bluetooth chip (MT7922)
- i915: Add HuC v8.5.0 for MTL
- mediatek: Update mt8195 SCP firmware to support hevc
- qcom: apq8016: add Dragonboard 410c WiFi and modem firmware
- cirrus: Add firmware for new Asus ROG Laptops
- brcm: Add symlinks from Pine64 devices to AW-CM256SM.txt
- amdgpu: Update GC 11.0.1 and 11.0.4
- rtw89: 8851b: add firmware v0.29.41.0
- amdgpu: various firmware updates for amd.5.5 release
- ice: update ice DDP comms package to 1.3.40.0
- rtlwifi: Add firmware v6.0 for RTL8192FU
- rtlwifi: Update firmware for RTL8188EU to v28.0
- cxgb4: Update firmware to revision 1.27.3.0

* Fri May 26 2023 Herton R. Krzesinski <herton@redhat.com>
- Join iwl3945-firmware and iwl4965-firmware into iwlegacy-firmware package.
- Create iwlwifi-dvm-firmware subpackage and fold some subpackages into it.
- Create iwlwifi-mvm-firmware subpackage and fold some subpackages into it.

* Tue May 16 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230515-150
- Update to upstream 20230515 release
- Drop ancient iwlwifi versioning and use upstream date format version
- cirrus: Add firmware and tuning files for HP G10 series laptops
- update firmware for mediatek bluetooth chip (MT7922)
- WHENCE: Cleanup Realtek BT firmware provenance
- update firmware for MT7922 WiFi device
- cnm: update chips&media wave521c firmware.
- cirrus: Add firmware and tuning files for Lenovo ThinkPad P1 Gen 6
- i915: Add GuC v70.6.6 for MTL
- amdgpu: update DCN 3.1.6 DMCUB firmware
- rtl_bt: Update RTL8852B BT USB firmware to 0xDBC6_B20F
- rtl_bt: Update RTL8761B BT USB firmware to 0xDFC6_D922
- rtl_bt: Update RTL8761B BT UART firmware to 0x9DC6_D922
- rtl_nic: update firmware of USB devices
- Update firmware file for Intel Bluetooth AX20x/AX21x
- update firmware for MT7981
- qca: Update firmware files for BT chip WCN6750
- mt76xx: Move the old Mediatek WiFi firmware to mediatek
- rtl_bt: Add firmware and config files for RTL8851B
- Update AMD cpu microcode
- add firmware for MT7981
- update firmware for MT7921 WiFi device
- update firmware for mediatek bluetooth chip (MT7921)
- update Intel qat firmware
- Add firmware for Cirrus CS35L41 on Lenovo Laptops
- update firmware for MT7916
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

* Sun Apr 09 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230404-149
- Split Realtek, Qcom Atheros, Mediatek, brcmfmac WiFi/BT firmwares to subpackages
- Update to upstream 20230404 release
- nvidia: update Tu10x and Tu11x signed firmware to support newer Turing HW
- update firmware for MT7922 WiFi/Bluetooth device
- Amphion: Update vpu firmware
- iwlwifi: add new FWs from core78-32 release
- iwlwifi: update 9000-family firmwares to core78-32
- amdgpu: Update SDMA 6.0.1 firmware
- amdgpu: Add PSP 13.0.11 firmware
- amdgpu: Update PSP 13.0.4 firmware
- amdgpu: Update GC 11.0.1 firmware
- amdgpu: Update DCN 3.1.4 firmware
- amdgpu: Add GC 11.0.4 firmware
- rtw88: 8822c: Update normal firmware to v9.9.15
- Update firmware for Intel Bluetooth 9462/9560/AX101/AX203/AX210/AX211
- add firmware files for NXP BT chipsets
- rtw89: 8852b: update format-1 fw to v0.29.29.0
- rtw89: 8852b: add format-1 fw v0.29.26.0
- rtw89: 8852b: rollback firmware to v0.27.32.1
- i915: Update MTL DMC to v2.12
- i915: Update ADLP DMC to v2.19
- mediatek: Update mt8192/mt8195 SCP firmware to support MM21 and MT21
- iwlwifi: update core69 and core72 firmwares for So device

* Sun Mar 12 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230310-148
- Update to upstream 20230310 release
- qat: update licence text
- rtl_bt: Update RTL8822C BT USB firmware to 0x0CC6_D2E3
- rtl_bt: Update RTL8822C BT UART firmware to 0x05C6_D2E3
- add fw for qat_4xxx
- Fix symlinks for Intel firmware
- update firmware for mediatek bluetooth chip (MT7921)
- update firmware for MT7921 WiFi device
- iwlwifi: update core69 and core72 firmwares for Ty device
- rtlwifi: Add firmware v16.0 for RTL8710BU aka RTL8188GU
- brcm: Add nvram for the Lenovo Yoga Book X90F / X90L convertible
- brcm: Fix Xiaomi Inc Mipad2 nvram/.txt file macaddr
- brcm: Add nvram for the Advantech MICA-071 tablet
- rtl_bt: Update RTL8852C BT USB firmware to 0xD7B8_FABF
- rtl_bt: Add firmware and config files for RTL8821CS
- rtw89: 8852b: update fw to v0.29.29.0
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

* Sun Feb 12 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230210-147
- Update to upstream 20230210 release
- Update AMD cpu microcode
- brcm: revert firmware files for Cypress devices
- brcm: restore previous firmware file for BCM4329 device
- rtw88: 8822c: Update normal firmware to v9.9.14
- i915: Add DMC v2.11 for MTL
- Add firmware for Cirrus CS35L41 on UM3402 ASUS Laptop
- Add missing tuning files for HP Laptops using Cirrus Amps
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
- update firmware for MT7921 WiFi device
- update firmware for mediatek bluetooth chip (MT7921)
- amdgpu: update vangogh firmware

* Mon Jan 23 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 20230117-146
- Update to upstream 20230117 release
- Update for Intel Bluetooth AX200/201/210/211/9260/9560
- brcm: add configuration files for CyberTan WC121
- qcom: add firmware files for Adreno A200
- rtw89: 8852c: update fw to v0.27.56.10
- QCA: Add Bluetooth firmware for QCA2066
- amdgpu: a bunch of additions/updates from amd-5.4
- iwlwifi: add/update new FWs from core76-35 release
- iwlwifi: update cc/Qu/QuZ firmwares for core76-35 release
- iwlwifi: add new FWs from core75-47 release
- iwlwifi: update 9000-family firmwares to core75-47
- amdgpu: update renoir PSP/DMCUB firmware
- amdgpu: update copyright date for LICENSE.amdgpu
- update firmware for MT7921/MT7922 WiFi device
- update firmware for mediatek bluetooth chip (MT7921/MT7922)
- cxgb4: Update firmware to revision 1.27.1.0
- qca: Update firmware files for BT chip WCN6750
