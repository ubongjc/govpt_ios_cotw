#!/usr/bin/env ruby
require 'xcodeproj'

puts "📦 Adding resource files to Xcode project..."
puts ""

project_path = 'GPT.xcodeproj'
project = Xcodeproj::Project.open(project_path)
target = project.targets.first

puts "Target: #{target.name}"
puts ""

# Find the GPT group
gpt_group = project.main_group.children.find { |child| child.display_name == 'GPT' }

if !gpt_group
  puts "❌ Could not find GPT group!"
  exit 1
end

# Find or create Resources group
resources_group = gpt_group.children.find { |child| child.display_name == 'Resources' }
if !resources_group
  resources_group = gpt_group.new_group('Resources', 'GPT/Resources')
  puts "✅ Created Resources group"
end

# Add seed_data.json
seed_data_path = 'GPT/Resources/seed_data.json'
existing_ref = project.main_group.find_file_by_path(seed_data_path)

if existing_ref
  puts "⏭️  seed_data.json already in project"
else
  # Add file reference
  file_ref = resources_group.new_reference('seed_data.json')
  file_ref.source_tree = '<group>'

  # Add to resources build phase (not source build phase)
  target.resources_build_phase.add_file_reference(file_ref)

  puts "✅ Added seed_data.json to Resources"
end

# Save project
project.save

puts ""
puts "=" * 60
puts "✅ COMPLETE! Resources added to project"
puts "=" * 60
puts ""
