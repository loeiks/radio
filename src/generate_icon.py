from PIL import Image, ImageDraw
import os

def create_radio_icon(size=64, background_color=(44, 62, 80), note_color=(46, 204, 113)):
    # Create a new image with transparency
    icon = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(icon)
    
    # Draw background circle
    padding = size // 8
    draw.ellipse([padding, padding, size - padding, size - padding], 
                 fill=background_color)
    
    # Draw musical note
    note_width = size // 4
    note_height = size // 2
    center_x = size // 2
    center_y = size // 2
    
    # Draw note head
    draw.ellipse([center_x - note_width//2, center_y, 
                  center_x + note_width//2, center_y + note_width],
                 fill=note_color)
    
    # Draw note stem
    draw.rectangle([center_x + note_width//4, center_y - note_height//2,
                   center_x + note_width//2, center_y + note_width//2],
                   fill=note_color)
    
    # Save in different sizes
    icon_sizes = [16, 32, 48, 64, 128]
    icon_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets')
    os.makedirs(icon_dir, exist_ok=True)
    
    for icon_size in icon_sizes:
        resized_icon = icon.resize((icon_size, icon_size), Image.Resampling.LANCZOS)
        icon_path = os.path.join(icon_dir, f'radio_icon_{icon_size}x{icon_size}.png')
        resized_icon.save(icon_path, 'PNG')
    
    # Save ICO file with all sizes
    icon_path = os.path.join(icon_dir, 'radio_icon.ico')
    icon.save(icon_path, 'ICO', sizes=[(size, size) for size in icon_sizes])
    
    return icon_path

if __name__ == '__main__':
    create_radio_icon()
