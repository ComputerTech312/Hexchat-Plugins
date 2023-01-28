local hexchat = hexchat
local lgi = require 'lgi'
local Gtk = lgi.Gtk

hexchat.register('Topic Window', '1.0', 'Displays the current channel\'s topic in a GTK window')

local function create_topic_window()
  local topic = hexchat.get_info("topic")
  local window = Gtk.Window {
    title = 'Topic for current channel',
    default_width = 300,
    default_height = 200,
  }
  local label = Gtk.Label {label = topic}
  window:add(label)
  window:show_all()
end

hexchat.hook_command("topicwindow", create_topic_window, "Open a window with the current channel's topic")
