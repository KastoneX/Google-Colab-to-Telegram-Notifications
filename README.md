# Google Colab to Telegram Notifications

This repository demonstrates how to send notifications from Google Colab to Telegram using a bot. Follow the steps below to get started.

## Setup Guide

### 1. Create a Telegram Bot

1. Open Telegram and search for `@BotFather`.
2. Start a conversation with `@BotFather` by sending `/start`.
3. Follow the instructions to create a new bot by sending `/newbot`.
4. After naming your bot, you will receive an API token. Keep this token safe.

### 2. Retrieve Chat ID

To send messages, you need your chat ID. Use the following code to get it.

### 3. Send Notifications from Google Colab

Use the following function to send messages to your Telegram chat

### Example: Integrating with Google Colab

To integrate this with your Google Colab workflow, simply call the `send_telegram_message` function at desired points in your code to send updates or notifications. Here’s an example:

```python
# Example of a Google Colab cell where you notify the completion of a process
send_telegram_message('Training completed! Check your results.')
```

## Notes

- Ensure your Telegram bot is active.
- Test your setup by sending a few test messages.
- Remember to handle your API token securely and do not expose it publicly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you have suggestions for improving this repository, please feel free to submit a pull request or open an issue.

## Acknowledgements

Special thanks to the Telegram Bot API documentation and the Python Requests library documentation for providing the necessary resources.

---

By following these steps, you'll be able to receive timely notifications from your Google Colab environment directly in your Telegram chat. Happy coding!
