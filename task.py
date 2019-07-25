import numpy as np
from physics_sim import PhysicsSim

class Task():
    
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__( self, init_pose=None, init_velocities=None, init_angle_velocities=None, runtime=5., target_pos=None ):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
         
    
       # Se a posição B ( alvo ) não for especificada, então assume uma posição padrão
        if target_pos is None:
            target_pos =  np.array([ 0., 0., 100. ]) 
            
            
        # Isola Coordenadas do Local a se deslocar
        x_tar     =   round( np.around( target_pos[ 0 ], decimals=0 ))
        y_tar     =   round( np.around( target_pos[ 1 ], decimals=0 ))
        z_tar     =   round( np.around( target_pos[ 2 ], decimals=0 ))
        
        
        # Se a posição A ( inicial ) não for especificada, então assume uma posição padrão
        if init_pose is None:
            init_pose = np.array([ 0.,  0.,  0.,  0.,  0.,  0. ])
        
        
        # Se a velocidade inicial não for especificada, então o drone direciona a velocidade de cada um dos eixos
        # X, Y & Z para as coordenadas a se deslocar
        if init_velocities is None:
            init_velocities = np.array([ x_tar * 0.7, y_tar * 0.7, z_tar * 0.7 ])
                
            
        # Se a posição A ( inicial ) não for especificada, então assume uma posição padrão
        if init_angle_velocities is None:
            init_angle_velocities = np.array([ 0.,  0.,  0. ])
            
                
        # Valores Padrão
        self.sim            =  PhysicsSim( init_pose, init_velocities, init_angle_velocities, runtime ) 
        self.action_repeat  =  3
        self.action_size    =  4
        self.action_low     =  0
        self.action_high    =  900
        self.state_size     =  self.action_repeat * 6
        self.target_pos     =  target_pos
        
        
        
    def get_distance( self, x_tar, y_tar, z_tar, x_pos, y_pos, z_pos ):                        
        """ Calcula a Distância entre DOIS Pontos, usando Geometria Analítica & Cálculo Vetorial """

        # calcula Hipotenusa entre os eixos X & Y
        cat_x    =   ( x_tar - x_pos  ) ** 2
        cat_y    =   ( y_tar - y_pos  ) ** 2          
        hip_xy   =   ( cat_x + cat_y  ) ** ( 1/2 )
        cat_xy   =     hip_xy ** 2

        # calcula Hipotenusa entre os eixos XY & Z
        cat_z    =   ( z_tar - z_pos  ) ** 2    
        hip_xyz  =   ( cat_xy + cat_z ) ** ( 1/2 )

        # retorna distância oriunda da Hipotenusa projetada nos eixos "X, Y & Z"
        hip_xyz  =    round( hip_xyz )
        return        hip_xyz  
        
        
        
    def get_reward( self ):               
        # Separa Valores dos Eixos Atuais
        x_pos     =   round( np.around( self.sim.pose[ 0 ],   decimals=0 ))
        y_pos     =   round( np.around( self.sim.pose[ 1 ],   decimals=0 ))
        z_pos     =   round( np.around( self.sim.pose[ 2 ],   decimals=0 ))
                
        # Separa Valores dos Eixos Desejados
        x_tar     =   round( np.around( self.target_pos[ 0 ], decimals=0 ))
        y_tar     =   round( np.around( self.target_pos[ 1 ], decimals=0 ))
        z_tar     =   round( np.around( self.target_pos[ 2 ], decimals=0 ))
          
        
        # se estiver no chão e o chão não for o objetivo, penaliza o agente
        if (( z_tar != 0 ) and ( z_pos < 1 )):
            reward   =  - 100000000
        else:
                        
            # recompensa da distância do ponto "A" Vs ponto "B"
            dist_pB  =    self.get_distance( x_tar, y_tar, z_tar, x_pos, y_pos, z_pos )
                        
            # realiza ajuste caso esteja no ponto exato
            if dist_pB < 2:
                reward = 30000000
                
            else:                
                reward = ((( 1 / dist_pB ) * 10000 ) ** 2 )
                                     
                    
        # divide por 3, em função de "self.action_repeat", desta forma as recompensas
        # seguem a estrutura planejada
        reward = reward / 3
        return reward
        

        
    def step( self, rotor_speeds ):
        """Uses action to obtain next state, reward, done."""
        reward    =  0
        pose_all  =  []
        for _ in range( self.action_repeat ):
            done  =  self.sim.next_timestep( rotor_speeds ) # update the sim pose and velocities
            reward += self.get_reward() 
            pose_all.append( self.sim.pose )
        next_state = np.concatenate( pose_all )
        return next_state, reward, done

    
    def reset( self ):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([ self.sim.pose ] * self.action_repeat ) 
        return state
    