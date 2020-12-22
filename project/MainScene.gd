extends Node2D

export (NodePath) var dropdown_path
onready var dropdown = get_node(dropdown_path)

func _ready():
	add_items()
	
func add_items():
	dropdown.add_item("Option 1")
	dropdown.add_item("Option 2")



func _on_loadDBButton_pressed():
	print('Load Data Base')

