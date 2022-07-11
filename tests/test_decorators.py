# Python's Libraries
import logging

# Third-party Libraries
from unittest import TestCase

# Own's Libraries
from src.stxloggerutil.log_admin import LogAdmin
from src.stxloggerutil.decorators import step
from src.stxloggerutil.log_admin import LogEnvironment


@step("Executing the example function on Production")
def example_Function(_parameter):
    logging.critical("Executing the example function on Production ... critical")
    logging.error("Executing the example function on Production ... error")
    logging.warning("Executing the example function on Production ... warning")
    logging.info("Executing the example function on Production ... info")
    logging.debug("Executing the example function on Production ... debug")


@step("Executing the example function with Level", _level=2)
def example_FunctionWithLevel(_parameter):
    logging.critical("Executing the example function with level ... critical")
    logging.error("Executing the example function with level ... error")
    logging.warning("Executing the example function with level ... warning")
    logging.info("Executing the example function with level ... info")
    logging.debug("Executing the example function with level ... debug")


@step("Executing the example function with Sublevel", _level=2.2)
def example_FunctionWithSublevel(_parameter):
    logging.critical("Executing the example function with sublevel ... critical")
    logging.error("Executing the example function with sublevel ... error")
    logging.warning("Executing the example function with sublevel ... warning")
    logging.info("Executing the example function with sublevel ... info")
    logging.debug("Executing the example function with sublevel ... debug")


@step("Executing the example function with Error", _level=3)
def example_FunctionWithError(_parameter):
    raise NameError("Example Error")


class StepTest(TestCase):

    def test_Given_ShowTimeAndProductionParameter_When_IsTrue_Then_ShowTime(self):
        LogAdmin.create_Logger(LogEnvironment.PRODUCTION, "test1")
        example_Function("cadenita")

    def test_Given_ShowTimeAndProductionParameter_When_IsFalse_Then_DontShowTime(self):
        LogAdmin.create_Logger(LogEnvironment.PRODUCTION, "test2", False)
        example_Function(12)

    def test_Given_ShowTimeAndDevelopmentParameter_When_IsTrue_Then_ShowTime(self):
        LogAdmin.create_Logger(LogEnvironment.DEVELOPMENT, "test1")
        example_Function("cadenita")

    def test_Given_ShowTimeAndDevelopmentParameter_When_IsFalse_Then_DontShowTime(self):
        LogAdmin.create_Logger(LogEnvironment.DEVELOPMENT, "test2", False)
        example_Function(23)

    def test_Given_LevelAndDevelopmentParameter_Then_ShowLevelDots(self):
        LogAdmin.create_Logger(LogEnvironment.DEVELOPMENT, "test1")
        example_FunctionWithLevel("cadenita")

    def test_Given_SublevelAndDevelopmentParameter_Then_ShowSublevelDots(self):
        LogAdmin.create_Logger(LogEnvironment.DEVELOPMENT, "test1")
        example_FunctionWithSublevel("cadenita")

    def test_Given_LevelAndDevelopmentParameter_WhenRaiseError_Then_ShowLevelDotsAndError(self):
        LogAdmin.create_Logger(LogEnvironment.DEVELOPMENT, "test1")
        with self.assertRaises(NameError):
            example_FunctionWithError("cadenita")
