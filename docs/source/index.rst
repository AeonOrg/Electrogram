Welcome to Electrogram
======================

.. raw:: html

    <div style="display: flex; align-items: center; gap: 20px; margin-top: 1rem; margin-bottom: 1.5rem;">
        <div>
            <p style="margin: 0; font-size: 1.2rem; font-weight: 500; opacity: 0.9;">
                Modern MTProto API Framework for Python
            </p>
            <div style="margin-top: 12px; display: flex; gap: 8px;">
                <a href="https://github.com/5hojib/Electrogram" style="padding: 4px 14px; background: var(--md-primary-fg-color); color: white; border-radius: 20px; font-size: 0.75rem; font-weight: 600; text-decoration: none;">GitHub</a>
                <a href="https://github.com/5hojib/Electrogram/issues" style="padding: 4px 14px; background: #f5f5f5; color: #333; border-radius: 20px; font-size: 0.75rem; font-weight: 600; text-decoration: none;">Issues</a>
            </div>
        </div>
    </div>

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_account")


    @app.on_message(filters.private)
    async def hello(client, message):
        await message.reply("Hello from Electrogram!")


    app.run()

**Electrogram** is a modern, elegant and asynchronous :doc:`MTProto API <topics/mtproto-vs-botapi>` framework.
It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot identity
(bot API alternative) using Python.

How the Documentation is Organized
----------------------------------

Contents are organized into sections composed of self-contained topics which can be all accessed from the sidebar.
Here below you can find a list of the most relevant pages for quick access.

First Steps
^^^^^^^^^^^

.. hlist::
    :columns: 1

    - :doc:`Quick Start <intro/quickstart>`: Overview to get you started quickly.
    - :doc:`Invoking Methods <start/invoking>`: How to call Electrogram's methods.
    - :doc:`Handling Updates <start/updates>`: How to handle Telegram updates.
    - :doc:`Error Handling <start/errors>`: How to handle API errors correctly.

API Reference
^^^^^^^^^^^^^

.. hlist::
    :columns: 1

    - :doc:`Electrogram Client <api/client>`: Reference details about the Client class.
    - :doc:`Available Methods <api/methods/index>`: List of available high-level methods.
    - :doc:`Available Types <api/types/index>`: List of available high-level types.
    - :doc:`Enumerations <api/enums/index>`: List of available enumerations.
    - :doc:`Bound Methods <api/bound-methods/index>`: List of convenient bound methods.

Meta
^^^^

.. hlist::
    :columns: 1

    - :doc:`Electrogram FAQ <faq/index>`: Answers to common Electrogram questions.
    - :doc:`Support Electrogram <support>`: Ways to show your appreciation.

.. toctree::
    :hidden:
    :caption: Introduction

    intro/quickstart
    intro/install

.. toctree::
    :hidden:
    :caption: Getting Started

    start/setup
    start/auth
    start/invoking
    start/updates
    start/errors
    start/examples/index

.. toctree::
    :hidden:
    :caption: API Reference

    api/client
    api/methods/index
    api/types/index
    api/bound-methods/index
    api/enums/index
    api/handlers
    api/decorators
    api/errors/index
    api/filters

.. toctree::
    :hidden:
    :caption: Topic Guides

    topics/use-filters
    topics/create-filters
    topics/more-on-updates
    topics/client-settings
    topics/text-formatting
    topics/smart-plugins
    topics/storage-engines
    topics/serializing
    topics/proxy
    topics/scheduling
    topics/mtproto-vs-botapi
    topics/debugging
    topics/test-servers
    topics/advanced-usage
    topics/voice-calls

.. toctree::
    :hidden:
    :caption: Meta

    faq/index
    support

.. toctree::
    :hidden:
    :caption: Telegram Raw API

    telegram/functions/index
    telegram/types/index
    telegram/base/index
