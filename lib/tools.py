from pydantic import BaseModel
from agents import function_tool

class DesignDataBaseEntry(BaseModel):
    rooms: list[str]
    design_style: str
    color_palette: list[str]
    furniture: list[str]


@function_tool
async def save_design_data_to_database(data: DesignDataBaseEntry):
    print("Design data saved to database:", data)
    # Here you would implement the actual database saving logi
    with open("output/design_output.txt", "w") as f:
        f.write(str(data))
    return "Design details successfully saved. Proceed to the next room's design."