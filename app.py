import streamlit as st
import asyncio
from lib.agent import run_agent
import tempfile
import os

from dotenv import load_dotenv

load_dotenv()

st.title("Interior Designer Agent")

style = st.text_input("Describe your intended interior design styling:")
image_file = st.file_uploader("Upload an image (PNG or JPG)", type=["png", "jpg", "jpeg"])

if st.button("Run Agent"):
    if style and image_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
          tmp_file.write(image_file.read())
          tmp_file_path = tmp_file.name
        
        # Display the uploaded floorplan image
        st.image(image_file, caption="Uploaded Floorplan", use_container_width=True)
        st.write("Running agent...")
        # Run the agent asynchronously
        result = asyncio.run(run_agent(style, tmp_file_path))
        if result:
            final_design = result['final_output']
            
            # Display the structured design data using the actual field names
            st.header("✨ Generated Design Plan")
            st.markdown(f"**Style:** {final_design.design_style}")
            st.markdown(f"**Rooms Designed:** {', '.join(final_design.rooms)}")
            st.markdown(f"**Color Palette:** {', '.join(final_design.color_palette)}")
            
            # Display furniture list clearly
            st.subheader("🛋️ Furniture Details")
            for detail in final_design.furniture:
                st.write(f"- {detail}")

            # Display images
            if 'image_paths' in result:
                st.header("🖼️ Room Visualizations")
                for img_path in result['image_paths']:
                    # Use os.path.basename for a cleaner caption
                    caption = os.path.basename(img_path) 
                    st.image(img_path, caption=caption, use_container_width=True)
                    
        else:
            st.error("No result returned from agent.")