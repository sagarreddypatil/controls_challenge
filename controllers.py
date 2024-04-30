class BaseController:
  def update(self, target_lataccel, current_lataccel, state):
    raise NotImplementedError


class OpenController(BaseController):
  def update(self, target_lataccel, current_lataccel, state):
    return target_lataccel


class SimpleController(BaseController):
  def update(self, target_lataccel, current_lataccel, state):
    return (target_lataccel - current_lataccel) * 0.3
  
class LazyController(BaseController):
  def update(self, target_lataccel, current_lataccel, state):
    return 0


CONTROLLERS = {
  'open': OpenController,
  'simple': SimpleController,
  'lazy': LazyController,
}
