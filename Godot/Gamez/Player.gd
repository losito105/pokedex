extends KinematicBody2D

var velocity = Vector2(0,0)
const speed = 180
const gravity = 40
const less_gravity = 25
const jump_force = -600




var drag = .5


const jump_buffer = 0.08


var dead = false




func _physics_process(delta):
	var grounded = is_on_floor()
	var pressed_jump = Input.is_action_just_pressed("jump")
	if !dead:
		if Input.is_action_pressed("move_right"):
			velocity.x += speed
			$AnimatedSprite.play("walk")
			$AnimatedSprite.flip_h = false
		elif Input.is_action_pressed("move_left"):
			velocity.x -= speed
			$AnimatedSprite.play("walk")
			$AnimatedSprite.flip_h = true
		if (pressed_jump and grounded):
			velocity.y = jump_force
			

	if Input.is_action_pressed("jump"):
		velocity.y += less_gravity 
	else:
		velocity.y += gravity
	
	if grounded and velocity.y > 25:
		velocity.y = 25
	if !grounded:
		$AnimatedSprite.play("jump")
		
	velocity = move_and_slide(velocity, Vector2.UP)
	velocity.x = lerp(velocity.x, 0, 0.25)
	
func jump():
	if dead:
		return
	velocity.y = jump_force
