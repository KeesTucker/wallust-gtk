#!/bin/bash

echo "Force updating text colour for GTK Colloid theme"

# Path to wallust.py and target directory
wallust_py="/home/kees/.config/wallust/templates/soggy-gtk/scripts/wallust.py"
target_dir="/home/kees/.config/wallust/templates/soggy-gtk/colloid"

# Extract WallustDark.text color (assumes class order doesn't change)
replacement=$(awk '
  $1 == "class" && $2 == "WallustDark(WallustBase):" { in_class=1 }
  in_class && $1 == "text" {
    gsub(/"/, "", $3)
    print "#" $3
    exit
  }
' "$wallust_py")

# Safety check
if [[ -z "$replacement" ]]; then
  echo "Failed to extract WallustDark.text color."
  exit 1
fi

echo "Replacing all #FFFFFF variants with $replacement"

# Run replacement
find "$target_dir" -type f -exec sed -i -E \
  "s/#?[Ff]{6}/$replacement/g" {} +

echo "Done."
