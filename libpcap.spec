# based on PLD Linux spec git://git.pld-linux.org/packages/libpcap.git
Summary:	System-independent interface for user-level packet capture
Name:		libpcap
Version:	1.7.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	9ce284eacc02cb5491e123b875f3f63c
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libnl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libpcap is a system-independent interface for user-level packet
capture. Libpcap provides a portable framework for low-level network
monitoring. Applications include network statistics collection,
security monitoring, network debugging, etc. Libpcap has
system-independent API that is used by several applications, including
tcpdump and arpwatch.

%package devel
Summary:	Header files and develpment documentation for libpcap
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for libpcap.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
export CFLAGS="$(pkg-config --cflags libnl-genl-3.0) %{rpmcflags}"
%configure \
	--enable-ipv6	\
	--with-libnl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README
%attr(755,root,root) %ghost %{_libdir}/libpcap.so.1
%attr(755,root,root) %{_libdir}/libpcap.so.*.*
%{_mandir}/man5/pcap-savefile.5*
%{_mandir}/man7/pcap-*.7*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcap-config
%attr(755,root,root) %{_libdir}/libpcap.so
%{_includedir}/pcap
%{_includedir}/pcap*.h
%{_mandir}/man1/pcap-config.1*
%{_mandir}/man3/pcap*.3*

