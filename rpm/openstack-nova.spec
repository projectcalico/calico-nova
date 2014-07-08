%global with_doc %{!?_without_doc:1}%{?_without_doc:0}

Name:             openstack-nova
Version:          2014.1.1_calico0.1
Release:          1%{?dist}
Summary:          OpenStack Compute (nova)

Group:            Applications/System
License:          ASL 2.0
URL:              http://openstack.org/projects/compute/
Source0:          https://launchpad.net/nova/icehouse/%{version}/+download/nova-%{version}.tar.gz

Source1:          nova-dist.conf
Source2:          nova.conf.sample
Source6:          nova.logrotate

Source10:         openstack-nova-api.init
Source100:        openstack-nova-api.upstart
Source11:         openstack-nova-cert.init
Source110:        openstack-nova-cert.upstart
Source12:         openstack-nova-compute.init
Source120:        openstack-nova-compute.upstart
Source13:         openstack-nova-network.init
Source130:        openstack-nova-network.upstart
Source14:         openstack-nova-objectstore.init
Source140:        openstack-nova-objectstore.upstart
Source15:         openstack-nova-scheduler.init
Source150:        openstack-nova-scheduler.upstart
Source16:         openstack-nova-conductor.init
Source160:        openstack-nova-conductor.upstart
Source18:         openstack-nova-xvpvncproxy.init
Source180:        openstack-nova-xvpvncproxy.upstart
Source19:         openstack-nova-console.init
Source190:        openstack-nova-console.upstart
Source24:         openstack-nova-consoleauth.init
Source240:        openstack-nova-consoleauth.upstart
Source25:         openstack-nova-metadata-api.init
Source250:        openstack-nova-metadata-api.upstart
Source26:         openstack-nova-cells.init
Source260:        openstack-nova-cells.upstart
Source27:         openstack-nova-spicehtml5proxy.init
Source270:        openstack-nova-spicehtml5proxy.upstart
Source28:         openstack-nova-novncproxy.init
Source280:        openstack-nova-novncproxy.upstart

Source20:         nova-sudoers

Source21:         nova-polkit.pkla
Source22:         nova-ifc-template

Source30:         openstack-nova-novncproxy.sysconfig

#
# patches_base=2014.1.1
#
Patch0001: 0001-Ensure-we-don-t-access-the-net-when-building-docs.patch
Patch0002: 0002-remove-runtime-dep-on-python-pbr.patch
Patch0003: 0003-Revert-Replace-oslo.sphinx-with-oslosphinx.patch
Patch0004: 0004-notify-calling-process-we-are-ready-to-serve.patch
Patch0005: 0005-Move-notification-point-to-a-better-place.patch

# This is EPEL specific and not upstream

BuildArch:        noarch
BuildRequires:    intltool
BuildRequires:    python-sphinx >= 1.1.2
BuildRequires:    python-oslo-sphinx
BuildRequires:    python-setuptools
BuildRequires:    python-netaddr
BuildRequires:    openstack-utils
BuildRequires:    python-pbr
BuildRequires:    python-d2to1
BuildRequires:    python-six
# These are required to build due to the requirements check added
BuildRequires:    python-paste-deploy >= 1.5.0
BuildRequires:    python-routes >= 1.12
BuildRequires:    python-sqlalchemy >= 0.7.8
BuildRequires:    python-webob >= 1.2.3
BuildRequires:    python-jinja2 >= 2.6

Requires:         openstack-nova-compute = %{version}-%{release}
Requires:         openstack-nova-cert = %{version}-%{release}
Requires:         openstack-nova-scheduler = %{version}-%{release}
Requires:         openstack-nova-api = %{version}-%{release}
Requires:         openstack-nova-network = %{version}-%{release}
Requires:         openstack-nova-objectstore = %{version}-%{release}
Requires:         openstack-nova-conductor = %{version}-%{release}
Requires:         openstack-nova-console = %{version}-%{release}
Requires:         openstack-nova-cells = %{version}-%{release}
Requires:         openstack-nova-novncproxy = %{version}-%{release}


%description
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

%package common
Summary:          Components common to all OpenStack Nova services
Group:            Applications/System

Requires:         python-nova = %{version}-%{release}
Requires:         python-keystoneclient
Requires:         python-oslo-rootwrap
Requires:         python-oslo-messaging >= 1.3.0-0.1.a4

Requires(post):   chkconfig
Requires(postun): initscripts
Requires(preun):  chkconfig
Requires(pre):    shadow-utils

Requires:         python-setuptools

%description common
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains scripts, config and dependencies shared
between all the OpenStack nova services.


%package compute
Summary:          OpenStack Nova Virtual Machine control service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}
Requires:         curl
Requires:         iscsi-initiator-utils
Requires:         iptables iptables-ipv6
Requires:         ipmitool
Requires:         vconfig
# tunctl is needed where `ip tuntap` is not available
Requires:         tunctl
Requires:         libguestfs-mount >= 1.7.17
# The fuse dependency should be added to libguestfs-mount
Requires:         fuse
Requires:         python-libguestfs
Requires:         libvirt >= 0.9.6
Requires:         libvirt-python
Requires:         openssh-clients
Requires:         rsync
Requires:         lvm2
Requires:         python-cinderclient
Requires(pre):    qemu-kvm
Requires:         genisoimage
Requires:         bridge-utils

%description compute
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling Virtual Machines.


%package network
Summary:          OpenStack Nova Network control service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}
Requires:         vconfig
Requires:         radvd
Requires:         bridge-utils
Requires:         dnsmasq
# dnsmasq-utils vailable from RDO
Requires:         dnsmasq-utils
# tunctl is needed where `ip tuntap` is not available
Requires:         tunctl
Requires:         ebtables

%description network
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling networking.


%package scheduler
Summary:          OpenStack Nova VM distribution service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description scheduler
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the service for scheduling where
to run Virtual Machines in the cloud.


%package cert
Summary:          OpenStack Nova certificate management service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description cert
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for managing certificates.


%package api
Summary:          OpenStack Nova API services
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description api
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing programmatic access.

%package conductor
Summary:          OpenStack Nova Conductor services
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description conductor
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing database access for
the compute service

%package objectstore
Summary:          OpenStack Nova simple object store service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description objectstore
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service providing a simple object store.


%package console
Summary:          OpenStack Nova console access services
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}
Requires:         python-websockify

%description console
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing
console access services to Virtual Machines.

%package cells
Summary:          OpenStack Nova Cells services
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description cells
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova Cells service providing additional 
scaling and (geographic) distribution for compute services.

%package novncproxy
Summary:          OpenStack Nova noVNC proxy service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}
Requires:         novnc
Requires: 	  python-websockify


%description novncproxy
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova noVNC Proxy service that can proxy 
VNC traffic over browser websockets connections.

%package -n       python-nova
Summary:          Nova Python libraries
Group:            Applications/System

Requires:         openssl
# Require openssh for ssh-keygen
Requires:         openssh
Requires:         sudo

Requires:         MySQL-python

Requires:         python-paramiko

Requires:         python-qpid
Requires:         python-kombu
Requires:         python-amqplib

Requires:         python-eventlet
Requires:         python-greenlet
Requires:         python-iso8601
Requires:         python-netaddr
Requires:         python-lxml
Requires:         python-anyjson
Requires:         python-boto
Requires:         python-cheetah
Requires:         python-ldap
Requires:         python-stevedore

Requires:         python-memcached

Requires:         python-sqlalchemy >= 0.7.8
Requires:         python-migrate

Requires:         python-paste-deploy >= 1.5
Requires:         python-routes >= 1.12
Requires:         python-webob >= 1.2.3

Requires:         python-glanceclient >= 1:0
Requires:         python-neutronclient
Requires:         python-novaclient
Requires:         python-oslo-config >= 1:1.2.0
Requires:         python-pyasn1
Requires:         python-six >= 1.4.1
Requires:         python-babel
Requires:         python-jinja2 >= 2.6

%description -n   python-nova
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains the nova Python library.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Compute
Group:            Documentation

BuildRequires:    graphviz

# Required to build module documents
BuildRequires:    python-boto
BuildRequires:    python-eventlet
# while not strictly required, quiets the build down when building docs.
BuildRequires:    python-migrate, python-iso8601

%description      doc
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains documentation files for nova.
%endif

%prep
%setup -q -n nova-%{version}

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1

# Apply EPEL patch

find . \( -name .gitignore -o -name .placeholder \) -delete

find nova -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i '/setuptools_git/d' setup.py
sed -i s/REDHATNOVAVERSION/%{version}/ nova/version.py
sed -i s/REDHATNOVARELEASE/%{release}/ nova/version.py

# Remove the requirements file so that pbr hooks don't add it 
# to distutils requiers_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%{__python} setup.py build

install -p -D -m 640 %{SOURCE2} etc/nova/nova.conf.sample

# Avoid http://bugzilla.redhat.com/1059815. Remove when that is closed
sed -i 's|group/name|group;name|; s|\[DEFAULT\]/|DEFAULT;|' etc/nova/nova.conf.sample

# Programmatically update defaults in sample config
# which is installed at /etc/nova/nova.conf

#  First we ensure all values are commented in appropriate format.
#  Since icehouse, there was an uncommented keystone_authtoken section
#  at the end of the file which mimics but also conflicted with our
#  distro editing that had been done for many releases.
sed -i '/^[^#[]/{s/^/#/; s/ //g}; /^#[^ ]/s/ = /=/' etc/nova/nova.conf.sample

#  TODO: Make this more robust
#  Note it only edits the first occurance, so assumes a section ordering in sample
#  and also doesn't support multi-valued variables like dhcpbridge_flagfile.
while read name eq value; do
  test "$name" && test "$value" || continue
  sed -i "0,/^# *$name=/{s!^# *$name=.*!#$name=$value!}" etc/nova/nova.conf.sample
done < %{SOURCE1}

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

pushd doc

%if 0%{?with_doc}
SPHINX_DEBUG=1 sphinx-build -b html source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo
%endif

# Create dir link to avoid a sphinx-build exception
mkdir -p build/man/.doctrees/
ln -s .  build/man/.doctrees/man
SPHINX_DEBUG=1 sphinx-build -b man -c source source/man build/man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 build/man/*.1 %{buildroot}%{_mandir}/man1/

popd

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/buckets
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/images
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/instances
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/keys
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/networks
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/tmp
install -d -m 755 %{buildroot}%{_localstatedir}/log/nova

# Setup ghost CA cert
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/CA
install -p -m 755 nova/CA/*.sh %{buildroot}%{_sharedstatedir}/nova/CA
install -p -m 644 nova/CA/openssl.cnf.tmpl %{buildroot}%{_sharedstatedir}/nova/CA
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/CA/{certs,crl,newcerts,projects,reqs}
touch %{buildroot}%{_sharedstatedir}/nova/CA/{cacert.pem,crl.pem,index.txt,openssl.cnf,serial}
install -d -m 750 %{buildroot}%{_sharedstatedir}/nova/CA/private
touch %{buildroot}%{_sharedstatedir}/nova/CA/private/cakey.pem

# Install config files
install -d -m 755 %{buildroot}%{_sysconfdir}/nova
install -p -D -m 640 %{SOURCE1} %{buildroot}%{_datadir}/nova/nova-dist.conf
install -p -D -m 640 etc/nova/nova.conf.sample  %{buildroot}%{_sysconfdir}/nova/nova.conf
install -p -D -m 640 etc/nova/rootwrap.conf %{buildroot}%{_sysconfdir}/nova/rootwrap.conf
install -p -D -m 640 etc/nova/api-paste.ini %{buildroot}%{_sysconfdir}/nova/api-paste.ini
install -p -D -m 640 etc/nova/policy.json %{buildroot}%{_sysconfdir}/nova/policy.json

# Install version info file
cat > %{buildroot}%{_sysconfdir}/nova/release <<EOF
[Nova]
vendor = Red Hat Inc.
product = OpenStack Nova
package = %{release}
EOF

# Install initscripts for Nova services
install -p -D -m 755 %{SOURCE10} %{buildroot}%{_initrddir}/openstack-nova-api
install -p -D -m 755 %{SOURCE11} %{buildroot}%{_initrddir}/openstack-nova-cert
install -p -D -m 755 %{SOURCE12} %{buildroot}%{_initrddir}/openstack-nova-compute
install -p -D -m 755 %{SOURCE13} %{buildroot}%{_initrddir}/openstack-nova-network
install -p -D -m 755 %{SOURCE14} %{buildroot}%{_initrddir}/openstack-nova-objectstore
install -p -D -m 755 %{SOURCE15} %{buildroot}%{_initrddir}/openstack-nova-scheduler
install -p -D -m 755 %{SOURCE16} %{buildroot}%{_initrddir}/openstack-nova-conductor
install -p -D -m 755 %{SOURCE18} %{buildroot}%{_initrddir}/openstack-nova-xvpvncproxy
install -p -D -m 755 %{SOURCE19} %{buildroot}%{_initrddir}/openstack-nova-console
install -p -D -m 755 %{SOURCE24} %{buildroot}%{_initrddir}/openstack-nova-consoleauth
install -p -D -m 755 %{SOURCE25} %{buildroot}%{_initrddir}/openstack-nova-metadata-api
install -p -D -m 755 %{SOURCE26} %{buildroot}%{_initrddir}/openstack-nova-cells
install -p -D -m 755 %{SOURCE27} %{buildroot}%{_initrddir}/openstack-nova-spicehtml5proxy
install -p -D -m 755 %{SOURCE28} %{buildroot}%{_initrddir}/openstack-nova-novncproxy

# Install sudoers
install -p -D -m 440 %{SOURCE20} %{buildroot}%{_sysconfdir}/sudoers.d/nova

# Install logrotate
install -p -D -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-nova

# Install pid directory
install -d -m 755 %{buildroot}%{_localstatedir}/run/nova

# Install template files
install -p -D -m 644 nova/cloudpipe/client.ovpn.template %{buildroot}%{_datarootdir}/nova/client.ovpn.template
install -p -D -m 644 %{SOURCE22} %{buildroot}%{_datarootdir}/nova/interfaces.template

# Install upstart jobs examples
install -p -m 644 %{SOURCE100} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE110} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE120} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE130} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE140} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE150} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE160} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE180} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE190} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE240} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE250} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE260} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE270} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE280} %{buildroot}%{_datadir}/nova/

# Install rootwrap files in /usr/share/nova/rootwrap
mkdir -p %{buildroot}%{_datarootdir}/nova/rootwrap/
install -p -D -m 644 etc/nova/rootwrap.d/* %{buildroot}%{_datarootdir}/nova/rootwrap/

install -d -m 755 %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d
install -p -D -m 644 %{SOURCE21} %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d/50-nova.pkla

# Install novncproxy service options template
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 %{SOURCE30} %{buildroot}%{_sysconfdir}/sysconfig/openstack-nova-novncproxy

# Remove unneeded in production stuff
rm -f %{buildroot}%{_bindir}/nova-debug
rm -fr %{buildroot}%{python_sitelib}/nova/tests/
rm -fr %{buildroot}%{python_sitelib}/run_tests.*
rm -f %{buildroot}%{_bindir}/nova-combined
rm -f %{buildroot}/usr/share/doc/nova/README*

%pre common
getent group nova >/dev/null || groupadd -r nova --gid 162
if ! getent passwd nova >/dev/null; then
  useradd -u 162 -r -g nova -G nova,nobody -d %{_sharedstatedir}/nova -s /sbin/nologin -c "OpenStack Nova Daemons" nova
fi
exit 0

%pre compute
usermod -a -G qemu nova
exit 0

%post compute
/sbin/chkconfig --add openstack-nova-compute
%post network
/sbin/chkconfig --add openstack-nova-network
%post conductor
/sbin/chkconfig --add openstack-nova-conductor
%post scheduler
/sbin/chkconfig --add openstack-nova-scheduler
%post cert
/sbin/chkconfig --add openstack-nova-cert
%post api
for svc in api metadata-api; do
    /sbin/chkconfig --add openstack-nova-$svc
done
%post objectstore
/sbin/chkconfig --add openstack-nova-objectstore
%post console
for svc in console consoleauth xvpvncproxy; do
    /sbin/chkconfig --add openstack-nova-$svc
done
%post cells
/sbin/chkconfig --add openstack-nova-cells

%preun compute
if [ $1 -eq 0 ] ; then
    for svc in compute; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun network
if [ $1 -eq 0 ] ; then
    for svc in network; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun scheduler
if [ $1 -eq 0 ] ; then
    for svc in scheduler; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun cert
if [ $1 -eq 0 ] ; then
    for svc in cert; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun api
if [ $1 -eq 0 ] ; then
    for svc in api metadata-api; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun objectstore
if [ $1 -eq 0 ] ; then
    for svc in objectstore; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun conductor
if [ $1 -eq 0 ] ; then
    for svc in conductor; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun console
if [ $1 -eq 0 ] ; then
    for svc in console consoleauth xvpvncproxy; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun cells
if [ $1 -eq 0 ] ; then
    for svc in cells; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun novncproxy
if [ $1 -eq 0 ] ; then
    for svc in novncproxy; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi

%postun compute
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in compute; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun network
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in network; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun scheduler
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in scheduler; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun cert
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in cert; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun api
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in api metadata-api; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun objectstore
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in objectstore; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun conductor
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in conductor; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun console
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in console consoleauth xvpvncproxy; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun cells
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in cells; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun novncproxy
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in novncproxy; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi

%files
%doc LICENSE
%{_bindir}/nova-all

%files common
%doc LICENSE
%dir %{_sysconfdir}/nova
%{_sysconfdir}/nova/release
%attr(-, root, nova) %{_datadir}/nova/nova-dist.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/nova.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/api-paste.ini
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/rootwrap.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/policy.json
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-nova
%config(noreplace) %{_sysconfdir}/sudoers.d/nova
%config(noreplace) %{_sysconfdir}/polkit-1/localauthority/50-local.d/50-nova.pkla

%dir %attr(0755, nova, root) %{_localstatedir}/log/nova
%dir %attr(0755, nova, root) %{_localstatedir}/run/nova

%{_bindir}/nova-clear-rabbit-queues
%{_bindir}/nova-manage
%{_bindir}/nova-rootwrap

%exclude %{_datarootdir}/nova/*.upstart
%{_datarootdir}/nova
%{_mandir}/man1/nova*.1.gz

%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova
%dir %{_sharedstatedir}/nova/buckets
%dir %{_sharedstatedir}/nova/images
%dir %{_sharedstatedir}/nova/instances
%dir %{_sharedstatedir}/nova/keys
%dir %{_sharedstatedir}/nova/networks
%dir %{_sharedstatedir}/nova/tmp

%files compute
%{_bindir}/nova-compute
%{_bindir}/nova-baremetal-deploy-helper
%{_bindir}/nova-baremetal-manage
%{_initrddir}/openstack-nova-compute
%{_datarootdir}/nova/openstack-nova-compute.upstart
%{_datarootdir}/nova/rootwrap/compute.filters

%files network
%{_bindir}/nova-network
%{_bindir}/nova-dhcpbridge
%{_initrddir}/openstack-nova-network
%{_datarootdir}/nova/openstack-nova-network.upstart
%{_datarootdir}/nova/rootwrap/network.filters

%files scheduler
%{_bindir}/nova-scheduler
%{_initrddir}/openstack-nova-scheduler
%{_datarootdir}/nova/openstack-nova-scheduler.upstart

%files cert
%{_bindir}/nova-cert
%{_initrddir}/openstack-nova-cert
%{_datarootdir}/nova/openstack-nova-cert.upstart
%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova/CA/
%dir %{_sharedstatedir}/nova/CA/certs
%dir %{_sharedstatedir}/nova/CA/crl
%dir %{_sharedstatedir}/nova/CA/newcerts
%dir %{_sharedstatedir}/nova/CA/projects
%dir %{_sharedstatedir}/nova/CA/reqs
%{_sharedstatedir}/nova/CA/*.sh
%{_sharedstatedir}/nova/CA/openssl.cnf.tmpl
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/cacert.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/crl.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/index.txt
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/openssl.cnf
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/serial
%dir %attr(0750, -, -) %{_sharedstatedir}/nova/CA/private
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/private/cakey.pem

%files api
%{_bindir}/nova-api*
%{_initrddir}/openstack-nova-*api
%{_datarootdir}/nova/openstack-nova-*api.upstart
%{_datarootdir}/nova/rootwrap/api-metadata.filters

%files conductor
%{_bindir}/nova-conductor
%{_initrddir}/openstack-nova-conductor
%{_datarootdir}/nova/openstack-nova-conductor.upstart

%files objectstore
%{_bindir}/nova-objectstore
%{_initrddir}/openstack-nova-objectstore
%{_datarootdir}/nova/openstack-nova-objectstore.upstart

%files console
%{_bindir}/nova-console*
%{_bindir}/nova-xvpvncproxy
%{_bindir}/nova-spicehtml5proxy
%{_initrddir}/openstack-nova-console*
%{_datarootdir}/nova/openstack-nova-console*.upstart
%{_initrddir}/openstack-nova-xvpvncproxy
%{_datarootdir}/nova/openstack-nova-xvpvncproxy.upstart
%{_initrddir}/openstack-nova-spicehtml5proxy*
%{_datarootdir}/nova/openstack-nova-spicehtml5proxy.upstart

%files cells
%{_bindir}/nova-cells
%{_initrddir}/openstack-nova-cells
%{_datarootdir}/nova/openstack-nova-cells.upstart

%files novncproxy
%{_bindir}/nova-novncproxy
%{_initrddir}/openstack-nova-novncproxy
%{_datarootdir}/nova/openstack-nova-novncproxy.upstart
%config(noreplace) %{_sysconfdir}/sysconfig/openstack-nova-novncproxy

%files -n python-nova
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitelib}/nova
%{python_sitelib}/nova-%{version}*.egg-info

%if 0%{?with_doc}
%files doc
%doc LICENSE doc/build/html
%endif

%changelog
* Tue Jul 08 2014 Neil Jerram <nj@metaswitch.com> - 2014.1.1_calico0.1-1
- Implement new 'ROUTED' interface type.

* Fri Jun 13 2014 Nikola Đipanov <ndipanov@redhat.com> 2014.1.1-1
- Update to latest stable/icehouse 2014.1.1 release

* Mon May 19 2014 Nikola Đipanov <ndipanov@redhat.com> 2014.1-4
- Drop parallel python packages in RDO el6

* Thu Apr 17 2014 Vladan Popovic <vpopovic@redhat.com> 2014.1-0.14
- Update to upstream 2014.1

* Tue Apr 15 2014 Vladan Popovic <vpopovic@redhat.com> 2014.1-0.13.rc2
- Update to upstream 2014.1.rc2

* Wed Apr 02 2014 Vladan Popovic <vpopovic@redhat.com> 2014.1-0.12.rc1
- Update to upstream 2014.1.rc1

* Wed Mar 19 2014 Vladan Popovic <vpopovic@redhat.com> - 2014.1-0.11.b3
- Update python.oslo.messaging requirement to 1.3.0-0.1.a4 - rhbz#1077860

* Fri Mar 07 2014 Vladan Popovic <vpopovic@redhat.com> - 2014.1-0.10.b3
- Update to Icehouse milestone 3

* Mon Feb 03 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.9.b2
- Avoid commented [DEFAULT] config issue in nova.conf

* Mon Jan 27 2014 Xavier Queralt <xqueralt@redhat.com> - 2014.1-0.8.b2
- Fix the patch for CVE-2013-7130 which was not backported properly

* Fri Jan 24 2014 Xavier Queralt <xqueralt@redhat.com> - 2014.1-0.7.b2
- Add build requirement on python-six

* Fri Jan 24 2014 Xavier Queralt <xqueralt@redhat.com> - 2014.1-0.6.b2
- Update to Icehouse milestone 2
- Require python-keystoneclient for api-paste - rhbz#909113
- Fix root disk leak in live migration - CVE-2013-7130

* Mon Jan 06 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.5.b1
- Avoid [keystone_authtoken] config corruption in nova.conf

* Mon Jan 06 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.4.b1
- Set python-six min version to ensure updated

* Mon Dec 16 2013 Xavier Queralt <xqueralt@redhat.com> - 2014.1-0.1.b1
- Update to Icehouse milestone 1
- Add python-oslo-sphinx to build requirements

* Tue Dec 03 2013 Xavier Queralt <xqueralt@redhat.com> - 2013.2-5
- Fix the CVE number references from the latest change

* Mon Nov 18 2013 Xavier Queralt <xqueralt@redhat.com> - 2013.2-4
- Remove cert and scheduler hard dependency on cinderclient - rhbz#1031679
- Require ipmitool for baremetal driver - rhbz#1022243
- Ensure we don't boot oversized images (CVE-2013-4463 and CVE-2013-2096)

* Wed Oct 23 2013 Xavier Queralt <xqueralt@redhat.com> - 2013.2-3
- Require bridge-utils on nova-compute package - rhbz#1009065

* Fri Oct 18 2013 Xavier Queralt <xqueralt@redhat.com> - 2013.2-2
- require webob1.2
- remove signing_dir from nova-dist.conf to use the default

* Thu Oct 17 2013 Xavier Queralt <xqueralt@redhat.com> - 2013.2-1
- Update to Havana final

* Tue Oct 15 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.2-0.26.rc2
- Update to Havana rc2

* Fri Oct 11 2013 Vladan Popovic <vpopovic@redhat.com> - 2013.2-0.25.rc1
- remove the -s option on qemu-img convert - rhbz#1016896

* Thu Oct 03 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.2-0.23.rc1
- Update to Havana rc1

* Wed Oct 02 2013 Pádraig Brady <pbrady@redhat.com> - 2013.2-0.22.b3
- Select the parallel installable python-jinja2-26

* Tue Oct 01 2013 Lon Hohberger <lhh@redhat.com> - 2013.2-0.21.b3.el6ost.1
- Fix Jinja2 Requires line to match what we have

* Wed Sep 18 2013 Xavier Queralt <xqueralt@redhat.com> - 2013.2-0.21.b3
- Depend on python-oslo-config >= 1:1.2.0 so it is upgraded automatically

* Thu Sep 12 2013 Pádraig Brady <pbrady@redhat.com> - 2013.2-0.20.b3
- Depend on genisoimage to support creating guest config drives

* Mon Sep 09 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.2-0.19.b3
- Fix compute_node_get_all() for Nova Baremetal

* Mon Sep 09 2013 Pádraig Brady <pbrady@redhat.com> - 2013.2-0.18.b3
- Avoid deprecated options in distribution config files

* Mon Sep 09 2013 Dan Prince <dprince@redhat.com> - 2013.2-0.17.b3
- Add dependency on python-babel
- Add dependency on python-jinja2

* Mon Sep 09 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.2-0.15.b3
- Update to Havana milestone 3

* Tue Aug 27 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.2-0.14.b2
- Fix the tarball download link (SOURCE0)

* Tue Aug 27 2013 Xavier Queralt <xqueralt@redhat.com> - 2013.2-0.13.b2
- Set auth_version=v2.0 in nova-dist.conf to avoid http://pad.lv/1154809

* Tue Aug 27 2013 Xavier Queralt <xqueralt@redhat.com> - 2013.2-0.12.b2
- Remove Folsom release deprecated config options from nova-dist.conf

* Tue Aug 27 2013 Xavier Queralt <xqueralt@redhat.com> - 2013.2-0.11.b2
- Add the second dhcpbridge-flagfile to nova-dist.conf 

* Tue Aug 27 2013 Xavier Queralt <xqueralt@redhat.com> - 2013.2-0.10.b2
- Change the default config to poll for DB connection indefinitely

* Wed Aug 07 2013 Xavier Queralt <xqueralt@redhat.com> - 2013.2-0.9.b2
- Create a nova-dist.conf file with default values under /usr/share

* Mon Jul 22 2013 Pádraig Brady <pbrady@redhat.com> - 2013.2-0.8.b2
- Update to Havana milestone 2

* Wed Jul 17 2013 Pádraig Brady <pbrady@redhat.com> - 2013.2-0.6.b1
- Upgrade /etc/sysconfig/openstack-nova-novncproxy correctly

* Mon Jun 24 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.2-0.5.h1
- Remove requirements file to be more flexible with dep versions

* Mon Jun 24 2013 Nikola Đipanov<ndipanov@redhat.com> - 2013.2-0.4.h1
- Add the novncproxy subpackage (moved from the novnc package)

* Fri Jun 14 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.2-0.3.h1
- Fix an issue with the version string

* Mon Jun 10 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.2-0.2.h1
- Add a runtime dep on python-six
- Fix verision reporting

* Fri Jun 07 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.2-0.1.h1
- Update to Havana milestone 1

* Fri May 31 2013 Pádraig Brady <pbrady@redhat.com> - 2013.1.1-3
- Depend on dnsmasq-utils to give direct control over dnsmasq leases

* Fri May 17 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.1.1-2
- Check QCOW2 image size during root disk creation (CVE-2013-2096)

* Mon May 13 2013 Pádraig Brady <pbrady@redhat.com> - 2013.1.1-1
- Update to stable/grizzly 2013.1.1 release

* Mon May 13 2013 Pádraig Brady <pbrady@redhat.com> - 2013.1-4
- Make openstack-nova metapackage depend on openstack-nova-cells
- Add a dependency on python-keystonclient (for auth middleware)

* Fri May 10 2013 Pádraig Brady <pbrady@redhat.com> - 2013.1-3
- Make openstack-nova-network depend on ebtables #961567

* Thu Apr 11 2013 Pádraig Brady <pbrady@redhat.com> - 2013.1-2
- Fix nova network dnsmasq invocation failure #951144

* Mon Apr 08 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.1-1
- Update to Grizzly final

* Tue Apr 02 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.1-0.12.rc2
- Update to Grizzly rc2

* Fri Mar 22 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.1-0.11.rc1
- Update to Grizzly rc1

* Wed Mar 20 2013 Pádraig Brady - 2013.1-0.10.g3
- Remove /etc/tgt/conf.d/nova.conf which was invalid for grizzly

* Tue Mar 12 2013 Pádraig Brady - 2013.1-0.9.g3
- Allow openstack-nova-doc to be installed in isolation

* Tue Feb 26 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.1-0.6.g3
- Add dep to python-pyasn1

* Mon Feb 25 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.1-0.5.g3
- Update to Grizzly milestone 3

* Mon Jan 14 2013 Nikola Đipanov <ndipanov@redhat.com> - 2013.1-0.4.g2
- Update to Grizzly milestone 2
- Add the version info file
- Add python-stevedore dependency
- Add the cells subpackage and init scripts

* Thu Dec 06 2012 Nikola Đipanov <ndipanov@redhat.com> 2013.1-0.3.g1
- Update to Grizzly milestone 1
- Remove volume subpackage - removed from Grizzly
- Add the conductor subpackage - new service added in Grizzly
- Depend on python-libguestfs instead of libguestfs-mount
- Don't add the nova user to the group fuse
- Removes openstack-utils from requirements for nova-common

* Thu Dec 06 2012 Nikola Đipanov <ndipanov@redhat.com> - 2012.2.1-3
- signing_dir renamed from incorrect signing_dirname in default nova.conf

* Tue Dec 04 2012 Nikola Đipanov <ndipanov@redhat.com> - 2012.2.1-2
- Fix rpc_control_exchange regression

* Fri Nov 30 2012 Nikola Đipanov <ndipanov@redhat.com> - 2012.2.1-1
- Update to folsom stable release 1

* Tue Oct 30 2012 Pádraig Brady <pbrady@redhat.com> - 2012.2-2
- Add support for python-migrate-0.6

* Fri Oct 12 2012 Pádraig Brady <pbrady@redhat.com> - 2012.2-1
- Update to folsom final

* Fri Oct 12 2012 Nikola Dipanov <ndipanov@redhat.com> - 2012.1.3-1
- Restore libvirt block storage connections on reboot
- Fix libvirt volume attachment error logging
- Ensure instances with deleted floating IPs can be deleted
- Ensure can contact floating IP after instance snapshot
- Fix tenant usage time accounting
- Ensure correct disk definitions are used on volume attach/detach
- Improve concurrency of long running tasks
- Fix unmounting of LXC containers in the presence of symlinks
- Fix external lock corruption in the presence of SELinux
- Allow snapshotting images that are deleted in glance
- Ensure the correct fixed IP is deallocated when deleting VMs

* Fri Aug 10 2012 Pádraig Brady <P@draigBrady.com> - 2012.1.1-15
- Fix package versions to ensure update dependencies are correct
- Fix CA cert permissions issue introduced in 2012.1.1-10

* Wed Aug  8 2012 Pádraig Brady <P@draigBrady.com> - 2012.1.1-13
- Log live migration errors
- Prohibit host file corruption through file injection (CVE-2012-3447)

* Mon Aug  6 2012 Pádraig Brady <P@draigBrady.com> - 2012.1.1-12
- Fix group installation issue introduced in 2012.1.1-10

* Mon Jul 30 2012 Pádraig Brady <P@draigBrady.com> - 2012.1.1-11
- Update from stable upstream including...
- Fix metadata file injection with xen
- Fix affinity filters when hints is None
- Fix marker behavior for flavors
- Handle local remote exceptions consistently
- Fix qcow2 size on libvirt live block migration
- Fix for API listing of os hosts
- Avoid lazy loading errors on instance_type
- Avoid casts in network manager to prevent races
- Conditionally allow queries for deleted flavours
- Fix wrong regex in cleanup_file_locks
- Add net rules to VMs on compute service start
- Tolerate parsing null connection info in BDM
- Support EC2 CreateImage API for boot from volume
- EC2 DescribeImages reports correct rootDeviceType
- Reject EC2 CreateImage for instance store
- Fix EC2 CreateImage no_reboot logic
- Convert remaining network API casts to calls
- Move where the fixed ip deallocation happens
- Fix the qpid_heartbeat option so that it's effective

* Fri Jul 27 2012 Pádraig Brady <P@draigBrady.com> - 2012.1.1-10
- Split out into more sub packages

* Fri Jul 20 2012 Pádraig Brady <P@draigBrady.com> - 2012.1.1-4
- Enable auto cleanup of old cached instance images
- Fix ram_allocation_ratio based over subscription
- Expose over quota exceptions via native API
- Return 413 status on over quota in the native API
- Fix call to network_get_all_by_uuids
- Fix libvirt get_memory_mb_total with xen
- Use compute_api.get_all in affinity filters (CVE-2012-3371)
- Use default qemu img cluster size in libvirt connect
- Ensure libguestfs has completed before proceeding

* Thu Jul  5 2012 Pádraig Brady <P@draigBrady.com> - 2012.1.1-3
- Distinguish volume overlimit exceptions
- Prohibit host file corruption through file injection (CVE-2012-3360, CVE-2012-3361)

* Wed Jun 27 2012 Pádraig Brady <P@draigBrady.com> - 2012.1.1-2
- Update to latest essex stable branch
- Support injecting new .ssh/authorized_keys files to SELinux enabled guests

* Fri Jun 22 2012 Pádraig Brady <P@draigBrady.com> - 2012.1.1-1
- Update to essex stable release 2012.1.1
- Improve performance and stability of file injection
- add upstart jobs, alternative to sysv initscripts

* Fri Jun 15 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-12
- update performance and stability fixes from essex stable

* Mon Jun 11 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-11
- fix an exception caused by the fix for CVE-2012-2654
- fix the encoding of the dns_domains table (requires a db sync)
- fix a crash due to a nova services startup race (#825051)

* Fri Jun 08 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-10
- Enable libguestfs image inspection

* Wed Jun 06 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-9
- Sync up with Essex stable branch, including...
- Fix for protocol case handling (#829441, CVE-2012-2654)

* Wed May 16 2012 Alan Pevec <apevec@redhat.com> - 2012.1-8
- Remove m2crypto and other dependencies no loner needed by Essex

* Wed May 16 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-7
- Depend on tunctl which can be used when `ip tuntap` is unavailable
- Sync up with Essex stable branch
- Handle updated qemu-img info output
- Replace openstack-nova-db-setup with openstack-db

* Wed May 09 2012 Alan Pevec <apevec@redhat.com> - 2012.1-6
- Remove the socat dependency no longer needed by Essex

* Tue May 01 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-5
- Start the services later in the boot sequence

* Fri Apr 27 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-4
- Fix install issues with new Essex init scripts

* Wed Apr 25 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-3
- Use parallel installed versions of python-routes and python-paste-deploy

* Thu Apr 19 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-2
- Sync up with Essex stable branch
- Support more flexible guest image file injection
- Enforce quota on security group rules (#814275, CVE-2012-2101)
- Provide startup scripts for the Essex VNC services
- Provide a startup script for the separated metadata api service

* Fri Apr 13 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-1
- Update to Essex release

* Sun Apr 01 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-0.1.rc1
- Update to Essex release candidate 1

* Thu Mar 29 2012 Pádraig Brady <P@draigBrady.com> - 2011.3.1-8
- Remove the dependency on the not yet available dnsmasq-utils

* Thu Mar 29 2012 Russell Bryant <rbryant@redhat.com> - 2011.3.1-7
- CVE-2012-1585 - Long server names grow nova-api log files significantly
- Resolves: rhbz#808148

* Tue  Mar 06 2012 Pádraig Brady <P@draigBrady.com> - 2011.3.1-5
- Require bridge-utils

* Mon Feb 13 2012 Pádraig Brady <P@draigBrady.com> - 2011.3.1-4
- Support --force_dhcp_release (#788485)

* Fri Jan 27 2012 Pádraig Brady <P@draigBrady.com> - 2011.3.1-3
- Suppress erroneous output to stdout on package install (#785115)

* Mon Jan 23 2012 Pádraig Brady <P@draigBrady.com> - 2011.3.1-2
- Fix a REST API v1.0 bug causing a regression with deltacloud

* Fri Jan 20 2012 Pádraig Brady <P@draigBrady.com> - 2011.3.1-1
- Update to 2011.3.1 release
- Allow empty mysql root password in mysql setup script
- Enable mysqld at boot in mysql setup script

* Wed Jan 18 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3.1-0.4.10818%{?dist}
- Update to latest 2011.3.1 release candidate
- Re-add nova-{clear-rabbit-queues,instance-usage-audit}

* Tue Jan 17 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3.1-0.3.10814
- nova-stack isn't missing after all

* Tue Jan 17 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3.1-0.2.10814
- nova-{stack,clear-rabbit-queues,instance-usage-audit} temporarily removed because of lp#917676

* Tue Jan 17 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3.1-0.1.10814
- Update to 2011.3.1 release candidate
- Only adds 4 patches from upstream which we didn't already have

* Wed Jan 11 2012 Pádraig Brady <P@draigBrady.com> - 2011.3-19
- Fix libguestfs support for specified partitions
- Fix tenant bypass by authenticated users using API (#772202, CVE-2012-0030)

* Fri Jan  6 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3-18
- Fix up recent patches which don't apply

* Fri Jan  6 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3-17
- Backport tgtadm off-by-one fix from upstream (#752709)

* Fri Jan  6 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3-16
- Rebase to latest upstream stable/diablo, pulling in ~50 patches

* Fri Jan  6 2012 Mark McLoughlin <markmc@redhat.com> - 2011.3-15
- Move recent patches into git (no functional changes)

* Fri Dec 30 2011 Pádraig Brady <P@draigBrady.com> - 2011.3-14
- Don't require the fuse group (#770927)
- Require the fuse package (to avoid #767852)

* Wed Dec 14 2011 Pádraig Brady <P@draigBrady.com> - 2011.3-13
- Sanitize EC2 manifests and image tarballs (#767236, CVE 2011-4596)
- update libguestfs support

* Tue Dec 06 2011 Russell Bryant <rbryant@redhat.com> - 2011.3-11
- Add --yes, --rootpw, and --novapw options to openstack-nova-db-setup.

* Wed Nov 30 2011 Pádraig Brady <P@draigBrady.com> - 2011.3-10
- Use updated parallel install versions of epel packages
- Add libguestfs support

* Tue Nov 29 2011 Pádraig Brady <P@draigBrady.com> - 2011.3-9
- Update the libvirt dependency from 0.8.2 to 0.8.7
- Ensure we don't access the net when building docs

* Tue Nov 29 2011 Russell Bryant <rbryant@redhat.com> - 2011.3-8
- Change default database to mysql. (#735012)

* Mon Nov 14 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-8
- Add ~20 significant fixes from upstream stable branch

* Wed Oct 26 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-7
- Fix password leak in EC2 API (#749385, CVE 2011-4076)

* Mon Oct 24 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-5
- Fix block migration (#741690)

* Fri Oct 21 2011 David Busby <oneiroi@fedoraproject.org> 2011.3-5
- Changed requirement from python-sphinx, to python-sphinx10
- Switch back to SysV init for el6

* Mon Oct 17 2011 Bob Kukura <rkukura@redhat.com> - 2011.3-4
- Add dependency on python-amqplib (#746685)

* Wed Sep 28 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-3
- Fix lazy load exception with security groups (#741307)
- Fix issue with nova-network deleting the default route (#741686)
- Fix errors caused by MySQL connection pooling (#741312)

* Mon Sep 26 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-2
- Manage the package's patches in git; no functional changes.

* Thu Sep 22 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-1
- Update to Diablo final.
- Drop some upstreamed patches.
- Update the metadata-accept patch to what's proposed for essex.
- Switch rpc impl from carrot to kombu.

* Mon Sep 19 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.10.d4
- Use tgtadm instead of ietadm (#737046)

* Wed Sep 14 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.9.d4
- Remove python-libguestfs dependency (#738187)

* Mon Sep  5 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.8.d4
- Add iptables rule to allow EC2 metadata requests (#734347)

* Sat Sep  3 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.7.d4
- Add iptables rules to allow requests to dnsmasq (#734347)

* Wed Aug 31 2011 Angus Salkeld <asalkeld@redhat.com> - 2011.3-0.6.d4
- Add the one man page provided by nova.
- Start services with --flagfile rather than --flag-file (#735070)

* Tue Aug 30 2011 Angus Salkeld <asalkeld@redhat.com> - 2011.3-0.5.d4
- Switch from SysV init scripts to systemd units (#734345)

* Mon Aug 29 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.4.d4
- Don't generate root CA during %%post (#707199)
- The nobody group shouldn't own files in /var/lib/nova
- Add workaround for sphinx-build segfault

* Fri Aug 26 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.3.d4
- Update to diablo-4 milestone
- Use statically assigned uid:gid 162:162 (#732442)
- Collapse all sub-packages into openstack-nova; w/o upgrade path
- Reduce use of macros
- Rename stack to nova-stack
- Fix openssl.cnf.tmpl script-without-shebang rpmlint warning
- Really remove ajaxterm
- Mark polkit file as %%config

* Mon Aug 22 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.2.1449bzr
- Remove dependency on python-novaclient

* Wed Aug 17 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.1.1449bzr
- Update to latest upstream.
- nova-import-canonical-imagestore has been removed
- nova-clear-rabbit-queues was added

* Tue Aug  9 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.2.1409bzr
- Update to newer upstream
- nova-instancemonitor has been removed
- nova-instance-usage-audit added

* Tue Aug  9 2011 Mark McLoughlin <markmc@redhat.com> - 2011.3-0.1.bzr1130
- More cleanups
- Change release tag to reflect pre-release status

* Wed Jun 29 2011 Matt Domsch <mdomsch@fedoraproject.org> - 2011.3-1087.1
- Initial package from Alexander Sakhnov <asakhnov@mirantis.com>
  with cleanups by Matt Domsch
