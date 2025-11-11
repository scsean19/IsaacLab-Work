from isaaclab.utils import configclass
from .flat_env_cfg import AnymalCFlatEnvCfg

@configclass
class AnymalCEfficientEnvCfg(AnymalCFlatEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        
        # Speed is less important
        self.rewards.track_lin_vel_xy_exp.weight = 0.8  # Reduced from 1.0
        
        # MAXIMIZE EFFICIENCY - heavy penalties on energy use
        self.rewards.dof_torques_l2.weight = -1.0e-4  # 4x more penalty (was -2.5e-5)
        self.rewards.action_rate_l2.weight = -0.05  # 5x more penalty (was -0.01)
        self.rewards.dof_acc_l2.weight = -1.0e-6  # More penalty on acceleration
        
        # Reward smooth, proper gait
        self.rewards.feet_air_time.weight = 1.0  # 2x reward (was 0.5)
        
        # Keep upright
        self.rewards.flat_orientation_l2.weight = -5.0

@configclass
class AnymalCEfficientEnvCfg_PLAY(AnymalCEfficientEnvCfg):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        self.observations.policy.enable_corruption = False
        self.events.base_external_force_torque = None
        self.events.push_robot = None