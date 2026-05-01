import os
from PIL import Image

def split_image(image_path, rows=4, cols=4, output_dir="split_result"):
    """
    將圖片切割成指定的列數與行數 (4x4)。
    """
    try:
        if not os.path.exists(image_path):
            print(f"錯誤：找不到檔案 {image_path}")
            return

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"已建立輸出目錄: {output_dir}")
            
        img = Image.open(image_path)
        width, height = img.size
        
        # 計算每一塊的大小
        tile_w = width // cols
        tile_h = height // rows
        
        print(f"原始圖片尺寸: {width}x{height}")
        print(f"切割後每塊尺寸: {tile_w}x{tile_h}")
        
        for r in range(rows):
            for c in range(cols):
                # 定義切割區域 (left, upper, right, lower)
                left = c * tile_w
                upper = r * tile_h
                right = left + tile_w
                lower = upper + tile_h
                
                # 執行切割
                tile = img.crop((left, upper, right, lower))
                
                # 存檔命名規則：tile_列_行.png
                output_filename = f"tile_{r+1}_{c+1}.png"
                output_path = os.path.join(output_dir, output_filename)
                tile.save(output_path)
                print(f"成功儲存: {output_path}")
                
        print("\n=== 所有圖片切割完成！ ===")
        print(f"請到 {os.path.abspath(output_dir)} 查看結果。")
        
    except Exception as e:
        print(f"執行過程中發生錯誤: {e}")

if __name__ == "__main__":
    # 指定目標圖片路徑
    target_image = "ChatGPT Image 2026年4月29日 下午07_19_24.png"
    
    # 執行 4x4 切割
    split_image(target_image, rows=4, cols=4)
