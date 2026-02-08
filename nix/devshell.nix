{ pkgs }:
pkgs.mkShell {
  # Add build dependencies
  packages = with pkgs; [
    black
  ];

  # Add environment variables
  env = { };

  # Load custom bash code
  shellHook = ''

  '';
}
