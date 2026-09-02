from slack_sdk import WebClient
from folio.config import slack
import tkinter as tk
from tkinter import filedialog

client = WebClient(token = slack)

def get_channel_id(channel_name: str):
    channel_name = channel_name.lstrip("#")
    cursor = None
    while True:
        result = client.conversations_list(limit = 200, cursor = cursor, types="public_channel,private_channel")
        for channel in result["channels"]:
            if channel["name"] == channel_name:
                return channel["id"]
        cursor = result.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break
    return None

def get_available_channel():
    channels = []
    cursor = None
    while True:
        result = client.conversations_list(limit = 200, cursor = cursor , types = "public_channel,private_channel")
        for ch in result["channels"]:
            channels.append(f"{ch['name']}")
        cursor = result.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break
    return ", ".join(channels)

def send_message(channel: str, message: str) -> str:
    if channel not in ["#new-channel", "#all-folio", "#social"]:
        print(f"[DEBUG] Invalid channel '{channel}' → forcing #new-channel")
        channel = "#new-channel"
    
    channel_id = get_channel_id(channel)
    print(f"[DEBUG] channel_id resolved to: {channel_id}")
    
    if not channel_id:
        print(f"[DEBUG] channel_id is None → raising error")
        raise ValueError(f"Channel {channel} not found")
    
    response = client.chat_postMessage(channel=channel_id, text=message)
    print(f"[DEBUG] Slack response ok={response['ok']}")
    
    return f"Message sent to → {channel}."


def read_message(channel: str, limit: int = 10):
    channel_id = get_channel_id(channel)
    if not channel_id:
        return f"Channel {channel} not found"
    result = client.conversations_history(channel = channel_id, limit = limit)
    return [msg.get("text", "") for msg in result["messages"]]

def upload_file(channel: str, title: str):
    channel_id = get_channel_id(channel)
    if not channel_id:
        return f"Channel {channel} not found"
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename()
    if not filepath:
        return "No file selected."
    client.files_upload_v2(channel = channel_id, file = filepath, title = title)
    return f"File uploaded to {channel}"

try:
    _channels = get_available_channel()
except Exception as e:
    print(f"[Slack] channel fetch failed: {e}")
    _channels = "new-channel, all-folio, social"

send_message.__doc__ = f"Send, post, or share any message or information to Slack. Use for: send to slack, post on slack, share info on slack. Never use send_slack. Call with channel=<#channel-name> and message=<text>. Available channels: {_channels}."
read_message.__doc__ = f"Read messages from Slack. Call with channel=<#channel-name>. Available channels: {_channels}."
upload_file.__doc__ = f"Upload a file to Slack. Call with channel=<#channel-name> and title=<filename>. Available channels: {_channels}."
