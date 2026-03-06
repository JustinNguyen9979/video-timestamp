from moviepy import VideoFileClip, CompositeVideoClip, VideoClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from datetime import datetime, timedelta
import sys
import os
import warnings
warnings.filterwarnings("ignore")

# ── BƯỚC 1: Nhận file video ──────────────────────────────────────────────────
print("\n" + "="*50)
print("  CHÈN TIMESTAMP VÀO VIDEO")
print("="*50)
print("\n📂 Kéo thả file video vào đây rồi nhấn Enter: ", end="", flush=True)

video_path = input().strip().strip("'\"")   # xử lý cả trường hợp macOS tự thêm nháy

if not os.path.exists(video_path):
    print(f"\n❌ Không tìm thấy file: {video_path}")
    sys.exit(1)

print(f"✅ Đã nhận file: {os.path.basename(video_path)}")

# ── BƯỚC 2: Nhập ngày giờ bắt đầu ───────────────────────────────────────────
print("\n🕐 Nhập ngày giờ bắt đầu (định dạng: DD/MM/YYYY HH:MM:SS)")
print("   Ví dụ: 03/03/2026 10:00:00")
print("   > ", end="", flush=True)

while True:
    time_input = input().strip()
    try:
        start_time = datetime.strptime(time_input, "%d/%m/%Y %H:%M:%S")
        print(f"✅ Thời gian bắt đầu: {start_time.strftime('%d/%m/%Y %H:%M:%S')}")
        break
    except ValueError:
        print("   ❌ Sai định dạng, nhập lại (DD/MM/YYYY HH:MM:SS): ", end="", flush=True)

# ── BƯỚC 3: Xử lý video ──────────────────────────────────────────────────────
base_name   = os.path.splitext(os.path.basename(video_path))[0]
output_path = os.path.join(os.path.dirname(video_path), f"{base_name}_timestamp.mp4")

print(f"\n⏳ Đang xử lý video...")

video = VideoFileClip(video_path)

TEXT_COLOR = (255, 255, 0, 255)
FONT_SIZE  = 26
POS_X, POS_Y = 15, video.h - 55

try:
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New.ttf", FONT_SIZE)
except:
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", FONT_SIZE)

def make_text_frame(t):
    current = start_time + timedelta(seconds=t)
    label   = current.strftime("%d/%m/%Y  %H:%M:%S")
    img     = Image.new("RGBA", (380, 44), (0, 0, 0, 0))
    draw    = ImageDraw.Draw(img)
    for dx, dy in [(-1,-1),(-1,1),(1,-1),(1,1),(0,2),(2,0)]:
        draw.text((10+dx, 8+dy), label, font=font, fill=(0, 0, 0, 160))
    draw.text((10, 8), label, font=font, fill=TEXT_COLOR)
    return np.array(img)

txt_clip = (VideoClip(make_text_frame, duration=video.duration)
            .with_position((POS_X, POS_Y)))

final = CompositeVideoClip([video, txt_clip])
final.write_videofile(output_path, codec="libx264", audio_codec="aac")

print(f"\n✅ Hoàn thành! File đã lưu tại:\n   {output_path}\n")
