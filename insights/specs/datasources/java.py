"""
Custom datasources for java information
"""
from insights.combiners.ps import Ps
from insights.core.context import HostContext
from insights.core.dr import SkipComponent
from insights.core.plugins import datasource

from . import cmd_and_pkg as ds_cmd_and_pkg


@datasource(Ps, HostContext)
def cmd_and_pkg(broker):
    """
    Datasource to get a list of the running Java processes and the RPM package providing
    that command.

    Returns:
        str: A multiline string of the command and provider package for the specified commands.
    """
    COMMANDS = ['java']
    results = ds_cmd_and_pkg(broker, COMMANDS)
    if results is not None:
        return results

    raise SkipComponent
