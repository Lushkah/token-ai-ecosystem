# Lushka Intel Arc Mining Runtime

This contains the supplied Intel Arc GPU dependency installer for infrastructure
that Lushka owns or is explicitly authorized to administer.

It installs/verifies OpenCL and Level Zero userspace dependencies and checks
access to `/dev/dri/render*`.

The mobile wallet does not execute this script or mine in the background.
A future authorized mining backend can report worker telemetry to the app.

Example on an authorized mining worker:
  chmod +x install-deps.sh
  ./install-deps.sh
