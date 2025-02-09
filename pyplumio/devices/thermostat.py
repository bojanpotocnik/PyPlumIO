"""Contains a thermostat class."""

from __future__ import annotations

import asyncio
from collections.abc import Coroutine, Generator, Sequence
from typing import TYPE_CHECKING, Any

from pyplumio.devices import AddressableDevice, SubDevice
from pyplumio.helpers.parameter import ParameterValues
from pyplumio.structures.thermostat_parameters import (
    ATTR_THERMOSTAT_PARAMETERS,
    THERMOSTAT_PARAMETERS,
    ThermostatBinaryParameter,
    ThermostatBinaryParameterDescription,
    ThermostatParameter,
)
from pyplumio.structures.thermostat_sensors import ATTR_THERMOSTAT_SENSORS

if TYPE_CHECKING:
    from pyplumio.frames import Frame


class Thermostat(SubDevice):
    """Represents a thermostat."""

    def __init__(
        self, queue: asyncio.Queue[Frame], parent: AddressableDevice, index: int = 0
    ):
        """Initialize a new thermostat."""
        super().__init__(queue, parent, index)
        self.subscribe(ATTR_THERMOSTAT_SENSORS, self._handle_thermostat_sensors)
        self.subscribe(ATTR_THERMOSTAT_PARAMETERS, self._handle_thermostat_parameters)

    async def _handle_thermostat_sensors(self, sensors: dict[str, Any]) -> bool:
        """Handle thermostat sensors.

        For each sensor dispatch an event with the
        sensor's name and value.
        """
        await asyncio.gather(
            *(self.dispatch(name, value) for name, value in sensors.items())
        )
        return True

    async def _handle_thermostat_parameters(
        self, parameters: Sequence[tuple[int, ParameterValues]]
    ) -> bool:
        """Handle thermostat parameters.

        For each parameter dispatch an event with the
        parameter's name and value.
        """

        def _thermostat_parameter_events() -> Generator[Coroutine, Any, None]:
            """Get dispatch calls for thermostat parameter events."""
            for index, values in parameters:
                description = THERMOSTAT_PARAMETERS[index]
                handler = (
                    ThermostatBinaryParameter
                    if isinstance(description, ThermostatBinaryParameterDescription)
                    else ThermostatParameter
                )
                yield self.dispatch(
                    description.name,
                    handler.create_or_update(
                        device=self,
                        description=description,
                        values=values,
                        index=index,
                        offset=(self.index * len(parameters)),
                    ),
                )

        await asyncio.gather(*_thermostat_parameter_events())
        return True
