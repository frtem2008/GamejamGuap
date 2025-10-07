{
  pkgs,
  lib,
  config,
  ...
}:
{
  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    # We require the python with C wrapper for compatibility with nixpkgs pygame
    package = pkgs.python313;
    venv.enable = true;
  };

  # https://devenv.sh/packages/
  packages = with pkgs; [
    # Required to install python dependencies easily
    python311Packages.pip

    # System dependencies for pygame
    alsa-lib
    libGL
    libsndfile
    SDL
    SDL_image
    SDL_mixer
    SDL_ttf
    wayland
    xorg.libXcursor
    xorg.libXi
    xorg.libXext
  ];

  # Install pygame via pip
  enterShell = ''
    echo "Installing pygame..."
    pip install pygame
  '';

  # Set up environment variables for Wayland and SDL
  env = {
    SDL_VIDEODRIVER = "wayland";
    PYTHONPYCACHEFLAG = "1";
  };

  # See full reference at https://devenv.sh/reference/options/
}
