from esphome import pins
from esphome.components import stepper
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_DIR_PIN, CONF_ID, CONF_ENABLE_PIN, CONF_SLEEP_PIN, CONF_STEP_PIN


a4988_ns = cg.esphome_ns.namespace('a4988')
A4988 = a4988_ns.class_('A4988', stepper.Stepper, cg.Component)

CONFIG_SCHEMA = stepper.STEPPER_SCHEMA.extend({
    cv.Required(CONF_ID): cv.declare_id(A4988),
    cv.Required(CONF_STEP_PIN): pins.gpio_output_pin_schema,
    cv.Required(CONF_DIR_PIN): pins.gpio_output_pin_schema,
    cv.Optional(CONF_SLEEP_PIN): pins.gpio_output_pin_schema,
    cv.Optional(CONF_ENABLE_PIN): pins.gpio_output_pin_schema,
}).extend(cv.COMPONENT_SCHEMA)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield stepper.register_stepper(var, config)

    step_pin = yield cg.gpio_pin_expression(config[CONF_STEP_PIN])
    cg.add(var.set_step_pin(step_pin))
    dir_pin = yield cg.gpio_pin_expression(config[CONF_DIR_PIN])
    cg.add(var.set_dir_pin(dir_pin))
    enable_pin = yield cg.gpio_pin_expression(config[CONF_ENABLE_PIN])
    cg.add(var.set_enable_pin(enable_pin))

    if CONF_SLEEP_PIN in config:
        sleep_pin = yield cg.gpio_pin_expression(config[CONF_SLEEP_PIN])
        cg.add(var.set_sleep_pin(sleep_pin))
