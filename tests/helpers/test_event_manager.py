"""Contains tests for the event manager."""

from unittest.mock import AsyncMock, call, patch

import pytest

from pyplumio.helpers.event_manager import EventManager


@pytest.fixture(name="event_manager")
def fixture_event_manager() -> EventManager:
    """Return the event manager."""
    event_manager = EventManager()
    event_manager.data = {"test_key": "test_value"}
    return event_manager


def test_getattr(event_manager: EventManager) -> None:
    """Test __getattr__ dunder method."""
    assert event_manager.test_key == "test_value"


async def test_wait_for(event_manager: EventManager) -> None:
    """Test wait_for method."""
    with patch("asyncio.wait_for") as mock_wait_for, patch(
        "pyplumio.helpers.event_manager.EventManager.create_event"
    ) as mock_create_event:
        mock_create_event.wait = AsyncMock()
        await event_manager.wait_for("test_key2")

    mock_create_event.assert_called_with("test_key2")
    mock_wait_for.assert_awaited_once_with(
        mock_create_event.return_value.wait.return_value, timeout=None
    )


async def test_get(event_manager: EventManager) -> None:
    """Test async getter."""
    assert await event_manager.get("test_key") == "test_value"


def test_get_nowait(event_manager: EventManager) -> None:
    """Test getter."""
    assert event_manager.get_nowait("test_key") == "test_value"
    assert event_manager.get_nowait("test_key2") is None


async def test_subscribe(event_manager: EventManager) -> None:
    """Test subscribe."""
    callback = AsyncMock(return_value=True)
    event_manager.subscribe("test_key2", callback)
    event_manager.dispatch("test_key2", "test_value2")
    event_manager.dispatch("test_key2", "test_value3")
    await event_manager.wait_until_done()
    callback.assert_has_awaits([call("test_value2"), call("test_value3")])


async def test_subscribe_once(event_manager: EventManager) -> None:
    """Test subscribe once."""
    callback = AsyncMock(return_value=True)
    event_manager.subscribe_once("test_key2", callback)
    event_manager.dispatch("test_key2", "test_value2")
    event_manager.dispatch("test_key2", "test_value3")
    await event_manager.wait_until_done()
    callback.assert_awaited_once_with("test_value2")


async def test_unsubscribe(event_manager: EventManager) -> None:
    """Test unsubscribe."""
    callback = AsyncMock(return_value=True)
    event_manager.subscribe("test_key2", callback)
    event_manager.unsubscribe("test_key2", callback)
    event_manager.dispatch("test_key2", "test_value2")
    await event_manager.wait_until_done()
    callback.assert_not_awaited()
