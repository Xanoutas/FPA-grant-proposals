# FreeCAD/FPA-grant-proposals/design_system.py

import os
import json

class DesignSystem:
    def __init__(self, theme_file):
        self.theme_file = theme_file
        self.theme_data = self.load_theme()

    def load_theme(self):
        if os.path.exists(self.theme_file):
            with open(self.theme_file, 'r') as file:
                return json.load(file)
        else:
            raise FileNotFoundError(f"Theme file {self.theme_file} not found")

    def get_color(self, color_name):
        return self.theme_data.get(color_name, None)

    def get_font(self, font_name):
        return self.theme_data.get(font_name, None)

    def get_component_style(self, component_name):
        return self.theme_data.get(component_name, None)

    def update_theme(self, new_theme_data):
        self.theme_data.update(new_theme_data)
        with open(self.theme_file, 'w') as file:
            json.dump(self.theme_data, file, indent=4)

# Example usage
if __name__ == "__main__":
    ds = DesignSystem("path/to/theme.json")
    print(ds.get_color("primary"))
    print(ds.get_font("heading"))
    ds.update_theme({"primary": "#FF0000"})