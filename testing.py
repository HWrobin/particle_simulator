from particle_simulator import *

sim = Simulation(
    width=1500,
    height=1000,
    title="Simulation",
    gridres=(50, 50),
    temperature=0,
    g=1,
    air_res=0.25,
    ground_friction=0.1,
)

# Adding two black walls as large, immovable particles
# Wall 1 - Positioned on the left side
for j in range(2):
    for i in range(50):
        Particle(
            sim,
            x=1300 + j * 100,  # Position at the very left
            y=1000 - i * 10,  # Centered vertically
            radius=5,  # Thickness of the wall
            color=[0, 0, 0],  # Black color
            mass=1,  # Infinite mass to make it immovable
            bounciness=1.0,  # Fully elastic collisions
            velocity=np.zeros(2),  # No initial velocity
            collisions=True,  # Enable collisions
            attract_r=50,  # No attraction
            repel_r=1,  # No repulsion
            attraction_strength=8,
            repulsion_strength=5,
            locked=True,  # Make sure the wall doesn't move
        )

for j in range(2):
    for i in range(50):
        Particle(
            sim,
            x=980 + j * 100,  # Position at the very left
            y=1000 - i * 10,  # Centered vertically
            radius=5,  # Thickness of the wall
            color=[0, 0, 0],  # Black color
            mass=1,  # Infinite mass to make it immovable
            bounciness=1.0,  # Fully elastic collisions
            velocity=np.zeros(2),  # No initial velocity
            collisions=True,  # Enable collisions
            attract_r=-1,  # No attraction
            repel_r=1,  # No repulsion
            attraction_strength=0,
            repulsion_strength=5,
            locked=True,  # Make sure the wall doesn't move
        )

for k in range(2):
    for i in range(8):
        for j in range(8):
            Particle(
                sim,
                x=1000 + k * 325 + i * 2,  # Position at the very left
                y=1000 - j * 5,  # Centered vertically
                radius=5,  # Thickness of the wall
                color=[0, 128, 192],  # Black color
                mass=1,  # Infinite mass to make it immovable
                bounciness=0,  # Fully elastic collisions
                velocity=np.zeros(2),  # No initial velocity
                collisions=True,  # Enable collisions
                attract_r=100,  # No attraction
                repel_r=23,  # No repulsion
                attraction_strength=2.5,
                repulsion_strength=1,
                locked=False,  # Make sure the wall doesn't move
            )

sim.simulate()
