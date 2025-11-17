#!/usr/bin/env ruby
require 'xcodeproj'

puts "🔧 Fixing resource file path..."
puts ""

project_path = 'GPT.xcodeproj'
project = Xcodeproj::Project.open(project_path)

# Find seed_data.json reference
seed_ref = nil
project.main_group.recursive_children.each do |item|
  if item.is_a?(Xcodeproj::Project::Object::PBXFileReference) && item.path == 'seed_data.json'
    seed_ref = item
    break
  end
end

if seed_ref
  puts "Found seed_data.json reference"
  puts "Current path: #{seed_ref.real_path}"

  # The file is at GPT/Resources/seed_data.json
  # But the reference should be relative to the Resources group
  seed_ref.path = 'seed_data.json'
  seed_ref.source_tree = '<group>'

  # Make sure the parent group has the correct path
  if seed_ref.parent && seed_ref.parent.path != 'Resources'
    seed_ref.parent.path = 'Resources'
    seed_ref.parent.source_tree = '<group>'
  end

  puts "✅ Fixed path"
else
  puts "❌ Could not find seed_data.json reference"
end

project.save

puts ""
puts "=" * 60
puts "✅ COMPLETE! Path fixed"
puts "=" * 60
puts ""
