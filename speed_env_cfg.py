from isaaclab.utils import configclass
from .flat_env_cfg import AnymalCFlatEnvCfg

@configclass
class AnymalCSpeedEnvCfg(AnymalCFlatEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        
        # MAXIMIZE SPEED!
        self.rewards.track_lin_vel_xy_exp.weight = 3.0  # 3x more important
        
        # Reduce energy penalties - we don't care about efficiency
        self.rewards.dof_torques_l2.weight = -5.0e-6  # Less penalty (was -2.5e-5)
        self.rewards.action_rate_l2.weight = -0.001  # Much less penalty (was -0.01)
        
        # Still keep upright
        self.rewards.flat_orientation_l2.weight = -5.0

@configclass
class AnymalCSpeedEnvCfg_PLAY(AnymalCSpeedEnvCfg):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        self.observations.policy.enable_corruption = False
        self.events.base_external_force_torque = None
        self.events.push_robot = None